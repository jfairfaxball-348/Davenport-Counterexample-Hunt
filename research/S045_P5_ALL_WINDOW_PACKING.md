# S045 — all-window sharp C5³ multi-block obstruction (CLM-0175)

13 October 2026. Entirely symbolic, exact ORIGINAL index counts. Strengthens the S044 seven-block + twelve-remainder hostile local example to **every number of intact pure blocks**; not a C15 or C20 candidate and not the historically source-stated C5 generalized UPPER.

Use the internally proved S042 CLM-0160 family, for every integer k≥2,
  A_k=e1^(5k−6) e2^4 e3^4 (e1+e2)^3 (e1+e3)^2 (e2+e3)^2
in Q=C5³ with 5k+9 distinct indexed terms and **no k pairwise disjoint nonempty Qzero blocks** (S042 independent integer-coordinate proof; not a solver).

Exactly as in S044 CLM-0170, partition it into k−2 disjoint five-point P_j=e1^5; a seven-point quotient-zero block B=e1²(e1+e2)³e2²; and a 12-point quotient-zero-sumfree leftover
  L=e1²e2²e3⁴(e1+e3)²(e2+e3)².
The counts add exactly: 5(k−2)+7+12=5k+9. For each t=0,...,k−2 define the ORIGINAL-INDEX local window W_t=B∪L∪P_1∪...∪P_t, size |W_t|=19+5t.

**Exact sharp packing theorem.** The maximum number of pairwise index-disjoint nonempty Qzero blocks in W_t is EXACTLY t+1. The lower bound is witnessed by B,P_1,...,P_t. If W_t admitted t+2 disjoint Qzero blocks, adjoining the remaining untouched (k−2−t) pure five-blocks would give k disjoint zeros inside A_k, contradicting CLM-0160. No enumeration, CAS, candidate construction or source-stated upper bound is needed.

At t=0 this recovers S044 sharp 19-point window with exactly1 zero block maximally; t=1 provides a 24-point TWO-intact-block window with exactly2 disjoint zeros maximally; t=2 gives 29-point THREE-intact-block window with exactly3 maximally. More generally EVERY t-window saturates the 'no (t+2) disjoint zeros' exchange obstruction. For k=7,10,16 (conditional n15/20/30 p5 CRT cores), this family exists at each corresponding t≤k−2. Therefore no argument depending ONLY on the number of disjoint quotient zeros in a B+L+t-pure-block union can force the missing extra block: it must use decorated H sums, a different global partition, or inverse constraints coming from an actual composite sequence.

**Hostile check.** All included P_j and B are ORIGINAL indexed Qzeros; L is ZSF. The 24/29 examples are not statements that an arbitrary window of those sizes has packing number t+1, and A_k's 5k+9 terms are QUOTIENT MODEL terms, not the length3n−2 genuine G candidate. Claim does not independently authenticate Yiu's D_t(C5³) upper or p5 η.
