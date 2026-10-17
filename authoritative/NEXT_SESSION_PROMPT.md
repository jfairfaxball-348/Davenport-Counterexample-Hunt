# S105 — SEARCH-FIRST ROUND 2 EXECUTION AND FALLBACK DECISION (FUTURE / NOT EXECUTED)

**Active owner directive (16 October 2026, carried forward unchanged): SEARCH_FIRST.**
- The primary goal is direct discovery of a zero-sumfree counterexample in C_n³: length 43 at n=15 (then 44), and length 58 at n=20.
- Subset-sum saturation and universal structural mathematics are the FALLBACK.
- Run S105 only on a separate later owner "Run next session", and run only ONE numbered session per invocation.
- Carry this directive, the counters and the fallback trigger into every future prompt until evidence or the owner changes them.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S104 merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s104_result`), `campaigns/REGISTRY.md`, `campaigns/CAM-0004/PREREGISTRATION.json`, `campaigns/CAM-0005/PREREGISTRATION.json`, `campaigns/CAM-0002/RESULT.json`, `campaigns/CAM-0003/RESULT.json`, `docs/PHASE_GATE_LEDGER.md` (S103 and S104 gates), `research/S104_ROUND1_RESULTS_AND_ROUND2_PREREGISTRATION.md`, and `sessions/S104/*`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S105/INPUT.md` and `INPUT_MANIFEST.json`.

**State at S104 close:**
- Phase 1 has a SCOPED PASS (search targets n15/n20); the general frontier map is still IN_PROGRESS.
- Phase 2 has a SCOPED PASS covering exact checkers A/B, the R1-ILS-1.0 engine and (S104 extension) the R2-LNS-1.0 engine only.
- Phase 3: round 1 (CAM-0002 n15, CAM-0003 n20; R1-ILS-1.0) COMPLETED in S104. All 12 workers were BUDGET_EXHAUSTED at 200,000 iterations, with best lengths 42 and 57 (= 3n−3), no hit and no candidate. Round 2 (CAM-0004 n15, CAM-0005 n20; R2-LNS-1.0) is PREREGISTERED and not activated.
- Search counters: setup sessions 1 (S103), active search sessions 1 (S104), completed materially distinct rounds 1.
- Claims total 347 (CLM-0347 two-term extension criterion), sources total 32 (the original 29 untouched), and the 30 frontier rows are untouched.

## 1. Activate and run round 2 (both targets)

1. **Re-verify before activation.** Recompute SHA-256 (LF bytes) of `tools/zsf/lns_engine.py`, `checker_a.py` and `checker_b.py` from the committed main checkout, and compare against `code_sha256` in both CAM-0004 and CAM-0005 pre-registrations. Rerun `python -I tools/zsf/test_zsf.py` and `python -I tools/zsf/preflight_lns.py` and require overall PASS from both.
   - If any check fails, do NOT activate. Record the blocker, fix it in a gated way and re-preregister. A blocked session is a setup session, not a round.
   - Record the Python and numpy versions. If they differ from 3.12.10 and 1.26.4, record the deviation explicitly.
2. **Activate** CAM-0004 and CAM-0005 exactly as pre-registered:
   - 6 workers per target: seeds 104001–104003 `--init uniform` and 104004–104006 `--init standard` (n15, target 43); seeds 104101–104103 `--init uniform` and 104104–104106 `--init standard` (n20, target 58);
   - `--iterations 1200 --walltime 7200`;
   - checkpoints in `campaigns/CAM-000x/checkpoints/seed-<SEED>.jsonl`.

   Run them as 12 concurrent background processes on the 16 logical CPUs. Do not change any parameter mid-run. Verify each worker's logged `param_hash` against `parameter_sha256_per_worker`. If a worker crashes, rerun it from the same seed per the pre-registration and record the crash.
3. **Report only actual results**, per worker and per target:
   - status: BUDGET_EXHAUSTED, WALLTIME_CAP_TRUNCATED or TARGET_REACHED_UNCERTIFIED;
   - iterations completed, elapsed time, best length attained, the length histogram, move statistics (k1_improve, k1_locally_maximal, k2_improve, plateau, restart), and the best sequence's SHA-256;
   - both checkers' verdicts on the best sequence, rerun standalone from the logged sequence (not the in-engine verdict).

   Write `campaigns/CAM-000{4,5}/RESULT.json` in the same form as the S104 round-1 results (including full-log SHA-256s), and commit the checkpoint logs.

   Do NOT invent rates or extrapolations. Budget exhaustion is NOT evidence of nonexistence and NOT a negative result. `k1_locally_maximal` counts are exact statements about visited states only.
4. **On a hit:** create `candidates/<id>/sequence.json` with the canonical sorted triples, modulus, length and SHA-256, following `candidates/README.md`. Rerun checker A and checker B standalone, and verify the A/B agreement plus direct witness absence.
   - Status is CANDIDATE only.
   - Plan a Lean 4 kernel proof, for example a certificate of the prefix Σ sets checked against CLM-0345 by kernel computation, plus a cold re-check in a later session before any certified claim.
   - Do not contact third parties, publish, or register with Palomar without explicit owner authorisation.
   - A surviving two-checker candidate means the fallback trigger is NOT met; then install a S106 prompt for candidate certification (Lean 4 plan and cold re-check) instead of the fallback prompt.
5. **Update the counters.** If round 2 genuinely ran on both targets, S105 counts as active search session 2 and round 2 as complete or partial as actually observed. A walltime-truncated worker makes the round partial for that target; say so. A partial round does not count as a completed round.

## 2. Mandatory fallback decision (in S105)

- **Trigger:** after **two completed, materially different, bounded and documented rounds** covering n15 and n20, if no real candidate survived two exact checkers, no significant certified exclusion was obtained and no substantive structural theorem was proved: write a negative/partial experimental closeout and switch the priority to SATURATION_FALLBACK.
- Switch in any case **no later than the close of the third active search session** without such evidence.
- Blocked setup sessions do not count as rounds. If an unresolvable blocker persists across two setup sessions, report it and pivot. S103 was setup session 1.
- Cosmetic parameter changes and benchmark improvements do not reset the trigger. CLM-0347 is an elementary tooling lemma, not a substantive theorem.
- **If round 2 completes on both targets with no surviving candidate**, the trigger IS met in S105:
  - write `research/S105_SEARCH_FIRST_EXPERIMENTAL_CLOSEOUT.md`, a negative/partial experimental closeout covering both rounds, all budgets, attained maxima, histograms and the explicit statement that HEURISTIC exhaustion proves nothing;
  - set `counterexample_hunt_strategy.priority` to SATURATION_FALLBACK with a dated switch rationale, and keep the search tooling and campaign records intact;
  - install a FULL S106 saturation-fallback prompt (see below).
- **If round 2 is partial** (any truncated worker) the trigger is not yet met by the two-round clause. Then install a S106 prompt that either completes round 2 or runs a materially different round 3 (pre-registered in S105). The third-active-session cap still forces the switch at the close of S106 at the latest.

**Fallback statement:** every zero-sumfree 57-term indexed sequence in C20³ has Σ (with the empty sum) equal to the whole group. By CLM-0345(c) this is equivalent to there being no zero-sumfree 58-term sequence, and it is OPEN.

**Fallback directions** for the S106 prompt:
- Kneser/stabiliser growth of Σ;
- near-saturation extremal structure (S104 observation: every round-1 best sequence had a value of multiplicity n−1 — heuristic only, a possible structural lead to state and test as a conjecture, not a claim);
- projections and lifting over 4·5 and 3·5 with carries;
- whether arbitrary extremal sequences admit the S060/S102 reductions.

The n15 analogue is length-42 saturation.

Maintain `counterexample_hunt_strategy` in STATE.json with: priority, targets, setup and active sessions, completed rounds, campaign statuses, two-checker results, gate states, decisive evidence and switch rationale.

## 3. Deliverables and close

- Create S105 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (a `validation/validate_s105.py` in the style of `validate_s104.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Add campaign result files and a registry update giving the actual status of CAM-0004/0005.
- Update: phase/session/failure/decision ledgers, STATE, README/START_HERE, and claims only where a real proof or exact computation exists.
- Leave the frontier unchanged unless there is an independently checked improvement. Keep the original 29 sources and 30 frontier rows intact.
- Install a FULL S106 prompt as determined by §1.4 and §2: candidate certification, round-2 completion/round 3, or SATURATION_FALLBACK.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, and never present a single solver or script as a certification.
