"""S115 bounded settled validation and checkpoint fault checks."""
import hashlib
import itertools as it
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
import checker_a,checker_b
import run_local


def direct(m,p,beta):
    if any(not any(m[:,j]) for j in range(m.shape[1])):
        return False
    for x in it.product(*(range(v+1) for v in beta)):
        if any(x) and np.all((m@x)%p == 0):
            return False
    return True


def main():
    begin=time.perf_counter(); out={'cases':[]}
    for p in (2,3):
        bounds=[v for v in it.product(range(p),repeat=4) if sum(v)<=3*(p-1)]
        da={}; db={}
        for piv in a.strata(4,3):
            m=a.matrices(p,piv,0,a.size(p,piv,4),4)
            verdict=a.survivors(m,p,piv,bounds)
            for j,key in enumerate(a.keys(m,p)):
                expected=np.array([direct(m[j],p,be) for be in bounds])
                assert np.array_equal(expected,verdict[:,j])
                da[int(key)]=verdict[:,j].tolist()
                if np.all(np.any(m[j]!=0,axis=0)):
                    for be in bounds[::max(1,len(bounds)//5)]:
                        seq=[tuple(m[j,:,i]) for i in range(4) for _ in range(be[i])]
                        va=checker_a.is_zero_sumfree(seq,(p,)*3)[0]
                        vb=checker_b.is_zero_sumfree(seq,(p,)*3)
                        assert va==vb==direct(m[j],p,be)
        for piv in b.strata(4,3):
            k=b.matrices(p,piv,0,b.size(p,piv,4),4)
            verdict=b.survivors(k,p,piv,bounds)
            images=b.image(k,p,piv)
            for j,key in enumerate(b.keys(images,p)):
                assert int(key) not in db
                db[int(key)]=verdict[:,j].tolist()
        assert da==db
        assert len(da)=={2:15,3:40}[p]
        out['cases'].append({'p':p,'matrices':len(da),'boxes':len(bounds),'direct_and_two_engines_agree':True})
    # Test real chunk durability on small p2,k6 synthetic profiles: stop/resume/full.
    base=ROOT/'sessions/S115/preflight_data'
    first=run_local.run('a',2,base/'resume',chunk=127,max_chunks=2)
    assert first['status']=='PARTIAL' and len(first['completed'])==2
    saved=(base/'resume/checkpoint.json').read_bytes()
    bad=json.loads(saved);bad['config']['code_sha256']['run_local.py']='tampered'
    (base/'resume/checkpoint.json').write_text(json.dumps(bad))
    try:
        run_local.run('a',2,base/'resume',chunk=127)
        raise AssertionError('tampered checkpoint accepted')
    except ValueError:
        pass
    (base/'resume/checkpoint.json').write_bytes(saved)
    # Orphan part is overwritten: emulate crash after data write but before checkpoint.
    (base/'resume/part-00-00000254.npz').write_bytes(b'orphan interrupted data')
    resumed=run_local.run('a',2,base/'resume',chunk=127)
    full=run_local.run('a',2,base/'full',chunk=127)
    run_local.consolidate(base/'resume');run_local.consolidate(base/'full')
    for key in ['all']+[f'profile{i}' for i in range(5)]:
        assert np.array_equal(np.load(base/'resume'/f'{key}.npy'),np.load(base/'full'/f'{key}.npy'))
    assert len(resumed['completed'])==len(full['completed'])
    out['restart']={'partial_chunks':2,'resume_equals_uninterrupted':True,'orphan_overwritten':True,'tampered_code_rejected':True}
    out['status']='PASS';out['seconds']=time.perf_counter()-begin
    out['code_sha256']={str(p.relative_to(ROOT)).replace('\\','/'):run_local.sha(p) for p in [Path(__file__),Path(a.__file__),Path(b.__file__),Path(run_local.__file__)]}
    assert out['seconds']<600
    (ROOT/'sessions/S115/PREFLIGHT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__': main()
