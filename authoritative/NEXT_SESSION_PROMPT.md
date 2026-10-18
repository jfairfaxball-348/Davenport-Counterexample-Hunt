# S113 — CLOSING THE ROUTE-SIEVE RESIDUE (FUTURE / NOT EXECUTED)

**Owner steering (18 October 2026, still in force):** generalise to all n or to families of n rather than pursuing n15/n20-specific search.
- S111 built the consolidation review, the even-n caps and the r+2 bound at even n.
- S112 combined several block routes (CLM-0374). That proved the support-≤5 bound at n = 15 by hand (CLM-0376), and showed that n = 20 counterexamples need ≥ 7 distinct values (CLM-0377).

S113 sharpens the sieve and attacks its explicit residue (CLM-0378).

**Active priority: SATURATION_FALLBACK** (since S105). General search stays closed, and any new exhaustive campaign on target groups needs a new owner decision.
- Run S113 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters, the search-reopen condition and the owner steering into future prompts.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree.
- Read:
  - `AGENTS.md`;
  - `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s111_result`, `s112_result`);
  - **`research/S111_CONSOLIDATION_REVIEW.md` (the entry point)**, `research/S112_MULTI_ROUTE_SIEVE.md` and `research/S111_R_PLUS_TWO_AND_EVEN_CAPS.md`;
  - `catalogue/CLAIMS.md` (CLM-0345..0378);
  - `docs/FAILURE_AND_LESSON_LEDGER.md` (S106–S112);
  - `sessions/S112/ROUTE_SIEVE.json` and `sessions/S112/S112_TESTS.json`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S113/INPUT.md` and `INPUT_MANIFEST.json`. Paraphrase product or model names in owner text (AGENTS rule 10), and grep the staged diff for them before committing. The commit message must carry no model names or attribution trailers naming a model.
- **Git credentials:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential for that command only. Do not change the stored configuration.
- **Before committing,** verify that every intended file change is on disk. Re-run any computation whose code changed after the run. Never kill processes by image name, and resolve the PID column explicitly before any kill.

**State at entry:**
- Claims 378. Sources 34 (original 29 untouched). Frontier 30 rows untouched.
- No campaign is active or pre-registered.
- Search counters frozen (setup 1, active 2, rounds 2). Fallback sessions 7.
- **Targets (OPEN):** SAT20, i.e. D(C20³) = 58, and SAT15, i.e. D(C15³) = 43.

## 1. S113 work

**(a) Sharper small-group constants (all-n benefit).**
- Determine exactly, on small groups only, the constants the sieve uses as ν_lb: D₂(C₃³), D₃(C₂³), D₂(C₄³), and if feasible D₂(C₅³). Use two independent algorithms, or a hand proof plus one algorithm.
- Re-run the route sieve (`tools/zsf/route_sieve.py`, extended, with both algorithms) for n ∈ {15, 20, 21, 28, 30, 33, 35} and record any change in the excluded support.
- This is arithmetic only. Record honestly if nothing changes.

**(b) Parity at even n inside the sieve.**
- Add the CLM-0372 constraint at even n: the values outside 2G with odd multiplicity number ≥ 6, never 7, and with exactly 6 their mod-2 images are F₂³∖{0,P}.
- Add an exact route-2 leftover analysis over F₂³ (ν of the actual image multiset rather than the D_j bound).
- Re-sieve n = 20, k = 7 (139 patterns) and n = 28, k = 6.

**(c) Route-wise image analysis of the residue.**
- For each surviving pattern, decide **route by route, in the small quotient groups only**, whether every image configuration closes that route. Use exact maximum packing of the leftover, with borrowing of full blocks. The routes are C₃³ and C₅³ for n = 15, and C₂³, C₄³ and C₅³ for n = 20.
- If a single route closes every configuration of a pattern, the pattern is excluded by proof plus a small-group computation.
- **Do not** combine the images of different routes. A joint analysis is equivalent, via the CRT, to enumerating value sets of the target group, and needs an owner decision.
- If the residue survives route-wise analysis, describe the exact joint family that remains and ask the owner whether a pre-registered campaign on it should be considered. Do not pre-register or run it in S113.

**(d) Lean certification:** deferred by owner steering; do not start it.

**Honesty rules.**
- Do not upgrade inherited or source claims, and do not relabel CLM-0366/0367.
- Never state SAT20/SAT15 or a D value.
- No new target-group computation without a new owner decision.

## 2. Deliverables and close

- Create S113 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (`validation/validate_s113.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note with exact small-group tests.
- Update: claims, ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 8), the consolidation review (in place, remaining the single entry point), README and START_HERE.
- Leave the frontier unchanged.
- Install a FULL S114 prompt, or an owner-decision blocker description if the next step needs one.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, a single solver as a certification, or a family-restricted exclusion as SAT20/SAT15.
