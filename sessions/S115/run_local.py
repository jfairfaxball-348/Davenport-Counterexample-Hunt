"""Bounded resumable local enumeration. No CRT joins or target sequence search.
Run preflight.py before freezing RUN_MANIFEST.json and launching this runner.
"""
import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path
import platform
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/zsf'))
PROFILES = [(2,4,8,8,8,13),(2,8,8,8,8,9),(3,8,8,8,8,8),(4,4,8,8,8,11),(4,7,8,8,8,8)]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()


def write_json(path,d):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8',newline='\n')
    os.replace(temp,path)


def run(engine,p,folder,cap=7200,chunk=2048,max_chunks=None):
    module = importlib.import_module('local_images_a' if engine=='a' else 'local_kernels_b')
    folder.mkdir(parents=True,exist_ok=True)
    bounds = [[x//(15//p) for x in prof] for prof in PROFILES]
    config = {'engine':engine,'p':p,'profiles':PROFILES,'bounds':bounds,'chunk':chunk,
              'code_sha256':{Path(module.__file__).name:sha(module.__file__), 'run_local.py':sha(__file__)},
              'python':platform.python_version(),'numpy':np.__version__}
    config = json.loads(json.dumps(config))
    cp = folder/'checkpoint.json'
    if cp.exists():
        state=json.loads(cp.read_text())
        if state['config'] != config:
            raise ValueError('checkpoint configuration/code/environment mismatch')
    else:
        state={'config':config,'completed':[],'status':'PARTIAL','seconds':0}
        write_json(cp,state)
    completed={tuple(x['id']) for x in state['completed']}
    start_clock=time.perf_counter()
    jobs=0
    for si,piv in enumerate(module.strata()):
        n=module.size(p,piv)
        for start in range(0,n,chunk):
            stop=min(n,start+chunk)
            cid=(si,start,stop)
            if cid in completed:
                continue
            if time.perf_counter()-start_clock >= cap or (max_chunks is not None and jobs>=max_chunks):
                return state
            begin=time.perf_counter()
            matrix=module.matrices(p,piv,start,stop)
            keep=module.survivors(matrix,p,piv,bounds)
            im=matrix if engine=='a' else module.image(matrix,p,piv)
            keys=module.keys(im,p)
            arrays={f'profile{i}':keys[keep[i]] for i in range(5)}
            # Store all keys too: permits independent full image-space coverage comparison.
            arrays['all']=keys
            part=folder/f'part-{si:02d}-{start:08d}.npz'
            tmp=part.with_suffix('.tmp')
            with tmp.open('wb') as f:
                np.savez_compressed(f,**arrays)
            os.replace(tmp,part)
            record={'id':list(cid),'file':part.name,'sha256':hashlib.sha256(part.read_bytes()).hexdigest(),
                    'counts':[int(x.sum()) for x in keep], 'seconds':time.perf_counter()-begin}
            state['completed'].append(record)
            state['seconds']+=record['seconds']
            write_json(cp,state)
            jobs+=1
        print(engine,p,'stratum',si,'complete',len(state['completed']),'chunks',flush=True)
    state['status']='COMPLETE'
    write_json(cp,state)
    return state


def consolidate(folder):
    state=json.loads((folder/'checkpoint.json').read_text())
    assert state['status']=='COMPLETE'
    all_arrays={key:[] for key in ['all']+[f'profile{i}' for i in range(5)]}
    for rec in state['completed']:
        path=folder/rec['file']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==rec['sha256']
        with np.load(path,allow_pickle=False) as data:
            for key in all_arrays:
                all_arrays[key].append(data[key])
    for key,arrays in all_arrays.items():
        values=np.sort(np.concatenate(arrays))
        assert len(values)==len(np.unique(values)), (key,'duplicate coverage')
        np.save(folder/(key+'.npy'),values,allow_pickle=False)
    return state


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('engine',choices=['a','b']);ap.add_argument('p',type=int,choices=[3,5])
    args=ap.parse_args()
    manifest=json.loads((ROOT/'sessions/S115/RUN_MANIFEST.json').read_text())
    for path,h in manifest['code_sha256'].items():
        assert sha(ROOT/path)==h, 'code changed after registration: '+path
    dest=ROOT/f'sessions/S115/data/{args.engine}{args.p}'
    s=run(args.engine,args.p,dest)
    if s['status']=='COMPLETE':
        consolidate(dest)
    print(args.engine,args.p,s['status'],s['seconds'],flush=True)
