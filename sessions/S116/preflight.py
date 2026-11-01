"""Bounded S116-P1/P2 settled validation, never target pair evaluation."""
from pathlib import Path
import hashlib, itertools, json, shutil, sys, tempfile, time
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/zsf'))
import pair_a as a
import pair_b as b
import pair_jobs as jobs
import local_images_a as images
import local_kernels_b as kernels
import checker_a,checker_b


def key(m,p):return sum(int(v)*p**i for i,v in enumerate(np.asarray(m).flat))


def spaces(p):
    aa=[];bb=[]
    for piv in images.strata(4,3):
        mm=images.matrices(p,piv,0,images.size(p,piv,4),4)
        aa.extend(int(x) for x in images.keys(mm,p))
    for piv in kernels.strata(4,3):
        kk=kernels.matrices(p,piv,0,kernels.size(p,piv,4),4)
        mm=kernels.image(kk,p,piv)
        bb.extend(int(x) for x in kernels.keys(mm,p))
    assert sorted(aa)==sorted(bb) and len(set(aa))==len(aa)
    assert len(aa)=={2:15,3:40}[p]
    return sorted(aa)


def independent_actual(x,y,p,q,k):
    # Brute CRT lookup and positional digit extraction, no engine helper.
    return [[next(t for t in range(p*q) if t%p==(int(x)//p**(r*k+c))%p and t%q==(int(y)//q**(r*k+c))%q)
             for c in range(k)] for r in range(3)]


def oracle(m,alpha,n):
    coeff=np.array(list(itertools.product(*(range(t+1) for t in alpha))),dtype=np.int64)
    return bool(np.any(np.all((coeff[1:]@np.asarray(m).T)%n==0,axis=1)))


def check_witness(result,m,alpha,n):
    if result['kind']!='ZERO':return
    w=result['witness']
    assert len(w)==len(alpha) and any(w) and all(0<=x<=bound for x,bound in zip(w,alpha))
    assert all(sum(x*y for x,y in zip(row,w))%n==0 for row in m)


def one(x,y,p,q,alpha,legacy=True):
    aa=a.classify(x,y,p,q,alpha);bb=b.classify(x,y,p,q,alpha)
    assert aa['kind']==bb['kind'],(x,y,alpha,aa,bb)
    m=independent_actual(x,y,p,q,len(alpha));n=p*q
    columns=list(zip(*m))
    orders=[next(t for t in range(1,n+1) if all(t*v%n==0 for v in col)) for col in columns]
    valid=len(set(columns))==len(columns) and all(t==n for t in orders)
    zero=oracle(m,alpha,n)
    expected='INVALID' if not valid else ('ZERO' if zero else 'ZSF')
    assert aa['kind']==expected
    check_witness(aa,m,alpha,n);check_witness(bb,m,alpha,n)
    if valid and legacy:
        seq=[g for g,count in zip(columns,alpha) for _ in range(count)]
        assert checker_a.is_zero_sumfree(seq,(n,)*3)[0]==(not zero)
        assert checker_b.is_zero_sumfree(seq,(n,)*3)==(not zero)
    return expected


def rejected(fn):
    try:fn()
    except (ValueError,AssertionError,FileNotFoundError):return True
    raise AssertionError('expected rejection')


def fault_tests(x,y):
    identity={'start':0,'stop':600,'chunk':37,'code':'fixture-v1','inputs':'settled-15x40','environment':'test','profile':[4]*4}
    evaluate=lambda lo,hi:a.traverse(x,y,lo,hi,2,3,[4]*4)
    receipt={}
    with tempfile.TemporaryDirectory(prefix='s116-preflight-') as temp:
        base=Path(temp)
        full=jobs.run(base/'full',identity,evaluate,120)
        assert full['status']=='COMPLETE' and full['next']==600
        # Independent explicit nested-coordinate coverage for the other engine.
        outa=list(evaluate(0,600));outb=list(b.traverse(x,y,0,600,2,3,[4]*4))
        assert [i for i,_ in outa]==[i for i,_ in outb]==list(range(600))
        assert [r['kind'] for _,r in outa]==[r['kind'] for _,r in outb]
        for mode in ('before_output','after_output','after_marker'):
            folder=base/mode
            try:jobs.run(folder,identity,evaluate,120,fault=mode)
            except RuntimeError:pass
            else:raise AssertionError('fault not injected')
            got=jobs.run(folder,identity,evaluate,120)
            assert got==full
            receipt[mode]='exact resumed receipt equals uninterrupted'
        folder=base/'budget'
        initial=jobs.run(folder,identity,evaluate,0)
        assert initial['status']=='BUDGET_EXHAUSTED' and initial['next']==0
        partial=jobs.run(folder,identity,evaluate,120,max_chunks=2)
        assert partial['next']==74 and partial['status']=='BUDGET_EXHAUSTED'
        assert jobs.run(folder,identity,evaluate,120)==full
        receipt['budget_resume']=True
        for field in ('code','inputs','environment','profile','start','stop','chunk'):
            changed=dict(identity);changed[field]='tampered'
            rejected(lambda:jobs.inspect(base/'full',changed))
        receipt['identity_fields_rejected']=list(identity)
        for mode in ('missing','corrupt','duplicate','gap'):
            folder=base/mode;shutil.copytree(base/'full',folder)
            if mode=='missing':(folder/'000000000000.rows.json').unlink()
            elif mode=='corrupt':(folder/'000000000000.rows.json').write_text('[]')
            elif mode=='duplicate':shutil.copyfile(folder/'000000000000.commit.json',folder/'000000000001.commit.json')
            else:(folder/'000000000000.commit.json').unlink()
            rejected(lambda:jobs.inspect(folder,identity))
        receipt['committed_corruption_rejected']=['missing','corrupt','duplicate','gap']
        def candidate(lo,hi):
            for i in range(lo,hi):yield i,{'kind':'ZSF' if i==17 else 'ZERO','witness':[1]}
        cand=jobs.run(base/'candidate',identity,candidate,120)
        assert cand['status']=='CANDIDATE' and cand['next']==18
        assert jobs.run(base/'candidate',identity,candidate,120)==cand
        def broken(lo,hi):
            yield lo,{'kind':'ZERO'}
            raise ArithmeticError('intentional checker failure')
        fail=jobs.run(base/'failed',identity,broken,120)
        assert fail['status']=='FAILED' and fail['next']==1 and fail['counts']=={'FAILED':1}
        assert jobs.run(base/'failed',identity,broken,120)==fail
        for name,callback in [('truncated',lambda lo,hi:iter([])),('duplicate_enum',lambda lo,hi:iter([(lo,{'kind':'ZERO'}),(lo,{'kind':'ZERO'})]))]:
            assert jobs.run(base/name,identity,callback,120)['status']=='FAILED'
        receipt['candidate_receipt']=cand;receipt['failed_receipt']=fail
        # Independent replay of the stored decisions and each exact endpoint.
        replay=[]
        for path in sorted((base/'full').glob('*.rows.json')):replay.extend(json.loads(path.read_bytes()))
        assert [(r['ordinal'],r['result']) for r in replay]==outa
        receipt['uninterrupted_receipt']=full
        receipt['independent_record_replay']=True
    return receipt


def main():
    began=time.monotonic();x,y=spaces(2),spaces(3);cases=[]
    for alpha in ([1]*4,[2]*4,[4]*4,[1,2,3,4]):
        counts={}
        for u,v in itertools.product(x,y):
            kind=one(u,v,2,3,alpha);counts[kind]=counts.get(kind,0)+1
            if time.monotonic()-began>600:raise TimeoutError('registered preflight cap')
        cases.append({'profile':alpha,'counts':counts,'pairs':600})
    controls=[]
    matrices=[
        ([[1,0,0],[0,1,0],[0,0,1]],[5,5,5],'positive basis'),
        ([[1,0,5],[0,1,5],[0,0,0]],[1,1,1],'pair-pass triple-zero'),
        ([[1,0,5,0,1,0],[0,1,5,0,0,1],[0,0,0,1,1,1]],[1,1,1,0,0,0],'left-only zero'),
        ([[0,1,0,1,0,5],[0,0,1,0,1,5],[1,1,1,0,0,0]],[0,0,0,1,1,1],'right-only zero'),
        ([[1,1,0,0],[0,0,1,0],[0,0,0,1]],[1]*4,'duplicate actual'),
        ([[2,0,0],[0,1,0],[0,0,1]],[1]*3,'wrong order'),
        ([[1,3,0,0],[0,2,1,0],[0,0,0,1]],[1]*4,'repeated projected column')]
    for matrix,alpha,name in matrices:
        m=np.asarray(matrix);kind=one(key(m%2,2),key(m%3,3),2,3,alpha)
        controls.append({'name':name,'kind':kind,'matrix':matrix,'profile':alpha})
    assert controls[0]['kind']=='ZSF' and all(c['kind']=='ZERO' for c in controls[1:4])
    for module in (a,b):
        rejected(lambda:module.classify(-1,0,2,3,[1]*4))
        rejected(lambda:module.classify(0,0,2,2,[1]*4))
        rejected(lambda:module.classify(0,0,2,3,[6]*4))
    faults=fault_tests(x,y)
    result={'status':'PASS','scope':'settled C6^3 tooling only','cases':cases,'controls':controls,'faults':faults,'seconds':time.monotonic()-began}
    (ROOT/'sessions/S116/PREFLIGHT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
