# S109 — SATURATION FALLBACK SESSION 4 (FUTURE / NOT EXECUTED)

**Active priority: SATURATION_FALLBACK.** It was switched in S105 by the owner directive's two-round trigger (directive of 16 October 2026).
- The SEARCH_FIRST rounds (S104 R1, S105 R2) reached only 3n−3 and are closed. That is not a negative result.
- Run S109 only on a separate later owner instruction to run the next session (the support-5 authorisation is not itself a run instruction), and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters and the search-reopen condition into every future prompt until evidence or the owner changes them.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S108 merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s108_result`), `research/S108_SATURATION_FALLBACK_SMALL_SUPPORT.md`, `research/S107_SATURATION_FALLBACK_MULTIPLICITY_DEFECT_TRANSFER.md`, `research/S106_SATURATION_FALLBACK_MULTIPLICITY_QUOTIENT.md`, `catalogue/CLAIMS.md` (CLM-0153, CLM-0345..0360), `docs/FAILURE_AND_LESSON_LEDGER.md` (S106–S108 entries), `docs/PHASE_GATE_LEDGER.md`, and `sessions/S108/*`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S109/INPUT.md` and `INPUT_MANIFEST.json`.
- **Git credential note:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential (`git credential-manager get` with username `jfairfaxball-348`) for that command only. Do not change the stored git or gh configuration.
- **File-name rule:** archived owner text must not contain product or model names (AGENTS rule 10); paraphrase them in INPUT files. Before committing, grep the staged diff case-insensitively for the assistant product name, its vendor name and its model-family names.

**State at S108 close:**
- Phase 1 has a SCOPED PASS (search targets); the general frontier map is still IN_PROGRESS.
- Phase 2 has a SCOPED PASS covering checkers A/B and the R1/R2 heuristic engines. There is no exhaustive, SAT or Lean tooling.
- Phase 3: search CLOSED; no campaign is active or pre-registered.
- Search counters (frozen): setup 1, active search sessions 2, completed rounds 2. Fallback sessions completed: 3 (S106–S108).
- Claims total 360, sources total 34 (the original 29 untouched), and the 30 frontier rows are untouched.

**Fallback targets (OPEN):**
- **SAT20:** D(C20³) = 58.
- **SAT15:** D(C15³) = 43.

**Proved so far (INTERNAL, elementary, no novelty claimed; S = a hypothetical zero-sumfree (3n−2)-term sequence over C_n³):**
- **CLM-0350:** order-n multiplicities ≤ n−2. Conditional on SOURCE_STATED rank-two D (CLM-0352).
- **CLM-0355 / CLM-0357:** the multiplicity-defect transfer to C_{nd/m} ⊕ C_n ⊕ C_n. At n=20, order-20 multiplicities ≤ 17 and order-10 multiplicities ≤ 8, conditional on CLM-0352 and CLM-0356 (D(C2⊕C20⊕C20) = 40).
- **CLM-0358:** box/kernel criterion. With distinct values a_1..a_k, multiplicities α_i ≤ n−1, and relation module K = {ρ ∈ (Z/n)^k : Σρ_i a_i = 0}, S is zero-sumfree iff every nonzero ρ ∈ K has some ⟨ρ_i⟩ > α_i.
- **CLM-0359 (unconditional):** |S| ≤ k(n−1) − n + n/|K|. Hence **S has at least 5 distinct values.**
- **CLM-0360:** for every ρ ∈ K of order n, Σ_{ρ_i≠0}(n−1−α_i) ≥ n−1.
- **Lever groups:** no exact D was found in the literature for C_e⊕C_n⊕C_n (e > 2) at n = 15, 20, so the S107 conditional caps stay conditional.

**Search-reopen condition (general):** an explicit owner directive, or a substantive structural reason recorded as a claim (for example a proved reduction to a small structured family amenable to exhaustive or SAT treatment), followed by a full pre-registration and gate. A parameter change of R1/R2 does not qualify.

**OWNER AUTHORISATION (2026-10-17, after S108, installed by a non-session governance commit):** the owner answered "Yes allow it" to whether a later session may build gated tooling and pre-register an EXHAUSTIVE support-5 campaign at n=15/20.
- **Scope:** exhaustive classification of zero-sumfree (3n−2)-term sequences over C_n³ with exactly 5 distinct values, for n = 15 and n = 20.
- **Order of work:**
  1. Tooling and Phase-2 gate.
  2. Pre-registration (CAM-0006 n15, CAM-0007 n20).
  3. Activation, only in a LATER session than the pre-registration.
- **Not covered:** this does NOT reopen general search, heuristic campaigns or other families. The priority stays SATURATION_FALLBACK.
- **Recorded in:** `authoritative/STATE.json` → `counterexample_hunt_strategy.owner_authorisations`.

## 1. S109 work (bounded; choose and finish a coherent subset)

1. **Support 5 by hand.**
   - **Setting:** S has five distinct values. Assume they generate C_n³, so K ≅ (Z/n)² is a rank-2 free summand of (Z/n)^5. The case where they generate a proper subgroup has larger K; handle it separately.
   - **Goal:** prove |S| ≤ 3n−3 or isolate precisely what survives. The S108 single-coordinate counting gives only 4n−5.
   - **Ideas:**
     - (i) *Planar counting:* choose two order-n generators ρ, τ of K and count escapes on the grid {sρ + tτ}, tracking for each coordinate i the line structure of the escape set {(s,t) : ⟨sρ_i + tτ_i⟩ > α_i}.
     - (ii) *Coordinate-free kernel vectors:* for each pair i < j there is ρ ∈ K of order n with ρ_i = ρ_j = 0, or a large subgroup with that property. Apply CLM-0360 to it. Combine the ten pair-inequalities with Σα = 3n−2 and the multiplicity caps.
     - (iii) Combine with CLM-0350/0357 (multiplicity caps) and CLM-0153.
   - Record exactly which (K, α) configurations survive any argument. Tabulate numerical consequences mechanically, not by hand (S107 lesson).
2. **Generalisation:** state the best general bound for k = r+2 distinct values over C_n^r that the planar argument yields, and test it on small groups.
3. **Support-5 EXHAUSTIVE track (owner-authorised; build, gate and pre-register, but DO NOT RUN in S109).**
   - **(a) Proved reductions first.** Write hand proofs (as claims) of every symmetry and reduction the enumeration uses, and state its completeness class precisely. Examples:
     - S is determined by its five values and multiplicities.
     - Zero-sumfreeness depends only on the relation module K ⊂ (Z/n)^5 and α (CLM-0358).
     - Invariance under coordinate permutation, under scaling a coordinate's value by a unit (with how this acts on K), and under GL₃(Z/n).
     - Reduction to K that are relation modules of 5 distinct values: K is a rank-2 free summand when the values generate C_n³; handle proper-subgroup supports separately.
     - Optimal α for a given K is a max-weight "escape cover" problem.
     - Any further pruning, such as the multiplicity caps CLM-0350/0357 and the relation bound CLM-0360, used only where it is proved for the target n.
   - **(b) Two independent exhaustive algorithms.** Implement two algorithmically distinct ones (AGENTS rule 6). Example: (A) enumerate canonical rank-2 summands K and solve the α-optimisation exactly; (B) enumerate canonical 5-value supports in C_n³ up to GL₃ and decide zero-sumfreeness via checkers on maximal multiplicity vectors. They must agree on every settled-group instance.
   - **(c) Pre-flight on settled groups only.** Use n ≤ 8 (or other n with known D(C_n³) = 3n−2: p-groups by SOURCE_STATED Olson, primes by CLM-0142). There the maximum support-5 length must be ≤ 3n−3, and both algorithms must agree. Record version, parameters, run time, the orbit count and its scaling. Measure and extrapolate the n=15/20 cost from settled-group timings and orbit counts only, with no n15/n20 enumeration.
   - **(d) Phase-2 gate extension.** Record it only if (a)–(c) pass.
   - **(e) Pre-register CAM-0006 (n15) and CAM-0007 (n20).** Include the explicit domain, the proved reductions, completeness class EXHAUSTIVE (for the support-5 family only), a bounded budget, a checkpoint format, a stopping rule, code SHA-256s, and an output-certificate plan (per-orbit verdict logs with hashes; two-algorithm agreement). A negative result covers ONLY the support-5 family, and is never SAT20/SAT15. If the honest cost estimate exceeds a reasonable bounded budget, do NOT pre-register; record the obstruction and the cost instead.
   - A hit would be CANDIDATE only (candidates/ quarantine, two checkers, Lean 4 plan, cold re-check). No external disclosure without owner authorisation.
**Honesty rules.**
- Failed attempts go in the failure ledger with their exact obstruction.
- Do not upgrade inherited or source claims.
- Do not claim SAT20/SAT15 or any D value.
- Exact tests run only on small or settled groups.

## 2. Deliverables and close

- Create S109 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (a `validation/validate_s109.py` in the style of `validate_s108.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note `research/S109_SATURATION_FALLBACK_<topic>.md`, with independent exact tests for any new lemma.
- Update: claims/sources (JSON and Markdown; never edit the original 29 source records; log inspections in an `s109_audit` block), phase/session/failure/decision ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 4, fallback_progress, search_reopen_condition_met), README/START_HERE.
- Leave the frontier unchanged unless there is an independently checked improvement.
- If CAM-0006/0007 were pre-registered: create `campaigns/CAM-0006/` and `campaigns/CAM-0007/` PREREGISTRATION.json and update `campaigns/REGISTRY.md`.
- Install a FULL S110 prompt. If S109 pre-registered CAM-0006/0007 and committed the gate, S110 activates them, re-verifying the hashes first. Otherwise S110 continues SATURATION_FALLBACK and the tooling work.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, or a single solver or script as a certification.
