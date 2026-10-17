"""Support-5 exhaustive tool, ALGORITHM A (S109).  EXHAUSTIVE for the support-<=5 family.

Question decided: is there a zero-sumfree sequence over C_n^3 with at most five distinct
values (as an indexed list a_1..a_5 with multiplicities alpha_i) and length >= L?

Reductions (proved in research/S109_SUPPORT5_EXHAUSTIVE_TOOLING.md, CLM-0361..0364):
  * zero-sumfreeness depends only on the relation module K = ker((Z/n)^5 -> C_n^3) and
    alpha (CLM-0358); WLOG the values generate C_n^3, so K is a free rank-2 summand of
    (Z/n)^5 (CLM-0361); K = prod_q K_q over prime powers q || n (CRT, CLM-0362);
  * each K_q is the graph of a linear map over a coordinate pair; A takes the
    lexicographically FIRST pair (i,j) whose 2x2 generator minor is a unit (CLM-0363);
  * simultaneous coordinate permutation (S_5) preserves the optimum (CLM-0364): A takes
    S_5-orbit representatives of the FIRST prime-power component and ALL K of the others.
Optimum per K: exact branch-and-bound on upper bounds u (start u_i = n-1): a violated
nonzero rho (v(rho) <= u) forces alpha_i <= v_i(rho)-1 for some i with v_i(rho) >= 1.

Usage:
  python -I tools/zsf/support5_a.py --n 6 [--threshold T] [--report-keys-at T]
      [--shard k --nshards N] [--checkpoint file.jsonl] [--out file.json]
Shards partition the enumeration by index mod N; a run is complete only when all N
shards end.  The checkpoint logs every K whose optimum is >= --report-keys-at.
"""
import argparse, hashlib, itertools, json, os, sys, time
import numpy as np

PAIRS = list(itertools.combinations(range(5), 2))
PERMS = list(itertools.permutations(range(5)))


def factor(n):
    f, p, m = {}, 2, n
    while m > 1:
        while m % p == 0:
            f[p] = f.get(p, 1) * p
            m //= p
        p += 1
    return f                                     # {prime: prime power}


def components(q, p):
    """All free rank-2 summands of (Z/q)^5 (q = p^k), each as an int array (q*q, 5) of its
    elements, enumerated by (first unit-minor pair, 3x2 matrix)."""
    st = np.array([(s, t) for s in range(q) for t in range(q)], dtype=np.int64)   # q^2 x 2
    out = []
    for (i, j) in PAIRS:
        others = [k for k in range(5) if k not in (i, j)]
        for L in itertools.product(range(q), repeat=6):
            Lm = np.array(L, dtype=np.int64).reshape(3, 2)
            # generator rows g1=(s,t)=(1,0), g2=(0,1); columns of the 2x5 generator matrix
            G = np.zeros((2, 5), dtype=np.int64)
            G[0, i], G[1, j] = 1, 1
            G[:, others] = Lm.T
            # keep iff no lexicographically earlier pair has a unit minor mod p
            ok = True
            for (a, b) in PAIRS:
                if (a, b) >= (i, j):
                    break
                if (G[0, a] * G[1, b] - G[0, b] * G[1, a]) % p:
                    ok = False
                    break
            if not ok:
                continue
            E = np.zeros((q * q, 5), dtype=np.int64)
            E[:, i], E[:, j] = st[:, 0], st[:, 1]
            E[:, others] = (st @ Lm.T) % q
            out.append(E)
    return out


def canon_key(E, q):
    """S_5-canonical key: min over coordinate permutations of the sorted encoded elements."""
    best = None
    w = q ** np.arange(4, -1, -1)
    for P in PERMS:
        key = tuple(sorted((E[:, list(P)] @ w).tolist()))
        if best is None or key < best:
            best = key
    return best


def orbit_reps(comps, q):
    seen, reps = set(), []
    for E in comps:
        k = canon_key(E, q)
        if k not in seen:
            seen.add(k)
            reps.append(E)
    return reps


def crt_combine(parts, n):
    """parts: list of (q, E_q); return all elements of K = prod K_q as residues mod n."""
    acc = np.zeros((1, 5), dtype=np.int64)
    for q, E in parts:
        Q = n // q
        coef = Q * pow(Q, -1, q)
        acc = (acc[:, None, :] + coef * E[None, :, :]).reshape(-1, 5) % n
    return acc


def optimum(V, n):
    """Exact max sum(alpha), alpha in [0,n-1]^5, every row of V (nonzero rho, residues)
    escaping: some i with alpha_i < V_i.  Branch and bound on upper bounds."""
    best = [-1]

    def rec(u):
        su = int(u.sum())
        if su <= best[0]:
            return
        viol = np.flatnonzero((V <= u).all(axis=1))
        if len(viol) == 0:
            best[0] = su
            return
        r = V[viol[0]]
        for i in range(5):
            if r[i] >= 1:
                u2 = u.copy()
                u2[i] = r[i] - 1
                rec(u2)
    rec(np.full(5, n - 1, dtype=np.int64))
    return best[0]


def run(n, threshold=None, report_keys_at=None, shard=0, nshards=1, checkpoint=None, ckpt_every=20000):
    t0 = time.perf_counter()
    ck = open(checkpoint, "a", encoding="utf-8", newline="\n") if checkpoint else None
    fac = sorted(factor(n).items())                 # [(p, q), ...]
    comp = {q: components(q, p) for p, q in fac}
    p0, q0 = fac[0]
    reps0 = orbit_reps(comp[q0], q0)
    hist, top, count, idx = {}, [], 0, -1
    for E0 in reps0:
        for rest in itertools.product(*[comp[q] for _, q in fac[1:]]):
            idx += 1
            if idx % nshards != shard:
                continue
            parts = [(q0, E0)] + [(q, E) for (_, q), E in zip(fac[1:], rest)]
            K = crt_combine(parts, n)
            V = K[(K != 0).any(axis=1)]
            o = optimum(V, n)
            hist[o] = hist.get(o, 0) + 1
            count += 1
            if report_keys_at is not None and o >= report_keys_at:
                top.append((o, canon_key(K, n)))
                if ck:
                    ck.write(json.dumps({"kind": "AT_OR_ABOVE", "index": idx, "optimum": o, "K": K.tolist()}) + "\n"); ck.flush()
            if ck and count % ckpt_every == 0:
                ck.write(json.dumps({"kind": "progress", "index": idx, "evaluated": count, "max": max(hist),
                                     "elapsed": round(time.perf_counter() - t0, 1)}) + "\n"); ck.flush()
    res = dict(algorithm="A", n=n, shard=shard, nshards=nshards, components={q: len(comp[q]) for _, q in fac},
               reps_first_component=len(reps0), pairs_evaluated=count,
               max_length=max(hist), histogram={str(k): v for k, v in sorted(hist.items())},
               seconds=round(time.perf_counter() - t0, 2))
    if report_keys_at is not None:
        uniq = sorted(set(top))
        res["orbits_at_or_above"] = {"threshold": report_keys_at, "count": len(uniq),
                                     "sha256": hashlib.sha256(json.dumps(uniq).encode()).hexdigest()}
    if threshold is not None:
        res["threshold"] = threshold
        res["any_at_or_above_threshold"] = max(hist) >= threshold
    if ck:
        ck.write(json.dumps(dict(kind="end", **res)) + "\n"); ck.close()
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--threshold", type=int, default=None)
    ap.add_argument("--report-keys-at", type=int, default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--nshards", type=int, default=1)
    ap.add_argument("--checkpoint", default=None)
    a = ap.parse_args()
    r = run(a.n, a.threshold, a.report_keys_at, a.shard, a.nshards, a.checkpoint)
    s = json.dumps(r, indent=1)
    if a.out:
        open(a.out, "w", newline="\n").write(s + "\n")
    print(s)
