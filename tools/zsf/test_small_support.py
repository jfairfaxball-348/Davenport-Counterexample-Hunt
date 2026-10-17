"""S108 exact tests of CLM-0358..0360 on SMALL groups only (n <= 10; no n=15/20 work).
Independent of the hand proofs: maximum zero-sumfree length over a fixed support is
computed by brute force over multiplicity vectors with the box/kernel criterion, and the
maximisers are re-checked by checkers A and B.

  CLM-0358  box/kernel criterion: with distinct values a_1..a_k and multiplicities
            alpha_i <= n-1, S is zero-sumfree iff no nonzero r in
            K = {r in (Z/n)^k : sum r_i a_i = 0} has <r_i> <= alpha_i for all i
            (<x> = least nonnegative residue mod n).
  CLM-0359  counting bound |S| <= k(n-1) - n + n/|K|; hence |supp S| <= r+1 over C_n^r
            implies |S| <= r(n-1)  (r = 2, 3 tested).
  CLM-0360  relation bound: for every r in K of order n,
            sum_{i in supp r} (n-1-alpha_i) >= n-1.
Run: python -I tools/zsf/test_small_support.py"""
import itertools, json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import checker_b as B


def kernel(vals, n, rank):
    k = len(vals)
    V = np.array(vals, dtype=np.int64)              # k x rank
    R = np.array(list(itertools.product(range(n), repeat=k)), dtype=np.int64)
    s = (R @ V) % n
    return R[(s == 0).all(axis=1)]


def max_len(vals, n, rank):
    K = kernel(vals, n, rank)
    Kn = K[(K != 0).any(axis=1)]
    k = len(vals)
    best, arg = -1, None
    for alpha in itertools.product(range(n), repeat=k):
        a = np.array(alpha)
        # zero-sumfree iff every nonzero kernel vector escapes the box somewhere
        if len(Kn) == 0 or (Kn > a).any(axis=1).all():
            if sum(alpha) > best:
                best, arg = sum(alpha), alpha
    return best, arg, len(K), Kn


def order_mod(v, n):
    o = 1
    while any((o * x) % n for x in v):
        o += 1
    return o


out = {}
rng = random.Random(108)
cnt = {}
crit_checks = rel_checks = 0
for rank, ns in ((2, (2, 3, 4, 5, 6, 7, 8, 9, 10)), (3, (2, 3, 4, 5, 6))):
    for n in ns:
        mods = (n,) * rank
        trials = 40 if (rank == 3 and n >= 5) else 80
        for _ in range(trials):
            k = rank + 1 if rng.random() < 0.85 else rng.randint(1, rank)
            vals = []
            while len(vals) < k:
                v = tuple(rng.randrange(n) for _ in range(rank))
                if any(v) and v not in vals:
                    vals.append(v)
            best, arg, Ksize, Kn = max_len(vals, n, rank)
            # CLM-0359 bound (k <= rank+1)
            assert best <= rank * (n - 1), (rank, n, vals, best)
            assert best <= k * (n - 1) - n + n / Ksize + 1e-9, (rank, n, vals, best, Ksize)
            # maximiser really zero-sumfree (independent checkers) and one more copy of any value is not
            S = [v for v, a in zip(vals, arg) for _ in range(a)]
            if S:
                assert A.is_zero_sumfree(S, mods)[0] and B.is_zero_sumfree(S, mods)
            # CLM-0358 criterion vs checkers on random multiplicity vectors
            for _ in range(5):
                alpha = [rng.randrange(n) for _ in vals]
                S2 = [v for v, a in zip(vals, alpha) for _ in range(a)]
                crit = len(Kn) == 0 or (Kn > np.array(alpha)).any(axis=1).all()
                zA = A.is_zero_sumfree(S2, mods)[0] if S2 else True
                assert crit == zA == (B.is_zero_sumfree(S2, mods) if S2 else True), (vals, alpha)
                crit_checks += 1
                # CLM-0360 for zero-sumfree instances
                if zA:
                    for r in Kn:
                        if order_mod(r, n) == n:
                            assert sum(n - 1 - alpha[i] for i in range(len(vals)) if r[i] % n) >= n - 1
                            rel_checks += 1
            cnt[f"r{rank}_n{n}"] = cnt.get(f"r{rank}_n{n}", 0) + 1
out["supports_checked"] = cnt
out["clm0358_criterion_agreements"] = crit_checks
out["clm0360_relation_checks"] = rel_checks
# exhaustive: every 4-element support in C_3^3 and C_2^3 (all nonzero values)
for n in (2, 3):
    elems = [v for v in itertools.product(range(n), repeat=3) if any(v)]
    worst = 0
    for vals in itertools.combinations(elems, 4):
        best, _, _, _ = max_len(list(vals), n, 3)
        worst = max(worst, best)
    assert worst <= 3 * (n - 1)
    out[f"exhaustive_4_supports_C{n}^3_max_len"] = worst
out["overall"] = "PASS"
print(json.dumps(out, indent=1))
