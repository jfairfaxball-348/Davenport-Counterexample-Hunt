"""Verify full local coverage and survivor sets, benchmark every surviving image stratum."""
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/zsf'))
sys.path.insert(0,str(ROOT/'sessions/S115'))
import local_images_a as a
import local_kernels_b as b
from run_local import PROFILES,sha


def decode(keys,p):
    x=keys.copy()
    m=np.empty((len(x),3,6),dtype=np.int16)
    for i in range(3):
        for j in range(6):
            m[:,i,j]=x%p;x//=p
    return m


def main():
    result={'status':'PASS','scope':'local full-order image classes; no CRT joins','components':{},'strata':[],'products':[]}
    data=ROOT/'sessions/S115/data'
    counts={}
    for p,expected in [(3,33880),(5,2558556)]:
        checkpoints={}
        for engine,mod in [('a',a),('b',b)]:
            folder=data/f'{engine}{p}'
            cp=json.loads((folder/'checkpoint.json').read_text())
            assert cp['status']=='COMPLETE'
            expected_chunks={(s,x,min(x+2048,mod.size(p,piv))) for s,piv in enumerate(mod.strata()) for x in range(0,mod.size(p,piv),2048)}
            recorded=[tuple(x['id']) for x in cp['completed']]
            assert len(recorded)==len(set(recorded)) and set(recorded)==expected_chunks
            for rec in cp['completed']:
                assert hashlib.sha256((folder/rec['file']).read_bytes()).hexdigest()==rec['sha256']
            checkpoints[engine]={'chunks':len(recorded),'seconds_in_chunks':cp['seconds']}
        all_a=np.load(data/f'a{p}/all.npy');all_b=np.load(data/f'b{p}/all.npy')
        assert len(all_a)==expected and np.array_equal(all_a,all_b)
        assert len(np.unique(all_a))==expected
        counts[p]=[]
        sums=[]
        for i,profile in enumerate(PROFILES):
            ka=np.load(data/f'a{p}/profile{i}.npy');kb=np.load(data/f'b{p}/profile{i}.npy')
            assert np.array_equal(ka,kb)
            counts[p].append(len(ka))
            sums.append(hashlib.sha256(ka.astype('<u8').tobytes()).hexdigest())
            images=decode(ka,p)
            pivs=np.argmax(images!=0,axis=2)
            beta=[x//(15//p) for x in profile]
            for piv in a.strata():
                loc=np.flatnonzero(np.all(pivs==piv,axis=1))
                if not len(loc):
                    result['strata'].append({'p':p,'profile':i,'pivot':piv,'survivors':0})
                    continue
                sample=loc[sorted(set([0,len(loc)//2,len(loc)-1]))]
                ms=images[sample]
                # Orthogonal complement of image row space, using B elimination.
                ks=b.image(ms,p,piv)
                kp=np.argmax(ks!=0,axis=2)
                ta=[];tb=[]
                for _ in range(7):
                    start=time.perf_counter_ns();va=a.survivors(ms,p,piv,[beta]);ta.append(time.perf_counter_ns()-start)
                    assert va.all()
                    start=time.perf_counter_ns()
                    # Each sample can have a different kernel pivot stratum.
                    for j in range(len(ks)):
                        assert b.survivors(ks[j:j+1],p,tuple(kp[j]),[beta]).all()
                    tb.append(time.perf_counter_ns()-start)
                def summary(v): return {'min_ns':min(v),'median_ns':int(np.median(v)),'max_ns':max(v),'batch_size':len(ms)}
                result['strata'].append({'p':p,'profile':i,'pivot':piv,'survivors':len(loc),'sample_keys':[int(x) for x in ka[sample]],
                                         'sample_sha256':hashlib.sha256(ka[sample].astype('<u8').tobytes()).hexdigest(),
                                         'a_timing':summary(ta),'b_timing':summary(tb)})
        result['components'][str(p)]={'all_images':expected,'independent_all_image_sets_equal':True,'survivors':counts[p],
                                      'survivor_key_sha256_le_uint64':sums,'checkpoints':checkpoints}
    for i,pr in enumerate(PROFILES):
        result['products'].append({'profile':pr,'p3':counts[3][i],'p5':counts[5][i],'pairs':counts[3][i]*counts[5][i]})
    total=sum(x['pairs'] for x in result['products'])
    result['total_remaining_cartesian_pairs']=total
    result['raw_total']=433419386400
    result['reduction_factor']=433419386400/total if total else None
    result['runtime_scenarios_CPU_hours']={str(us)+'us':total*us/1e6/3600 for us in [1,10,100]}
    result['not_measured']='target pair throughput, coupled filter effectiveness, full target search runtime'
    result['nonempty_strata_benchmarked']=sum(x['survivors']>0 for x in result['strata'])
    result['code_sha256']={str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in [Path(__file__),Path(a.__file__),Path(b.__file__)]}
    (ROOT/'sessions/S115/RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in result.items() if k!='strata'},indent=2))


if __name__=='__main__':main()
