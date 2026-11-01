"""Synthetic full-work costs and local-only input verification. No target join."""
from pathlib import Path
import hashlib,io,json,platform,statistics,sys,time,zipfile
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/zsf'))
import pair_a as a
import pair_b as b


def timing(fn):
    times=[]
    for _ in range(31):
        start=time.perf_counter_ns();fn();times.append((time.perf_counter_ns()-start)/1e9)
    return {'min':min(times),'median':statistics.median(times),'max':max(times),'seconds':times}


def main():
    s=ROOT/'sessions/S115';manifest=json.loads((s/'ARCHIVE_MANIFEST.json').read_text())
    blob=(s/'LOCAL_EVIDENCE.zip').read_bytes()
    assert hashlib.sha256(blob).hexdigest()==manifest['sha256']
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        raw=z.read('data/a5/profile2.npy')
        assert hashlib.sha256(raw).hexdigest()==manifest['files']['data/a5/profile2.npy']
        assert z.read('data/b5/profile2.npy')==raw
    first=(s/'representatives2.npy').read_bytes()
    old=json.loads((s/'SHA256SUMS.json').read_text())['files']
    assert hashlib.sha256(first).hexdigest()==old['sessions/S115/representatives2.npy']
    arrays=[np.load(io.BytesIO(first),allow_pickle=False),np.load(io.BytesIO(raw),allow_pickle=False)]
    assert [len(x) for x in arrays]==[145,40110]
    inputs=[];local=[]
    for p,xx in zip((3,5),arrays):
        assert np.all(xx[1:]>xx[:-1])
        for code in xx:
            m=a.decode(code,p,6);n=b.unpack(code,p,6)
            assert m.tolist()==n
            assert sum(int(v)*p**i for i,v in enumerate(m.flat))==int(code)
        # Independent key roundtrip on every input; only three local setup samples.
        for index in (0,len(xx)//2,len(xx)-1):
            code=int(xx[index]);matrix=b.unpack(code,p,6)
            local.append({'p':p,'index':index,'key':code,'a_decode':timing(lambda:a.decode(code,p,6)),
                          'b_decode_and_kernel':timing(lambda:b.kernel_vectors(b.unpack(code,p,6),p))})
        inputs.append({'p':p,'count':len(xx),'file_sha256':hashlib.sha256(first if p==3 else raw).hexdigest()})
    # Arrays below are artificial operation fixtures, not S115 pairs or kernels.
    alpha=[3,8,8,8,8,8];left,right=a.grids(alpha)
    synthetic_matrix=np.arange(18,dtype=np.int64).reshape(3,6)%15
    u=np.arange(27*6,dtype=np.int64).reshape(27,6)%3
    v=(np.arange(125*6,dtype=np.int64).reshape(125,6)*7+1)%5
    ta=timing(lambda:a.scan(synthetic_matrix,15,left,right))
    tg=timing(lambda:a.grids(alpha))
    tb=timing(lambda:b.intersection(u,v,3,5,alpha))
    # Reserve per-pair setup for both engines, even though caching could remove it.
    setup_a=sum(max(row['a_decode']['max'] for row in local if row['p']==p) for p in (3,5))
    setup_b=sum(max(row['b_decode_and_kernel']['max'] for row in local if row['p']==p) for p in (3,5))
    per_a=ta['max']+tg['max']+setup_a
    per_b=tb['max']+setup_b
    # Boundary arithmetic checked using two formulations, no predicate calls.
    shards=[[start,min(start+40110,5815950)] for start in range(0,5815950,40110)]
    assert len(shards)==145 and sum(hi-lo for lo,hi in shards)==5815950
    assert all(lo==i*40110 and hi==(i+1)*40110 for i,(lo,hi) in enumerate(shards))
    assert divmod(5815949,40110)==(144,40109)
    out={'status':'PASS','scope':'synthetic primitive costs, not measured target pair rates','environment':{'python':platform.python_version(),'platform':platform.platform(),'numpy':np.__version__},
         'inputs':inputs,'local_setup':local,'primitive_a':ta,'grid_setup_a':tg,'primitive_b':tb,
         'operation_dimensions':{'left':list(left.shape),'right':list(right.shape),'kernel_product':[27,125,6]},
         'synthetic_fixture_sha256':hashlib.sha256(synthetic_matrix.tobytes()+u.tobytes()+v.tobytes()).hexdigest(),
         'per_pair_measured_component_maxima_seconds':{'a':per_a,'b':per_b},
         'tenfold_scenario_hours':{'a':per_a*5815950*10/3600,'b':per_b*5815950*10/3600},
         'tenfold_per_row_seconds':{'a':per_a*40110*10,'b':per_b*40110*10},
         'shards':shards,'target_pairs_evaluated':0,
         'caveat':'Synthetic full-work costs omit some admissibility, witness validation, JSON/checkpoint and OS overhead; tenfold margin is a planning scenario, not a rigorous runtime bound.'}
    (ROOT/'sessions/S116/BENCHMARK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('local_setup','primitive_a','primitive_b','grid_setup_a','shards')},indent=2))


if __name__=='__main__':main()
