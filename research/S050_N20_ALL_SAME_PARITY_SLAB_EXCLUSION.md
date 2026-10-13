# S050 — unrestricted eight-point slab exclusion in C20³ (CLM-0192)
13 October 2026; symbolic original-index proof; internally reviewed, not independently certified. **Fixed special U22 only; NOT a proof of D(C20³)=58.**

## Hypothetical original-index configuration
Let G=C20³, H=2G≅C10³, and iota:H→2G be the canonical doubling identification; NO split C2³⊕C10³ is assumed. Suppose a minimally zero-sum T has 59 distinct indexed original positions partitioned into 22 disjoint parity-zero PAIRS (44 positions), eight further individual positions g1,...,g8 lying in ANY ONE SAME parity class modulo 2, and seven remaining singleton positions sr indexed by each nonzero r∈F2³ once. Assume the 22 pair sums, interpreted by iota inverse in H, form U=f1⁹ f2⁹ f3⁴. Unlike S049, make **no restriction** on the eight gi beyond shared parity: they need not be distinct as G values, their first two coordinates and their third coordinates are arbitrary, and their common parity class need not be the S048 chosen one.

The inclusive subset sumset of U has first two coordinates unrestricted and third in {0,6,7,8,9} after negation. Hence E(U)=H\(-Σ(U)) has precisely third coordinates A={1,2,3,4,5}⊂Z10.

Let ai∈Z20 be the third coordinate of gi. Since all eight share G modulo 2, all ai have the same parity. For any even-cardinality subset J of their ORIGINAL indices define wJ=iota^-1(Σ_{j∈J}gj)∈H, with third coordinate (Σ_{j∈J}aj)/2 mod10; this expression is well-defined modulo 10 because the G-sum is even. For nonempty J, J and any subset of the 22 external pair blocks together use at most 8+44=52<59 original positions, so G-minimality forces wJ∈E(U). For any Fano line L (three of seven odd singleton classes) or complementary Fano cap Lc (four), write hC=iota^-1(Σ_{r∈C}sr). Its quotient sum is even. The union C∪J together with any external pairs uses at most 4+8+44=56<59 and is nonempty even for J empty, so **hC+wJ∈E(U) for EVERY even-cardinality J, including J=∅**. No extension membership for C=all seven and all eight is used.

## Four-pair subset-sum lemma, no enumeration
Take an ARBITRARY perfect pairing of the eight original gi positions into four disjoint two-point groups. Let bj=(a_{u_j}+a_{v_j})/2 mod10, j=1,...,4. Every nonempty union of groups is a nonempty even subset of the eight points, so every nonempty subset sum of b1,...,b4 belongs to A={1,2,3,4,5}; in particular each bj∈A.

**Elementary classification:** four entries bj∈{1,...,5} whose EVERY nonempty subset sum modulo 10 lies in A must, up to order, be either (1,1,1,1) or (2,1,1,1).
- If a 5 occurs, any second entry produces residue 6,7,8,9 or0 outside A.
- If a 4 occurs, all other entries must be1 by two-entry tests, but a 4+1+1 triple produces 6 outside A.
- If a 3 occurs, others are1 or2. A 2 produces an illegal 3+2+1=6 triple; if all other entries are1 the full sum is6. Therefore all bj≤2.
- If at least two 2s occur, either the full total is at least6 and at most8 (when exactly two 2s, total6; when three, a triple of 2s sums6; when four likewise), giving an invalid subset. Thus at most one2 remains. Both displayed possibilities satisfy the stated nonempty condition.

The second possibility (2,1,1,1) produces SIX distinct subset sums, 0,1,2,3,4,5, including the empty subset. But fix ANY Fano line L: all six sums are realised by even J formed from these same four disjoint pair groups, and all third(hL)+third(wJ) must lie in A of cardinality only five. Translation mod10 is injective, contradiction. Consequently **every arbitrary pairing has all four bj=1**, and because any selected pair {gi,gj} extends to a perfect pairing of eight, (ai+aj)/2=1 mod10, equivalently ai+aj≡2 mod20, for every i≠j. With at least three indices this forces a1=...=a8=a∈Z20, and 2a≡2 mod20, i.e. **a is 1 or 11 modulo20**.

## Global Fano contradiction
The full eight-point sum has H-third v=8a/2=4a≡4 mod10. For EVERY Fano line and cap C, both hC and hC+v are in E(U) by the PROPER subset tests above, hence third(hC)∈A∩(A−4)={1}. Denote V all seven nonzero parity singleton indices. Each line plus its complementary cap partitions V, so third(hV)=1+1=2 mod10. Each singleton appears on exactly THREE of the seven Fano lines, so Σ_{L line}hL=3hV in H (the non-split iota inverse applies to each even parity sum). Third coordinates give 7·1=3·2, i.e. 7=6 mod10, an impossibility.

**Proved CLM-0192:** NO minimally zero-sum T59 with the specified special U22 core, eight arbitrary original G positions from any single mod2 parity class, and seven other singleton representatives once each. This STRICTLY generalises CLM-0189 (which fixed gi=G_f3+2di and hence ai=1). It does not exclude other U22 cores, other partitions/re-pairings of 59 original positions, nor profiles not admitting this precise 22+8+7 pattern.

## Hostile checks
All pairings are used to certify an equality for **any two original gi**; unlike S047, we never count the 763→127 matching compression as independent inequalities. For the (2,1,1,1) obstruction we rely on all SIX distinct H-third values, including the empty J only in the NONEMPTY line C union. For J alone, only NONEMPTY even subsets are tested. The total T is never used as a proper subset. The canonical iota applies only to parity-zero sums. No numerical mathematical search, CAS, orbit generation or external certification was used.
