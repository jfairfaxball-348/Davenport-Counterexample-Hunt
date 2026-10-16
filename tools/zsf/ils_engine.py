"""Round-1 HEURISTIC search engine (preregistered as CAM-0002 / CAM-0003 method R1).

Iterated local search over unrestricted indexed sequences in C_n^3:
  * construction: repeatedly append a legal element (-g not in Sigma) chosen by
    softmin of exact NEW subset-sum coverage |(g+Sigma) minus Sigma|, computed for all g at once
    from the exact autocorrelation of the Sigma indicator (FFT, rounded to
    integers, then the chosen element's coverage is re-derived exactly by the
    oracle update);
  * ruin-and-regrow: delete r random terms from the current maximal sequence,
    rebuild Sigma exactly from the survivors, regrow to maximality;
  * accept if new length >= current length, else with probability p_worse.
Any sequence reaching target_len is immediately re-verified by checker A and the
independent checker B, written to the checkpoint and the run stops.

Deterministic for fixed (n, seed, iterations, parameters): wall time is only a
safety cap whose triggering is logged as an incomplete (budget-truncated) run.
Completeness class: HEURISTIC.  Exhausting the budget proves NOTHING.

Usage:
  python -I tools/zsf/ils_engine.py --n 15 --target 43 --seed 103001 \
      --iterations 20000 --walltime 5400 --checkpoint path.jsonl
"""
import argparse, hashlib, json, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import checker_b as B

ENGINE_VERSION = "R1-ILS-1.0"


def new_coverage_all(sig):
    """Exact integer array N with N[g] = |(g+Sigma) minus Sigma| for every g."""
    a = sig.astype(np.float64)
    F = np.fft.fftn(a)
    corr = np.rint(np.fft.ifftn(F * np.conj(F)).real).astype(np.int64)
    return int(sig.sum()) - corr


def grow(o, rng, temp, n):
    while True:
        legal = o.legal_mask()
        if not legal.any():
            return
        cov = new_coverage_all(o.sig)
        idx = np.flatnonzero(legal)
        c = cov.ravel()[idx].astype(np.float64)
        w = np.exp(-(c - c.min()) / temp)
        w /= w.sum()
        pick = idx[int(rng.choices(range(len(idx)), weights=w.tolist())[0])]
        g = np.unravel_index(pick, o.mods)
        ok = o.push(tuple(int(v) for v in g))
        assert ok


def rebuild(seq, mods):
    o = A.Oracle(mods)
    for g in seq:
        ok = o.push(g)
        assert ok, "subsequence of zero-sumfree sequence must stay zero-sumfree"
    return o


def canon(seq, n):
    s = sorted(tuple(int(v) for v in g) for g in seq)
    blob = json.dumps({"modulus": n, "rank": 3, "length": len(s), "sequence": s}, separators=(",", ":"))
    return s, hashlib.sha256(blob.encode("utf-8")).hexdigest()


def run(n, target, seed, iterations, walltime, checkpoint, temp=0.6, rmin=2, rmax=6,
        p_worse=0.02, ckpt_every=500):
    mods = (n, n, n)
    rng = random.Random(seed)
    t0 = time.perf_counter()
    o = A.Oracle(mods)
    grow(o, rng, temp, n)
    cur = list(o.seq)
    best = list(cur)
    hist = {}
    status = "BUDGET_EXHAUSTED"
    it = 0
    params = dict(n=n, target=target, seed=seed, iterations=iterations, walltime=walltime, temp=temp,
                  rmin=rmin, rmax=rmax, p_worse=p_worse, engine=ENGINE_VERSION)
    phash = hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()
    ck = open(checkpoint, "a", encoding="utf-8") if checkpoint else None

    def log(kind, **kw):
        rec = dict(kind=kind, iter=it, param_hash=phash, elapsed=round(time.perf_counter() - t0, 1), **kw)
        if ck:
            ck.write(json.dumps(rec) + "\n"); ck.flush()
        return rec

    log("start", params=params)
    for it in range(1, iterations + 1):
        if time.perf_counter() - t0 > walltime:
            status = "WALLTIME_CAP_TRUNCATED"
            break
        r = rng.randint(rmin, min(rmax, len(cur)))
        keep_idx = sorted(rng.sample(range(len(cur)), len(cur) - r))
        o = rebuild([cur[i] for i in keep_idx], mods)
        grow(o, rng, temp, n)
        new = list(o.seq)
        hist[len(new)] = hist.get(len(new), 0) + 1
        if len(new) >= len(cur) or rng.random() < p_worse:
            cur = new
        if len(new) > len(best):
            best = new
        if len(best) >= target:
            okA, _ = A.is_zero_sumfree(best, mods)
            okB = B.is_zero_sumfree(best, mods)
            s, h = canon(best, n)
            log("CANDIDATE_QUARANTINE", length=len(best), checkerA=okA, checkerB=okB, sequence=s, sha256=h)
            status = "TARGET_REACHED_UNCERTIFIED"
            break
        if it % ckpt_every == 0:
            s, h = canon(best, n)
            log("checkpoint", best_len=len(best), cur_len=len(cur), best_sha256=h, best=s,
                length_histogram=hist)
    s, h = canon(best, n)
    okA, _ = A.is_zero_sumfree(best, mods)
    okB = B.is_zero_sumfree(best, mods)
    rec = log("end", status=status, iterations_done=it, best_len=len(best), best_sha256=h, best=s,
              best_checkerA=okA, best_checkerB=okB, length_histogram=hist)
    if ck:
        ck.close()
    return rec


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--target", type=int, required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--iterations", type=int, required=True)
    ap.add_argument("--walltime", type=float, required=True)
    ap.add_argument("--checkpoint", default=None)
    a = ap.parse_args()
    rec = run(a.n, a.target, a.seed, a.iterations, a.walltime, a.checkpoint)
    print(json.dumps({k: v for k, v in rec.items() if k != "best"}))
