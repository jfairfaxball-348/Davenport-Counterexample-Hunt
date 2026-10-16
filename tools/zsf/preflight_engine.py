"""S103 engine pre-flight on SETTLED groups only (n=4,5,6; D(C_n^3)=3n-2 is
source-stated: p-groups n=4,5 [Olson], n=6 [Schmid2011, CLM-0064]).  Also checks
the FFT new-coverage formula against direct exact oracle updates.
No n=15 or n=20 search is performed.  Run: python -I tools/zsf/preflight_engine.py"""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import ils_engine as E

out = {}
# FFT coverage formula vs exact for random prefixes (n=15,20 prefixes only of length<=8; not a search)
rng = random.Random(5)
checked = 0
for n in (4, 6, 15, 20):
    mods = (n, n, n)
    for _ in range(5):
        o = A.Oracle(mods)
        for _ in range(rng.randint(0, 8)):
            o.push(tuple(rng.randrange(n) for _ in range(3)))
        cov = E.new_coverage_all(o.sig)
        for _ in range(40):
            g = tuple(rng.randrange(n) for _ in range(3))
            direct = int((o.sig | A.translate(o.sig, g)).sum()) - int(o.sig.sum())
            assert cov[g] == direct, (n, g)
            checked += 1
out["fft_coverage_vs_direct_checks"] = checked
for n, seed in ((4, 1), (5, 2), (6, 3)):
    rec = E.run(n, 3 * n - 2, seed, iterations=150, walltime=600, checkpoint=None)
    assert rec["best_len"] == 3 * n - 3 and rec["status"] == "BUDGET_EXHAUSTED", rec
    assert rec["best_checkerA"] and rec["best_checkerB"]
    out[f"n{n}"] = {k: rec[k] for k in ("status", "iterations_done", "best_len", "best_sha256", "length_histogram")}
out["overall"] = "PASS"
print(json.dumps(out, indent=1))
