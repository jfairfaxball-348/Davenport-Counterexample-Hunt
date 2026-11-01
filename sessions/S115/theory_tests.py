"""S115-T1 exact small-group pair-mask tests and parity census."""
import hashlib
import itertools as it
import json
from pathlib import Path
import time
ROOT=Path(__file__).resolve().parents[2]


def pair_mask(g,h,p,a,b):
    mask=0
    for x in range(a+1):
        for y in range(b+1):
            if x+y and all((x*u+y*v)%p==0 for u,v in zip(g,h)):
                mask |= 1 << (x*(b+1)+y)
    return mask


def canonical_binary(columns):
    rows=[sum(((v>>i)&1)<<j for j,v in enumerate(columns)) for i in range(3)]
    r=0
    for j in range(len(columns)):
        hit=next((s for s in range(r,3) if rows[s]>>j&1),None)
        if hit is None: continue
        rows[r],rows[hit]=rows[hit],rows[r]
        for s in range(3):
            if s!=r and rows[s]>>j&1: rows[s]^=rows[r]
        r+=1
        if r==3: break
    assert r==3
    return tuple(rows)


def main():
    start=time.perf_counter()
    # Direct integer-coordinate summation compared with intersection of local bitsets.
    vectors=list(it.product(range(6),repeat=3))[1:]
    decisions=0
    for g in vectors:
        for h in vectors:
            for a,b in it.product((1,2),repeat=2):
                local=bool(pair_mask(g,h,2,a,b)&pair_mask(g,h,3,a,b))
                direct=False
                for coeff in it.product(range(a+1),range(b+1)):
                    if coeff==(0,0): continue
                    total=tuple(sum(t*v[j] for t,v in zip(coeff,(g,h)))%6 for j in range(3))
                    if total==(0,0,0): direct=True
                assert local==direct
                decisions+=1
            assert time.perf_counter()-start<300
    pair_seconds=time.perf_counter()-start
    # No pair zero but a triple zero: pair pruning alone cannot prove global ZSF.
    triple=((1,0,0),(0,1,0),(5,5,0))
    assert all(not (pair_mask(g,h,2,1,1)&pair_mask(g,h,3,1,1)) for g,h in it.combinations(triple,2))
    assert all(sum(g[j] for g in triple)%6==0 for j in range(3))
    start2=time.perf_counter();orbits=set();raw=0;missing=repeat=0
    for absent in range(1,8):
        for six in it.permutations([x for x in range(1,8) if x!=absent]):
            for seventh in range(1,8):
                orbits.add(canonical_binary(six+(seventh,)))
                raw+=1
                if seventh==absent: missing+=1
                else: repeat+=1
    assert raw==35280 and len(orbits)==210 and raw//168==len(orbits)
    assert time.perf_counter()-start2<60
    canonical='\n'.join(','.join(map(str,x)) for x in sorted(orbits))+'\n'
    (ROOT/'sessions/S115/PARITY_ORBITS.txt').write_text(canonical,encoding='ascii',newline='\n')
    result={'status':'PASS','pair_decisions':decisions,'pair_seconds':pair_seconds,
            'pair_scope':'all ordered nonzero pairs of C6^3, bounds (a,b) in {1,2}^2; repeats allowed',
            'pair_insufficiency_example':{'values':triple,'multiplicities':[1,1,1],'zero_coefficients':[1,1,1]},
            'n20_parity':{'raw_labelled':raw,'GL3_F2_order':168,'orbits':len(orbits),'missing_seventh_orbits':missing//168,
                          'repeated_seventh_orbits':repeat//168,'mod4_lifts_per_orbit':4096,'mod4_total':210*4096,
                          'seconds':time.perf_counter()-start2,'orbit_sha256':hashlib.sha256(canonical.encode()).hexdigest()},
            'code_sha256':hashlib.sha256(Path(__file__).read_bytes().replace(b'\r\n',b'\n')).hexdigest()}
    (ROOT/'sessions/S115/THEORY_TESTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
