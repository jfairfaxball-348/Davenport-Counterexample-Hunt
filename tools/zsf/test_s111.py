"""S111 exact tests on SETTLED / small groups only (no C15^3 or C20^3 sequence).

  T1  even-n caps: mechanical re-derivation from the CLM-0355 bound
      |S| <= m - d + d(Q), Q = C_{nd/m} + C_n + C_n, using only Q with nd/m = 2
      (D(C2+Cn+Cn) = 2n, CLM-0356) and nd/m = 1 (rank two, CLM-0352), even n <= 400.
  T2  even-n caps: random exact transfer instances at n = 4..14: maximal zero-sumfree
      S = h^(n-2) T (ord h = n) and S = h^(n/2-1) T (ord h = n/2), lengths vs bounds.
  T3  CLM-0369/0370 (a = 2 block reduction), constructive: for random sequences of length
      r(n-1)+1 with <= r+2 distinct values over C_n^r, n = 2b, the proof's procedure
      produces a nonempty zero-sum, verified by checkers A and B.
  T4  CLM-0372 obstruction: exact maximum mod-a block packing (a = 3, 5) for the exhibited
      n = 15 instances, by minimal-block DP, cross-checked by all-block recursion.
  T5  CLM-0372 (even-n parity structure, r = 3): random 6/7-valued sequences of length
      3n-2, n = 4..14; outside the residual Fano case the procedure yields a verified
      zero-sum; plus the exact Fano-complement fact over F_2^3.
Run: python -I tools/zsf/test_s111.py <out.json>"""
import itertools, json, os, random, sys
from functools import lru_cache
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import checker_b as B

out = {}
rng = random.Random(111)


def divisors(x):
    return [d for d in range(1, x + 1) if x % d == 0]


# ---------------- T1 ----------------
def caps(n):
    """Return {m: cap} for orders m | n, using the e=1 and e=2 levers only."""
    res, levers = {}, []
    for m in divisors(n)[1:]:
        excluded = set()
        for d in divisors(m):
            e = n * d // m
            if (n * d) % m or e not in (1, 2):
                continue
            dQ = (n + n - 1) if e == 2 else (2 * n - 2)  # d(Q) = D(Q) - 1
            for j in range(1, d + 1):
                bound = m - d + dQ
                formula = (n + 1 + d) > (m + e) if e == 2 else (n + 2 > m + 1)
                assert (bound < 3 * n - 2) == formula
                if bound < 3 * n - 2:
                    excluded.add(m - j)
                    levers.append((m, d, e, j))
        cap = m - 1
        while cap in excluded:
            cap -= 1
        res[m] = cap
    return res, levers


t1 = []
for n in range(4, 401, 2):
    c, lev = caps(n)
    assert c[n] == n - 3, n
    assert c[n // 2] == n // 2 - 2, n
    assert all(c[m] == m - 1 for m in c if m not in (n, n // 2)), n
    assert {(m, d) for m, d, e, j in lev if e == 2} == {(n, 2), (n // 2, 1)}, n
    t1.append(n)
out["T1_even_caps_mechanical"] = {"n_checked": f"even 4..400 ({len(t1)} values)",
                                  "result": "order-n cap n-3, order-n/2 cap n/2-2, no other order changed; "
                                            "only (m,d) = (n,2), (n/2,1) give nd/m = 2", "pass": True}


# ---------------- helpers ----------------
def sigma_add(sig, g):
    return sig | A.translate(sig, g)


def greedy_max(prefix, mods, forbid, rng):
    sig = A.empty_sigma(mods)
    for g in prefix:
        assert not sig[A.neg(g, mods)]
        sig = sigma_add(sig, g)
    S = list(prefix)
    cand = [g for g in itertools.product(*[range(m) for m in mods]) if any(g) and g not in forbid]
    grew = True
    while grew:
        grew = False
        rng.shuffle(cand)
        for g in cand:
            if not sig[A.neg(g, mods)]:
                S.append(g); sig = sigma_add(sig, g); grew = True
    return S


# ---------------- T2 ----------------
t2 = {}
for n in (4, 6, 8, 10, 12, 14):
    mods = (n, n, n)
    trials = 60 if n <= 8 else 25
    rec = {}
    for label, h, mult, bound in (("ord_n_mult_n-2", (1, 0, 0), n - 2, 3 * n - 3),
                                  ("ord_n/2_mult_n/2-1", (2, 0, 0), n // 2 - 1, 5 * n // 2 - 2)):
        best = 0
        for _ in range(trials):
            S = greedy_max([h] * mult, mods, {h}, rng)
            assert A.is_zero_sumfree(S, mods)[0] and B.is_zero_sumfree(S, mods)
            assert S.count(h) == mult and len(S) <= bound, (n, label, len(S))
            best = max(best, len(S))
        rec[label] = {"trials": trials, "max_length_found": best, "bound": bound}
    t2[n] = rec
out["T2_even_caps_transfer_random"] = {"cases": t2, "pass": True}


# ---------------- T3 ----------------
D_known = {}  # D(C_b^r) = r(b-1)+1 used only as the proof's premise; witness search is exact


def a2_reduction(S, n, r):
    """Proof procedure of CLM-0370 for a = 2. Returns indices of a nonempty zero-sum."""
    b = n // 2
    vals = sorted(set(S))
    idx = {v: [i for i, s in enumerate(S) if s == v] for v in vals}
    blocks, left = [], []
    for v in vals:
        o = 1 if all(x % 2 == 0 for x in v) else 2
        I = idx[v]
        q = len(I) // o
        blocks += [I[k * o:(k + 1) * o] for k in range(q)]
        left += I[q * o:]
    need = r * (b - 1) + 1
    extra = 0
    if len(blocks) < need:
        img = [tuple(x % 2 for x in S[i]) for i in left]
        w = B.zero_sum_witness(img, (2,) * r)
        assert w is not None
        blocks.append([left[k] for k in w]); extra = 1
    assert len(blocks) >= need, "more than one extra block needed"
    bs = []
    for blk in blocks:
        s = [sum(S[i][c] for i in blk) % n for c in range(r)]
        assert all(x % 2 == 0 for x in s)
        bs.append(tuple((x // 2) % b for x in s))
    w = B.zero_sum_witness(bs, (b,) * r)
    assert w is not None, "block sums zero-sumfree: would contradict D(C_b^r)"
    return sorted(i for k in w for i in blocks[k]), extra


t3 = {}
for r, ns, trials in ((2, (4, 6, 8, 10), 300), (3, (4, 6, 8, 10, 12, 14), 200), (4, (4, 6), 100)):
    for n in ns:
        mods = (n,) * r
        L = r * (n - 1) + 1
        ext = [0, 0]
        for _ in range(trials):
            k = r + 2
            vals = set()
            while len(vals) < k:
                g = tuple(rng.randrange(n) for _ in range(r))
                if any(g):
                    vals.add(g)
            vals = list(vals)
            while True:
                al = [rng.randrange(n) for _ in range(k)]
                s = sum(al)
                if s >= L:
                    break
            # trim to exactly L keeping al_i <= n-1
            while sum(al) > L:
                i = rng.randrange(k)
                if al[i] > 0:
                    al[i] -= 1
            S = [v for v, m in zip(vals, al) for _ in range(m)]
            rng.shuffle(S)
            w, e = a2_reduction(S, n, r)
            assert B.verify_witness(S, mods, w)
            sub = [S[i] for i in w]
            assert not A.is_zero_sumfree(sub, mods)[0] and not B.is_zero_sumfree(sub, mods)
            ext[e] += 1
        t3[f"r{r}_n{n}"] = {"trials": trials, "length": L, "extra_block_used": ext[1], "no_extra": ext[0]}
out["T3_a2_reduction_constructive"] = {"cases": t3, "pass": True}


# ---------------- T4 ----------------
def packing(a, vals, alpha, cap):
    """Exact maximum number of disjoint nonempty subsequences with sum 0 in C_a^3.
    dp: recursion over MINIMAL zero-sum vectors (every packing refines to one);
    brute: recursion over ALL zero-sum sub-vectors of length <= cap = D(C_a^3)."""
    V = np.array(vals)
    zero = lambda y: not ((np.array(y) @ V) % a).any()
    zs = [x for x in itertools.product(range(a + 1), repeat=5) if any(x) and zero(x)]
    M = [x for x in zs if not any(any(y) and y != x and zero(y)
                                  for y in itertools.product(*[range(c + 1) for c in x]))]

    @lru_cache(maxsize=None)
    def dp(al):
        return max([1 + dp(tuple(p - c for p, c in zip(al, x))) for x in M
                    if all(c <= p for c, p in zip(x, al))] + [0])

    @lru_cache(maxsize=None)
    def brute(rem):
        best = 0
        for y in itertools.product(*[range(c + 1) for c in rem]):
            if any(y) and sum(y) <= cap and zero(y):
                best = max(best, 1 + brute(tuple(p - c for p, c in zip(rem, y))))
        return best
    return len(M), dp, brute


t4 = {}
for a, b, vals, alpha, small in ((3, 5, [(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 1, 2)],
                                  (2, 2, 11, 14, 14), (2, 2, 5, 5, 5)),
                                 (5, 3, [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1), (1, 1, 2)],
                                  (4, 3, 9, 14, 13), (4, 3, 4, 9, 8))):
    nM, dp, brute = packing(a, vals, alpha, 3 * a - 2)
    pd = dp(alpha)
    need = 3 * b - 2
    assert sum(alpha) == 3 * a * b - 2 and max(alpha) <= a * b - 1 and pd < need
    # minimal zero-sums have length <= D(C_a^3) = 3a-2, so the brute cut is exact
    assert brute(small) == dp(small)
    t4[f"a{a}_b{b}"] = {"n": a * b, "values_mod_a": vals, "alpha": alpha, "minimal_zero_sum_vectors": nM,
                        "max_packing": pd, "needed_D(C_b^3)": need,
                        "cross_check": {"alpha": small, "dp": dp(small), "brute": brute(small)}}
out["T4_odd_packing_obstructions"] = {"cases": t4, "pass": True}

# ---------------- T5 ----------------
def disjoint_pair(img):
    """Two disjoint nonempty zero-sum index sets of a short sequence over C_2^3, or None."""
    k = len(img)
    zs = [m for m in range(1, 1 << k)
          if not any(sum(img[i][c] for i in range(k) if m >> i & 1) % 2 for c in range(3))]
    for x in zs:
        for y in zs:
            if x & y == 0:
                return [i for i in range(k) if x >> i & 1], [i for i in range(k) if y >> i & 1]
    return None


def parity_reduction(S, n):
    """Proof procedure of CLM-0372 (r = 3, n = 2b). Returns (witness or None, |O|, residual)."""
    b = n // 2
    vals = sorted(set(S))
    idx = {v: [i for i, s in enumerate(S) if s == v] for v in vals}
    blocks, left = [], []
    for v in vals:
        o = 1 if all(x % 2 == 0 for x in v) else 2
        I = idx[v]
        q = len(I) // o
        blocks += [I[k * o:(k + 1) * o] for k in range(q)]
        left += I[q * o:]
    O = len(left)
    img = [tuple(x % 2 for x in S[i]) for i in left]
    residual = O == 6 and len(set(img)) == 6
    need = 3 * b - 2
    deficit = need - len(blocks)
    assert deficit <= max(0, (O - 2) // 2)
    if deficit >= 1:
        if deficit == 1:
            w = B.zero_sum_witness(img, (2, 2, 2))
            assert w is not None
            blocks.append([left[k] for k in w])
        else:
            assert deficit == 2
            pr = disjoint_pair(img)
            if pr is None:
                assert residual, "two disjoint mod-2 zero-sums missing outside the residual case"
                return None, O, True
            blocks += [[left[k] for k in pr[0]], [left[k] for k in pr[1]]]
    bs = [tuple((sum(S[i][c] for i in blk) % n) // 2 for c in range(3)) for blk in blocks]
    w = B.zero_sum_witness(bs, (b, b, b))
    assert w is not None
    return sorted(i for k in w for i in blocks[k]), O, residual


t5 = {}
for n in (4, 6, 8, 10, 12, 14):
    mods = (n, n, n)
    L = 3 * n - 2
    stats = {"trials": 0, "zero_sum_found": 0, "residual_unhandled": 0, "O_hist": {}}
    for trial in range(150):
        k = rng.choice((6, 7))
        force_residual = trial % 5 == 0
        vals = set()
        if force_residual:
            P = rng.choice([v for v in itertools.product((0, 1), repeat=3) if any(v)])
            for im in itertools.product((0, 1), repeat=3):
                if any(im) and im != P:
                    vals.add(tuple(x + 2 * rng.randrange(n // 2) for x in im))
        while len(vals) < k:
            g = tuple(rng.randrange(n) for _ in range(3))
            if any(g):
                vals.add(g)
        vals = list(vals)
        while True:
            al = [rng.randrange(n) for _ in range(k)]
            if trial % 2 == 0:
                al = [x | 1 if x < n - 1 or (n - 1) % 2 else x - 1 for x in al]
            if sum(al) >= L:
                break
        while sum(al) > L:
            i = rng.randrange(k)
            if al[i] > 1 or (al[i] > 0 and not force_residual):
                al[i] -= 1
        S = [v for v, m in zip(vals, al) for _ in range(m)]
        rng.shuffle(S)
        w, O, res = parity_reduction(S, n)
        stats["trials"] += 1
        stats["O_hist"][O] = stats["O_hist"].get(O, 0) + 1
        if w is None:
            stats["residual_unhandled"] += 1
            assert res and O == 6
        else:
            assert B.verify_witness(S, mods, w)
            sub = [S[i] for i in w]
            assert not A.is_zero_sumfree(sub, mods)[0] and not B.is_zero_sumfree(sub, mods)
            stats["zero_sum_found"] += 1
    t5[n] = stats
# the Fano-complement fact used in the proof: 6 distinct nonzero vectors of F_2^3 never
# contain two disjoint zero-sums, 7 distinct always do
six = [v for v in itertools.product((0, 1), repeat=3) if any(v)]
assert all(disjoint_pair([v for v in six if v != P]) is None for P in six)
assert disjoint_pair(six) is not None
out["T5_even_parity_structure"] = {"cases": t5, "fano_fact": "6 distinct nonzero: no two disjoint zero-sums; 7: yes",
                                  "pass": True}

out["overall"] = "PASS"
json.dump(out, open(sys.argv[1], "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:3000])
