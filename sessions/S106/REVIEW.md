# S106 hostile same-executor review — 17 October 2026

**ACCEPT, narrowly:** CLM-0348..0351 as elementary programme proofs (CLM-0350 conditional on CLM-0352), CLM-0352 as SOURCE_STATED, and SRC-0033/0034 at STATEMENT_INSPECTED. This is NOT an independent or kernel validation.

**Attacks and resolutions:**
1. *Was "Keep going?" a valid invocation?* It came from the owner in chat immediately after the S105 report, whose installed next step is S106. It is read as "run next session" and authorises S106 only. The interpretation is recorded in INPUT.md.
2. *CLM-0348: is order n really enough for basis completion over a non-field?* Yes. Order n means that for every p | n some coordinate is a unit mod p. The local completion has determinant ±a_i, a unit. CRT gluing gives a unit determinant mod n. It was checked by explicit construction for all 40,567 order-n elements, n = 2..20.
3. *CLM-0349 (⇒): does adding m−k copies of g need copies we don't have?* The block has m−1 copies, and m−k ≤ m−1 since k ≥ 1. The k = 0 case is itself a zero-sum. Both directions were also checked against checkers A/B on 1,981 random instances, with T allowed to contain g.
4. *CLM-0350: is the source premise properly scoped?* The rank-two value is SOURCE_STATED from two inspected statements; the original proofs were not re-inspected. CLM-0350 is labelled conditional. The exhaustive n=3,4 check (max |T| = 2n−2) is consistent with it. Note that D(C_3²), D(C_4²) are also p-group values, internally provable via Olson, but that is not claimed here.
5. *CLM-0350 scope:* it caps only elements of order exactly n. Elements of smaller order m only get the trivial cap m−1. Nothing is claimed about the sizes of quotients by smaller-order elements.
6. *CLM-0351: are the boundaries right?* With m−2 copies, the available additions are 1..m−2, which excludes only k = 1 (it would need m−1 copies). The disjointness corollary uses g ≠ 0, which holds since m ≥ 3. Checked on 1,892 random instances.
7. *Is the n−2 obstruction stated honestly?* Yes. The 2-wise rank-two constant is only cited (not inspected), and it is used only to explain why counting fails, never as a premise of a claim.
8. *Do the tests amount to an unregistered search?* No. They run only in settled groups (n ≤ 12 for the random and exhaustive parts; the basis-completion check enumerates group elements, not sequences). Nothing ran at n = 15/20.
9. *Novelty:* none claimed. Quotient arguments of this type are classical (cf. Gao 2000, METADATA_ONLY).

**Residual limitations:**
- CI is ABSENT_NOT_PASS.
- The review is internal, by the same executor.
- No Lean formalisation exists.
- SAT20/SAT15 remain OPEN.
