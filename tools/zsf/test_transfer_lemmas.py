"""S107 exact tests of CLM-0353..0355 on SETTLED/small groups only (no n=15/20
sequence search).  Independent of the hand proofs: direct exact computation.

  CLM-0353  h^(m-j) T zero-sumfree  <=>  every nonempty subsequence of T with sum in <h>
            has sum in {h, 2h, ..., (j-1)h}            (h of order m, 1 <= j <= m)
  CLM-0354  in (Z/n)^3 every h of order m equals (n/m) u for some u of order n
            (exhaustive for all h, n = 2..20), so G/<h> ~ C_{n/m} + C_n + C_n.
  CLM-0355  transfer: if S = h^(m-j) T is zero-sumfree and d | m, j <= d, then
            hbar^(d-j) pi(T) is zero-sumfree in Q = G/<dh> ~ C_{nd/m} + C_n + C_n
            (explicit coordinates via a basis matrix with first column u).
Run: python -I tools/zsf/test_transfer_lemmas.py"""
import itertools, json, math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import checker_b as B

# helpers copied verbatim from test_quotient_lemmas.py (importing it would rerun its tests)
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




def scale(k, v, n):
    return tuple((k * x) % n for x in v)


def find_u(h, n):
    """CLM-0354 recipe: h has order m, q = n/m; every coordinate of h is divisible by q,
    w = h/q satisfies q w = h; then u = w + m t for some t (q m t = 0) has order n."""
    m = order(h, (n, n, n))
    q = n // m
    assert all(x % q == 0 for x in h)
    w = tuple(x // q for x in h)
    for t in itertools.product(range(q), repeat=3):
        u = tuple((wi + m * ti) % n for wi, ti in zip(w, t))
        if math.gcd(math.gcd(*u), n) == 1:
            assert scale(q, u, n) == tuple(x % n for x in h)
            return u
    return None


def inv3(M, n):
    """Inverse of a 3x3 matrix (columns M[0..2]) over Z/n, as rows of the inverse."""
    a = [[M[c][r] for c in range(3)] for r in range(3)]   # a[r][c]
    det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
           + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])) % n
    di = pow(det, -1, n)
    adj = [[0] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            mr = [i for i in range(3) if i != r]; mc = [j for j in range(3) if j != c]
            minor = a[mr[0]][mc[0]] * a[mr[1]][mc[1]] - a[mr[0]][mc[1]] * a[mr[1]][mc[0]]
            adj[c][r] = ((-1) ** (r + c)) * minor
    return [[(adj[r][c] * di) % n for c in range(3)] for r in range(3)]


def coords(Minv, x, n):
    return tuple(sum(Minv[r][c] * x[c] for c in range(3)) % n for r in range(3))


out = {}
# CLM-0354 exhaustive
cnt = 0
for n in range(2, 21):
    for h in itertools.product(range(n), repeat=3):
        if h == (0, 0, 0):
            continue
        m = order(h, (n, n, n))
        q = n // m
        # proof recipe: h = q w (w exists since m h = 0); fix w per prime as in the proof, else brute force
        u = find_u(h, n)
        assert u is not None, (n, h)
        cnt += 1
out["clm0354_all_nonzero_elements_checked"] = cnt

rng = random.Random(107)
a53 = 0
for n in (3, 4, 5, 6, 8, 9, 10, 12):
    mods = (n, n, n)
    for _ in range(200):
        h = tuple(rng.randrange(n) for _ in range(3))
        if h == (0, 0, 0):
            continue
        m = order(h, mods)
        j = rng.randint(1, m)
        H = cyclic(h, mods)
        T = [tuple(rng.randrange(n) for _ in range(3)) for _ in range(rng.randint(0, 6))]
        N = nonempty_sums(T, mods)
        S = [h] * (m - j) + T
        lhs = A.is_zero_sumfree(S, mods)[0]
        assert lhs == B.is_zero_sumfree(S, mods)
        allowed = {scale(k, h, n) for k in range(1, j)}
        rhs = all((not N[x]) or x in allowed for x in H)
        assert lhs == rhs, (n, h, j, T)
        a53 += 1
out["clm0353_random_agreements"] = a53

a55 = 0
for n in (4, 6, 8, 9, 10, 12):
    mods = (n, n, n)
    for _ in range(150):
        h = tuple(rng.randrange(n) for _ in range(3))
        if h == (0, 0, 0):
            continue
        m = order(h, mods)
        j = rng.randint(1, m)
        divs = [d for d in range(1, m + 1) if m % d == 0 and d >= j]
        if not divs:
            continue
        d = rng.choice(divs)
        # build a zero-sumfree S = h^(m-j) T by random legal pushes of T terms
        o = A.Oracle(mods)
        for _ in range(m - j):
            assert o.push(h)
        T = []
        for _ in range(rng.randint(0, 12)):
            t = tuple(rng.randrange(n) for _ in range(3))
            if t != tuple(x % n for x in h) and o.push(t):
                T.append(t)
        u = find_u(h, n)
        M = complete_basis(u, n)
        Minv = inv3(M, n)
        qmod = n * d // m                     # Q = C_qmod + C_n + C_n
        Qmods = (qmod, n, n)
        proj = lambda x: (lambda c: (c[0] % qmod, c[1], c[2]))(coords(Minv, x, n))
        hb = proj(h)
        assert order(hb, Qmods) == d, (n, h, d, hb)
        seqQ = [hb] * (d - j) + [proj(t) for t in T]
        okA = A.is_zero_sumfree(seqQ, Qmods)[0] if seqQ else True
        okB = B.is_zero_sumfree(seqQ, Qmods) if seqQ else True
        assert okA and okB, (n, h, j, d, T)
        a55 += 1
out["clm0355_random_transfers_checked"] = a55
out["overall"] = "PASS"
print(json.dumps(out, indent=1))
