# S107 hostile same-executor review — 17 October 2026

**ACCEPT, narrowly:** CLM-0353/0354/0355 as elementary programme proofs, CLM-0356 as SOURCE_STATED, and CLM-0357 as conditional on CLM-0352/0356. This is NOT an independent or kernel validation.

**Attacks and resolutions:**
1. *CLM-0353 ranges:* the block has m−j copies. Completing kh to zero needs m−k copies, which are available iff k ≥ j. So the allowed sums are exactly k ∈ [1, j−1]. Checked against checkers A/B on 1,587 random instances, including j = m (no block) and T containing h.
2. *CLM-0354: does q | h_i hold for every coordinate?* The order of h_i in Z/n divides m, so n/gcd(h_i,n) divides m, so q = n/m divides gcd(h_i,n). For p | m the contradiction step is right: if p divides every w_i, then h = qw ∈ qpG, so (m/p)h = 0. Checked by running the construction on all 44,080 nonzero elements, n ≤ 20.
3. *CLM-0355: is the image of h of order exactly d, and is k mod d nonzero?* ⟨dh⟩ has index d in ⟨h⟩, so h̄ has order d. The allowed k satisfy 1 ≤ k ≤ j−1 ≤ d−1, so they are distinct and nonzero mod d. The test checks the order of h̄ explicitly in coordinates, and the zero-sumfreeness with both checkers, on 897 constructed instances.
4. *Arithmetic of the corollary at n=20:* d(C2⊕C20⊕C20) = 39 (CLM-0356). For h of order 20 with multiplicity 18 (j = 2, d = 2): |S| ≤ 20 − 2 + 39 = 57 < 58. For h of order 10 with multiplicity 9 (j = 1, d = 1): nd/m = 2, so |S| ≤ 9 + 39 = 48 < 58. Both are correct.
5. *Conditional caps:* the first draft had off-by-one errors. They were recomputed mechanically from the inequality and fixed, and the slip is recorded in the failure ledger.
6. *Source scope:* CLM-0356 is a statement recalled inside Girard–Schmid as Theorem 2.7, attributed to earlier work. Only the statement was inspected, so it is SOURCE_STATED. The original SRC-0005 record is unchanged, and the inspection is logged in `s107_audit`.
7. *Overreach check:* no claim about n=15 beyond CLM-0350. The conditional n=15 consequences are stated only as implications from unknown D* values.
8. *Search discipline:* the tests are small-group exact validations only. There was no n=15/20 sequence search, no campaign, and no candidate.

**Residual limitations:**
- CI is ABSENT_NOT_PASS.
- The review is internal, by the same executor.
- No Lean formalisation exists.
- SAT20/SAT15 remain OPEN.
