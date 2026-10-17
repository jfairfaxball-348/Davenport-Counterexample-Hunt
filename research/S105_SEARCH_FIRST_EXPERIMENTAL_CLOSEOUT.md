# S105 — Round-2 results and SEARCH_FIRST experimental closeout (17 October 2026)

This is the negative/partial experimental closeout required by the owner directive of 16 October 2026 once the two-round fallback trigger is met. **It is not a negative mathematical result.** Both rounds are HEURISTIC; exhausting their budgets says nothing about whether a zero-sumfree sequence of length 43 in C15³ or of length 58 in C20³ exists.

## 1. Round-2 pre-activation re-verification

- The SHA-256 of `tools/zsf/lns_engine.py` (`8cf7633d…`), `checker_a.py` (`72dd6122…`) and `checker_b.py` (`6f2a0588…`) were computed from both the git blob and the working tree at main `35ee471`. All equal the `code_sha256` values in CAM-0004 and CAM-0005.
- `test_zsf.py` gave overall PASS (`sessions/S105/TEST_OUTPUT.json`).
- `preflight_lns.py` gave overall PASS, with output byte-identical in content to the S104 pre-flight (`sessions/S105/LNS_PREFLIGHT.json`).
- Python is 3.12.10 and numpy is 1.26.4, the registered versions. No deviation.

**Pre-registration defect, found and disclosed.** The S104 `parameter_sha256_per_worker` values were computed with walltime serialised as the integer `7200`. The engine serialises the argparse float `7200.0`, so every logged `param_hash` differs from the registered hash. For every worker, three things were checked:
- the logged `params` record equals the registered parameter values exactly;
- the registered hash is reproduced from those values with an int walltime;
- the logged hash is reproduced from the same values with a float walltime.

The run therefore used exactly the registered parameters. The defect is in the S104 documentation, not a run deviation. It is recorded in both RESULT files and in the failure ledger.

## 2. Round 2 (R2-LNS-1.0) — actual results

Activation was at 2026-10-17T09:51:06Z, and all 12 workers had ended by 09:58:33Z. They ran as 12 concurrent processes using the registered commands. No worker crashed, was truncated or reached the target.

| Campaign | Seed | Init (start length) | Status | Iterations | Elapsed (s) | Best length | Checker A / B | k1 improve | k2 improve | Restarts |
|---|---|---|---|---|---|---|---|---|---|---|
| CAM-0004 n15 | 104001 | uniform (15) | BUDGET_EXHAUSTED | 1200 | 259.3 | 42 | ZSF / ZSF | 93 | 28 | 4 |
| | 104002 | uniform (15) | BUDGET_EXHAUSTED | 1200 | 201.9 | 42 | ZSF / ZSF | 84 | 33 | 5 |
| | 104003 | uniform (16) | BUDGET_EXHAUSTED | 1200 | 227.3 | 42 | ZSF / ZSF | 96 | 24 | 4 |
| | 104004 | standard (42) | BUDGET_EXHAUSTED | 1200 | 223.3 | 42 | ZSF / ZSF | 0 | 0 | 6 |
| | 104005 | standard (42) | BUDGET_EXHAUSTED | 1200 | 237.9 | 42 | ZSF / ZSF | 0 | 0 | 6 |
| | 104006 | standard (42) | BUDGET_EXHAUSTED | 1200 | 277.1 | 42 | ZSF / ZSF | 0 | 0 | 6 |
| CAM-0005 n20 | 104101 | uniform (17) | BUDGET_EXHAUSTED | 1200 | 334.6 | 57 | ZSF / ZSF | 127 | 30 | 4 |
| | 104102 | uniform (16) | BUDGET_EXHAUSTED | 1200 | 275.8 | 57 | ZSF / ZSF | 101 | 38 | 4 |
| | 104103 | uniform (17) | BUDGET_EXHAUSTED | 1200 | 294.1 | 57 | ZSF / ZSF | 86 | 45 | 3 |
| | 104104 | standard (57) | BUDGET_EXHAUSTED | 1200 | 355.8 | 57 | ZSF / ZSF | 0 | 0 | 6 |
| | 104105 | standard (57) | BUDGET_EXHAUSTED | 1200 | 446.0 | 57 | ZSF / ZSF | 0 | 0 | 6 |
| | 104106 | standard (57) | BUDGET_EXHAUSTED | 1200 | 333.9 | 57 | ZSF / ZSF | 0 | 0 | 6 |

The best-sequence SHA-256s, histograms, multiplicities, move statistics and full-log hashes are in `campaigns/CAM-0004/RESULT.json` and `campaigns/CAM-0005/RESULT.json`. The checker verdicts were recomputed standalone from the logged best sequences.

**Move statistics.**
- **n15:** 273 k1 improvements and 85 k2 improvements. 6,927 visited states were exactly k=1-locally maximal. There were 6,842 plateau swaps and 31 restarts.
- **n20:** 314 k1 improvements and 113 k2 improvements. 6,886 visited states were exactly k=1-locally maximal. There were 6,773 plateau swaps and 29 restarts.

Every k1/k2 improvement was a step from below 3n−3 toward 3n−3. None went beyond it.

**Observations (HEURISTIC, descriptive only):**
- R2's exact repair moves lift uniform random maximal sequences, which start at length 15–17, up to 3n−3 within each restart.
- Every k=1 neighbourhood of every visited length-(3n−3) state was exactly closed. That means no single removal from such a state admitted two additions. This is an exact statement about the visited states only.
- Best sequences now include non-standard structures with small support: for example multiplicities 13, 13, 3, … with 13–15 distinct values at n15, and 18, 9, 5, … at n20. So the S104 pattern "one value of multiplicity n−1" is **not** universal among the 3n−3 sequences this engine finds. That weakens the S104 heuristic lead.

## 3. Both rounds together

| Round | Method | n15 best (target 43) | n20 best (target 58) | Workers | Status |
|---|---|---|---|---|---|
| 1 (S104) | R1-ILS-1.0: softmin regrow + random ruin, 200,000 iterations per worker | 42 | 57 | 12/12 BUDGET_EXHAUSTED | COMPLETE, no hit |
| 2 (S105) | R2-LNS-1.0: exact remove-k/add-(k+1) repair (CLM-0347), tabu plateau, structured seeds, 1200 iterations per worker | 42 | 57 | 12/12 BUDGET_EXHAUSTED | COMPLETE, no hit |

Across both rounds, the attained maximum equals 3n−3 = 42 resp. 57, the recorded lower-bound construction length. No sequence of length ≥ 3n−2 was produced. There is no candidate, and `candidates/` contains only its README.

## 4. Fallback decision (directive §2, applied)

- Two completed, materially different, bounded and documented rounds covered n15 and n20 (round 1 in S104, round 2 in S105).
- No candidate survived the two exact checkers, because none was produced.
- No significant certified exclusion was obtained. None was attempted: the search was HEURISTIC.
- No substantive structural theorem was proved. CLM-0347 is an elementary tooling lemma.

**The trigger is MET. As of S105 the priority switches from SEARCH_FIRST to SATURATION_FALLBACK.** The search tooling, pre-registrations, results and logs are preserved unchanged. Search may be reopened only by an explicit owner directive, or by a new pre-registered campaign justified by a substantive structural reason recorded in the claims ledger. A parameter change of R1 or R2 is not such a reason.

**Final counters:** setup sessions 1 (S103), active search sessions 2 (S104, S105), completed materially distinct rounds 2.

**Fallback statement (OPEN):** every zero-sumfree 57-term indexed sequence in C20³ has Σ (including the empty sum) equal to the whole group. By CLM-0345(c), this is equivalent to there being no zero-sumfree 58-term sequence. The n15 analogue is length-42 saturation in C15³, equivalent to no zero-sumfree 43-term sequence.
