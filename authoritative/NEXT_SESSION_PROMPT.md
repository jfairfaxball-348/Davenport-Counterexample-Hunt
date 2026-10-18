# S111 — CONSOLIDATION AND GENERALISATION REVIEW (FUTURE / NOT EXECUTED)

**Owner steering (18 October 2026, after S110; installed by a non-session governance commit):** review what has been done and generalise it to all n, or to families of n, rather than pursuing more n15/n20-specific work. The owner's reply "yes" approved this outline:
- (a) a single review document classifying every result;
- (b) the even-n multiplicity caps;
- (c) a serious attempt at the "r+2 values" theorem, guided by the computed data;
- (d) the Lean-certificate assessment dropped for now.

**Active priority: SATURATION_FALLBACK** (since S105). The support-5 exhaustive track is COMPLETE (S110). General search stays closed, and any new exhaustive campaign needs a new owner decision.
- Run S111 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters, the search-reopen condition and this steering into future prompts.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the governance merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy` including `owner_steering`, `s110_result`), the research notes S103–S110, `catalogue/CLAIMS.md` (CLM-0345..0367), `docs/FAILURE_AND_LESSON_LEDGER.md` (S103–S110), and `campaigns/CAM-0006/RESULT.json`, `campaigns/CAM-0007/RESULT.json`, `sessions/S109/PREFLIGHT_SUMMARY.json`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S111/INPUT.md` and `INPUT_MANIFEST.json`. Paraphrase product or model names in owner text (AGENTS rule 10), and grep the staged diff for them before committing.
- **Git credentials:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential for that command only. Do not change the stored configuration.
- **Before committing,** verify that every intended file change is on disk: read files before rewriting them, and check that write tools succeeded. Never kill processes by image name.

**State at entry:**
- Claims 367. Sources 34 (original 29 untouched). Frontier 30 rows untouched.
- No campaign is active or pre-registered.
- Search counters frozen (setup 1, active 2, rounds 2). Fallback sessions 5.
- **Targets (OPEN):** SAT20, i.e. D(C20³) = 58, and SAT15, i.e. D(C15³) = 43.

## 1. S111 work

**(a) Consolidation review.** Write `research/S111_CONSOLIDATION_REVIEW.md`, classifying every result from S103–S110 (CLM-0345..0367), plus any earlier result worth carrying forward, into three groups:
- **ALL-n:** any n, and where applicable any rank r or any finite abelian group. Examples: CLM-0349/0353, CLM-0358, CLM-0359 (at most r+1 values over C_n^r gives length ≤ r(n−1)), CLM-0361..0364.
- **CONDITIONAL-on-family:** holds for all n for which some smaller group is understood. Examples: CLM-0350, which needs only the classical rank-two value; CLM-0355, the transfer to C_e⊕C_n⊕C_n.
- **n-SPECIFIC:** for example CLM-0357, CLM-0366/0367, the S104/S105 heuristic rounds, and the S060–S102 axial programme.

For each result, state exactly what it depends on (proof, source, computation) and its scope. Keep it concise. It must be readable as the single entry point to "what we know".

**(b) Even-n multiplicity caps (all even n).**
- Generalise CLM-0357 using SRC-0005 Theorem 2.7, D(C2⊕C2m⊕C2mn) = 2m+2mn, already SOURCE_STATED as CLM-0356, applied to C2⊕C_n⊕C_n for every even n.
- **Expected statement:** for every even n ≥ 4, a zero-sumfree (3n−2)-term sequence over C_n³ has order-n multiplicities ≤ n−3, and order-(n/2) multiplicities ≤ n/2 − 2. Re-derive the exact caps from the CLM-0355 inequality *mechanically*, for all relevant (m, d) with nd/m = 2, and prove them for general even n.
- Test against the settled even n (4, 6, 8, 10, 12, 14) in small exact computations only.

**(c) The "r+2 values" theorem.**
- **Conjecture:** every zero-sumfree sequence over C_n^r with at most r+2 distinct values has length ≤ r(n−1).
- **Known or evident cases:** r = 1 (D(C_n) = n) and r = 2 (rank-two D).
- **Evidence for r = 3:** CLM-0365/0366/0367 (maximum 3n−3 for n ∈ {2..7, 10, 12, 15, 20}).
- **Goal:** prove it for r = 3 and all n, or for a large family of n, or isolate exactly where a proof fails.
- **Tools:** CLM-0358 (box/kernel criterion with a rank-2 relation module K when the values generate), CLM-0359/0360, the multiplicity caps, and planar counting over K.
- **Use the computed data as a guide.**
  - The attained optimum values have visible structure: {26, 34, 42} at n=15, {33, 36, 39, 45, 48, 57} at n=20, and the S109 settled histograms.
  - Inspect which relation modules attain 3n−3 and the next values, using the existing tools in settled or small groups only, or the committed n15/n20 logs.
  - Formulate lemmas from what you observe.
- Any new lemma needs a hand proof plus independent exact tests on small groups.
- If a full proof succeeds for r = 3, it would make CLM-0366/0367 consequences of a theorem. State the implication carefully, and do not retroactively relabel the computations.

**(d) Lean certification:** deferred by owner steering; do not start it.

**Honesty rules.**
- Failed attempts go in the failure ledger with their exact obstruction.
- Do not upgrade inherited or source claims.
- Never state SAT20/SAT15 or a D value.
- No new target-group computation without a new owner decision.

## 2. Deliverables and close

- Create S111 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (`validation/validate_s111.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write the consolidation review and a research note for (b) and (c), with exact tests on small groups.
- Update: claims, ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 6), README/START_HERE (pointing to the consolidation review as the entry point).
- Leave the frontier unchanged.
- Install a FULL S112 prompt that continues the generalisation line, informed by what S111 achieves.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, a single solver as a certification, or a family-restricted exclusion as SAT20/SAT15.
