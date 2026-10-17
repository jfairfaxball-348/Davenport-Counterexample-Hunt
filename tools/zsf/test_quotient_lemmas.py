"""S106 exact tests of the multiplicity/quotient lemmas CLM-0348..0351 on SETTLED
small groups only (no n=15/20 search).  Independent of the hand proofs: every
equivalence is checked by direct exact subset-sum computation.

  CLM-0348  every g of order n in (Z/n)^3 completes to a basis (explicit matrix,
            determinant a unit mod n) -- checked exhaustively for n in 2..20.
  CLM-0349  g^(m-1) T zero-sumfree  <=>  no nonempty subsequence of T sums into <g>.
  CLM-0351  g^(m-2) T zero-sumfree (v_g(T)=0) <=> every nonempty subsequence of T
            with sum in <g> has sum exactly g.
  CLM-0350  (consequence with D(C_n^2)=2n-1): exhaustive check that in (Z/n)^3,
            n=3,4, no zero-sumfree sequence g^(n-1) T has |T| > 2n-2, by exhaustive
            DFS over T (nondecreasing order) with the CLM-0349 criterion.
Run: python -I tools/zsf/test_quotient_lemmas.py"""
import itertools, json, math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import checker_b as B


def nonempty_sums(T, mods):
    """Boolean array N with N[x] True iff x = sum of a NONEMPTY subsequence of T."""
    N = np.zeros(mods, dtype=bool)
    for t in T:
        t = tuple(int(v) % m for v, m in zip(t, mods))
        N = N | A.translate(N, t)
        N[t] = True
    return N


def cyclic(g, mods):
    out, x = [], tuple([0] * len(mods))
    while True:
        out.append(x)
        x = tuple((a + b) % m for a, b, m in zip(x, g, mods))
        if x == out[0]:
            return out


def order(g, mods):
    return len(cyclic(g, mods))


def det3(M, n):
    a, b, c = M
    return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0])) % n


def complete_basis(g, n):
    """CLM-0348 construction: per prime power p^k || n pick i with a_i a unit mod p,
    complete with the other unit vectors; glue the three columns by CRT."""
    fac = {}
    m = n
    p = 2
    while m > 1:
        while m % p == 0:
            fac[p] = fac.get(p, 1) * p
            m //= p
        p += 1
    cols_by_q = {}
    for p, q in fac.items():
        i = next(j for j in range(3) if g[j] % p)
        others = [j for j in range(3) if j != i]
        e = lambda j: tuple(1 if k == j else 0 for k in range(3))
        cols_by_q[q] = [tuple(x % q for x in g), e(others[0]), e(others[1])]
    cols = []
    for c in range(3):
        vec = []
        for k in range(3):
            x = 0
            for q, cl in cols_by_q.items():   # CRT
                Q = n // q
                x += cl[c][k] * Q * pow(Q, -1, q)
            vec.append(x % n)
        cols.append(tuple(vec))
    return cols


out = {}
# CLM-0348
cnt = 0
for n in range(2, 21):
    for g in itertools.product(range(n), repeat=3):
        if math.gcd(math.gcd(math.gcd(*g), n), n) != 1:
            continue
        M = complete_basis(g, n)
        assert M[0] == tuple(x % n for x in g)
        assert math.gcd(det3(M, n), n) == 1, (n, g)
        cnt += 1
out["clm0348_basis_completions_checked"] = cnt

rng = random.Random(106)
agree49 = agree51 = 0
for n in (3, 4, 5, 6, 8, 9, 10, 12):
    mods = (n, n, n)
    for _ in range(250):
        g = tuple(rng.randrange(n) for _ in range(3))
        if g == (0, 0, 0):
            continue
        m = order(g, mods)
        H = set(cyclic(g, mods))
        T = [tuple(rng.randrange(n) for _ in range(3)) for _ in range(rng.randint(0, 6))]
        N = nonempty_sums(T, mods)
        # CLM-0349
        lhs = A.is_zero_sumfree([g] * (m - 1) + T, mods)[0]
        assert lhs == B.is_zero_sumfree([g] * (m - 1) + T, mods)
        rhs = not any(N[h] for h in H)
        assert lhs == rhs, ("0349", n, g, T)
        agree49 += 1
        # CLM-0351 (m>=3, g not in T)
        if m >= 3 and g not in [tuple(x % n for x in t) for t in T]:
            lhs = A.is_zero_sumfree([g] * (m - 2) + T, mods)[0]
            rhs = all((not N[h]) or h == g for h in H)
            assert lhs == rhs, ("0351", n, g, T)
            agree51 += 1
out["clm0349_random_agreements"] = agree49
out["clm0351_random_agreements"] = agree51

# CLM-0350 exhaustive in (Z/n)^3, n=3,4: max |T| with g^(n-1)T zsf equals 2n-2 (g=e1 suffices
# by CLM-0348 + automorphism invariance CLM-0345(d); also checked for one non-basis g).
for n in (3, 4):
    mods = (n, n, n)
    elems = list(itertools.product(range(n), repeat=3))
    res = {}
    for g in ((1, 0, 0), (1, 1, n - 1)):
        H = set(cyclic(g, mods))
        best = 0

        def dfs(start, T, N):
            global best
            best = max(best, len(T))
            for i in range(start, len(elems)):
                t = elems[i]
                N2 = N | A.translate(N, t)
                N2[t] = True
                if not any(N2[h] for h in H):
                    dfs(i, T + [t], N2)
        dfs(0, [], np.zeros(mods, dtype=bool))
        assert best == 2 * n - 2, (n, g, best)
        res[str(g)] = best
    out[f"clm0350_exhaustive_n{n}_max_T"] = res
out["overall"] = "PASS"
print(json.dumps(out, indent=1))
