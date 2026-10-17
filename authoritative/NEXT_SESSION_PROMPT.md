# S110 — SUPPORT-5 EXHAUSTIVE CAMPAIGN ACTIVATION (FUTURE / NOT EXECUTED)

**Active priority: SATURATION_FALLBACK**, plus the **owner-authorised support-5 exhaustive track** (2026-10-17, PR #114: "Yes allow it"; scope = sequences with at most five distinct values only).
- General search stays closed.
- Run S110 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters, the search-reopen condition and the authorisation scope into every future prompt.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S109 merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s109_result`), `research/S109_SUPPORT5_EXHAUSTIVE_TOOLING.md`, `campaigns/CAM-0006/PREREGISTRATION.json`, `campaigns/CAM-0007/PREREGISTRATION.json`, `campaigns/REGISTRY.md`, `sessions/S109/PREFLIGHT_SUMMARY.json`, `docs/PHASE_GATE_LEDGER.md` (S109 gates), and `sessions/S109/*`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S110/INPUT.md` and `INPUT_MANIFEST.json`. Paraphrase any product or model names in owner text (AGENTS rule 10), and grep the staged diff for them before committing.
- **Git credentials:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential for that command only. Do not change the stored configuration.
- **Processes:** never kill interpreter processes by image name. Resolve PIDs by command line (S109 lesson).
- **Before committing,** verify that every intended file change is actually on disk (S109 lesson: a refused write left a stale prompt in a first commit).

**State at S109 close:**
- Claims 365. Sources 34 (original 29 untouched). Frontier 30 rows untouched.
- Phase 2 SCOPED PASS covering checkers A/B, R1/R2, and the support-5 tools (`tools/zsf/support5_a.py` SHA-256 `41d37aa63767d3eb7767d55eb300eb01d7df34b84c5f99318b3a1bb857bd4279`, `support5_b.py` `f2d06fe1db89a1dba886327504f936cbc94dcfbce127c44a1923a930cd48dc3a`).
- CAM-0006 (n=15, L=43) and CAM-0007 (n=20, L=58) are PREREGISTERED, EXHAUSTIVE for the support-≤5 family only.
- Search counters frozen (setup 1, active 2, rounds 2). Fallback sessions 4.
- **Proved:**
  - CLM-0350/0357: multiplicity caps (conditional).
  - CLM-0359: any counterexample has at least 5 distinct values (unconditional).
  - CLM-0361..0364: support-5 reductions.
- **Computed:** CLM-0365, the settled pre-flight. The maximum support-≤5 length is 3n−3 for n ∈ {2..7, 10, 12}.

## 1. Activate CAM-0006 and CAM-0007 exactly as pre-registered

1. **Re-verify before activation.**
   - Recompute the LF-normalised SHA-256 of both tools from the committed main checkout, and compare against `code_sha256` in both pre-registrations.
   - Rerun one settled pre-flight point per algorithm (`--n 6 --report-keys-at 0`) and require the S109 values (max 15; orbit-set hash beginning `adacfc5720cb`, equal for A and B).
   - Record the Python/numpy versions; any deviation from 3.12.10 / 1.26.4 must be recorded.
   - If anything fails, do NOT activate. Record the blocker, fix it in a gated way and re-preregister.
2. **Run, using the pre-registered command for each shard k = 0..13 and each algorithm:**

   `timeout 43200 python -I tools/zsf/support5_<a|b>.py --n <15|20> --threshold <43|58> --report-keys-at <43|58> --shard k --nshards 14 --checkpoint campaigns/CAM-000x/checkpoints/<a|b>-s<k>.jsonl --out campaigns/CAM-000x/checkpoints/<a|b>-s<k>.json`

   - **Order:** CAM-0006 A and B, then CAM-0007 B, then CAM-0007 A.
   - **Concurrency:** at most 14 concurrent processes.
   - Run as background processes, and do not change parameters mid-run.
   - Record crashes and re-runs from the same shard. A shard killed by `timeout` is WALLTIME_CAP_TRUNCATED.
3. **Report only actual results.** For each campaign and algorithm:
   - shards completed or truncated;
   - total pairs evaluated versus expected: n15 A 791,934, B 349,690; n20 A 4,162,730, B 2,866,880;
   - max optimum, the merged histogram, AT_OR_ABOVE records, wall and CPU time, and the SHA-256 of every shard log.

   Write `campaigns/CAM-000{6,7}/RESULT.json` and commit the logs, or their summaries plus hashes if they are large.
4. **Interpretation.**
   - **Both algorithms complete with full coverage and max ≤ L−1.** Record a COMPUTED_EXACT claim: "no zero-sumfree sequence over C_n³ with at most five distinct values has length 3n−2". Its scope is the support-≤5 family only, NOT SAT20/SAT15 and not a D value. The certificate is the two-algorithm agreement plus the committed logs; there is no Lean/DRAT certificate.
   - **Partial or truncated runs:** report them as PARTIAL, with no claim.
   - **Any AT_OR_ABOVE record:** recover α and the values, write `candidates/<id>/sequence.json` (canonical sorted triples + SHA-256), and run checkers A/B standalone. The status is CANDIDATE only. Plan the Lean 4 proof and a cold re-check in a later session. No external disclosure without owner authorisation.
   - **Disagreement between A and B:** BLOCKER. Investigate it and make no claim.
5. If time remains after the runs, continue the by-hand support-5 analysis or the other fallback work, scaled down.

## 2. Deliverables and close

- Create S110 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (`validation/validate_s110.py`, which checks coverage sums, the hashes of committed logs, and A/B agreement), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Update: the registry (CAM-0006/0007 status), claims, phase/session/failure/decision ledgers, STATE (`counterexample_hunt_strategy`), README/START_HERE.
- The frontier is unchanged; a support-≤5 exclusion is not a frontier change.
- Install a FULL S111 prompt. It continues SATURATION_FALLBACK. For example, extend the exhaustive approach to 6 values only with a new owner decision, or attack support ≥ 6 by hand.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, a single solver as a certification, or a family-restricted exclusion as SAT20/SAT15.
