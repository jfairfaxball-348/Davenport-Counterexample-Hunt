"""Round-2 HEURISTIC search engine R2-LNS-1.0 (preregistered as CAM-0004 / CAM-0005).

Materially different from R1-ILS-1.0 (random ruin + softmin regrow, length-only
acceptance).  R2 is an exact large-neighbourhood "remove k, add k+1"
deficiency-repair search driven by the complement of Sigma:

  Fact used (prefix criterion, CLM-0345): a zero-sumfree S extends by one term
  iff some g has -g not in Sigma(S), i.e. iff Sigma(S) != G.  Hence after
  removing a sub-multiset R from a maximal S, the sequence S-R admits |R|+1
  further terms iff a depth-|R| chain of additions leaves Sigma != G.  For the
  last two levels this is decided for ALL first-additions a at once:
  |Sigma(T+a)| = |Sigma(T)| + newcov_T(a)  (exact FFT autocorrelation, rounded),
  so T admits two more terms iff some legal a has |Sigma(T)| + newcov_T(a) < |G|.

  * k=1 move (EXHAUSTIVE within the neighbourhood): every distinct value x of S
    is removed in turn and the 2-addition test above is evaluated over all a;
  * k=2 move (SAMPLED): m2 random removal pairs; the first addition a is
    enumerated over all legal a (ordered by low new coverage, capped), the last
    two levels by the FFT test;
  * on success the found additions are pushed through the exact oracle (any
    FFT disagreement would raise), then the sequence is regrown to maximality
    by uniform random legal pushes;
  * otherwise a plateau (lateral) swap: remove a random value x and add a
    random legal a != x not tabu, regrow to maximality (length can only stay
    equal or grow, since S-x+a is maximal-or-extendable);
  * restart from the seed family after `stall` non-improving iterations.
Seed families: "uniform" (uniform random legal greedy to maximality) or
"standard" (e1^(n-1) e2^(n-1) e3^(n-1), the length 3n-3 structured sequence,
CLM-0346), both deterministic in (seed).

Completeness class: HEURISTIC.  Exhausting the budget proves NOTHING; the k=1
exhaustive sweep is exact only for the specific visited states.

Usage:
  python -I tools/zsf/lns_engine.py --n 15 --target 43 --seed 104001 \
      --init uniform --iterations 4000 --walltime 7200 --checkpoint path.jsonl
"""
import argparse, hashlib, json, os, random, sys, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import checker_b as B

ENGINE_VERSION = "R2-LNS-1.0"


def new_coverage_all(sig):
    """Exact integer array N with N[g] = |(g+Sigma) minus Sigma| for every g."""
    a = sig.astype(np.float64)
    F = np.fft.fftn(a)
    corr = np.rint(np.fft.ifftn(F * np.conj(F)).real).astype(np.int64)
    return int(sig.sum()) - corr


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


def grow_uniform(o, rng):
    while True:
        idx = np.flatnonzero(o.legal_mask())
        if len(idx) == 0:
            return
        g = np.unravel_index(int(idx[rng.randrange(len(idx))]), o.mods)
        assert o.push(tuple(int(v) for v in g))


def two_more(o, N, rng):
    """Return a legal a such that o.seq+a still has a legal term, else None (exact via FFT)."""
    legal = o.legal_mask().ravel()
    if not legal.any():
        return None
    cov = new_coverage_all(o.sig).ravel()
    ok = np.flatnonzero(legal & (o.coverage() + cov < N))
    if len(ok) == 0:
        return None
    return tuple(int(v) for v in np.unravel_index(int(ok[rng.randrange(len(ok))]), o.mods))


def finish_two(o, a, rng):
    """Push a then one uniform legal b; both pushes are exact oracle checks."""
    assert o.push(a), "FFT/oracle disagreement on first addition"
    idx = np.flatnonzero(o.legal_mask())
    assert len(idx) > 0, "FFT/oracle disagreement on second addition"
    b = tuple(int(v) for v in np.unravel_index(int(idx[rng.randrange(len(idx))]), o.mods))
    assert o.push(b)


def remove_values(seq, vals):
    rest = list(seq)
    for v in vals:
        rest.remove(v)
    return rest


def standard_seed(n):
    return [(1, 0, 0)] * (n - 1) + [(0, 1, 0)] * (n - 1) + [(0, 0, 1)] * (n - 1)


def run(n, target, seed, init, iterations, walltime, checkpoint, m2=12, cap_a=64,
        tabu_len=8, stall=200, ckpt_every=50):
    mods = (n, n, n)
    N = n ** 3
    rng = random.Random(seed)
    t0 = time.perf_counter()

    def fresh():
        if init == "standard":
            o = rebuild(standard_seed(n), mods)
        else:
            o = A.Oracle(mods)
        grow_uniform(o, rng)
        return list(o.seq)

    cur = fresh()
    best = list(cur)
    tabu = []
    since = 0
    stats = Counter()
    hist = {}
    status = "BUDGET_EXHAUSTED"
    it = 0
    params = dict(n=n, target=target, seed=seed, init=init, iterations=iterations, walltime=walltime,
                  m2=m2, cap_a=cap_a, tabu_len=tabu_len, stall=stall, engine=ENGINE_VERSION)
    phash = hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()
    ck = open(checkpoint, "a", encoding="utf-8") if checkpoint else None

    def log(kind, **kw):
        rec = dict(kind=kind, iter=it, param_hash=phash, elapsed=round(time.perf_counter() - t0, 1), **kw)
        if ck:
            ck.write(json.dumps(rec) + "\n"); ck.flush()
        return rec

    log("start", params=params, init_len=len(cur))
    for it in range(1, iterations + 1):
        if time.perf_counter() - t0 > walltime:
            status = "WALLTIME_CAP_TRUNCATED"
            break
        new = None
        # k=1: exhaustive over distinct values of cur
        vals = sorted(set(cur))
        rng.shuffle(vals)
        for x in vals:
            o = rebuild(remove_values(cur, [x]), mods)
            a = two_more(o, N, rng)
            if a is not None:
                finish_two(o, a, rng)
                grow_uniform(o, rng)
                new = list(o.seq)
                stats["k1_improve"] += 1
                break
        else:
            stats["k1_locally_maximal"] += 1
        # k=2: sampled pairs, first addition enumerated (capped), last two by FFT
        if new is None:
            for _ in range(m2):
                pair = rng.sample(cur, 2)
                o = rebuild(remove_values(cur, pair), mods)
                legal = np.flatnonzero(o.legal_mask())
                if len(legal) == 0:
                    continue
                cov = new_coverage_all(o.sig).ravel()[legal]
                order = legal[np.argsort(cov, kind="stable")][:cap_a]
                for fi in order:
                    a1 = tuple(int(v) for v in np.unravel_index(int(fi), mods))
                    assert o.push(a1)
                    a = two_more(o, N, rng)
                    if a is not None:
                        finish_two(o, a, rng)
                        grow_uniform(o, rng)
                        new = list(o.seq)
                        break
                    o.pop()
                if new is not None:
                    stats["k2_improve"] += 1
                    break
        if new is not None and len(new) > len(cur):
            cur = new
            since = 0
        else:
            # plateau swap with tabu on re-adding removed values
            since += 1
            stats["plateau"] += 1
            x = rng.choice(sorted(set(cur)))
            o = rebuild(remove_values(cur, [x]), mods)
            mask = o.legal_mask()
            idx = [int(i) for i in np.flatnonzero(mask)
                   if tuple(int(v) for v in np.unravel_index(int(i), mods)) not in tabu + [x]]
            if idx:
                g = tuple(int(v) for v in np.unravel_index(idx[rng.randrange(len(idx))], mods))
                assert o.push(g)
                grow_uniform(o, rng)
                cur = list(o.seq)
                tabu = (tabu + [x])[-tabu_len:]
            if since >= stall:
                stats["restart"] += 1
                cur = fresh()
                tabu = []
                since = 0
        hist[len(cur)] = hist.get(len(cur), 0) + 1
        if len(cur) > len(best):
            best = list(cur)
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
                length_histogram=hist, move_stats=dict(stats))
    s, h = canon(best, n)
    okA, _ = A.is_zero_sumfree(best, mods)
    okB = B.is_zero_sumfree(best, mods)
    rec = log("end", status=status, iterations_done=it, best_len=len(best), best_sha256=h, best=s,
              best_checkerA=okA, best_checkerB=okB, length_histogram=hist, move_stats=dict(stats))
    if ck:
        ck.close()
    return rec


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--target", type=int, required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--init", choices=("uniform", "standard"), required=True)
    ap.add_argument("--iterations", type=int, required=True)
    ap.add_argument("--walltime", type=float, required=True)
    ap.add_argument("--checkpoint", default=None)
    a = ap.parse_args()
    rec = run(a.n, a.target, a.seed, a.init, a.iterations, a.walltime, a.checkpoint)
    print(json.dumps({k: v for k, v in rec.items() if k != "best"}))
