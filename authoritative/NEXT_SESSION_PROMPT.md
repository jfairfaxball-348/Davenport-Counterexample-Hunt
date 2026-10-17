# S107 — SATURATION FALLBACK SESSION 2 (FUTURE / NOT EXECUTED)

**Active priority: SATURATION_FALLBACK.** It was switched in S105 by the owner directive's two-round trigger (directive of 16 October 2026).
- The SEARCH_FIRST rounds (S104 R1, S105 R2) reached only 3n−3 and are closed. That is not a negative result.
- Run S107 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters and the search-reopen condition into every future prompt until evidence or the owner changes them.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S106 merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s106_result`), `research/S106_SATURATION_FALLBACK_MULTIPLICITY_QUOTIENT.md`, `research/S105_SEARCH_FIRST_EXPERIMENTAL_CLOSEOUT.md`, `catalogue/CLAIMS.md` (CLM-0038, CLM-0153, CLM-0345..0352, and the rank-two Property B claims CLM-0092/0093/0110), `catalogue/SOURCES.md` (SRC-0010, SRC-0014, SRC-0025, SRC-0026, SRC-0033, SRC-0034), `docs/FAILURE_AND_LESSON_LEDGER.md` (S106 entry), and `sessions/S106/*`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S107/INPUT.md` and `INPUT_MANIFEST.json`.
- **Git credential note:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential for that command only. Do not change the stored git or gh configuration.

**State at S106 close:**
- Phase 1 has a SCOPED PASS (search targets); the general frontier map is still IN_PROGRESS.
- Phase 2 has a SCOPED PASS covering checkers A/B and the R1/R2 heuristic engines. There is no exhaustive, SAT or Lean tooling.
- Phase 3: rounds 1–2 COMPLETED and search CLOSED; no campaign is active or pre-registered.
- Search counters (frozen): setup 1, active search sessions 2, completed rounds 2. Fallback sessions completed: 1 (S106).
- Claims total 352, sources total 34 (the original 29 untouched), and the 30 frontier rows are untouched.

**Fallback targets (OPEN):**
- **SAT20:** every zero-sumfree 57-term sequence in C20³ has Σ = G, i.e. D(C20³) = 58.
- **SAT15:** the analogue with 42 terms in C15³, i.e. D(C15³) = 43.

Both are instances of CLM-0002.

**S106 results (INTERNAL, elementary, no novelty claimed):**
- CLM-0348: basis completion.
- CLM-0349: g^{m−1}T is zero-sumfree iff the image of T in G/⟨g⟩ is zero-sumfree.
- CLM-0350: conditional on SOURCE_STATED CLM-0352, every zero-sumfree (3n−2)-term sequence over C_n³ has every order-n multiplicity ≤ n−2.
- CLM-0351: g^{m−2}T is zero-sumfree iff every nonempty subsequence of T with sum in ⟨g⟩ sums to exactly g.

**Search-reopen condition:** an explicit owner directive, or a substantive structural reason recorded as a claim (for example a proved reduction to a small structured family amenable to exhaustive or SAT treatment), followed by a full pre-registration and gate. A parameter change of R1/R2 does not qualify.

## 1. S107 work (bounded; choose and finish a coherent subset)

1. **The multiplicity-(n−2) case.**
   - **Setting:** S is a hypothetical zero-sumfree (3n−2)-term sequence over C_n³ with v_g(S) = n−2 for some g of order n. Let T be the 2n remaining terms and π the projection to C_n² (CLM-0348).
   - **Known by CLM-0351:** every zero-sum subsequence of π(T) lifts to G-sum exactly g, and any two of them intersect.
   - **Goal:** exclude the case, or isolate exactly what survives, using the equal-lift condition rather than disjointness counting (see the S106 failure-ledger entry). Ideas:
     - (i) For a minimal zero-sum U of π(T), the complement R = T·U^{−1} has π(R) zero-sumfree of length 2n−|U|. If |U| = 2, π(R) has maximal length 2n−2, and the rank-two inverse structure (Property B, CLM-0093/0110 for primes; the multiplicative extension to n = 15, 20 must be source-checked before use) constrains it.
     - (ii) Exchange arguments. Two different zero-sum subsequences U ≠ V of π(T) with U ∩ V ≠ ∅ have σ(U) = σ(V) = g in G. Then U·V^{−1} and V·U^{−1} have equal G-sums and, being disjoint, can be combined with the complement.
     - (iii) Use the η(C_n²) = 3n−2 short zero-sum value (SOURCE_STATED in SRC-0033) only if its scope is checked.
   - **Equality structure:** record precisely whether the case is excluded for all n, for primes only, or conditionally.
2. **Smaller-order multiplicities and support size.**
   - Bound multiplicities of elements of order m < n (for n = 20: orders 2, 4, 5, 10) in a zero-sumfree (3n−2)-term sequence, via quotients G/⟨g⟩. Identify the exact quotient groups and which of their Davenport constants are known (p-groups, rank ≤ 2) or only bounded. Use only source-checked values.
   - **Combine with CLM-0350:** a counterexample needs at least ⌈(3n−2)/(n−2)⌉ = 4 distinct values. Compare with CLM-0153 (basis plus one extra value impossible).
   - Decide whether a **small-support classification** (support ≤ 4 or 5 with multiplicities ≤ n−2) is provable by hand, or would need exact tooling. If it needs tooling, this could become a claim-backed search-reopen reason. In that case S107 may only *propose* the gated pre-registration for S108, never run it.
3. **Optional:** a Phase-2 gate extension for symmetry-reduced exhaustive tooling (design and settled-group tests only), if item 2 makes it necessary.

**Honesty rules.**
- A failed attempt goes in the failure ledger with its precise obstruction.
- Do not upgrade inherited or source claims.
- Do not use rank-two inverse results for composite n without source-checking their composite-n validity.
- Do not claim SAT20/SAT15 or any D value.

## 2. Deliverables and close

- Create S107 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (a `validation/validate_s107.py` in the style of `validate_s106.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note `research/S107_SATURATION_FALLBACK_<topic>.md` and independent exact tests on settled groups for any new lemma.
- Update: claims/sources (JSON and Markdown), phase/session/failure/decision ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 2, fallback_progress, search_reopen_condition_met), README/START_HERE.
- Leave the frontier unchanged unless there is an independently checked improvement. Keep the original 29 sources and 30 frontier rows intact.
- Install a FULL S108 prompt: continue SATURATION_FALLBACK, or propose a gated pre-registration if the reopen condition is genuinely met (stating why).
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, or a single solver or script as a certification.
