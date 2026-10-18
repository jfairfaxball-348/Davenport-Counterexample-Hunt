"""S113 lemma tests (evidence only; the results of S113 are the hand proofs in
research/S113_CLOSED_FORM_ROUTE_THEOREMS.md).  Arithmetic over integers and multiplicity
patterns only: no group element of any target group is formed.

  L1  Theorem A constructions: for every pair of coprime odd A < B with A >= 3, B <= BMAX,
      except (3,5) and (3,7), the explicit w-vector of the proof satisfies system (W):
      w_i in [1, AB-1], sum w = 2AB-3, sum(w mod A) = A-3, sum(w mod B) = B-3.
  L2  Theorem A exceptions, by brute force over all w-multisets (a search for a counterexample
      to the lemma): (3,5) has no solution with w_i >= 0; (3,7) has none with w_i >= 1 and
      some with a w_i = 0.
  L3  Theorem A reduction: for n = pq (odd primes) the five-valued patterns surviving routes p
      and q under an independently written CLM-0374 closure test are exactly the all-order-n
      patterns alpha_i = n - 1 - w_i with w a solution of (W); compared for every pq <= 65 by
      enumerating all five-valued patterns, and with tools/zsf/route_sieve.py algorithm B.
  L4  Theorem B: (a) the p = 5 conditions (B1)-(B4) with the CLM-0350 cap have no solution
      (brute force); (b) for every prime 7 <= p <= PMAX the explicit pattern of the proof
      satisfies them and survives routes 2, 4, p under the independent closure test; (c) for
      n = 4p, p in {5, 7, 11, 13}, the six-valued survivors of the closure test all satisfy
      (B1)-(B4), and there are none at p = 5.
Run: python -I tools/zsf/test_s113.py <out.json>"""
import itertools, json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import route_sieve as RS

BMAX, PMAX = 401, 199
out = {}


def is_prime(m):
    return m > 1 and all(m % d for d in range(2, int(m ** 0.5) + 1))


def ok_W(w, A, B):
    n = A * B
    return (len(w) == 5 and all(1 <= x <= n - 1 for x in w) and sum(w) == 2 * n - 3
            and sum(x % A for x in w) == A - 3 and sum(x % B for x in w) == B - 3)


def construct_A(A, B):
    """The explicit solution of (W) used in the proof of Theorem A(ii)."""
    n = A * B
    if A == 3:                       # j-construction: w = 3a, all floor(3a/B) = 1
        k = B // 3
        a = [k + 1] * 4 + ([2 * k - 3] if B % 3 == 1 else [2 * k - 1])
        return [3 * x for x in a]
    al, be = pow(A, -1, B), pow(B, -1, A)
    if A >= 7:                       # construction 1 with c = 1
        c = 1
        m = n - 4 - c
        a = (m * pow(A, -1, B)) % B
        b = (m - a * A) // B
        return [A * al, B * be, c, a * A, b * B]
    if A == 5 and B >= 11:           # construction 2
        return [A * al, B * be, 1, A, n - 5 - A]
    return {(5, 7): [15, 15, 15, 15, 7], (5, 9): [1, 10, 10, 30, 36]}[(A, B)]


# ---------------- L1 ----------------
pairs = [(A, B) for A in range(3, BMAX, 2) for B in range(A + 2, BMAX + 1, 2)
         if math.gcd(A, B) == 1 and (A, B) not in ((3, 5), (3, 7))]
bad = [(A, B) for A, B in pairs if not ok_W(construct_A(A, B), A, B)]
assert bad == [], bad[:5]
out["L1_theorem_A_constructions"] = {"pairs_checked": len(pairs), "BMAX": BMAX, "failures": 0,
                                     "pass": True}


# ---------------- L2 ----------------
def all_W(A, B, wmin):
    n = A * B
    return [w for w in itertools.combinations_with_replacement(range(wmin, n), 5)
            if sum(w) == 2 * n - 3 and sum(x % A for x in w) == A - 3
            and sum(x % B for x in w) == B - 3]


s35 = all_W(3, 5, 0)
s37_cap, s37_all = all_W(3, 7, 1), all_W(3, 7, 0)
assert s35 == [] and s37_cap == [] and s37_all != []
assert all(0 in w for w in s37_all)
out["L2_theorem_A_exceptions"] = {"(3,5)_w>=0": 0, "(3,7)_w>=1": 0,
                                  "(3,7)_w>=0": [list(w) for w in s37_all], "pass": True}


# ---------------- independent CLM-0374 closure test ----------------
def routes_indep(n):
    """Prime powers a | n with D(C_a^3), D(C_{n/a}^3) recorded; (D1, D2 bound, D(C_b^3))."""
    def recorded(b):
        if b == 1:
            return True
        ps = [p for p in range(2, b + 1) if b % p == 0 and is_prime(p)]
        if len(ps) == 1:
            return True
        if len(ps) == 2 and 2 in ps:
            e2 = 0
            while b % 2 == 0:
                b //= 2
                e2 += 1
            return e2 == 1 or b == 3
        return False
    R = []
    for a in range(2, n):
        ps = [p for p in range(2, a + 1) if a % p == 0 and is_prime(p)]
        if n % a == 0 and len(ps) == 1 and recorded(n // a):
            D1 = 3 * a - 2
            D2 = 7 if a == 2 else (5 * a - 3 if is_prime(a) else 2 * D1)
            R.append((a, D1, D2, 3 * (n // a) - 2))
    return R


def nu(Rl, D1, D2):
    if Rl < D1:
        return 0
    if Rl < D2:
        return 1
    return 2 + (Rl - D2) // D1


def closes(n, pattern, RT):
    for a, D1, D2, Db in RT:
        t0 = Rl = 0
        for d, al in pattern:
            o = a // math.gcd(a, n // d)
            t0 += al // o
            Rl += al % o
        if t0 + nu(Rl, D1, D2) >= Db:
            return True
    return False


def cap(n, d):
    c = d - 1
    if d == n:
        c = min(c, n - 2)
    return c


def survivors(n, k, caps=cap):
    """All k-valued patterns (multisets of (order, alpha)) with sum 3n-2 surviving every route."""
    RT = routes_indep(n)
    items = [(d, al) for d in range(2, n + 1) if n % d == 0 for al in range(1, caps(n, d) + 1)]
    L, res = 3 * n - 2, []
    # enumeration over sorted multiplicity multisets first, orders second
    alist = sorted({al for _, al in items})
    for alphas in itertools.combinations_with_replacement(alist, k):
        if sum(alphas) != L:
            continue
        choices = [[d for d, al in items if al == a] for a in alphas]
        seen = set()
        for ds in itertools.product(*choices):
            pat = tuple(sorted(zip(ds, alphas)))
            if pat in seen:
                continue
            seen.add(pat)
            if not closes(n, pat, RT):
                res.append(pat)
    return res


# ---------------- L3 ----------------
L3 = {}
for p in (3, 5, 7):
    for q in (5, 7, 11, 13):
        n = p * q
        if q <= p or n > 65:
            continue
        surv = survivors(n, 5)
        from_W = sorted(tuple(sorted((n, n - 1 - w) for w in W)) for W in all_W(p, q, 1))
        assert sorted(set(surv)) == sorted(set(from_W)), n
        RT, cnt, _ = RS.count_B(n, 5, keep=0)
        assert cnt[5] == len(set(surv)), (n, cnt[5], len(surv))
        L3[str(n)] = {"five_valued_survivors": len(set(surv)), "equal_to_system_W": True,
                      "route_sieve_B_count": cnt[5]}
assert L3["15"]["five_valued_survivors"] == 0 and L3["21"]["five_valued_survivors"] == 0
out["L3_theorem_A_reduction"] = {"cases": L3, "pass": True}


# ---------------- L4 ----------------
def B_conditions(p, alphas):
    x = [a + 1 for a in alphas]
    return (len(alphas) == 6 and all(a % 2 == 1 for a in alphas)
            and sum(1 for a in alphas if a % 4 == 3) in (4, 6)
            and sum((-v) % p for v in x) in (p - 4, 2 * p - 4)
            and sum(alphas) == 12 * p - 2)


# (a) p = 5, cap alpha <= n-2 = 18
sol5 = [al for al in itertools.combinations_with_replacement(range(1, 19, 2), 6) if B_conditions(5, al)]
assert sol5 == []
# (b) explicit pattern for p >= 7
checked = []
for p in range(7, PMAX + 1):
    if not is_prime(p):
        continue
    n = 4 * p
    al = [2 * p - 3] * 4 + [2 * p + 5] * 2
    assert B_conditions(p, al) and max(al) <= n - 3
    assert not closes(n, [(n, a) for a in al], routes_indep(n))
    checked.append(p)
# (c) six-valued survivors at n = 4p satisfy (B1)-(B4)
L4c = {}
for p in (5, 7, 11, 13):
    n = 4 * p
    def cap_even(n, d):
        c = d - 1
        if d == n:
            c = min(c, n - 2)
        return c
    surv = survivors(n, 6, cap_even)
    assert all(all(d == n for d, _ in pat) and B_conditions(p, [a for _, a in pat]) for pat in surv)
    L4c[str(n)] = len(surv)
assert L4c["20"] == 0
out["L4_theorem_B"] = {"p5_conditions_solutions": 0, "explicit_pattern_primes_checked": len(checked),
                       "PMAX": PMAX, "six_valued_survivors_cap_n_minus_2_only": L4c,
                       "all_satisfy_B1_B4": True, "pass": True}

# ---------------- L5: Theorem C sharpness witnesses (survive every route) ----------------
wit = {15: [3, 8, 8, 8, 8, 8], 21: [2, 5, 5, 11, 19, 19], 20: [1, 3, 3, 3, 14, 17, 17]}
for n, al in wit.items():
    assert sum(al) == 3 * n - 2 and not closes(n, [(n, a) for a in al], routes_indep(n))
out["L5_theorem_C_witnesses"] = {str(n): al for n, al in wit.items()}
out["L5_theorem_C_witnesses"]["pass"] = True

out["overall"] = "PASS"
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)
print(json.dumps(out, indent=1))
