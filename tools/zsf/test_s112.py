"""S112 exact tests on SETTLED small groups only (no C15^3 / C20^3 sequence).

  T1  D_2(C_2^3) = 7: every 7-term sequence over C_2^3 has two disjoint nonempty zero-sums,
      and six distinct nonzero vectors do not (exhaustive over multisets).
  T2  CLM-0374 soundness, constructive: random sequences of length 3n-2 with 5..7 distinct
      values over C_n^3, n in {6, 10, 12}.  For every route the sieve declares closing, the
      proof's procedure (blocks g^o, exact maximum disjoint zero-sum packing of the leftover
      image, zero-sum among block sums in aG ~ C_b^3) yields a nonempty zero-sum, verified
      by checkers A and B.
Run: python -I tools/zsf/test_s112.py <out.json>"""
import itertools, json, math, os, random, sys
from functools import lru_cache
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import checker_a as A
import checker_b as B
import route_sieve as RS

out = {}
rng = random.Random(112)

# ---------------- T1 ----------------
F2 = list(itertools.product((0, 1), repeat=3))


def two_disjoint(seq):
    k = len(seq)
    zs = [m for m in range(1, 1 << k)
          if not any(sum(seq[i][c] for i in range(k) if m >> i & 1) % 2 for c in range(3))]
    return any(x & y == 0 for x in zs for y in zs)


all7 = list(itertools.combinations_with_replacement(F2, 7))
assert all(two_disjoint(list(s)) for s in all7)
six = [v for v in F2 if any(v) and v != (1, 1, 1)]
assert not two_disjoint(six)
out["T1_D2_C2cubed"] = {"multisets_of_7": len(all7), "all_have_two_disjoint": True,
                        "six_distinct_nonzero_counterexample": six, "D_2": 7, "pass": True}


# ---------------- T2 ----------------
def order(g, n):
    return n // math.gcd(n, *g) if any(g) else 1


def max_packing(img, a):
    """Exact max number of disjoint nonempty zero-sum subsequences of img over C_a^3,
    by DP over multiplicity vectors of the distinct images (minimal zero-sum blocks)."""
    vals = sorted(set(img))
    mult = tuple(img.count(v) for v in vals)
    k = len(vals)

    def zero(x):
        return all(sum(x[i] * vals[i][c] for i in range(k)) % a == 0 for c in range(3))

    @lru_cache(maxsize=None)
    def f(rem):
        best, chosen = 0, None
        for x in itertools.product(*[range(m + 1) for m in rem]):
            if any(x) and zero(x):
                v = 1 + f(tuple(r - y for r, y in zip(rem, x)))[0]
                if v > best:
                    best, chosen = v, x
        return best, chosen
    blocks, rem = [], mult
    while True:
        v, x = f(rem)
        if not v:
            break
        blocks.append(x)
        rem = tuple(r - y for r, y in zip(rem, x))
    return vals, blocks


def route_zero_sum(S, n, a, need_check):
    b = n // a
    idx = {}
    for i, g in enumerate(S):
        idx.setdefault(g, []).append(i)
    blocks, left = [], []
    for g, I in idx.items():
        o = a // math.gcd(a, n // order(g, n))
        q = len(I) // o
        blocks += [I[j * o:(j + 1) * o] for j in range(q)]
        left += I[q * o:]
    img = [tuple(x % a for x in S[i]) for i in left]
    vals, packs = max_packing(img, a)
    pool = {v: [left[j] for j in range(len(left)) if img[j] == v] for v in vals}
    for x in packs:
        blk = []
        for v, c in zip(vals, x):
            blk += pool[v][:c]
            pool[v] = pool[v][c:]
        blocks.append(blk)
    if len(blocks) < 3 * b - 2:
        assert not need_check, "sieve said closed but blocks fall short"
        return None
    bs = []
    for blk in blocks:
        s = [sum(S[i][c] for i in blk) % n for c in range(3)]
        assert all(x % a == 0 for x in s)
        bs.append(tuple((x // a) % b for x in s))
    w = B.zero_sum_witness(bs, (b, b, b))
    assert w is not None
    return sorted(i for j in w for i in blocks[j])


t2 = {}
for n in (6, 10, 12):
    mods = (n, n, n)
    RT = RS.routes(n)
    L = 3 * n - 2
    caps = dict(RS.order_types(n))
    stats = {"routes": sorted(RT), "trials": 0, "closing_route_runs": 0, "verified": 0}
    for trial in range(120):
        k = rng.choice((5, 6, 7))
        vals = set()
        while len(vals) < k:
            g = tuple(rng.randrange(n) for _ in range(3))
            if any(g):
                vals.add(g)
        vals = list(vals)
        cap = [caps[order(g, n)] for g in vals]
        if sum(cap) < L:
            continue
        al = [rng.randint(1, c) for c in cap]
        while sum(al) != L:
            i = rng.randrange(k)
            if sum(al) > L and al[i] > 1:
                al[i] -= 1
            elif sum(al) < L and al[i] < cap[i]:
                al[i] += 1
        S = [g for g, m in zip(vals, al) for _ in range(m)]
        stats["trials"] += 1
        pattern = [(order(g, n), m) for g, m in zip(vals, al)]
        for a, r in RT.items():
            blocks = left = 0
            for d, m in pattern:
                o = a // math.gcd(a, n // d)
                blocks += m if o == 1 else m // o
                left += 0 if o == 1 else m % o
            closes = blocks + RS.nu_lb_A(left, r["D1"], r["D2"]) >= r["Db"]
            if not closes:
                continue
            stats["closing_route_runs"] += 1
            w = route_zero_sum(S, n, a, True)
            assert B.verify_witness(S, mods, w)
            sub = [S[i] for i in w]
            assert not A.is_zero_sumfree(sub, mods)[0] and not B.is_zero_sumfree(sub, mods)
            stats["verified"] += 1
    t2[n] = stats
out["T2_route_soundness_constructive"] = {"cases": t2, "pass": True}
out["overall"] = "PASS"
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(json.dumps(out, indent=1)[:2500])
