# S097 — Exact original q-matching horizontal-flat rigidity in axial G20

16 October 2026. **INTERNAL SAME_EXECUTOR, SOURCE-CONDITIONAL S060/S092 HAND PROOF.** Entry main 8a540ddaad503e9c7ddaef4ca6c93d43be93048f, directly authenticated Git root e9c9b4c127b82d44dc59534642ef176e26cbdb5d; S096 merged with two parents. Incoming S097 FUTURE prompt blob b1fadf2aed6c36c2d732c9894a054cf90dcd4e6e. No numerical search, generated lifts, solver, CAS, SAT/ILP, Lean, Palomar, campaign, external certification or source promotion.

## 1. Twelve genuinely original grouped q values

Let G=(Z/20)^3, H=(Z/10)^3, iota(h)=2h in G, q=(0,0,1) in Q=G/2G. Work conditionally in the TRUE S060 original 59-index model: 22 distinct labelled complete original pairs (a_i,b_i), U*=e1^8e2^8e3^6 with (a_i+b_i)=2u_i, eight individually indexed g positions, and seven individually indexed singleton s_r. The twelve disjoint actual q-supervertex groups are {g_1},...,{g_8}, {S=s_q}, {X_1,Y_1}, {X_2,Y_2}, {X_3,Y_3}, with true G20 sums w_1,...,w_12 each of parity q. This is a grouping of FIFTEEN original physical outsider positions, NOT twelve freely constructed or independent H vectors. All original indices stay distinct even when G values coincide.

The ORIGINAL all-59 total-zero requirement implies, with full modulo20 carry,

    sum_{j=1}^{12} w_j= -2sum(U*)= -(16,16,12)=(4,4,8) in G. (1)

For every nonempty proper EVEN subset J of the twelve q-group labels, pair all groups of J internally and pair its complement internally: this extends to a genuine perfect matching of the twelve. The half h(J)=iota^{-1}(sum_{j in J} w_j) belongs to H. The original 28-block all-q matching atom condition forces

    h(J) in E(U*) = H \ B(U*),
    B(U*)={(-k1,-k2,-k3) mod10: 0<=k1<=8, 0<=k2<=8,0<=k3<=6}. (2)

Indeed if h lies in B, choose literally k1 among the eight e1 original pair labels, k2 among the eight e2 labels and k3 among the six e3 labels. Select BOTH original members of those chosen complete pairs and all original positions making up the q groups of J. The G sum is exactly 2(h+(k1,k2,k3))=0; it is NONEMPTY and PROPER because J omits at least two q groups. This is a genuine original support and does not suppress carries or split V_l. Equation (2) is NECESSARY, not a certificate that remaining q or mixed tests pass.

There are exactly 2046 nonempty proper even grouped J (2^11 minus the empty and full cases), NOT to be conflated with the separate 2048 ungrouped Fano-transversal outsider residuals. J=all12 is specifically excepted because its full-U completion is the full ambient 59-index total zero. The entire true q P_q/I/alpha E(U\I) and non-q mixed gates remain additional requirements.

The axial box gives the exact H10 test

    h in E(U*) iff [h1=1 or h2=1 or h3 in {1,2,3}] mod10. (3)

## 2. CLM-0337: six flat q groups force a common *G20* third coordinate

Call an ACTUAL q group HORIZONTAL-FLAT if BOTH its first and second G20 coordinates lie in {0,10}, and write F for the set of distinct original group labels with this property. Their true third coordinates z_i are ODD mod20.

For EVERY even J⊆F, the true H horizontal coordinates h1(J),h2(J) lie in {0,5}. Thus any proper nonempty J from F must satisfy

    h3(J) in {1,2,3} in H3=C10.                       (4)

**Theorem (exact full-carry six-flat rigidity).** If |F|>=6 and all required proper q-group gates hold, all groups in F have ONE AND THE SAME G20 third coordinate z, where z=1 or z=11 mod20.

Take any six actual labels from F and ANY perfect matching of those six into three genuine two-group subsets P1,P2,P3. Set b_r=h3(P_r), represented as integers 1,2 or3 by (4). The union of all six has third H value b1+b2+b3 mod10 and is itself a PROPER nonempty even grouped J. The integer sum lies 3..9 with no modulo10 wrap, and (4) requires it in {1,2,3}; hence b1+b2+b3=3 and every b_r=1.

Any two distinct labels i,j can be included in such a six-group matching, pairing the other four arbitrarily. Consequently

    z_i+z_j =2 mod20 for EVERY distinct i,j among the six. (5)

Subtracting equations sharing one i makes all other z_j equal; using >=3 distinct labels forces all six z equal. Then 2z=2 mod20 gives EXACTLY z=1 or11; the latter torsion alternative must NOT be discarded. If F has more than six labels, repeat with five fixed labels and each additional one to propagate the same z. This proves actual original modulo20 third-coordinate equality, NOT merely a projected F5 multiplicity statement. QED.

**New combined consequence:** for any such flat w_j, ((w_j-q0)/2) mod5=(0,0,0) in F5^3 with q0=(0,0,1). Horizontal differences 0 or10 become 0 or5 in H, and (z-1)/2 is0 or5, both projecting to zero mod5. Therefore SIX flat groups would occupy one identical projected q-half-value. Existing S092 CLM-0325, in exactly this source-conditional real original axial framework under its true q necessary gates, already excludes six-or-more occurrences of ANY one projected q-half-value. Combining S097 rigidity and the pre-existing S092 proof gives

    |F| <= 5                                                (6)

for any fully necessary-q-gated axial S060 baseline. This is the genuine new bridge: before imposing (4), six group third coordinates could have different mod5 projections and S092's simple repeated-fibre filter would not rule out the INPUT. Do NOT describe (6) as a new standalone reproof of S092, nor extend it unconditionally to arbitrary U22/P26 or all original G59.

## 3. CLM-0338: independent eight-flat proper zero, seven-flat external slab

A direct bound needs NO S092. If eight distinct q groups are flat, (5) forces their common z=1 or11. Their actual eight-group G total has third coordinate 8z=8 mod20, and horizontal coordinates 0 or10. Thus

    h(J)=(5epsilon1,5epsilon2,4) in H, epsilon_r in {0,1}. (7)

This is OUTSIDE E(U*) by (3). A literal proper original G zero uses all original indices in those eight actual q groups, together with both physical endpoints of 5epsilon1 distinct e1 full pairs, 5epsilon2 distinct e2 full pairs, and ALL SIX indexed e3 full pairs. Sum in G is 2((5epsilon1,5epsilon2,4)+(5epsilon1,5epsilon2,6))=0. There are four omitted q groups, so the index subset is definitely proper, not the full-twelve exception. Therefore independently |F|<=7, sharpened to <=5 only via S092.

There is also a necessary external horizontal slab at the seven-flat boundary. If seven distinct q groups are flat and v is any other ACTUAL q group, write its horizontal G coordinates (2a,2b), a,b mod10, and its ODD third G coordinate z_v. Suppose neither a nor b lies in {1,6}, equivalently neither horizontal G coordinate of v lies in {2,12}. For each odd j=1,3,5,7 choose j distinct flat groups and v. Each of these FOUR genuine q-group supports is even, nonempty and proper (at most eight of twelve groups). Its horizontal half-coordinates are a+5epsilon and b+5eta, neither equal1 under the assumption, irrespective of chosen flat groups. Thus all four true third halves must be in {1,2,3} by (3).

All seven flat thirds share z=1 or11 by the six-flat theorem. For 1,3,5,7 selected flat groups, the four true even-sum third halves form

    d, d+z, d+2z, d+3z mod10, d=(z_v+z)/2 in C10. (8)

The division by2 applies to the EVEN summed G third coordinate (z_v+z), not an individually odd q group. Since z=1 mod10, these are four consecutive residues in C10, which cannot all lie in the three-element set {1,2,3}. For a violating j, set k_r=(-h_r(J)) mod10: k1,k2 are each in 0..8 (h1,h2≠1), and k3 is in0..6 (h3∉{1,2,3}). Take the real q groups and BOTH actual endpoints of exactly those k_r full U pairs. This explicitly constructs a nonempty proper zero. Therefore each nonflat external q group must have at least ONE horizontal original G20 coordinate in {2,12}. The seven-flat case itself is already impossible when S092 is added, but the implication is a valid independent original-index gate.

## 4. Exact S096 physical-model reproduction

S096's same-59-index model has NINE distinct flat q groups: S,g1,...,g8, all horizontal0 in original G20. In particular the eight physically distinct original singleton outsider indices S,g1,...,g7 all equal (0,0,1). Their subtotal is (0,0,8). Select BOTH true original endpoints of every one of the six e3 full pairs i=17,...,22, adding (0,0,12). The resulting 8+12=20 ORIGINAL positions sum (0,0,20)=0; the other 39 positions are omitted. This is a proper p000 zero that already kills the complete matching gate WITHOUT even selecting g8.

Another distinct proper original FOUR-index witness is {g8,g1,a17,b17}, because their G third coordinates are 17+1+2=20, with both horizontals0. This complements S096's previously identified different proper four-q-outsider zero {S,g8,g1,g2}. These are actual supports, not counterexamples to a theorem: S096 deliberately failed the q gate and was never an admissible G59.

## 5. Full original twelve-q attempt and precise failure

The positive result rules out the broad family of six-or-more horizontal-flat actual q groups (including all S096 models sharing those nine group horizontal values), with real full modulo20 constraints and proper support completions. It does NOT force any S095 CLM-0333/0334/0335 trigger in an arbitrary remaining case with at most five flat q groups. The scalar q flat count and actual total identity (1) do not alone determine the same SIX singleton X_l/Y_l lifts, four genuinely coupled Fano x_0,x_12,x_13,x_23 with C/Delta, or ANY of the 22 actual non-q pair endpoint shifts. The required shared seven-channel contradiction has not been derived.

We have not classified the remaining twelve q-group values subject to ALL 2046 proper grouped gate constraints, let alone the separate 2048 genuine ungrouped outsider/Fano residuals. Actual q P_q/I/alpha E(U*\I), arbitrary non-q signed multi-splits, FULL8/exact12/13+ split-mask alternatives, 26 hubs, alternate P26, arbitrary U22 and unrestricted 59-original configurations remain OPEN. No D(C20^3)=58 theorem, G58 zero-sumfree sequence or new certified counterexample is claimed. Phase1 HOLD, CAM-0001 BLOCKED; no new source/frontier entries.

**Missing mathematical bridge for S098:** impose the SAME real twelve q group values and all q matching gates on the at-most-five flat class, and prove a physical Fano/endpoint incompatibility or literal proper original zero from their joint values and G20 carries. Neither a mod5-only projection nor free independently chosen Fano corners suffice.

## 6. Hostile evidence coverage matrix

| Obligation | S097 proved | Limit |
|---|---|---|
| Original q indices, total carries | 8 g + S + three actual two-singleton V; sum (4,4,8) mod20 | Conditional S060 axial U* |
| Exact proper grouped q gates | (2) for each of 2046 possible even proper J; true original pair completions | Not full arbitrary twelve-q feasibility |
| Flat six | z exactly 1 or11 in G20, all six share projected half-value | Use S092 to exclude six |
| Flat eight | Explicit proper original E(U*) zero | Standalone q gate |
| Flat seven | Every other q group horizontal 2 or12 on some axis | Conditional antecedent; seven impossible with S092 |
| S096 physical assignment | 20-index and 4-index additional p000 zeros | Partial-gated nonminimal model |
| Fano/2048/multisplits/26 hubs/FULL8/exact12/13+ | Not solved | OPEN |
| Arbitrary U22/P26/G59, G58, D20 | Not solved | NO CLAIM |
| Evidence class | Hand proof INTERNAL SAME_EXECUTOR; no search | Not independent/formal certification |
