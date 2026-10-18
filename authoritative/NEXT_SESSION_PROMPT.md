# S112 — GENERALISATION CONTINUED: EVEN-n PARITY RESIDUE AND ODD-n BLOCK-SUM VALUES (FUTURE / NOT EXECUTED)

**Owner steering (18 October 2026, still in force):** review what has been done and generalise it to all n, or to families of n, rather than pursuing more n15/n20-specific work. S111 executed the approved outline:
- (a) the consolidation review;
- (b) even-n caps;
- (c) the r+2 attempt;
- (d) Lean deferred.

S112 continues the same line, informed by S111's results.

**Active priority: SATURATION_FALLBACK** (since S105). The support-5 exhaustive track is complete (S110). General search stays closed, and any new exhaustive campaign needs a new owner decision.
- Run S112 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters, the search-reopen condition and the owner steering into future prompts.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree.
- Read:
  - `AGENTS.md`;
  - `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s111_result`);
  - **`research/S111_CONSOLIDATION_REVIEW.md` (the entry point)** and `research/S111_R_PLUS_TWO_AND_EVEN_CAPS.md`;
  - `catalogue/CLAIMS.md` (CLM-0345..0373);
  - `docs/FAILURE_AND_LESSON_LEDGER.md` (S106–S111);
  - `sessions/S111/S111_TESTS.json` and `sessions/S111/two_a*_{A,B}.json`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S112/INPUT.md` and `INPUT_MANIFEST.json`. Paraphrase product or model names in owner text (AGENTS rule 10), and grep the staged diff for them before committing.
- **Git credentials:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential for that command only. Do not change the stored configuration.
- **Before committing,** verify that every intended file change is on disk: read files before rewriting them, and check that write tools succeeded. Re-run any computation whose code changed after the run, so that recorded outputs come from the committed code. Never kill processes by image name.

**State at entry:**
- Claims 373. Sources 34 (original 29 untouched). Frontier 30 rows untouched.
- No campaign is active or pre-registered.
- Search counters frozen (setup 1, active 2, rounds 2). Fallback sessions 6.
- **Targets (OPEN):** SAT20, i.e. D(C20³) = 58, and SAT15, i.e. D(C15³) = 43.

**Key S111 facts:**
- CLM-0370/0371: the 5-value bound holds at every n = 2b with D(C_b³) known, including n = 20 and 28.
- CLM-0372: at such n, a counterexample has ≥ 6 values of odd multiplicity outside 2G. With exactly six, their mod-2 images are F₂³∖{0,P}, and seven is impossible.
- CLM-0373: the counting block method cannot reach odd n. TWO(a) is false for a = 3, 4, 5, and packing falls short at n = 15.

## 1. S112 work

**(a) The even-n parity residue (all n = 2b with D(C_b³) known).**
- **Goal:** prove that the residual configuration of CLM-0372 cannot occur, at least for **6-valued** sequences, and if possible for 7-valued ones too. A 6-valued residual sequence has all multiplicities odd, all values outside 2G, and mod-2 images F₂³∖{0,P}.
- **Tools to combine:**
  - the a = 2 blocks, but with the *values* of their sums in 2G ≅ C_b³ rather than their number;
  - the even-n caps (CLM-0368);
  - the relation module and box criterion (CLM-0358/0360) restricted to the residual pattern;
  - a second block level (a = 4 where 4 | n: n = 20 = 4·5 with D(C5³) known by CLM-0142, and n = 28 = 4·7);
  - the transfer CLM-0355.
- **Expected deliverable:** either a proof that 6-valued counterexamples are impossible at every such n, which would make support ≥ 7 necessary at n = 20 by proof, or a precise statement of the minimal sub-case that resists, with its exact obstruction.
- Exact tests only on settled small even n (n ≤ 14).

**(b) Odd n: use the block-sum values.**
- At n = ab with a ∈ {3, 5}, the block sums o_i·g_i plus ≤ 2 extras form a ≤ 7-valued sequence in C_b³. Its relation module is tied to that of S.
- Formulate and attempt a lemma combining the mod-a packing deficit (≤ 2) with this relation structure. Example target: when the deficit is 2, the block-sum sequence of length 3b−4 together with the leftover always has a zero-sum.
- Test any lemma exactly on small odd composite settled cases only. n = 9 is a prime power (control); n = 15 is a target and must **not** be computed without an owner decision. Use C_a³ and C_b³ components separately where possible.
- Failures go in the failure ledger with the exact obstruction.

**(c) Rank generalisation (optional, if time).** State and prove the general-r version of CLM-0372: the a = 2 parity structure for sequences over C_{2b}^r.

**(d) Lean certification:** deferred by owner steering; do not start it.

**Honesty rules.**
- Do not upgrade inherited or source claims, and do not relabel CLM-0366/0367.
- Never state SAT20/SAT15 or a D value.
- No new target-group computation without a new owner decision.
- If (a) yields a finite residual family at n = 20 suitable for exhaustive computation, describe it and ask the owner. Do not pre-register or run it in S112.

## 2. Deliverables and close

- Create S112 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (`validation/validate_s112.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note with exact small-group tests.
- Update: claims, ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 7), the consolidation review (add the new results in place, keeping it the single entry point), README and START_HERE.
- Leave the frontier unchanged.
- Install a FULL S113 prompt.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, a single solver as a certification, or a family-restricted exclusion as SAT20/SAT15.
