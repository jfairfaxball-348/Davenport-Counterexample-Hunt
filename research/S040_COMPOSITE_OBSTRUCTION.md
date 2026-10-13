# S040 — Composite lifting obstruction and attempted central routes

## CLM-0150 — exact one- or two-position failure of bare prime multiwise lifting

For a subgroup H of a finite abelian G, indexed disjoint quotient blocks yield the elementary inequality D(G)<=D_(D(H))(G/H) (proved in S002). To use it at G=C_(pm)^3 and attain the conjectured 3pm-2, a **sufficient** bare-input condition is

D_(3m-2)(C_p^3) <= 3pm-2,

given an exact quotient D(C_m^3)=3m-2. The condition is not necessary for the real Davenport equality.

At p=2, programme-proved CLM-0048 gives the **exact** D_k(C2^3)=2k+3, so the pure subgroup bound equals 6m-1, exactly ONE higher than 6m-2 for every m with k>=2. At p=3, the original BSP2007 **SOURCE_STATED**, not independently classified in this programme, formula D_k(C3^3)=3k+6 (k>=3) makes the pure subgroup bound 9m, TWO higher than 9m-2. The p5 D_k=5k+10 for k>=2 is additionally SOURCE_STATED/Yiu ancillary predicates unauthenticated; it likewise misses by two.

For the five retained original frontier intervals, the exact bare-source arithmetic is:

| n | quotient m, kernel p | k=D(C_m^3) | bare upper D_k(C_p^3) | 3n-2 | bare gap |
|---|---|---|---|---|---|
| 15 | 5,3 | 13 | 3*13+6=45 | 43 | 2 |
| 20 | 10,2 | 28 | 2*28+3=59 | 58 | 1 |
| 21 | 7,3 | 19 | 3*19+6=63 | 61 | 2 |
| 28 | 14,2 | 40 | 2*40+3=83 | 82 | 1 |
| 30 | 10,3 | 28 | 3*28+6=90 | 88 | 2 |

The quotient exact m10,m14 values are original classical SOURCE_STATED frontier facts; the p3 Dk input is SOURCE_STATED. Each row is therefore an implication from precisely labelled premises, not a new original-case exact evaluation. The displayed upper bounds are the SAME five existing historical upper endpoints, and DO NOT alter any frontier row.

**Sharp obstacle.** Even replacing the listed bare Dk estimates by the TRUE EXACT values would not make the bare inequality certify 3n-2, since those Dk values are strictly above the target threshold. This establishes a method-specific insufficiency, NOT that rank-three equality fails or that no stronger theorem is possible. A proof must exploit additional coupled structure beyond mere cardinality of quotient-zero-sum blocks, use a different decomposition, or supply some other argument. For n15 the alternate p5 direction is also two high if the SOURCE_STATED p5 exact multiwise formula is granted.

## Front C — sustained central obstruction attack and falsification

C1 tested whether the -3 margin in CLM-0149 alone supplies the tight condition D_(3m-2)(C_p^3)<=3pm-2. Substitution gives upper 3pm+(p^2-2p-3), exceeding the target by p^2-2p-1 for p>=7. This is positive (p7:34), so the large-prime route CANNOT by itself settle composite equality by one raw subgroup step. A sharper eta numerical bound or short-block count would need to save an order-p^2 offset to close this using only that route.

C2 tested whether a proof could simply replace sharp p2/p3 (and source-stated p5) multiwise bounds by the conjecture-compatible numbers pk+2p-2. At p2 the proven exact value is pk+3>pk+2p-2=pk+2 by 1. At p3 the original SOURCE_STATED exact formula is pk+6>pk+4 by 2; independently authenticating that lower extremal example is still a relevant task. Thus that proposed blanket inequality is ruled out already by an independently proved p2 instance, regardless of the composite conjecture. It is wrong to treat the rank-three conjecture as a direct corollary of such a false prime multiwise assertion.

C3 considered whether grouping quotient zero sums differently, preserving their **decorated H-sums** rather than discarding all combinatorial information, can bypass a 1/2-position deficit. This is a valid new strategy but NOT a theorem here: S002's inequality knows only existence of k arbitrary quotient zero-sum blocks, while a sequence just below sharp D_k may have at most k-1 disjoint such blocks. The original lifts have arbitrary CRT components, so there is no unproved automatic decoration restriction to exploit. Need a genuine theorem guaranteeing a decorated zero sum from the full family of overlapping quotient blocks or a classification/transfer covering its extremal patterns. No such theorem was proved. This is the concrete target for S041, and no claim that all approaches were exhausted is made.

## Hostile validation and scope

Rechecked the line count pR+1 and plane count R using quotient projective spaces; the off-line partition is indexed even for duplicate values, zeros excluded by short-freeness. Crucial strict inequality N>2(pR+1) is (p-7)R+2>0 **at p7**, so the formerly troublesome m<=2 branch is actually impossible. Case m3 uses ceil(1/R)=1, not zero; m4 uses ceil0=0; m>=5 uses ceil((4-m)/R)=0 because m<=p-1<R+4. Property C is used on any 3p-3 **indexed** U-positions, and its repeated value is nonzero, hence lies in one linear line. k=j boundary and postremoval eta threshold were checked separately. Composite examples distinguish exact proven p2 from SOURCE_STATED p3/p5 and prime-power historical premises. No reverse inference D(G)=3n-2 from local Dk and no claim of present-day openness.

One result, CLM-0148, is an alternative proof of a PUBLISHED numerical inequality (not a new eta upper); CLM-0149 is a composition of previously proved programme inputs; CLM-0150 isolates an elementary method gap. Novelty/priority NOT assessed. No mathematical numerical/computational search, candidate, solver, Lean, Palomar, campaign, manuscript, outreach or external contact.
