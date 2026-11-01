"""Run only S114 PLAN.md bounded arithmetic, settled validation and benchmark."""
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'tools/zsf'))
import image_profile as ip
import checker_a
import checker_b
import numpy


def partitions(total, k, low=1, cap=18):
    if k == 0:
        if total == 0:
            yield ()
        return
    for a in range(low, min(cap, total//k)+1):
        for rest in partitions(total-a, k-1, a, cap):
            yield (a,)+rest


def profiles(n, k):
    # Independent of route_sieve.py: partitions first, then order assignments.
    divs = [d for d in range(2, n+1) if n % d == 0]
    caps = {d: d-1 for d in divs}
    caps[n] = n-2-(n % 2 == 0)
    if n % 2 == 0:
        caps[n//2] = n//2-2
    routes = {15: (3, 5), 20: (2, 4, 5)}[n]
    out = set()
    for alpha in partitions(3*n-2, k, cap=max(caps.values())):
        for orders in it.product(*([d for d in divs if caps[d] >= a] for a in alpha)):
            if any(alpha[i] == alpha[i-1] and orders[i] < orders[i-1] for i in range(1, k)):
                continue
            survive = True
            for q in routes:
                os = [q//math.gcd(q, n//d) for d in orders]
                blocks = sum(a//o for a, o in zip(alpha, os))
                rem = sum(a % o for a, o in zip(alpha, os))
                thresholds = [0, 3*q-2]
                second = {2: 7, 3: 12, 4: 20, 5: 22}[q]
                thresholds += [second+j*(3*q-2) for j in range(3*n)]
                guaranteed = max(j for j, t in enumerate(thresholds) if t <= rem)
                if blocks+guaranteed >= 3*(n//q)-2:
                    survive = False
                    break
            if survive:
                out.add(tuple(sorted(zip(orders, alpha))))
    return sorted(out)


def verify(values, alpha, n):
    witness = ip.box_zero(values, alpha, n)
    seq = [g for g, a in zip(values, alpha) for _ in range(a)]
    a = checker_a.is_zero_sumfree(seq, (n,)*3)[0]
    b = checker_b.is_zero_sumfree(seq, (n,)*3)
    assert a == b == (witness is None), (n, values, alpha, witness, a, b)
    if witness is not None:
        assert any(witness) and all(0 <= x <= m for x, m in zip(witness, alpha))
        assert all(sum(x*g[j] for x, g in zip(witness, values)) % n == 0 for j in range(3))
    return a


def main():
    start = time.perf_counter()
    out = {'environment': {'python': sys.version, 'platform': platform.platform(), 'numpy': numpy.__version__},
           'scope': 'S114-V1/V2; settled groups only; no target sequence search', 'profiles': {}, 'preflight': []}
    old = json.loads((ROOT/'sessions/S112/ROUTE_SIEVE.json').read_text())['cases']
    for n, k in [(15, 6), (20, 7)]:
        ps = profiles(n, k)
        assert len(ps) == old[str(n)]['surviving_patterns_by_k'][str(k)]
        # S112 truncates its saved n20 example list at 40; compare every saved entry.
        previous = {tuple(map(tuple, p)) for p in old[str(n)]['examples_first_surviving_k']}
        assert previous <= set(ps)
        out['profiles'][str(n)] = {'count': len(ps), 'patterns': ps, 'saved_S112_examples_matched': len(previous)}
        # Comparison only after independent output is complete; no imported sieve logic above.
        import route_sieve
        _, old_counts, old_lists = route_sieve.count_B(n, k, keep=200)
        assert set(ps) == {tuple(map(tuple, p)) for p in old_lists[k]}
        assert len(ps) == old_counts[k]
        out['profiles'][str(n)]['full_fresh_S112_B_list_match'] = True
        assert all(d == n for pattern in ps for d, a in pattern)
        print('profiles', n, len(ps), flush=True)
    for n, primes, alpha in [(2, (2,), (1,)*6), (3, (3,), (2,2,2,1)), (6, (2,3), (4,)*4)]:
        begin = time.perf_counter()
        components = [list(ip.rref_images(p, len(alpha))) for p in primes]
        for p, cs in zip(primes, components):
            assert len(cs) == len(set(cs)) == ip.gaussian(len(alpha), 3, p)
        count = valid = 0
        for cs in it.product(*components):
            assert time.perf_counter()-start < 600, 'bounded validation budget exhausted'
            count += 1
            values = ip.crt_images(primes, cs)
            if len(set(values)) != len(values) or any(ip.order(g, n) != n for g in values):
                continue
            valid += 1
            assert not verify(values, alpha, n)
        out['preflight'].append({'n': n, 'alpha': alpha, 'representatives': count, 'distinct_full_order': valid,
                                 'three_checkers_agree': True, 'seconds': time.perf_counter()-begin})
        print('preflight', out['preflight'][-1], flush=True)
    for n in (2,3,4,5,6):
        basis = ((1,0,0),(0,1,0),(0,0,1))
        assert verify(basis, (n-1,)*3, n)
        assert not verify(basis, (n,n-1,n-1), n)
    # V2 first explicit refutation of pure-component sufficiency.
    begin = time.perf_counter()
    tested = 0
    for gs in it.permutations([g for g in it.product(range(6), repeat=3) if ip.order(g,6)==6], 2):
        tested += 1
        assert time.perf_counter()-begin < 60
        if all(ip.local_pure_zero(gs, (1,1), 6, p) is None for p in (2,3)):
            witness = ip.box_zero(gs, (1,1), 6)
            if witness is not None:
                assert not verify(gs, (1,1), 6)
                out['lemma_counterexample'] = {'n':6, 'values':gs, 'alpha':[1,1], 'zero_coefficients':witness, 'pairs_tested':tested,
                                              'minimal_length_reason':'one nonzero term has no zero; length two is minimal'}
                break
    assert 'lemma_counterexample' in out
    # Fixed settled sample: no randomness and no target enumeration.
    begin = time.perf_counter()
    cases = 0
    digest = hashlib.sha256()
    c2 = next(c for c in ip.rref_images(2,6) if all(any(g) for g in c))
    valid_benchmark = 0
    for c3 in it.islice(ip.rref_images(3,6), 256):
        assert time.perf_counter()-begin < 60
        values = ip.crt_images((2,3),(c2,c3))
        valid_benchmark += int(len(set(values)) == 6 and all(ip.order(g, 6) == 6 for g in values))
        witness = ip.box_zero(values, (1,3,3,3,3,3), 6)
        digest.update(json.dumps([values,witness]).encode())
        cases += 1
    elapsed = time.perf_counter()-begin
    out['benchmark'] = {'n':6, 'k':6, 'alpha':[1,3,3,3,3,3], 'cases':cases, 'seconds':elapsed,
                        'seconds_per_case':elapsed/cases, 'output_sha256':digest.hexdigest(),
                        'distinct_full_order_cases':valid_benchmark,
                        'limitation':'lexicographic prefix, includes invalid supports; not a target throughput prediction'}
    a,b = ip.gaussian(6,3,3),ip.gaussian(6,3,5)
    out['cost'] = {'n15_components':[a,b], 'n15_pairs_per_profile':a*b, 'n15_five_profiles':5*a*b,
                   'n20_rank3_free_image_components':[2**12*ip.gaussian(7,3,2),ip.gaussian(7,3,5)],
                   'note':'all regenerated profiles at both targets have full-order values; n20 local-ring enumerator not implemented'}
    out['seconds'] = time.perf_counter()-start
    out['code_sha256'] = {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                          [Path(__file__), ROOT/'tools/zsf/image_profile.py', ROOT/'tools/zsf/checker_a.py', ROOT/'tools/zsf/checker_b.py']}
    (ROOT/'sessions/S114/RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS', out['seconds'], 'seconds', flush=True)


if __name__ == '__main__':
    main()
