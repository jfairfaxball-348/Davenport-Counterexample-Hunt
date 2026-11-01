"""S115-L2: independent orbit traversal over stored p3 local images only."""
import hashlib
import itertools as it
import json
from pathlib import Path
import time
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
PROFILES=[(2,4,8,8,8,13),(2,8,8,8,8,9),(3,8,8,8,8,8),(4,4,8,8,8,11),(4,7,8,8,8,8)]


def decode(keys):
    digits=np.empty((len(keys),18),dtype=np.int16)
    for j in range(18): digits[:,j]=(keys//3**j)%3
    return digits.reshape(-1,3,6)


def canonical(m):
    # Vectorized row operations after permuting image columns.
    a=m.copy();row=np.zeros(len(a),dtype=np.int16)
    inv=np.array([0,1,2],dtype=np.int16)
    for col in range(6):
        for target in range(3):
            ids=np.flatnonzero(row==target)
            if not len(ids): continue
            candidates=a[ids,target:,col]!=0
            good=np.any(candidates,axis=1);ids=ids[good]
            if not len(ids): continue
            pivot=candidates[good].argmax(axis=1)+target
            saved=a[ids,target].copy();a[ids,target]=a[ids,pivot];a[ids,pivot]=saved
            a[ids,target]=a[ids,target]*inv[a[ids,target,col]][:,None]%3
            for other in range(3):
                if other!=target:
                    a[ids,other]=(a[ids,other]-a[ids,other,col,None]*a[ids,target])%3
            # Mark chosen rows negatively until the column is complete.
            row[ids]=-target-1
        row=np.where(row<0,-row,row)
    assert np.all(row==3)
    return a.reshape(-1,18).astype(np.uint64)@np.array([3**j for j in range(18)],dtype=np.uint64)


def scalar_key(columns):
    # Independent scalar Gaussian elimination and key calculation for union-find B.
    rows=[list(r) for r in zip(*columns)];r=0
    for c in range(6):
        t=next((i for i in range(r,3) if rows[i][c]%3),None)
        if t is None: continue
        rows[r],rows[t]=rows[t],rows[r]
        rows[r]=[(v*pow(rows[r][c],-1,3))%3 for v in rows[r]]
        for i in range(3):
            if i!=r:
                coeff=rows[i][c]
                rows[i]=[(x-coeff*y)%3 for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==3:break
    result=0;power=1
    for line in rows:
        for value in line: result+=value*power;power*=3
    return result


def main():
    manifest=json.loads((ROOT/'sessions/S115/ORBIT_RUN_MANIFEST.json').read_text())
    for path,h in manifest['sha256'].items():
        assert hashlib.sha256((ROOT/path).read_bytes().replace(b'\r\n',b'\n') if path.endswith(('.py','.md')) else (ROOT/path).read_bytes()).hexdigest()==h,path
    start=time.perf_counter();results=[]
    for pi,profile in enumerate(PROFILES):
        keys=np.load(ROOT/f'sessions/S115/data/a3/profile{pi}.npy')
        mats=decode(keys)
        blocks=[tuple(i for i,x in enumerate(profile) if x==v) for v in sorted(set(profile))]
        perms=[]
        for pieces in it.product(*(list(it.permutations(block)) for block in blocks)):
            perm=list(range(6))
            for block,piece in zip(blocks,pieces):
                for i,j in zip(block,piece):perm[i]=j
            perms.append(perm)
        minima=keys.copy()
        for perm in perms:
            transformed=canonical(mats[:,:,perm])
            where=np.searchsorted(keys,transformed)
            assert np.all(where<len(keys)) and np.array_equal(keys[where],transformed)
            minima=np.minimum(minima,transformed)
            assert time.perf_counter()-start<600
        reps_a,sizes=np.unique(minima,return_counts=True)
        parent=list(range(len(keys)));index={int(v):i for i,v in enumerate(keys)}
        def root(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]];x=parent[x]
            return x
        for block in blocks:
            for x,y in zip(block,block[1:]):
                for i,m in enumerate(mats):
                    cols=[tuple(map(int,m[:,j])) for j in range(6)]
                    cols[x],cols[y]=cols[y],cols[x]
                    j=index[scalar_key(cols)]
                    u,v=root(i),root(j)
                    if u!=v:parent[max(u,v)]=min(u,v)
        groups={}
        for i,k in enumerate(keys):groups.setdefault(root(i),[]).append(int(k))
        reps_b=np.array(sorted(min(v) for v in groups.values()),dtype=np.uint64)
        assert np.array_equal(reps_a,reps_b)
        assert sorted(sizes)==sorted(len(v) for v in groups.values())
        np.save(ROOT/f'sessions/S115/representatives{pi}.npy',reps_a,allow_pickle=False)
        hist={str(s):int(np.count_nonzero(sizes==s)) for s in np.unique(sizes)}
        p5count=len(np.load(ROOT/f'sessions/S115/data/a5/profile{pi}.npy'))
        results.append({'profile':profile,'p3_survivors':len(keys),'stabilizer_order':len(perms),'p3_orbits':len(reps_a),
                        'orbit_size_histogram':hist,'independent_representatives_equal':True,'p5_survivors':p5count,
                        'representative_product':len(reps_a)*p5count,
                        'representative_sha256_le_uint64':hashlib.sha256(reps_a.astype('<u8').tobytes()).hexdigest()})
        print(pi,'orbits',len(reps_a),'product',len(reps_a)*p5count,flush=True)
    out={'status':'PASS','cases':results,'seconds':time.perf_counter()-start,'total_representative_product':sum(x['representative_product'] for x in results),
         'scope':'p3 profile-stabilizer quotient times all p5 survivors; covering representative system, not exact joint orbit count'}
    (ROOT/'sessions/S115/ORBIT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
