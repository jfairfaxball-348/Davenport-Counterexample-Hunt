# S106 — SATURATION FALLBACK SESSION 1 (FUTURE / NOT EXECUTED)

**Active priority: SATURATION_FALLBACK.** It was switched in S105 by the owner directive's two-round trigger (directive of 16 October 2026).
- SEARCH_FIRST ran two complete, materially different HEURISTIC rounds: CAM-0002/0003 (R1, S104) and CAM-0004/0005 (R2, S105). Both reached only 3n−3 (42 at n15, 57 at n20). There was no hit and no candidate, and this is NOT a negative result.
- Run S106 only on a separate later owner "Run next session", and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters and the search-reopen condition into every future prompt until evidence or the owner changes them.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S105 merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s105_result`), `research/S105_SEARCH_FIRST_EXPERIMENTAL_CLOSEOUT.md`, `research/S104_ROUND1_RESULTS_AND_ROUND2_PREREGISTRATION.md`, `research/S103_SEARCH_TOOLING_AND_PREREGISTRATION.md` (CLM-0345), `catalogue/CLAIMS.md` (CLM-0038, CLM-0049, CLM-0051, CLM-0345..0347, and the S060/S102 axial claims CLM-0221/0222/0344), `docs/PHASE_GATE_LEDGER.md`, `campaigns/REGISTRY.md`, and `sessions/S105/*`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S106/INPUT.md` and `INPUT_MANIFEST.json`.
- **Git credential note:** the gh CLI keyring account (`jball348-svg`) has no write access. S104 and S105 pushed through Git Credential Manager as `jfairfaxball-348`, with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). They opened and merged the PR with `GH_TOKEN` taken from that credential for that command only. Do not change the stored git or gh configuration.

**State at S105 close:**
- Phase 1 has a SCOPED PASS (search targets n15/n20); the general frontier map is still IN_PROGRESS.
- Phase 2 has a SCOPED PASS covering exact checkers A/B and the heuristic engines R1/R2 only. There is no exhaustive, SAT/DRAT/LRAT or Lean tooling.
- Phase 3: rounds 1 and 2 are COMPLETED, and the search is closed. No campaign is active or pre-registered. CAM-0001 is still BLOCKED.
- Final search counters: setup sessions 1, active search sessions 2, completed materially distinct rounds 2.
- Fallback sessions completed: 0.
- Claims total 347, sources total 32 (the original 29 untouched), and the 30 frontier rows are untouched.

**Search-reopen condition:** an explicit owner directive, or a substantive structural reason recorded as a claim (for example a proved reduction of the 58-term question to a small structured family amenable to exhaustive or SAT treatment), followed by a full pre-registration and gate. A parameter change of R1/R2 does not qualify.

## 1. Fallback targets (both OPEN)

- **SAT20:** every zero-sumfree 57-term indexed sequence S in C20³ has Σ(S) = G, with Σ including the empty sum. By CLM-0345(c), SAT20 is equivalent to there being no zero-sumfree 58-term sequence, and with CLM-0038 to D(C20³) = 58.
- **SAT15:** the same with 42 terms in C15³, equivalent to D(C15³) = 43.

Record SAT20 and SAT15 as stable claim IDs with an honest status if they are not already recorded. They are OPEN conjectures; never mark them PROGRAMME_PROVED without a complete proof.

## 2. S106 work (bounded; choose and finish a coherent subset)

1. **Source frontier for subset-sum growth.**
   - Identify the precise published tools on the growth and structure of Σ(S):
     - Kneser's addition theorem and its subset-sum generalisations, such as the DeVos–Goddyn–Mohar generalisation of Kneser to subset sums of sequences;
     - Olson-type lower bounds on |Σ(S)| for zero-sumfree S;
     - inverse results on long zero-sumfree sequences and on D(C_n³) for composite n, for example structure of maximal-length zero-sumfree sequences in rank 2, which is known, and how it is used for rank 3.
   - Give each new source a stable SRC-#### with its true access level: METADATA_ONLY unless the statement or proof was actually inspected.
   - Record direct links only, with no PDF copies.
   - Never cite from memory as SOURCE_STATED.
2. **Programme lemmas (aim for at least one nontrivial PROGRAMME_PROVED claim).** Candidate directions, with hand proofs written in full in a research note:
   - **(a) Prefix growth with stabilisers.** For zero-sumfree S = g_1..g_L, prove a Kneser-type lower bound on |Σ_k| − |Σ_{k−1}| in terms of the stabiliser H_k = Stab(Σ_k) and the order of g_k mod H_{k−1}. The elementary fact that g_k + Σ_{k−1} ⊄ Σ_{k−1} gives strict growth; strengthen it. Then derive what a 57-term zero-sumfree S with Σ(S) ≠ G must look like: the possible stabiliser chains, and the number of terms that can lie in a proper subgroup coset structure.
   - **(b) Projection/lifting.** Use C20³ → C4³ and C20³ → C5³, which are settled p-group quotients with D = 3n−2. Bound the number of terms that can avoid producing zero-sum subsequences in the quotients, and analyse the carries. Compare with CLM-0049 (upper bound 59 via historical D(C10³) = 28) and determine exactly what a 58-term zero-sumfree sequence would have to satisfy in each projection.
   - **(c) Extremal structure.** Decide whether every zero-sumfree 57-term S with Σ(S) ≠ G must admit the S060/S102 axial reductions (CLM-0221/0222/0344). If it does, record the exact implication. If not, record the obstruction.
   - **(d) Heuristic leads (descriptive only).** The S104/S105 best sequences, including 3n−3 sequences with small support such as multiplicities 13, 13, 3, … at n15, may be inspected as examples. They are not evidence of SAT20.
3. **Optional exact calibration (pre-register only; do not run in S106).** If useful, pre-register an EXHAUSTIVE calibration in a SETTLED group, for example structure of all zero-sumfree (3n−3)-term sequences in C4³ up to GL₃ symmetry. This first requires a Phase-2 gate extension for symmetry-reduced exhaustive tooling, with a proved reduction. No run on n15/n20.

**Honesty rules.**
- A failed attempt is recorded as a failure with its precise obstruction (failure ledger), not as progress.
- Do not upgrade inherited or source claims to PROGRAMME_PROVED.
- Do not claim SAT20/SAT15 or any D value.

## 3. Deliverables and close

- Create S106 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (a `validation/validate_s106.py` in the style of `validate_s105.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note `research/S106_SATURATION_FALLBACK_<topic>.md`.
- Update: claims/sources (JSON and Markdown), phase/session/failure/decision ledgers, STATE (`counterexample_hunt_strategy`: priority SATURATION_FALLBACK, fallback sessions completed 1, decisive evidence, any new reopen reason), README/START_HERE.
- Leave the frontier unchanged unless there is an independently checked improvement. Keep the original 29 sources and 30 frontier rows intact.
- Install a FULL S107 prompt continuing SATURATION_FALLBACK. If S106 proves a structural reduction that genuinely meets the search-reopen condition, the S107 prompt may instead propose a gated, pre-registered exact campaign. It must state why the condition is met, and never activate the campaign in the same session as the pre-registration.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, or a single solver or script as a certification.
