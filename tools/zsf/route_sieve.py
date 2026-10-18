"""S112 multi-route block sieve (CLM-0374/0375): arithmetic over multiplicity patterns only.

For n and a candidate zero-sumfree S over C_n^3 with |S| = 3n-2 and k distinct values, a
"route" is a prime power a | n with D(C_a^3) and D(C_b^3), b = n/a, recorded (CLM-0039 /
0064..0066 / 0142).  For a value of order d, its image in G/aG has order o = a/gcd(a, n/d).
Route a yields a nonempty zero-sum (CLM-0369, CLM-0374) whenever
    t0 + nu_lb(R) >= D(C_b^3),   t0 = sum floor(alpha_i/o_i) (alpha_i if o_i = 1),
                                 R  = sum (alpha_i mod o_i),
where nu_lb(R) = max j with D_j(C_a^3) <= R, using D_1 = 3a-2, D_2 (7 for a = 2; 5a-3 for
odd prime a, CLM-0143; 2 D_1 otherwise) and D_j <= D_2 + (j-2) D_1.
Multiplicity caps: alpha <= d-1; order n: n-2 (CLM-0350); even n: order n <= n-3 and order
n/2 <= n/2-2 (CLM-0368).
A multiplicity pattern (multiset of (order, alpha) with sum 3n-2) SURVIVES if no route closes it.
Two independent algorithms count surviving patterns:
  A  item-by-item counting knapsack DP over additive route statistics;
  B  recursive enumeration of multisets with a separately written closure test.
Usage: python -I tools/zsf/route_sieve.py <out.json> n:kmax [n:kmax ...]
"""
import json, math, sys, time


def factor(n):
    f, p = {}, 2
    while n > 1:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    return f


def prime_power(n):
    return n > 1 and len(factor(n)) == 1


def D_recorded(b):
    """D(C_b^3) = 3b-2 recorded: b = 1, prime powers (CLM-0039/0142), 2p^k (CLM-0065),
    3*2^k incl. 6 (CLM-0064/0066)."""
    if b == 1 or prime_power(b):
        return True
    f = factor(b)
    return len(f) == 2 and ((f.get(2) == 1) or (f.get(3) == 1 and 2 in f))


def routes(n):
    out = {}
    for a in range(2, n):
        if n % a == 0 and prime_power(a) and D_recorded(n // a):
            p = min(factor(a))
            D1 = 3 * a - 2
            D2 = 7 if a == 2 else (5 * a - 3 if (a == p and p > 2) else 2 * D1)
            out[a] = {"Db": 3 * (n // a) - 2, "D1": D1, "D2": D2}
    return out


def order_types(n):
    T = []
    for d in range(2, n + 1):
        if n % d:
            continue
        amax = d - 1
        if d == n:
            amax = min(amax, n - 2)
            if n % 2 == 0:
                amax = min(amax, n - 3)
        if n % 2 == 0 and d == n // 2:
            amax = min(amax, n // 2 - 2)
        T.append((d, amax))
    return T


# ---------------- algorithm A ----------------
def nu_lb_A(R, D1, D2):
    if R < D1:
        return 0
    if R < D2:
        return 1
    return 2 + (R - D2) // D1


def count_A(n, kmax):
    RT = routes(n)
    A = sorted(RT)
    L = 3 * n - 2
    items = []
    for d, amax in order_types(n):
        os_ = [a // math.gcd(a, n // d) for a in A]
        for al in range(1, amax + 1):
            c = []
            for o in os_:
                c += [al // o, al % o] if o > 1 else [al, 0]
            items.append((al, tuple(c)))
    zero = (0, 0) + (0,) * (2 * len(A))  # (k, sum, stats...)
    dp = {zero: 1}
    for al, c in items:  # unbounded multiplicity of each item, counted as multisets
        new = dict(dp)
        frontier = dp
        while frontier:
            nxt = {}
            for st, cnt in frontier.items():
                k, s = st[0] + 1, st[1] + al
                if k > kmax or s > L:
                    continue
                key = (k, s) + tuple(x + y for x, y in zip(st[2:], c))
                nxt[key] = nxt.get(key, 0) + cnt
            for key, cnt in nxt.items():
                new[key] = new.get(key, 0) + cnt
            frontier = nxt
        dp = new
    surv = {k: 0 for k in range(1, kmax + 1)}
    for st, cnt in dp.items():
        k, s = st[0], st[1]
        if k == 0 or s != L:
            continue
        closed = any(st[2 + 2 * j] + nu_lb_A(st[3 + 2 * j], RT[a]["D1"], RT[a]["D2"]) >= RT[a]["Db"]
                     for j, a in enumerate(A))
        if not closed:
            surv[k] += cnt
    return RT, surv


# ---------------- algorithm B ----------------
def disjoint_guaranteed(R, D1, D2):
    j = 0
    while True:
        need = D1 if j == 0 else (D2 if j == 1 else D2 + (j - 1) * D1)
        if R >= need:
            j += 1
        else:
            return j


def count_B(n, kmax, keep=40):
    RT = routes(n)
    L = 3 * n - 2
    items = [(d, al) for d, amax in order_types(n) for al in range(1, amax + 1)]
    surv = {k: 0 for k in range(1, kmax + 1)}
    examples = {k: [] for k in range(1, kmax + 1)}

    def closes(pattern):
        for a, r in RT.items():
            blocks = left = 0
            for d, al in pattern:
                o = a // math.gcd(a, n // d)
                if o == 1:
                    blocks += al
                else:
                    blocks += al // o
                    left += al % o
            if blocks + disjoint_guaranteed(left, r["D1"], r["D2"]) >= r["Db"]:
                return True
        return False

    def rec(start, pattern, s):
        if s == L and pattern:
            k = len(pattern)
            if not closes(pattern):
                surv[k] += 1
                if len(examples[k]) < keep:
                    examples[k].append([list(x) for x in pattern])
            return
        if len(pattern) == kmax:
            return
        for i in range(start, len(items)):
            d, al = items[i]
            if s + al > L:
                continue
            rec(i, pattern + [(d, al)], s + al)

    rec(0, [], 0)
    return RT, surv, examples


def main():
    out = {"cases": {}}
    for arg in sys.argv[2:]:
        n, kmax = map(int, arg.split(":"))
        t0 = time.time()
        RT, sA = count_A(n, kmax)
        RT2, sB, ex = count_B(n, kmax)
        assert RT == RT2 and sA == sB, (n, sA, sB)
        first = next((k for k in range(1, kmax + 1) if sA[k]), None)
        out["cases"][str(n)] = {"routes": RT, "kmax": kmax, "surviving_patterns_by_k": sA,
                                "all_supports_excluded_up_to": (first - 1) if first else f">={kmax}",
                                "examples_first_surviving_k": ex.get(first, []) if first else [],
                                "A_equals_B": True, "seconds": round(time.time() - t0, 1)}
        print(n, sA, flush=True)
    json.dump(out, open(sys.argv[1], "w"), indent=1)


if __name__ == "__main__":
    main()
