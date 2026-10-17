"""S104 pre-flight of R2-LNS-1.0 on SETTLED groups only (n=3,4,5 p-groups [Olson];
n=6 [Schmid2011, CLM-0064]; D(C_n^3)=3n-2 so the maximum zero-sumfree length is 3n-3).
Also checks the FFT two-addition test against exhaustive exact oracle enumeration.
No n=15 or n=20 search is performed.  Run: python -I tools/zsf/preflight_lns.py"""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import lns_engine as L

out = {}
rng = random.Random(104)
agree = 0
for n in (3, 4, 5, 6):
    mods = (n, n, n)
    N = n ** 3
    for _ in range(30):
        o = A.Oracle(mods)
        L.grow_uniform(o, rng)
        T = L.remove_values(o.seq, [o.seq[rng.randrange(len(o.seq))]])
        if len(T) > 2 and rng.random() < 0.5:
            T = T[:-1]
        t = L.rebuild(T, mods)
        fft_ok = L.two_more(t, N, random.Random(0)) is not None
        brute = False
        elems = [tuple(int(v) for v in np.unravel_index(i, mods)) for i in range(N)]
        for a in elems:
            if t.push(a):
                if t.legal_mask().any():
                    brute = True
                t.pop()
            if brute:
                break
        assert fft_ok == brute, (n, T)
        agree += 1
out["two_more_fft_vs_exhaustive_agreements"] = agree
for n, seed, init in ((3, 1, "uniform"), (4, 2, "uniform"), (5, 3, "standard"), (6, 4, "uniform"), (6, 5, "standard")):
    rec = L.run(n, 3 * n - 2, seed, init, iterations=40, walltime=600, checkpoint=None)
    assert rec["best_len"] == 3 * n - 3 and rec["status"] == "BUDGET_EXHAUSTED", rec
    assert rec["best_checkerA"] and rec["best_checkerB"]
    out[f"n{n}_{init}"] = {k: rec[k] for k in ("status", "iterations_done", "best_len", "best_sha256",
                                               "length_histogram", "move_stats")}
# determinism
r1 = L.run(5, 13, 9, "uniform", iterations=15, walltime=600, checkpoint=None)
r2 = L.run(5, 13, 9, "uniform", iterations=15, walltime=600, checkpoint=None)
assert r1["best_sha256"] == r2["best_sha256"] and r1["length_histogram"] == r2["length_histogram"]
out["determinism"] = "PASS"
out["overall"] = "PASS"
print(json.dumps(out, indent=1))
