# S104 — SEARCH-FIRST ROUND 1 EXECUTION (FUTURE / NOT EXECUTED)

**Active owner directive (16 October 2026, carried forward unchanged): SEARCH_FIRST.**
- The primary goal is direct discovery of a zero-sumfree counterexample in C_n³: length 43 at n=15 (then 44), and length 58 at n=20.
- Subset-sum saturation and universal structural mathematics are the FALLBACK.
- Run S104 only on a separate later owner "Run next session", and run only ONE numbered session per invocation.
- Carry this directive, the counters and the fallback trigger into every future prompt until evidence or the owner changes them.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S103 merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s103_result`), `campaigns/REGISTRY.md`, `campaigns/CAM-0002/PREREGISTRATION.json` and `campaigns/CAM-0003/PREREGISTRATION.json`, `docs/PHASE_GATE_LEDGER.md` (S103 gates), `research/S103_SEARCH_TOOLING_AND_PREREGISTRATION.md`, and `sessions/S103/*`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S104/INPUT.md` and `INPUT_MANIFEST.json`.

**State at S103 close:**
- Phase 1 has a SCOPED PASS (search targets n15/n20); the general frontier map is still IN_PROGRESS.
- Phase 2 has a SCOPED PASS covering exact checkers A/B and the R1-ILS-1.0 heuristic engine only.
- Phase 3: CAM-0002 and CAM-0003 are PREREGISTERED and not activated.
- Search counters: setup sessions 1 (S103), active search sessions 0, completed materially distinct rounds 0.
- Claims total 346, sources total 32 (the original 29 untouched), and the 30 frontier rows are untouched.

## 1. Activate and run round 1 (both targets)

1. **Re-verify before activation.** Recompute SHA-256 of `tools/zsf/ils_engine.py`, `checker_a.py` and `checker_b.py` from the committed main checkout, and compare against `code_sha256` in both pre-registrations. Rerun `python -I tools/zsf/test_zsf.py` and require overall PASS.
   - If either check fails, do NOT activate. Record the blocker, fix it in a gated way and re-preregister.
   - Record the Python and numpy versions. If they differ from 3.12.10 and 1.26.4, record the deviation explicitly.
2. **Activate** CAM-0002 and CAM-0003 exactly as pre-registered:
   - 6 workers per target, seeds 103001–103006 (n15, target 43) and 103101–103106 (n20, target 58);
   - `--iterations 200000 --walltime 7200`;
   - checkpoints in `campaigns/CAM-000x/checkpoints/seed-<SEED>.jsonl`.
   
   Run them as background processes; 12 concurrent processes fit on the 16 logical CPUs. Do not change any parameter mid-run. If a worker crashes, rerun it from the same seed per the pre-registration and record the crash.
3. **Report only actual results**, per worker and per target:
   - status: BUDGET_EXHAUSTED, WALLTIME_CAP_TRUNCATED or TARGET_REACHED_UNCERTIFIED;
   - iterations completed, elapsed time, best length attained, the length histogram, and the best sequence's SHA-256;
   - both checkers' verdicts on the best sequence.
   
   Commit the checkpoint logs. If they are very large, commit the final summary records and the SHA-256 of the full logs.
   
   Do NOT invent rates or extrapolations. Budget exhaustion is NOT evidence of nonexistence and NOT a negative result.
4. **On a hit:** create `candidates/<id>/sequence.json` with the canonical sorted triples, modulus, length and SHA-256, following `candidates/README.md`. Rerun checker A and checker B standalone, and verify the A/B agreement plus direct witness absence.
   - Status is CANDIDATE only.
   - Plan a Lean 4 kernel proof, for example a certificate of the prefix Σ sets checked against CLM-0345 by kernel computation, plus a cold re-check in a later session before any certified claim.
   - Do not contact third parties, publish, or register with Palomar without explicit owner authorisation.
5. **Update the counters.** If round 1 genuinely ran on both targets, S104 counts as active search session 1 and round 1 as complete or partial as actually observed. A walltime-truncated worker makes the round partial for that target; say so.

## 2. Pre-register a materially different round 2 (do not run it in S104)

Pre-register CAM-0004 (n15) and CAM-0005 (n20) round 2 using a method that is **materially different** from R1. Parameter tweaks of R1 do not count. Candidate methods:
- **(a) Structured seeds.** Grow from structured near-extremal prefixes, such as unions of cyclic progressions, sequences supported on few cosets of a subgroup, or lifts of extremal C3³/C5³ (n=15) or C4³/C5³ (n=20) sequences via the CRT. Then apply exact local search.
- **(b) SAT/CP candidate generation.** Fix the support multiset pattern and solve for coordinates. This requires gated SAT tooling first, and its output stays a candidate generator only.
- **(c) Large-neighbourhood swaps.** Use an exact "remove k, add k+1" deficiency-repair move driven by the complement of Σ.

State the domain, any proved reductions (CLM-0345(d) only, unless newly proved), the completeness class, budget, seeds, code SHA-256s, checkpoints and stopping rule. Implement and test the new engine and pre-flight it on settled groups only. Record a Phase-2 gate extension if new tooling is introduced.

## 3. Mandatory fallback trigger (unchanged)

- After **two completed, materially different, bounded and documented rounds** covering n15 and n20, if no real candidate survived two exact checkers, no significant certified exclusion was obtained and no substantive structural theorem was proved: write a negative/partial experimental closeout and switch the priority to SATURATION_FALLBACK.
- Switch in any case **no later than the close of the third active search session** without such evidence.
- Blocked setup sessions do not count as rounds. If an unresolvable blocker persists across two setup sessions, report it and pivot. S103 was setup session 1.
- Cosmetic parameter changes and benchmark improvements do not reset the trigger.
- **Fallback statement:** every zero-sumfree 57-term indexed sequence in C20³ has Σ (with the empty sum) equal to the whole group. By CLM-0345(c) this is equivalent to there being no zero-sumfree 58-term sequence, and it is OPEN.
- **Fallback directions:** Kneser/stabiliser growth of Σ, near-saturation extremal structure, projections and lifting over 4·5 and 3·5 with carries, and whether arbitrary extremal sequences admit the S060/S102 reductions. The n15 analogue is length-42 saturation.

Maintain `counterexample_hunt_strategy` in STATE.json with: priority, targets, setup and active sessions, completed rounds, campaign statuses, two-checker results, gate states, decisive evidence and switch rationale.

## 4. Deliverables and close

- Create S104 INPUT, INPUT_MANIFEST, PLAN, VALIDATION, SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Add campaign result files and a registry update giving the actual status of CAM-0002/0003 (ACTIVE→COMPLETED, PARTIAL or TRUNCATED), plus the round-2 pre-registration.
- Update: phase/session/failure/decision ledgers, STATE, README/START_HERE, and claims only where a real proof or exact computation exists.
- Leave the frontier unchanged unless there is an independently checked improvement. Keep the original 29 sources and 30 frontier rows intact.
- Install a FULL S105 prompt. It continues SEARCH_FIRST (round 2 execution) unless the fallback trigger is met; in that case install the saturation fallback prompt.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, and never present a single solver or script as a certification.
