"""Support-5 exhaustive tool, ALGORITHM B (S109).  Independent of support5_a.py (no shared
code).  Decides the same question by different means:

  * components: every free rank-2 summand of (Z/q)^5 is produced as the kernel of a
    surjective 3x5 matrix [I_3 | X] with permuted columns; the kernel set is computed by
    solving the three equations for the three pivot coordinates, and duplicates are
    removed by an explicit element-set dictionary (no first-pair rule);
  * S_5 reduction is applied to the LAST prime-power component (A uses the first);
  * optimum per K: dense dynamic programme.  F[a1..a4] = min v_5(rho) over nonzero rho
    with (v_1..v_4)(rho) <= (a1..a4); prefix minima along four axes; the best alpha_5 at
    (a1..a4) is min(n-1, F-1) (infeasible if F = 0); maximise a1+..+a4+alpha_5.

Usage:
  python -I tools/zsf/support5_b.py --n 6 [--threshold T] [--report-keys-at T]
      [--shard k --nshards N] [--checkpoint file.jsonl] [--out file.json]
Shards partition the enumeration by index mod N; a run is complete only when all N
shards end.  The checkpoint logs every K whose optimum is >= --report-keys-at.
"""
import argparse, hashlib, itertools, json, time
import numpy as np


def prime_powers(n):
    res, d, m = [], 2, n
    while m > 1:
        if m % d == 0:
            pk = 1
            while m % d == 0:
                pk *= d
                m //= d
            res.append((d, pk))
        d += 1
    return res


def kernels(q):
    """Kernels of [I|X] matrices (pivot columns any 3-subset) over Z/q, deduplicated."""
    found = {}
    st = [(s, t) for s in range(q) for t in range(q)]
    for piv in itertools.combinations(range(5), 3):
        free = [c for c in range(5) if c not in piv]
        for X in itertools.product(range(q), repeat=6):
            # equations: rho_piv[r] + X[r][0]*rho_free0 + X[r][1]*rho_free1 = 0
            elems = []
            for s, t in st:
                v = [0] * 5
                v[free[0]], v[free[1]] = s, t
                for r in range(3):
                    v[piv[r]] = (-(X[2 * r] * s + X[2 * r + 1] * t)) % q
                elems.append(tuple(v))
            key = frozenset(elems)
            if key not in found:
                found[key] = elems
    return [np.array(sorted(v), dtype=np.int64) for v in found.values()]


def canonical(E, base):
    enc = lambda M: tuple(sorted(int(x) for x in M @ np.array([base ** 4, base ** 3, base ** 2, base, 1])))
    return min(enc(E[:, list(P)]) for P in itertools.permutations(range(5)))


def reps_under_s5(Ks, q):
    out = {}
    for E in Ks:
        c = canonical(E, q)
        out.setdefault(c, E)
    return list(out.values())


def combine(parts, n):
    """Chinese remaindering of component element lists into residues mod n."""
    elems = np.zeros((1, 5), dtype=np.int64)
    for q, E in parts:
        r = n // q
        e = (r * pow(r, -1, q)) % n
        elems = ((elems[:, None, :] + e * E[None, :, :]) % n).reshape(-1, 5)
    return elems


def best_alpha_sum(K, n):
    V = K[(K != 0).any(axis=1)]
    INF = n + 1
    F = np.full((n, n, n, n), INF, dtype=np.int64)
    np.minimum.at(F, (V[:, 0], V[:, 1], V[:, 2], V[:, 3]), V[:, 4])
    for ax in range(4):
        F = np.minimum.accumulate(F, axis=ax)
    a5 = np.minimum(n - 1, F - 1)
    grid = np.indices((n, n, n, n)).sum(axis=0)
    tot = np.where(a5 >= 0, grid + a5, -1)
    return int(tot.max())


def run(n, threshold=None, report_keys_at=None, shard=0, nshards=1, checkpoint=None, ckpt_every=20000):
    t0 = time.perf_counter()
    log = open(checkpoint, "a", encoding="utf-8", newline="\n") if checkpoint else None
    pp = prime_powers(n)
    comps = {q: kernels(q) for _, q in pp}
    qlast = pp[-1][1]
    reps_last = reps_under_s5(comps[qlast], qlast)
    hist, keys, cnt, pos = {}, set(), 0, -1
    for head in itertools.product(*[comps[q] for _, q in pp[:-1]]):
        for E_last in reps_last:
            pos += 1
            if pos % nshards != shard:
                continue
            parts = list(zip([q for _, q in pp[:-1]], head)) + [(qlast, E_last)]
            K = combine(parts, n)
            o = best_alpha_sum(K, n)
            hist[o] = hist.get(o, 0) + 1
            cnt += 1
            if report_keys_at is not None and o >= report_keys_at:
                keys.add((o, canonical(K, n)))
                if log:
                    log.write(json.dumps({"kind": "AT_OR_ABOVE", "index": pos, "optimum": o, "K": K.tolist()}) + "\n"); log.flush()
            if log and cnt % ckpt_every == 0:
                log.write(json.dumps({"kind": "progress", "index": pos, "evaluated": cnt, "max": max(hist),
                                      "elapsed": round(time.perf_counter() - t0, 1)}) + "\n"); log.flush()
    res = dict(algorithm="B", n=n, shard=shard, nshards=nshards, components={q: len(comps[q]) for _, q in pp},
               reps_last_component=len(reps_last), pairs_evaluated=cnt,
               max_length=max(hist), histogram={str(k): v for k, v in sorted(hist.items())},
               seconds=round(time.perf_counter() - t0, 2))
    if report_keys_at is not None:
        u = sorted(keys)
        res["orbits_at_or_above"] = {"threshold": report_keys_at, "count": len(u),
                                     "sha256": hashlib.sha256(json.dumps([[o, list(k)] for o, k in u]).encode()).hexdigest()}
    if threshold is not None:
        res["threshold"] = threshold
        res["any_at_or_above_threshold"] = max(hist) >= threshold
    if log:
        log.write(json.dumps(dict(kind="end", **res)) + "\n"); log.close()
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
