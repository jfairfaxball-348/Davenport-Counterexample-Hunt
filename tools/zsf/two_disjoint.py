"""S111 exact check of the finite lemma TWO(a) over C_a^3, a in {3, 4, 5}.

TWO(a): every sequence over C_a^3 with at most 5 distinct values and length >= 4a-2
contains two disjoint nonempty zero-sum subsequences.

By the hand reductions in research/S111_R_PLUS_TWO_AND_EVEN_CAPS.md section 5
it suffices to check the 'reduced' instances: 5 distinct nonzero values b_1..b_5
with multiplicities r_i <= ord(b_i)-1 and sum_i (a-1-r_i) <= a-3, over the
enumerated families below (GL_3 normalisation documented per family).

Two independently implemented algorithms decide each instance:
  A  relation-module box enumeration: all x in [0,a-1]^5 with sum x_i b_i = 0,
     then a pair test  exists y,z nonzero zero-sum vectors with y+z <= r.
  B  pair dynamic programme over the indexed sequence: reachable states
     (sum1, sum2, nonempty1, nonempty2) when each term goes to set 1, set 2 or
     neither; success iff (0, 0, 1, 1) is reachable.
Usage: python -I tools/zsf/two_disjoint.py <a> <A|B> <out.json>
"""
import hashlib, itertools, json, sys, time
import numpy as np


def elements(a):
    return [e for e in itertools.product(range(a), repeat=3) if any(e)]


def order(e, a):
    for k in range(1, a + 1):
        if all((k * x) % a == 0 for x in e):
            return k


def betas(a):
    """All deficiency vectors beta in N^5 with sum <= a-3."""
    out = []
    for b in itertools.product(range(a - 2), repeat=5):
        if sum(b) <= a - 3:
            out.append(b)
    return out


def families(a):
    """Yield (family_name, list of 5-tuples of values)."""
    E = elements(a)
    e123 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    if a == 3:
        # full enumeration, no symmetry used
        yield "ALL_5_SUBSETS", list(itertools.combinations(E, 5))
        return
    # generating case: three values form a basis -> GL_3 maps them to e1,e2,e3
    rest = [e for e in E if e not in e123]
    yield "GEN_E123_ORDERED_PAIR", [tuple(e123) + (u, v) for u in rest for v in rest if u != v]
    if a == 4:
        # non-generating: mod-2 reductions span <= a plane -> GL_3 maps into H = {x3 even}
        H = [e for e in E if e[2] % 2 == 0]
        yield "NONGEN_H_ALL_5_SUBSETS", list(itertools.combinations(H, 5))
    if a == 5:
        # non-generating: values in a plane, two of them non-collinear -> e1, e2
        P = [e for e in E if e[2] == 0 and e not in e123[:2]]
        yield "NONGEN_PLANE_E12_TRIPLES", [tuple(e123[:2]) + t for t in itertools.combinations(P, 3)]


def admissible(vals, a, beta):
    r = tuple(a - 1 - b for b in beta)
    if any(ri < 0 or ri > order(v, a) - 1 for ri, v in zip(r, vals)):
        return None
    return r


# ---------------- algorithm A ----------------
def make_A(a):
    grid = np.array(list(itertools.product(range(a), repeat=5)), dtype=np.int64)  # a^5 x 5
    def kernel(vals):
        V = np.array(vals, dtype=np.int64)  # 5 x 3
        s = (grid @ V) % a
        z = grid[(s == 0).all(1)]
        return z[(z != 0).any(1)]
    def decide(Z, r):
        r = np.array(r)
        Zr = Z[(Z <= r).all(1)]
        if len(Zr) == 0:
            return False
        return bool(((Zr[:, None, :] + Zr[None, :, :]) <= r).all(-1).any())
    return kernel, decide


# ---------------- algorithm B ----------------
def make_B(a):
    N = a ** 3
    enc = lambda e: (e[0] * a + e[1]) * a + e[2]
    allE = list(itertools.product(range(a), repeat=3))
    shift = {}
    for g in allE:
        shift[g] = np.array([enc(tuple((x + y) % a for x, y in zip(h, g))) for h in allE])
    def decide(vals, r):
        seq = [v for v, m in zip(vals, r) for _ in range(m)]
        R = np.zeros((2, 2, N, N), dtype=bool)
        R[0, 0, 0, 0] = True
        for g in seq:
            p = shift[g]
            new = R.copy()
            for f1 in range(2):
                for f2 in range(2):
                    src = R[f1, f2]
                    t1 = np.zeros((N, N), dtype=bool); t1[p, :] = src
                    new[1, f2] |= t1
                    t2 = np.zeros((N, N), dtype=bool); t2[:, p] = src
                    new[f1, 1] |= t2
            R = new
            if R[1, 1, 0, 0]:
                return True
        return bool(R[1, 1, 0, 0])
    return decide


def main():
    a, alg, out = int(sys.argv[1]), sys.argv[2], sys.argv[3]
    t0 = time.time()
    B = betas(a)
    res = {"a": a, "algorithm": alg, "beta_vectors": len(B), "families": {}}
    h = hashlib.sha256()
    failures = []
    if alg == "A":
        kernel, decA = make_A(a)
    else:
        decB = make_B(a)
    for name, sets in families(a):
        inst = 0
        for vals in sets:
            if alg == "A":
                Z = kernel(vals)
            for beta in B:
                r = admissible(vals, a, beta)
                if r is None:
                    continue
                inst += 1
                ok = decA(Z, r) if alg == "A" else decB(vals, r)
                h.update(repr((vals, r, ok)).encode())
                if not ok:
                    failures.append({"values": vals, "r": r})
        res["families"][name] = {"value_lists": len(sets), "instances": inst}
    res["instances_total"] = sum(f["instances"] for f in res["families"].values())
    res["failures"] = failures[:50]
    res["failure_count"] = len(failures)
    res["decision_stream_sha256"] = h.hexdigest()
    res["TWO_holds_on_all_instances"] = not failures
    res["seconds"] = round(time.time() - t0, 1)
    json.dump(res, open(out, "w"), indent=1, default=list)
    print(json.dumps({k: v for k, v in res.items() if k != "failures"}, default=list))


if __name__ == "__main__":
    main()
