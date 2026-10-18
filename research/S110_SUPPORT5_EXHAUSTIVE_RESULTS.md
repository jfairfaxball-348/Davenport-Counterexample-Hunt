# S110 — Support-≤5 exhaustive campaigns CAM-0006 / CAM-0007: results (17–18 October 2026)

Priority: **SATURATION_FALLBACK**, with the owner-authorised support-5 track (PR #114). The campaigns were pre-registered in S109 (PR #116) and activated in S110, exactly as pre-registered.

## 1. Pre-activation re-verification

- The LF SHA-256 of `tools/zsf/support5_a.py` (`41d37aa6…`) and `support5_b.py` (`f2d06fe1…`) from main `e3ecb17` equal both pre-registrations.
- Python 3.12.10 and numpy 1.26.4: no deviation.
- The settled re-check at n=6 gives max 15 for both algorithms, with orbit-set hash `adacfc5720cb…` for both, equal to S109.

## 2. Execution

- `sessions/S110/run_campaigns.sh` ran 56 shard jobs (14 per algorithm per campaign), each under `timeout 43200`, with at most 14 concurrent processes. The order was CAM-0006 A+B, then CAM-0007 B, then CAM-0007 A, as pre-registered.
- Activation was at 2026-10-17T14:23:30Z, and the last shard ended at 2026-10-18T00:49:43Z.
- **All 56 shards exited 0. No shard was truncated or crashed, and no parameter changed.**
- Idle sleep was held by the app's keep-awake hold and by a runtime-only inhibitor, `sessions/S110/stay_awake.ps1`. No settings were changed.

## 3. Results (`campaigns/CAM-0006/RESULT.json`, `campaigns/CAM-0007/RESULT.json`)

| Campaign | Algorithm | Pairs evaluated / expected | Max optimum | ≥ 3n−2 | Histogram of optima | CPU-h |
|---|---|---|---|---|---|---|
| CAM-0006, n=15, L=43 | A | 791,934 / 791,934 | 42 | 0 | 26: 35, 34: 15909, 42: 775990 | 8.5 |
| | B | 349,690 / 349,690 | 42 | 0 | 26: 21, 34: 7120, 42: 342549 | 0.5 |
| CAM-0007, n=20, L=58 | A | 4,162,730 / 4,162,730 | 57 | 0 | 33: 39, 36: 229, 39: 186, 45: 34727, 48: 138476, 57: 3989073 | 117.7 |
| | B | 2,866,880 / 2,866,880 | 57 | 0 | 33: 36, 36: 438, 39: 486, 45: 27565, 48: 131091, 57: 2707264 | 19.2 |

**Two-algorithm agreement:**
- Coverage is full for every algorithm and campaign.
- The maxima are equal.
- No relation module reaches the threshold.
- The sets of attained optimum values are identical: {26, 34, 42} at n=15 and {33, 36, 39, 45, 48, 57} at n=20.

The counts differ only because the two algorithms enumerate different representative systems (CLM-0364).

**Cost:** 8.9 CPU-h (n15) + 136.9 CPU-h (n20), measured under 14-way contention. The S109 estimate was ≈ 72 CPU-h; the actual cost was about twice that, mainly algorithm A at n=20 (≈ 0.1 s per pair rather than the estimated 0.05 s). Every shard finished well inside the 12 h cap: the longest took 30,327 s.

## 4. Conclusions

**CLM-0366 (COMPUTED_EXACT; CONDITIONAL on the programme proofs CLM-0358, CLM-0361..0364).** No zero-sumfree sequence over C15³ with at most five distinct values has length 43. The maximum is 42 = 3n−3.

**CLM-0367 (COMPUTED_EXACT; same basis).** No zero-sumfree sequence over C20³ with at most five distinct values has length 58. The maximum is 57 = 3n−3.

**Combined with CLM-0359 (unconditional):** a zero-sumfree sequence of length 3n−2 over C15³ or C20³, that is a counterexample to SAT15/SAT20, would need **at least 6 distinct values**.

**Scope and certificate:**
- These are exclusions of one structured family only. They are **not** SAT15/SAT20, not a D value, and the frontier is unchanged.
- The certificate is two independent same-executor exhaustive algorithms with full coverage, plus committed shard logs (SHA-256s recorded in RESULT.json). There is no Lean/DRAT certificate, so the result is not FORMALLY_CERTIFIED.
- Correctness of the reduction rests on the hand proofs CLM-0358 and CLM-0361..0364, which both algorithms share. An error there would affect both.

## 5. Status

- Search counters for the original SEARCH_FIRST rounds are unchanged. The support-5 track is now complete.
- Priority stays SATURATION_FALLBACK.
- **Next:** support ≥ 6. Six values give relation modules of rank 3 (|K| = n³). The S108 counting gives |S| ≤ 6(n−1) − n + 1/n², which is far from 3n−3.
  - Exhaustive enumeration of rank-3 summands of (Z/n)^6 is roughly n^9 / 720 per prime-power component pairing, which is likely infeasible at n=20 by these methods.
  - Extending the exhaustive track to 6 values would need a new owner decision and a feasibility study first.
