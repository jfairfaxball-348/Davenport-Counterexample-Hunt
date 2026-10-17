# S104 — Round-1 search results and round-2 pre-registration (17 October 2026)

Priority: **SEARCH_FIRST** (owner directive of 16 October 2026, unchanged). Targets: a zero-sumfree sequence of length 43 in C15³ (then 44) and of length 58 in C20³.

## 1. Pre-activation re-verification

- SHA-256 of `tools/zsf/ils_engine.py` (`e0749fc3…`), `checker_a.py` (`72dd6122…`) and `checker_b.py` (`6f2a0588…`) from the committed main checkout `eec2f52` equal the `code_sha256` values in both CAM-0002 and CAM-0003 pre-registrations (git blob bytes and working-tree bytes both checked).
- `python -I tools/zsf/test_zsf.py`: overall **PASS** (`sessions/S104/TEST_OUTPUT.json`).
- Python 3.12.10, numpy 1.26.4: identical to the pre-registered versions, so there is no deviation.
- Every worker's logged `param_hash` equals its pre-registered `parameter_sha256_per_worker` value.

## 2. Round 1 (R1-ILS-1.0) — actual results

Activation 2026-10-17T09:00:09Z, all 12 workers ended by 09:22:03Z. 12 concurrent processes, exactly the pre-registered commands (`--iterations 200000 --walltime 7200`). No parameter was changed, no worker crashed, and no worker hit the walltime cap.

| Campaign | Seed | Status | Iterations | Elapsed (s) | Best length | Best SHA-256 (prefix) | Checker A | Checker B |
|---|---|---|---|---|---|---|---|---|
| CAM-0002 n15 | 103001 | BUDGET_EXHAUSTED | 200000 | 934.5 | 42 | 8642ebd4 | ZSF | ZSF |
| | 103002 | BUDGET_EXHAUSTED | 200000 | 962.9 | 42 | d8955292 | ZSF | ZSF |
| | 103003 | BUDGET_EXHAUSTED | 200000 | 917.7 | 42 | 8d5d2ae4 | ZSF | ZSF |
| | 103004 | BUDGET_EXHAUSTED | 200000 | 951.7 | 42 | c82c1f55 | ZSF | ZSF |
| | 103005 | BUDGET_EXHAUSTED | 200000 | 959.8 | 42 | 7614739e | ZSF | ZSF |
| | 103006 | BUDGET_EXHAUSTED | 200000 | 953.2 | 42 | 8e0518a7 | ZSF | ZSF |
| CAM-0003 n20 | 103101 | BUDGET_EXHAUSTED | 200000 | 1312.1 | 57 | ab4f265d | ZSF | ZSF |
| | 103102 | BUDGET_EXHAUSTED | 200000 | 1312.5 | 57 | 6b0119a2 | ZSF | ZSF |
| | 103103 | BUDGET_EXHAUSTED | 200000 | 1308.0 | 57 | 7716e0d6 | ZSF | ZSF |
| | 103104 | BUDGET_EXHAUSTED | 200000 | 1313.1 | 57 | 5fa3ad45 | ZSF | ZSF |
| | 103105 | BUDGET_EXHAUSTED | 200000 | 1310.9 | 57 | b4689cf9 | ZSF | ZSF |
| | 103106 | BUDGET_EXHAUSTED | 200000 | 1306.1 | 57 | 5a0f2ab2 | ZSF | ZSF |

Full SHA-256 values, per-worker length histograms and the full-log hashes are in `campaigns/CAM-0002/RESULT.json` and `campaigns/CAM-0003/RESULT.json`. The checker verdicts were recomputed standalone, outside the engine, from the logged best sequences, and the logged canonical hashes were recomputed.

**Aggregate histogram of post-move lengths (1.2 million moves per target):**
- n15: 42 → 1,172,955; 41 → 3,350; 34 → 23,539; the rest are scattered between 25 and 40. No move produced 43.
- n20: 57 → 1,189,598; 56 → 3,918; 45 → 5,054; 48 → 1,237; the rest are scattered between 44 and 55. No move produced 58.

**Observations (HEURISTIC, descriptive only, no claim):**
- Every best sequence has length exactly 3n−3, and |Σ| = n³ as maximality forces.
- Each best sequence contains one value with the maximal possible multiplicity n−1 (14 resp. 19). Its 22–26 (n15) resp. 30–33 (n20) distinct values are not the standard three-value sequence.
- The engine readily finds many non-standard maximal length-(3n−3) sequences but never exceeds 3n−3.
- The low clusters (34 at n15; 45 and 48 at n20) are other maximal plateaux that ruin-and-regrow occasionally falls into.

**Semantics:** this is budget exhaustion of a HEURISTIC method. It is **not** evidence that no zero-sumfree sequence of length 43 or 58 exists, and it is **not** a negative result. No candidate exists, `candidates/` is unchanged, and the frontier is unchanged.

**Round status:** round 1 is **COMPLETE** on both targets: all 12 workers reached their iteration budget, none was truncated. Counters: setup sessions 1 (S103), active search sessions 1 (S104), completed materially distinct rounds 1.

## 3. CLM-0347 (PROGRAMME_PROVED, elementary)

Let T be zero-sumfree in a finite abelian group G, with Σ including the empty sum. **Claim:** there exist a, b with Tab zero-sumfree iff some a with −a ∉ Σ(T) satisfies |Σ(T)| + |(a+Σ(T)) \ Σ(T)| < |G|.

*Proof.* By the prefix criterion (CLM-0345), Tab is zero-sumfree iff −a ∉ Σ(T) and −b ∉ Σ(Ta). For fixed legal a, a legal b exists iff Σ(Ta) ≠ G. Also Σ(Ta) = Σ(T) ∪ (a+Σ(T)), so its size is |Σ(T)| + |(a+Σ(T)) \ Σ(T)|. ∎

The values |(a+Σ)\Σ| for all a at once are |Σ| minus the cyclic autocorrelation of the indicator of Σ. They are computed by FFT and rounded to integers, as in R1, and agree with direct exact updates in the S103 and S104 tests. Every move R2 finds is replayed through the exact oracle, so an FFT error could only cause a missed move, never a false sequence.

## 4. Round 2 — CAM-0004 (n15) / CAM-0005 (n20), PREREGISTERED, not run in S104

**Method R2-LNS-1.0** (`tools/zsf/lns_engine.py`, prompt option (c), with structured seeds from option (a) for half the workers):
- **Exact k=1 move.** For each visited maximal state and each distinct value x, remove x and decide by CLM-0347, over all first additions a at once, whether two terms can be added. This neighbourhood is decided exhaustively per state.
- **k=2 move.** Sample 12 removal pairs. For each, enumerate up to 64 lowest-coverage legal first additions and decide the last two levels by CLM-0347.
- **Plateau.** Otherwise take a tabu plateau swap (remove x, add a legal a ≠ x not on the tabu list of 8) and regrow uniformly. Restart after 200 non-improving iterations.
- **Seeds.** 104001–104003 / 104101–104103 start uniform; 104004–104006 / 104104–104106 start from the standard sequence.
- **Budget.** 1200 iterations, 7200 s walltime cap per worker, 6 workers per target.

**Why it is materially different from R1:**
- R1 uses random ruin with softmin-coverage regrow and accepts on length alone.
- R2 makes systematic exact neighbourhood decisions driven by the complement of Σ, uses uniform growth, adds a tabu plateau walk and a structured seed family.
- R2 is not a parameter tweak of R1.

**Other registration details:**
- Reductions: none used. CLM-0345(d) is recorded only.
- Completeness class: HEURISTIC.
- Code SHA-256: `lns_engine.py` 8cf7633d…, plus checker A/B unchanged. Per-worker parameter hashes are in the pre-registrations.

**Pre-flight** (`sessions/S104/LNS_PREFLIGHT.json`, settled groups n=3,4,5,6 only):
- 120 FFT two-addition decisions agree with exhaustive oracle enumeration.
- The best length is exactly 3n−3 for both seed families, never more.
- k1/k2 improvement moves are exercised at n=6.
- Determinism PASS.

**Budget sizing.** It used only component timing on fixed inputs, not a search: rebuild 1.2–1.6 ms and one FFT 0.4–0.9 ms at n15/n20.

**Phase-2 gate extension:** SCOPED PASS for R2-LNS-1.0, recorded in `docs/PHASE_GATE_LEDGER.md`. Activation is permitted from S105, after this commit is on main and the hashes are re-verified.

## 5. Fallback trigger status

- Completed rounds: 1 of 2. Active search sessions: 1 of 3.
- No candidate, no certified exclusion and no substantive structural theorem so far. CLM-0347 is an elementary tooling lemma, not a substantive theorem.
- The trigger is **not yet met**. S105 runs round 2.
- If round 2 also yields nothing substantive, S105 meets the two-round condition and must write the negative/partial experimental closeout and switch to SATURATION_FALLBACK.
