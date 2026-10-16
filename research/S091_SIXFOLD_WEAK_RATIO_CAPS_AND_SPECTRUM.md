# S091 — exclusion of weak-only and high 3/4 outsider spectra in genuine axial sixfold

16 October 2026. **INTERNAL SAME_EXECUTOR, conditional hand mathematics only.** Entry original remote main \`062a33c976c7fc2e5c4b60d497419bf25dc4c0c2\`, true Git root tree \`a270f3b82bca0543288e04ecfec7c48c2297f395\`. S090 authored commit \`37b0668648727e0ac9d5ad284ae541c3861a13cb\` has sole parent \`8a927ce00b0b9e264f5429fb239baaa36bfc6b58\`; genuine ordinary S090 merge has exactly those two commits as second and first parents respectively. No numerical mathematical search, orbit enumeration, CAS/SAT/ILP, generated model, Lean, Palomar, new campaign, independent certification, source upgrade or publication.

## 1. Real original-index hypotheses (not a projection survivor)

Assume the same **59 individually indexed G=(Z/20)^3 original positions** conditional on S060/S081–S090, including the 22 labelled complete pairs U*=e1^8 e2^8 e3^6, eight actual g positions, s_q and the SAME six X_i,Y_i originals forming three actual disjoint paired V_i. The twelve actual disjoint q-supervertices have projected half-value total (2,2,4) in F5^3. Six actual q groups have common projected half-value (v,3), v=(a,b)!=(0,0), and six actual outsider groups have projections (e_i v+w_i,3e_i). Thus
\[
\sum_{i=1}^6e_i=2,\quad\sum_{i=1}^6w_i=W=(2,2)-3v.
\]
Put c=1−3a, d=1−3b, C0={x=1 or y=1}, C4={x=c or y=d}, P=C0∩C4. When ab!=0, P={A=(1,d),B=(c,1)} and W=A+B, with A!=B. On an axis P is respectively the entire x=1 or y=1 line.

Every **nonempty proper** outsider J of size at most five has the exact S089/S090 available original-index projected gates:
- even |J|: e_J!=2 implies w_J∈C0; e_J!=0 implies w_J∈C4;
- odd |J|: e_J∉{1,3} implies w_J∈C0; e_J∉{1,4} implies w_J∈C4.

In particular e4 singletons lie C0, e3 singletons C4; pairs of e4/e3 lie P; e4 triples (sum e=2) lie P, e3 triples (sum e=4) lie C0; e1+e3 pairs (sum e=4) lie P and e1+e3+e3 triples (sum e=2) lie P. Any failed gate truly lifts to a nonempty PROPER original G zero: select its actually labelled q originals and the genuinely available repeated q groups for the third cancellation, then BOTH endpoints of k_l=(-h_l mod10) labelled full U* pairs, with bounds k1<=8,k2<=8,k3<=6. At least one of twelve q groups is omitted. No all-six-outsider/FULL12 test is used. These gates are NECESSARY, never sufficient for an original-index survivor.

## 2. CLM-0319 — no THREE e4 outsiders, for every nonzero v

Take any three labels with e=4. Their three pair sums are in P (e-pair sum3), their full triple residual is in P (e-triple sum2), and EACH singleton is in C0.

On an axis P has one prescribed coordinate1. All three pair sums equal1 in that coordinate, hence all three individual coordinates equal3 (2*3=1 mod5). Their triple coordinate is 9=4, not1. Contradiction.

For ab!=0 write each pair sum as A or B. If m of the three pair sums are B, then, because every original label occurs in exactly two pairs, the triple sum is
\[
3((3-m)A+mB)=
\begin{cases}
4A&(m=0),\\
A+3B&(m=1),\\
3A+B&(m=2),\\
4B&(m=3).
\end{cases}
\]
Elementary coordinate equality with A or B allows ONLY: v=(4,4) for m=0 or3; v=(3,1) for m=1; v=(1,3) for m=2. Indeed 4A=B or 4B=A forces c=d=4; A+3B=B forces A+2B=0, equivalently c=2,d=3; 3A+B=A forces 2A+B=0, equivalently c=3,d=2. All other supposed equalities require nonzero A or B to vanish.

At v=(3,1), B=2A. Exactly one pair must sum B, two sum A. Inverting the three pair equations gives individual residuals A,A,0 up to permutation. But the actual e4 singleton with residual 0 lies outside C0. v=(1,3) is the horizontal-coordinate swap. At v=(4,4), B=−A, and the only admissible m values force all three pair sums identical, giving individual residuals 3A or 3B. Here A=(1,4) and B=(4,1), so these are (3,2) or (2,3), neither in C0. Contradiction in all cases. Therefore n4<=2 (not an all12 statement).

## 3. CLM-0320 — no FOUR e3 outsiders, for every nonzero v

Select four actual labels of type e3. All their pairs sum into P; all their triples sum into C0; and their four singletons lie C4. The two remaining outsider e-values have sum0 because 4*3=2 mod5, so up to order their ratios are (0,0), (1,4), or (2,3).

**Axis.** Let a=0,b!=0, so P is x=1 and W_x=2 (the symmetric axis swaps coordinates). All four e3 x-coordinates equal3 by their pair gates. Every three-e3 residual has x=9=4, so its true C0 triple gate demands that its y-sum equal1. Comparing the four triples forces the four y-coordinates equal; 3y=1 implies y=2. Thus the four actual residuals are u=(3,2), with x-total2 and the remaining two must have x-sum0. If their ratios are (0,0), both strong residuals have x=1, sum2!=0. If (2,3), the strong e2 residual has x=1 and the fifth e3 has x=3 by its pair gate with u, sum4!=0. If (1,4), the e1 residual has x=3 by its mixed e1+e3 pair gate, but its genuine e1+e3+e3 triple residual has x=3+2*3=4, outside P. All impossible.

**Off-axis pair geometry.** For four w labels with every pair sum in {A,B}, either all four are the same u=3A (or, symmetrically, 3B), or three are u=3A and the fourth is z=B−3A (or swap A/B). Proof: if every pair has the same value A, all labels equal3A. Otherwise choose a triangle with two A-coloured and one B-coloured edges. The two vertices on the B edge coincide at 3B and the other equals A−3B. A fourth vertex must pair into {A,B} with both equal vertices, so it is either 3B or A−3B. The latter would pair with the exceptional vertex to give 2A−B, neither A nor B, since A!=B. Hence it is 3B. This classifies ALL four labels (and also covers a triangle with all one colour and an exceptional fourth).

Take the orientation with u=3A. An all-u e3 triple has residual 3u=4A=(4,4d), which must lie C0, forcing d=4. The actual e3 singleton u=(3,3d) must lie C4, forcing c=3 (because d!=0). Thus v=(1,4), A=(1,4), B=(3,1), u=(3,2), z=B−3A=(0,4), and W=(4,0). The opposite A/B orientation is the coordinate-swapped v=(4,1).

If the four e3 residuals are u,u,u,u, their sum is (2,3), so the remaining residual sum R=(2,2). If they are u,u,u,z, their sum equals W, so R=0. In both cases:
- ratios (0,0): both residuals belong to {A,B}; their possible sums are 2A=(2,3), A+B=(4,0), 2B=(1,2), neither R=(2,2) nor R=0;
- ratios (1,4): the e1 residual t, by its pair gate with u, belongs to {A−u=u, B−u=z}. But its true e1+two-u triple must lie P; t+2u is (4,1) or (1,3), neither in P={A,B};
- ratios (2,3): the e2 singleton s lies in P and the remaining fifth e3 residual t=R−s must, by pairing with u, lie in {u,z}. When R=(2,2), t∈{(1,3),(4,1)}; when R=0, t∈{(4,1),(2,4)}. Neither intersects {u,z}.

All proper original-index gates used involve at most three outsiders, hence none is FULL12. Conclude n3<=3 for every v!=0.

## 4. CLM-0321 — eliminate the entire NO-STRONG spectrum

Let n0=n2=0. By S090 n1<=3; by sections2–3 n4<=2,n3<=3. As n1+n3+n4=6 and n1+3n3+4n4=2 mod5, the only possibility is the multiset **1^3 3^3**: for n1=0 the caps sum to at most five, for n1=1 or2 the available pairs (n3,n4) give residues other than2; for n1=3 only (n3,n4)=(3,0) has residue2. We now EXCLUDE this last case using original proper gates.

Name the three e1 residuals z_i and three e3 residuals u_j. Every cross z_i+u_j lies P. On an axis with P coordinate1, the e3 pairs force all u_j to have that coordinate3 and then cross pairs force all z_i to have it3. The six-residual coordinate total is 6*3=3, contrary to W coordinate2.

Off-axis, the 3×3 cross sums all lie in the TWO-POINT set {A,B}. If two u_j differ, then for every z_i the two cross sums must be the distinct values A and B in a fixed orientation, uniquely determining z_i; so all z_i coincide. Consequently either ALL three e1 z_i coincide, or ALL three e3 u_j coincide.

If all e3 equal u, their pair sum 2u∈P forces u=3A or3B; their triple 3u∈C0 and their singleton u∈C4 together force (c,d)=(3,4) or (4,3), respectively. In the first orientation v=(1,4), u=(3,2), and each e1 z_i by its cross pair belongs to {u,(0,4)}. Its actual odd triple with two different e3 labels has e-total2, hence z_i+2u∈P. But z_i+2u is (4,1) or (1,3), neither A=(1,4) nor B=(3,1). Symmetric contradiction in the other orientation.

If all e1 equal z, let m of the three pair sums among e3 labels equal A, the other 3−m equal B. Writing U=sum u_j and 2U=mA+(3−m)B and W=3z+U gives z=(2−m)A+(m−1)B. For m=0 or3, the three e3 labels are identically 3B or3A, and an actual mixed e1+e3 pair has residual z+u=2(A+B), which belongs P only if A+2B=0 or 2A+B=0, i.e. v=(3,1) or (1,3). For m=1, two e3 labels are 3B and z=A, requiring z+3B=A+3B∈P and hence A+2B=0, v=(3,1). For m=2, two e3 labels are 3A and z=B, forcing 2A+B=0, v=(1,3). At v=(3,1), B=2A: if all e3 pair sums are B, then all u_j=3B=A and their genuine e3 triple is 3A=(3,4), outside C0; if any pair sum is A, at least one e3 singleton is either 3A=(3,4) or 0, both outside C4={x=2 or y=3}. Thus v=(3,1) fails; swap axes for (1,3). No no-strong sixfold outsider multiset exists.

## 5. CLM-0322 — precisely EIGHT generic surviving RATIO multisets, not projections

Away from the THREE exceptional v=(3,1),(1,3),(4,4), S090 also gives n0+n2<=2. Moreover no TWO e2 can coexist here: their real pair has e-sum4 and must have residual in P, but 2A,A+B,2B∉P outside those exceptions (and on an axis the prescribed P-coordinate of that pair would be2, not1). Combining n1<=3, n3<=3, n4<=2, n0+n2∈{1,2}, n2<=1 and the actual totals sum n_i=6,sum i*n_i=2 mod5, hand-checking the at-most-two-strong rows yields exactly these **arithmetically necessary** multisets:
\[
\begin{array}{l|l}
n_0+n_2=1 & 0\,3^3\,4^2;\quad 0\,1^2\,3^2\,4;\quad 2\,1\,3^2\,4^2;\quad 2\,1^3\,3\,4\\
n_0+n_2=2 & 0^2\,1\,3\,4^2;\quad 0^2\,1^3\,4;\quad 0\,2\,1\,3^3;\quad 0\,2\,1^2\,4^2
\end{array}
\]
For transparency, row s=1 follows from n1+n3+n4=5 and the e-total; row s=2 from n1+n3+n4=4 with either 0^2 or 0·2 (the 2^2 option is prohibited by its pair). No numerical search or model generation was used. **NO assertion** that any of these eight multisets admits residuals passing all 62 properly available clauses. At the three exceptional v, n0+n2>2 has not been excluded, so this table is NOT exhaustive there.

## 6. Exact remaining mathematical bridge and nonpromotion

A sharply isolated generic open case is the real e-spectrum 0·3^3·4^2. To exclude it one must show there are no labelled residuals s,u1,u2,u3,t1,t2 with total s+Σu+Σt=W, s∈P, every e3 singleton in C4, every e4 singleton in C0, all three u-pairs and the t-pair in P, every u-triple in C0, each u+t pair in C4, and ALL remaining exact S089 proper singleton/pair/triple clauses on these same labels. This assertion is NOT proved here. The other seven generic spectra and every exceptional-v s>=3 case likewise remain under their genuine 31 representative / 62 paired necessary tests. Thus there is **NO full sixfold no-go**; descending to fivefold is premature.

Even a COMPLETE projected sixfold no-go for axial U* would not close the other q-spectrum cases or the true H=(Z/10)^3 E(U*) on ALL actual proper even supports, four coupled Fano x_eps from SAME six original X/Y and C/Delta, 2048 actual outsider masks, all q-split I/alpha with E(U*\I), signed non-q splits, 26 hubs, FULL8/exact12/13/14/>=15 carries, arbitrary U22 and P26. No fully S060-gated 59-original T, no zero-sumfree G58, NO D(C20^3)=58, NO global rank-three Davenport resolution. 29 original source records and 30 original frontier rows unchanged; Phase1 IN_PROGRESS/HOLD, CAM-0001 BLOCKED, no hosted CI PASS, SAME_EXECUTOR review only.
