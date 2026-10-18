# S111 — SATURATION FALLBACK SESSION 6: SUPPORT ≥ 6 (FUTURE / NOT EXECUTED)

**Active priority: SATURATION_FALLBACK** (since S105). The owner-authorised support-5 exhaustive track (PR #114) is COMPLETE (S110). The authorisation covered the support-≤5 family only. General search stays closed, and any exhaustive work on six or more values needs a NEW owner decision.
- Run S111 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters and the search-reopen condition into every future prompt.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S110 merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s110_result`), `research/S110_SUPPORT5_EXHAUSTIVE_RESULTS.md`, `research/S109_SUPPORT5_EXHAUSTIVE_TOOLING.md`, `research/S108_SATURATION_FALLBACK_SMALL_SUPPORT.md`, `catalogue/CLAIMS.md` (CLM-0350..0367), `docs/FAILURE_AND_LESSON_LEDGER.md` (S106–S110), and `sessions/S110/*`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S111/INPUT.md` and `INPUT_MANIFEST.json`. Paraphrase product or model names in owner text (AGENTS rule 10), and grep the staged diff for them before committing.
- **Git credentials:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential for that command only. Do not change the stored configuration.
- **Before committing,** verify that every intended file change is on disk: read files before rewriting them, and check that write tools succeeded. Never kill processes by image name.

**State at S110 close:**
- Claims 367. Sources 34 (original 29 untouched). Frontier 30 rows untouched.
- Phase 2 SCOPED PASS: checkers A/B, R1/R2, and the support-5 exhaustive tools.
- No campaign is active or pre-registered. CAM-0006/0007 are COMPLETED, EXHAUSTIVE, with no hit.
- Search counters frozen (setup 1, active 2, rounds 2). Fallback sessions 5.
- **Targets (OPEN):** SAT20, i.e. D(C20³) = 58, and SAT15, i.e. D(C15³) = 43.
- **Established** (INTERNAL, same executor; for S a hypothetical zero-sumfree (3n−2)-term sequence over C_n³):
  - CLM-0350/0357: order-n multiplicities ≤ n−2. At n=20, order-20 multiplicities ≤ 17 and order-10 multiplicities ≤ 8. Conditional on SOURCE_STATED rank-two D and D(C2⊕C20⊕C20).
  - CLM-0355: transfer of multiplicity defects to C_{nd/m} ⊕ C_n ⊕ C_n.
  - CLM-0358/0360: box/kernel criterion and relation bound.
  - **CLM-0359 + CLM-0366/0367: S has at least 6 distinct values at n = 15, 20.** CLM-0366/0367 are COMPUTED_EXACT: two independent exhaustive algorithms, conditional on the hand proofs CLM-0358/0361..0364, not formally certified.

## 1. S111 work (bounded; choose and finish a coherent subset)

1. **Support 6 by hand.**
   - Six distinct values that generate C_n³ give a relation module K of rank 3 (|K| = n³). The counting bound gives only |S| ≤ 5n−6 + 1/n².
   - Try planar or volume refinements: count escapes over 2- and 3-dimensional sub-lattices of K. Use CLM-0360 for every order-n ρ with small support, together with the multiplicity caps and the fact that every 5-value sub-configuration has length ≤ 3n−3 (CLM-0366/0367 apply to subsequences).
   - In particular, removing all copies of any one value leaves a sequence with at most 5 values, of length ≤ 3n−3. So every value of S has multiplicity ≥ |S| − (3n−3) = 1, and the sum over any 5 values is ≤ 3n−3. Combine such inequalities over all 6 deletions.
   - Record exactly what survives. Tabulate numbers mechanically.
2. **Feasibility study only, with nothing run on n15/n20.** Estimate the size of a support-6 exhaustive enumeration: rank-3 free summands of (Z/n)^6 up to S₆, per prime-power component, via the Gaussian binomial [6 choose 3]_p and the S109 timing models. Report whether it is feasible, and with what proved reductions (for example the multiplicity caps, or the subsequence bound from item 1). Any campaign needs a new owner decision, Phase-2 tooling extensions with two independent algorithms, a settled-group pre-flight, and a pre-registration in a later session.
3. **Certification option (report only).** Assess what a Lean 4 kernel check of CLM-0366/0367 would require: formalising CLM-0358/0361..0364 plus a verified enumeration. Do not start it without owner direction.

**Honesty rules.**
- Failed attempts go in the failure ledger with their exact obstruction.
- Do not upgrade inherited or source claims.
- Never state SAT20/SAT15 or a D value.
- Exact tests run only on small or settled groups.

## 2. Deliverables and close

- Create S111 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (`validation/validate_s111.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note `research/S111_SATURATION_FALLBACK_<topic>.md`, with independent exact tests on small groups for any new lemma.
- Update: claims, ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 6), README/START_HERE.
- Leave the frontier unchanged.
- Install a FULL S112 prompt. If a support-6 exhaustive campaign is feasible and justified, end with a precise owner question; do not pre-register without owner authorisation.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, a single solver as a certification, or a family-restricted exclusion as SAT20/SAT15.
