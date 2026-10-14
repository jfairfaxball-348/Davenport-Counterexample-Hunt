# S055 — original-index one-split complement duality (CLM-0209)

14 October 2026. Pure symbolic exact reduction within the S053/S054 hypothetical G=C20³, H=C10³, iota(h)=2h, Q=G/2G. Not a nonzero-parity split exclusion and not a 58-term zero-free candidate.

Write U=(u_1,...,u_22) for the H pair-sums of the 22 ORIGINAL pairs (a_i,b_i), a_i+b_i=iota(u_i); X is the 15 ORIGINAL outsider positions, and Σ_X X=iota(c) with c=−Σ_U u_i in H. Every outsider subset A with quotient sum t_i=π(a_i)=π(b_i) makes a_i+Σ_A X and b_i+Σ_A X elements of ker π=iota(H). The seven distinct nonzero Fano singleton parities span Q, so for EVERY t∈Q there are EXACTLY 2^(15−3)=4096 indexed subsets A⊆X with πΣ_A=t. This is a parity-fibre count, NOT mathematical candidate enumeration.

Fix i and set V_i=U without ORIGINAL index i, c_i=−ΣV_i=c+u_i. Define z_a(A)=iota^−1(a_i+Σ_A X) and z_b(A)=iota^−1(b_i+Σ_A X) for parity-matched A. Complements are in the SAME parity fibre because πΣ_X X=0, so πΣ_(X\A) X=t_i. The crucial exact ORIGINAL-index identity is

    z_a(A)+z_b(X\A)
      = iota^−1(a_i+b_i+Σ_X X)
      = u_i+c = c_i.

For ANY indexed H sequence V, the extension set E(V)={x:V*x is zero-sumfree} satisfies E(V)=−ΣV−E(V) by complementing the ORIGINAL subset indices in V. Applying this to V_i gives

    z_a(A)∈E(V_i)   IFF   z_b(X\A)∈E(V_i).

This involution pairs the 8192 labelled one-split conditions (two ORIGINAL choices a/b for each of 4096 parity-matched A) into 4096 equivalent complementary pairs, with NO fixed pair because a_i and b_i are distinct ORIGINAL positions. Consequently the entire I={i} necessary-and-sufficient split screening from S053 can be checked in one-sided form:

    for every indexed A⊆X with πΣ_A=t_i,
       z_a(A)∈E(U\{i}).

Equivalent formulation with b instead of a. Across the 22 labelled pair indices there are 22×4096=90,112 one-sided labelled conditions; repeated H values may cause dependencies, so 90,112 is NOT a count of independent H constraints. These conditions MUST be combined with all |I|≥2 split cases and the 4,094 proper no-split outsider-shadow cases; satisfying one-splits alone is NOT enough for a minimal T.

## Reverse audit and targeted obstruction

The value c_i is c+u_i, not c, since the indexed pair-sum u_i is deleted. Using E(U) instead of E(U\{i}) invalidates the theorem. The complement must exchange a_i and b_i AS WELL AS A and X\A; complementing A while keeping a_i fixed does not generally preserve E(V_i). The involution works also for t_i=0 formally, but S054 already conditionally eliminates all such original lifts. A parity-matched outsider subset may be empty only for t_i=0; in the surviving nonzero class every A is nonempty and proper, but the proof does not need that observation.

A four-cycle switch of two matchings of the same eight g ORIGINAL positions changes the H block values while preserving the union of those four positions. Extending an equality of total sums to a contradiction requires a nontrivial INVERSE property of maximal H atoms. The S054 minimality proof applies individually to every matching but does not assert injectivity or inequality among the resulting sums, so comparing two such matchings does not, by itself, kill the one-split fibre. Likewise the seven Fano L/L^c partitions are simultaneously required, but the label count is not independent information.

This exact complement duality is a quantitative *logical reduction* and a hostile guardrail for future inverse attacks; it does NOT prove there is any U22/lift satisfying all demands, nor that none exists. The nonzero original-index split case remains OPEN.
