# Restart audit — 1 November 2026 (governance, not numbered research session)

**Snapshot:** main `63960a2aa123c4e2c07a81ebf1ba85d37231607e`; last completed research session S113, merged 18 October 2026. **No new computations or claims proved by this audit.** This note is a repository/claimed-evidence review and a bounded external-literature review, not independent verification of every proof. The previous 18 October proof-only owner steering is superseded for future work by the 1 November owner directive to resume proof-or-counterexample-directed long enumeration after feasibility and pre-registration. Historical instructions and results remain archived.

## 1. Position

Question: does every sequence of 3n-2 elements of C_n^3 have a nonempty zero-sum subsequence, i.e. D(C_n^3)=3n-2? A counterexample is an explicit zero-sumfree sequence of length 3n-2, with n=15, L=43, and n=20, L=58 currently prioritised. **Neither target is settled.**

- S104/S105: two distinct heuristic rounds, CAM-0002–0005, reached 42/57 only. A completed budget is *not* an exclusion.
- S109/S110: two algorithmically independent full exhaustive implementations of the support-at-most-five family, CAM-0006/0007. All 56 shards complete and maxima 42 at n=15 and 57 at n=20, approximately 146 aggregate CPU-hours. Common proof assumptions CLM-0358/0361..0364 are same-executor, with no formal certification.
- S111/S112/S113: hand arguments exclude support <=5 at n=15 (CLM-0376) and, conditional on explicitly recorded smaller-group D values, support <=6 at n=20 (CLM-0382). Thus a target counterexample needs >=6 distinct values for n=15, >=7 for n=20. S113 proves the block-route *counting method* sharp on stated families, not the conjecture.
- S112 CLM-0378: exactly five support-six multiplicity profiles at n=15 survive the **multiplicity-only** multi-route sieve; all values have order 15: (2,4,8,8,8,13), (2,8,8,8,8,9), (3,8,8,8,8,8), (4,4,8,8,8,11), (4,7,8,8,8,8). At n=20, 139 seven-value multiplicity profiles survive. They are arithmetic survivors, **not** actual candidate sequences.
- S103 exact checkers are useful: checker_a.py uses Boolean subset-sum propagation; checker_b.py independently counts subsets in pure Python; the campaigns and provenance are committed. A Lean 4 certificate pipeline, SAT LRAT/DRAT proof pipeline and hosted CI are not built.

## 2. Repository inventory and evidence caveats

Main tree has 1,627 entries (including directories); 383 claims: 313 PROGRAMME_PROVED, 26 SOURCE_STATED, 7 COMPUTED_EXACT, 37 INHERITED_UNVERIFIED; **none formally certified**. Sources: 34, of which 14 PROOF_INSPECTED, 7 STATEMENT_INSPECTED, 5 ABSTRACT_INSPECTED, 6 METADATA_ONLY and 2 SECONDARY_ONLY. The frontier records thirty n rows, with unresolved intervals n15 43..45, n20 58..59, n21 61..63, n28 82..83, n30 88..90 (frontier snapshot as of 12 October; recheck before present-day novelty statements). The long historical blocker and decision ledgers are preserved; old blockers are not automatically live blockers. There is no active or preregistered search. CI is ABSENT_NOT_PASS.

Proof statuses are internal programme classifications, not peer review or kernel verification. Re-reading committed statements, reviews, logs, counts and selected code does not independently certify all 383 statements or rerun 146 CPU-hours. Do not upgrade any claims by this note.

## 3. Current prior-art orientation — bounded audit, pending primary-proof inspection

- Classical prime-power/rank-two Davenport theorems and the historically settled n=2p^a and n=3*2^a families remain baseline (see SRC-0001/0002/0003/0023).
- Sze Chun Yiu (2026), *The fourth generalized Davenport constant of C_5^3*, https://arxiv.org/abs/2609.04950 : relevant architecture of multiplicity/geometric reductions followed by multiple independent exhaustive algorithms; the invariant is generalized D_k, not D(C_15^3) or D(C_20^3). Already catalogued SRC-0029; inspect exact version and certificates.
- Guoqing Wang (2026), *Disproof of a Conjectured Upper Bound for the Davenport Constant*, https://arxiv.org/abs/2609.29878 : high-rank counterexamples do not refute homocyclic rank-three equality. Review for transferable constructions, not for a purported direct result.
- Han–Zhang (2026), *Davenport Constants of Finite Abelian Groups*, https://arxiv.org/abs/2610.15102 : general asymptotic/upper bounds, not authenticated exact target values (already SRC-0032).
- Geroldinger–Wang–Yang (2026), *On a classical zero-sum invariant II*, https://arxiv.org/abs/2609.17127 : missing-subsequence-sums/saturation structural tools could inform the fallback strategy; distinct problem.
- Grinsztajn 2026 general bound D(C_n^3)<=4n-P(n)-2, pointer https://teorth.github.io/optimizationproblems/constants/53a.html (SRC-0030/0031), does not strengthen recorded n15/n20 intervals, and primary proof PDF requires direct inspection.
- Davenport Constant Database https://github.com/jessicajhan/DavenportConstantDB covers abelian groups of order up to 500 in its described scope, not target group orders 3375 and 8000.

**No exact target theorem authenticated in this bounded audit. That is not a proof of openness or priority.** S114 must search current primary statements, versions, citations and active computation repos before writing novelty claims, then update sources only with actual inspected evidence.

## 4. Method verdict and restart priorities

**Exhausted:** rerunning unchanged S110 support-5 code at n15/n20, and bare multiplicity route counting on the families for which S113 proves sharpness. **Not exhausted:** support >=6/7 *image-level* search; certificate-guided SAT/backtracking; targeted lemma falsification; and rigorous saturation classification.

**Priority A — n=15, support exactly six.** Test the five CLM-0378 multiplicity profiles against actual order-15 values. Use C15^3 ~= C3^3 x C5^3 and GL3(F3) x GL3(F5), but every orbit reduction and any assumption that the support generates must be proved for the fixed-profile scope, not imported uncritically from CLM-0361. Build an exact sequence checker plus another independent implementation; use canonicalisation, subgroup/CRT pruning, and low-cost prefix subset-sum rejection. Benchmark and bound the exact case count before announcing an exhaustive campaign. A completed exclusion would upgrade n15 necessary support to >=7, **not** settle SAT15.

**Priority B — n=20, support exactly seven.** Refine the 139 CLM-0378 multiplicity-only survivors with the true C4^3 and C5^3 images, order constraints and the CLM-0372 mod-2 parity/Fano conditions. Avoid a naively enlarged rank-four relation-module enumeration. After successful n15 engine validation, quantify feasibility on n20 and narrow the profile family.

**Priority C — proof-guided search.** Test proposed restricted TWO*(a) or relation-module CRT box lemmas with exact counterexample-finding, and the saturation equivalence CLM-0345: a 3n-3 zero-sumfree sequence with subset sums != whole group would extend to a counterexample. A complete negative finite lemma may be a publishable step after independent checks.

## 5. Rules for future long laptop campaigns

A laptop budget (e.g. 6-12 hours) is not a mathematical certificate. Give each campaign: scope (n, support, multiplicities, element orders), sound/practical reductions with proofs, expected covering shard count, deterministic seeds or canonical exhaustive indexing, fixed code and environment digests, resource limits, checkpoints/resume without double-counting, stopping rule, complete exit/log hashes, an independent cross-check, and interpretation of possible outcomes. Run a settled-group preflight and controlled timing experiment first. Record HEURISTIC runs separately from EXHAUSTIVE ones. A negative conclusion requires exact coverage and verification per AGENTS rule 6; an actual candidate requires the AGENTS rule 5 quarantine/certification protocol.

**Execution status:** this governance note creates no research session, new claim, candidate, pre-registered campaign or actual target computation. S114 is a proposed tooling/literature/feasibility session. Starting an overnight campaign requires its own gated, preregistered later session.

## 6. Unfinished obligations and practical next moves

1. Modern primary literature statement/proof-level and version audit for n15/n20, including whether bounds/source dependencies improved since Oct12.
2. Reproduce CLM-0378's five n15 and 139 n20 arithmetic survivors independently; preserve full explicit profile lists and hashes.
3. Independent re-review of S109 reduction and exact search symmetry (shared-premise risk).
4. Implement/benchmark genuine support-six CRT/image solver, with complete coverage proof or clearly marked heuristic status; exploit available cores and RAM safely.
5. Choose next theorem obligation from an actually hard finite residue, not merely more symbolic necessary conditions; keep counterexample search as a parallel output.
6. Add CI, solver certificate verification, and optionally Lean kernel certification only where there is an actual certificate/theorem to validate.
7. Rewrite short live state/entry point without deleting the original detailed archive or silently relabelling claims.
