"""S103 unit tests and cross-validation for the exact zero-sumfree checkers.

Run:  python -I tools/zsf/test_zsf.py   (from repository root; prints JSON summary)
Deterministic: all randomness uses random.Random(seed) with recorded seeds.
"""
import json, os, random, sys, hashlib, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import checker_a as A
import checker_b as B
import brute as C

results = {}


def both(seq, mods):
    a, _ = A.is_zero_sumfree(seq, mods)
    b = B.is_zero_sumfree(seq, mods)
    if a != b:
        raise AssertionError(f"A/B disagree on {seq} mod {mods}: {a} {b}")
    if not b:
        w = B.zero_sum_witness(seq, mods)
        assert w is not None and B.verify_witness(seq, mods, w), (seq, w)
    return a


def standard(n):
    return [(1, 0, 0)] * (n - 1) + [(0, 1, 0)] * (n - 1) + [(0, 0, 1)] * (n - 1)


# 1. empty sequence
for n in (2, 15, 20):
    assert both([], (n, n, n)) is True
results["empty_sequence"] = "PASS"

# 2. zero element alone and inside
for n in (2, 15, 20):
    assert both([(0, 0, 0)], (n, n, n)) is False
    assert both([(1, 2, 3), (0, 0, 0), (4, 5, 6)], (n, n, n)) is False
    assert both([(n, 0, 2 * n)], (n, n, n)) is False  # wraps to zero
results["zero_element"] = "PASS"

# 3. duplicates: g^(ord-1) zero-sumfree, g^ord not; g, -g not
for n in (2, 3, 15, 20):
    g = (1, 0, 0)
    assert both([g] * (n - 1), (n, n, n)) is True
    assert both([g] * n, (n, n, n)) is False
    assert both([(3, 4, 5), (n - 3, n - 4, n - 5)], (n, n, n)) is False
results["duplicates_and_inverses"] = "PASS"

# 4. modular wraparound: (n-1,0,0) + (1,0,0) = 0 ; (n-1,n-1,n-1)+(1,1,1)=0
for n in (15, 20):
    assert both([(n - 1, 0, 0), (1, 0, 0)], (n, n, n)) is False
    assert both([(n - 1, n - 1, n - 1), (1, 1, 1)], (n, n, n)) is False
    assert both([(n - 1, n - 1, n - 1), (2, 1, 1)], (n, n, n)) is True
    assert both([(-1, 0, 0), (1, 0, 0)], (n, n, n)) is False  # negative input normalised
results["modular_wraparound"] = "PASS"

# 5. standard 3(n-1) lower-bound sequence: zero-sumfree AND saturating
std = {}
for n in (15, 20):
    s = standard(n)
    t0 = time.perf_counter(); okA, _ = A.is_zero_sumfree(s, (n, n, n)); tA = time.perf_counter() - t0
    t0 = time.perf_counter(); okB = B.is_zero_sumfree(s, (n, n, n)); tB = time.perf_counter() - t0
    assert okA and okB
    sat = int(A.subset_sums(s, (n, n, n)).sum())
    cnt, _ = B.subset_counts(s, (n, n, n))
    satB = sum(1 for v in cnt if v > 0)
    assert sat == satB == n ** 3
    # every one-element extension fails (consequence of saturation)
    for x in range(n):
        for y in range(0, n, 7):
            assert both(s + [(x, y, (x + y) % n)], (n, n, n)) is False
    std[n] = {"length": len(s), "zero_sumfree_A": okA, "zero_sumfree_B": okB,
              "sigma_size_A": sat, "sigma_size_B": satB, "group_order": n ** 3,
              "seconds_A": round(tA, 4), "seconds_B": round(tB, 4)}
results["standard_sequence"] = std

# 6. seeded random short sequences vs brute force, several groups
cross = {}
for mods, seed, trials, Lmax in [((2, 2, 2), 1, 400, 6), ((3, 3, 3), 2, 400, 8), ((4, 4, 4), 3, 300, 10),
                                 ((5, 5, 5), 4, 300, 12), ((6, 6, 6), 5, 200, 12), ((15, 15, 15), 6, 200, 12),
                                 ((20, 20, 20), 7, 200, 12), ((2, 4, 8), 8, 300, 10)]:
    rng = random.Random(seed)
    nzsf = 0
    for _ in range(trials):
        L = rng.randint(0, Lmax)
        # bias toward few distinct values so both outcomes occur
        base = [tuple(rng.randrange(m) for m in mods) for _ in range(rng.randint(1, 4))]
        seq = [rng.choice(base) if rng.random() < 0.5 else tuple(rng.randrange(m) for m in mods) for _ in range(L)]
        a = both(seq, mods)
        c = C.is_zero_sumfree(seq, mods)
        assert a == c, (seq, mods, a, c)
        nzsf += a
    cross["x".join(map(str, mods))] = {"seed": seed, "trials": trials, "zero_sumfree": nzsf, "agree_A_B_brute": True}
results["random_vs_bruteforce"] = cross

# 7. oracle rollback exactness and push legality == checker
rng = random.Random(11)
for n in (15, 20):
    mods = (n, n, n)
    o = A.Oracle(mods)
    snaps = [o.sig.copy()]
    pushed = 0
    for step in range(4000):
        if o.seq and rng.random() < 0.35:
            o.pop(); snaps.pop()
            assert (o.sig == snaps[-1]).all()
        else:
            g = tuple(rng.randrange(n) for _ in range(3))
            lm = o.legal_mask()
            assert bool(lm[g]) == o.legal(g)
            if o.push(g):
                pushed += 1
                snaps.append(o.sig.copy())
                assert (o.sig == A.subset_sums(o.seq, mods)).all()
    assert both(o.seq, mods) is True
    results[f"oracle_rollback_n{n}"] = {"seed": 11, "steps": 4000, "pushes": pushed, "final_len": len(o.seq), "status": "PASS"}


# 8. exhaustive max zero-sumfree length for small groups (DFS over multisets in
#    nondecreasing element order via Oracle) vs known D: p-groups / rank<=2 D=D*.
def max_zsf(mods):
    elems = [e for e in __import__("itertools").product(*[range(m) for m in mods]) if any(e)]
    o = A.Oracle(mods)
    best = [0, None]
    nodes = [0]

    def dfs(start):
        nodes[0] += 1
        if len(o.seq) > best[0]:
            best[0] = len(o.seq); best[1] = list(o.seq)
        for i in range(start, len(elems)):
            if o.push(elems[i]):
                dfs(i)
                o.pop()
    dfs(0)
    return best[0], best[1], nodes[0]

exh = {}
for mods, Dstar in [((2, 2, 2), 4), ((3, 3), 5), ((2, 4), 5), ((4, 4), 7), ((2, 2, 4), 6), ((3, 3, 3), 7)]:
    t0 = time.perf_counter()
    m, ex, nodes = max_zsf(mods)
    assert m == Dstar - 1, (mods, m)
    assert B.is_zero_sumfree(ex, mods) and C.is_zero_sumfree(ex, mods) if len(ex) <= 16 else True
    exh["x".join(map(str, mods))] = {"max_zsf_len": m, "D": m + 1, "expected_Dstar": Dstar,
                                     "dfs_nodes": nodes, "seconds": round(time.perf_counter() - t0, 2)}
results["exhaustive_small_groups"] = exh

results["overall"] = "PASS"
print(json.dumps(results, indent=1, sort_keys=True))
