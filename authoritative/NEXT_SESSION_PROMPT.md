# S108 — SATURATION FALLBACK SESSION 3 (FUTURE / NOT EXECUTED)

**Active priority: SATURATION_FALLBACK.** It was switched in S105 by the owner directive's two-round trigger (directive of 16 October 2026).
- The SEARCH_FIRST rounds (S104 R1, S105 R2) reached only 3n−3 and are closed. That is not a negative result.
- Run S108 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters and the search-reopen condition into every future prompt until evidence or the owner changes them.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S107 merge is still the head.
- Read `AGENTS.md`, `authoritative/STATE.json` (`counterexample_hunt_strategy`, `s107_result`), `research/S107_SATURATION_FALLBACK_MULTIPLICITY_DEFECT_TRANSFER.md`, `research/S106_SATURATION_FALLBACK_MULTIPLICITY_QUOTIENT.md`, `catalogue/CLAIMS.md` (CLM-0038, CLM-0049, CLM-0051, CLM-0142, CLM-0152, CLM-0153, CLM-0345..0357), `catalogue/SOURCES.md` (SRC-0004, SRC-0005, SRC-0008, SRC-0010, SRC-0015, SRC-0016, SRC-0033, SRC-0034), `docs/FAILURE_AND_LESSON_LEDGER.md` (S106, S107 entries), and `sessions/S107/*`.
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S108/INPUT.md` and `INPUT_MANIFEST.json`.
- **Git credential note:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential (`git credential-manager get` with username `jfairfaxball-348`) for that command only. Do not change the stored git or gh configuration.

**State at S107 close:**
- Phase 1 has a SCOPED PASS (search targets); the general frontier map is still IN_PROGRESS.
- Phase 2 has a SCOPED PASS covering checkers A/B and the R1/R2 heuristic engines. There is no exhaustive, SAT or Lean tooling.
- Phase 3: search CLOSED; no campaign is active or pre-registered.
- Search counters (frozen): setup 1, active search sessions 2, completed rounds 2. Fallback sessions completed: 2 (S106, S107).
- Claims total 357, sources total 34 (the original 29 untouched), and the 30 frontier rows are untouched.

**Fallback targets (OPEN):**
- **SAT20:** D(C20³) = 58, i.e. every zero-sumfree 57-term sequence has Σ = G.
- **SAT15:** D(C15³) = 43.

**Proved so far (INTERNAL, elementary, no novelty claimed; S = a hypothetical zero-sumfree (3n−2)-term sequence over C_n³):**
- **CLM-0349 / CLM-0351 / CLM-0353:** h^{m−j}T is zero-sumfree iff every nonempty T′ ⊆ T with σ(T′) ∈ ⟨h⟩ has σ(T′) ∈ {h,…,(j−1)h}.
- **CLM-0354:** every h of order m in C_n^r is (n/m)u with u of order n, and G/⟨dh⟩ ≅ C_{nd/m} ⊕ C_n^{r−1}.
- **CLM-0355 (transfer):** if v_h(S) = m−j and d | m with d ≥ j, then |S| ≤ m − d + d(C_{nd/m} ⊕ C_n ⊕ C_n). For |S| = 3n−2 the case is excluded when that group has D = D* and n+1+d > m+nd/m.
- **CLM-0350 / CLM-0357:**
  - n=15: order-15 multiplicities ≤ 13.
  - n=20: order-20 multiplicities ≤ 17 and order-10 multiplicities ≤ 8. This is conditional on SOURCE_STATED CLM-0352 (rank two) and CLM-0356 (D(C2⊕C20⊕C20) = 40).
- **Levers (conditional, unknown):**
  - n=20: D*(C4⊕C20⊕C20) gives order-20 cap 15 / order-10 cap 7 / order-5 cap 3. D*(C5⊕C20⊕C20) gives order-20 cap 14 / order-4 cap 2. D*(C10⊕C20⊕C20) gives order-20 cap 9 / order-10 cap 4 / order-4 cap 1 / no order-2 terms.
  - n=15: D*(C3⊕C15⊕C15) gives order-15 cap 11 / order-5 cap 3. D*(C5⊕C15⊕C15) gives order-15 cap 9 / order-3 cap 1.

**Search-reopen condition:** an explicit owner directive, or a substantive structural reason recorded as a claim (for example a proved reduction to a small structured family amenable to exhaustive or SAT treatment), followed by a full pre-registration and gate. A parameter change of R1/R2 does not qualify.

## 1. S108 work (bounded; choose and finish a coherent subset)

1. **Source frontier for the lever groups.**
   - Determine what is published about D(C_e ⊕ C_n ⊕ C_n) for (e, n) ∈ {(4,20), (5,20), (10,20), (3,15), (5,15)}. Also determine what is published about general families such as D(C_m ⊕ C_n ⊕ C_n) for m | n with special m: Gao 2000 (SRC-0004, METADATA_ONLY); Delorme–Ordaz–Quiroz (SRC-0011) on Z_n ⊕ Z_nm ⊕ Z_nmq for n = 2, 3; BSP (SRC-0008/0021) on C3⊕C3⊕C3d; Girard–Schmid inverse results; any 2024–2026 work.
   - Record each source with its true access level. Never promote a remembered statement to SOURCE_STATED.
2. **Internal proofs for a lever group, where feasible.**
   - Try to prove D(C_e ⊕ C_n ⊕ C_n) = D* for one lever group by the same transfer technique applied inside C_e ⊕ C_n ⊕ C_n. That means quotients by suitable elements, landing in rank-two groups or in C2-type groups (CLM-0356).
   - Alternatively prove the weaker multiplicity statements that the lever is actually used for. For example, show directly that a zero-sumfree sequence of the relevant length over C4 ⊕ C20 ⊕ C20 cannot exist under the multiplicity hypotheses that S inherits.
   - State precisely which multiplicity hypotheses transfer.
3. **Combine caps into support structure.**
   - With the n=20 caps (order 20 ≤ 17, order 10 ≤ 8, orders 5/4/2 ≤ 4/3/1), a counterexample has at least 4 distinct values. Combine this with CLM-0153 (basis plus one extra value impossible) and with projections C20³ → C10³ (CLM-0152 parity pairing) or C20³ → C4³/C5³.
   - Aim for a structural statement, for example that the support is not contained in a small number of cyclic subgroups. Record exactly what survives.
   - If a reduction to a finite structured family appears, it could become a claim-backed search-reopen reason. S108 may only *propose* a gated pre-registration for S109, never run it.

**Honesty rules.**
- Failed attempts go in the failure ledger with their exact obstruction.
- Tabulate numerical consequences mechanically from the proved inequality (S107 lesson).
- Do not upgrade inherited or source claims.
- Do not claim SAT20/SAT15 or any D value.
- Exact tests run only on small or settled groups.

## 2. Deliverables and close

- Create S108 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (a `validation/validate_s108.py` in the style of `validate_s107.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note `research/S108_SATURATION_FALLBACK_<topic>.md`, with independent exact tests for any new lemma.
- Update: claims/sources (JSON and Markdown; never edit the original 29 source records, log inspections in an `s108_audit` block), phase/session/failure/decision ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 3, fallback_progress, search_reopen_condition_met), README/START_HERE.
- Leave the frontier unchanged unless there is an independently checked improvement.
- Install a FULL S109 prompt: continue SATURATION_FALLBACK, or propose a gated pre-registration if the reopen condition is genuinely met (stating why).
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, or a single solver or script as a certification.
