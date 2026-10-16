"""S103 throughput benchmark (NOT a search): times exact oracle primitives on
fixed deterministic inputs for n=15 and n=20.  No sequence longer than the
standard 3(n-1) is sought or recorded.

Run: python -I tools/zsf/bench.py
"""
import json, os, platform, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import checker_a as A
import checker_b as B

out = {"python": platform.python_version(), "numpy": np.__version__, "platform": platform.platform(),
       "cpu_count": os.cpu_count(), "processor": platform.processor()}
for n in (15, 20):
    mods = (n, n, n)
    rng = random.Random(1000 + n)
    elems = [tuple(rng.randrange(n) for _ in range(3)) for _ in range(20000)]
    o = A.Oracle(mods)
    # push/pop cycles from the empty state with random single elements
    t0 = time.perf_counter(); k = 0
    for g in elems:
        if o.push(g):
            o.pop(); k += 1
    t_pp = time.perf_counter() - t0
    # legal_mask at a depth-(n-1) prefix (first standard block)
    for _ in range(n - 1):
        assert o.push((1, 0, 0))
    t0 = time.perf_counter()
    for _ in range(5000):
        o.legal_mask()
    t_lm = time.perf_counter() - t0
    # full checks of the standard sequence
    s = [(1, 0, 0)] * (n - 1) + [(0, 1, 0)] * (n - 1) + [(0, 0, 1)] * (n - 1)
    t0 = time.perf_counter()
    for _ in range(200):
        A.is_zero_sumfree(s, mods)
    t_fa = (time.perf_counter() - t0) / 200
    t0 = time.perf_counter(); B.is_zero_sumfree(s, mods); t_fb = time.perf_counter() - t0
    out[f"n{n}"] = {"push_pop_cycles": k, "push_pop_per_sec": round(k / t_pp),
                    "legal_mask_per_sec": round(5000 / t_lm),
                    "checkerA_full_check_seconds_len%d" % len(s): round(t_fa, 6),
                    "checkerB_full_check_seconds_len%d" % len(s): round(t_fb, 4)}
print(json.dumps(out, indent=1))
