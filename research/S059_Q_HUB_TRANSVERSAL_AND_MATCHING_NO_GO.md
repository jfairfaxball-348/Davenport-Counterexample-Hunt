# S059 — The q-hub maximal-matching saturation theorem and an actual original-index hostile model

14 October 2026. Exactly one extended Phase-1 SYMBOLIC research session, confined to the hypothetical C20^3 T59 original-index bridge. The session does **not** prove D(C20^3)=58, construct a zero-sumfree length58 original sequence, or exclude every U22. All claims are INTERNAL symbolic deductions, not independently certified. The maximum-length H=C10^3 designation uses SOURCE_STATED SRC-0023 D(H)=28; the direct atom constructions and equivalences below do NOT use SRC-0015 D_3(C5^3)=25.

## 1. New universally valid q-direction grouping (CLM-0219)

Set G=C20^3, Q=G/2G=F2^3, H=C10^3 and iota:H→2G, h↦2h. Work with the **conditional canonical** T59 profile: 22 original parity-zero pairs (a_i,b_i), eight original g_j of one common NONZERO parity q∈Q, and the seven original s_r with parity r at every nonzero r∈Q. These are 59 distinct original *positions*; coincident values are allowed. The T sum is zero; T minimality is assumed only for implication to atoms.

Partition the seven Fano positions canonically, using q, into the four DISJOINT indexed groups
P_0={s_q}, P_1={s_r,s_{r+q}}, P_2={s_t,s_{t+q}}, P_3={s_u,s_{u+q}},
where {r,r+q}, {t,t+q}, {u,u+q} are the three nonzero cosets of the line <q> in Q. EACH P_l has quotient parity q, since r+(r+q)=q. With the eight g singletons these are **TWELVE disjoint q-parity original-index supervertices**. No G→Q splitting has been used; each vertex has its ACTUAL sum in G.

More generally choose any m of the 22 original pairs whose common member parity t_i equals q, leave the other 22−m pairs intact, and SPLIT each chosen pair into its two distinct q-parity ORIGINAL members. The resulting number of q-parity supervertices is N=12+2m. For every perfect matching M of these N vertices, form N/2 indexed H edge values
h_ab=iota^{-1}(value(P_a)+value(P_b)).
These edge blocks are disjoint sets of ORIGINAL G positions and partition all q-vertices. Together with the 22−m unbroken H pair blocks they partition ALL T into (22−m)+(N/2)=28 nonempty parity-zero indexed blocks. If T is minimally zero-sum, the induced 28-term H sequence is minimally zero-sum. If SOURCE_STATED D(H)=28 is accepted, it is extremal.

There are (N−1)!! distinct labelled perfect matchings; this is an elementary pairing count and emphatically NOT a count of independent value restrictions. At m=0 there are 11!!=10,395 matching partitions, beyond the old g-only 105 matching configurations per Fano line. At m=1 there are 13!!=135,135.

For any chosen q-hub pseudo-vertex v_1, define d_j=iota^{-1}(v_j−v_1) in H, since all vertex parities equal q, and let w=v_1 mod10. Every H edge has the exact coupled form h_jk=w+d_j+d_k, extending S056's eight-original-g edge-potential identity to these **disjoint original-index superblocks**. When vertices are regrouped or changed, the superblock identities must be rebuilt; never reuse an edge from overlapping decompositions as if its original indices were disjoint.

### Exact matching-atom equivalence, not independence

Let U^(m) be the H sequence of the 22−m UNSPLIT pair values, assume the total T sum is zero, and write v(J)=iota^{-1}(sum of all q-hub supervertices with labels in J) for each EVEN-cardinality J⊆[N]. This value is well-defined in H. For any H sequence V let E(V)=H\{-sum(V_I):I⊆indexed V}, including the empty subset.

Then the following statements are EQUIVALENT:

(A) Every perfect matching of the N supervertices, together with the unsplit pairs, gives an indexed **minimally zero-sum** H sequence of length28.

(B) U^(m) is zero-sumfree in H and **every nonempty proper EVEN-cardinality** subset J of the q-hub supervertices satisfies v(J)∈E(U^(m)).

Proof (A⇒B): Unbroken U^(m) alone is zero-free because it is a proper block subcollection. For a nonempty proper even J choose a matching pairing vertices WITHIN J and WITHIN its complement (both have even size). Those edge blocks are a proper nonempty part of the resulting H atom. If v(J) were the negative sum of some unsplit U subset, its union with those J edge blocks would be a proper H zero-sum subcollection: contradiction.

Proof (B⇒A): Fix any matching and a nonempty subset of its 28 blocks, using a subset I of unsplit pair blocks and a subset J of its matched q vertices. J has even size. If 0<|J|<N, condition (B) rules out zero sum. If J=∅, zero-freeness of U^(m) rules out nonempty I. If J=[N], the total T sum gives v(J)=−sum U^(m); hence the partial sum is −sum(U^(m)\I), zero only when I contains ALL unsplit blocks. This is the full 28-block sequence, permitted. Thus the H sequence is a minimal atom. QED.

This equivalence assumes NO independence among the (N−1)!! matching partitions; one complete family merely tests the indicated even-index subsets of a single q-hub supervertex representation.

For m=0, exactly 2^11=2,048 q-hub supervertex selections have even cardinality, including empty and full; **2,046** are genuine E(U22) tests. The FULL original 15-outsider parity-zero fibre has 4,096 selections, with empty/full excluded to leave 4,094 proper tests (S053). Therefore **2,048 original proper outsider parity-zero subsets CUT one or more of the three singleton q-pairs and are not represented at all by this fixed q-hub matching family**. This is an exact partition of LABELLED subsets, not independent H values, and it does not encompass pair splits. Of the seven Fano lines, three contain q and correspond to unions of q-pseudo pairs; the four Fano lines avoiding q meet EACH of the three {r,r+q} q-pairs in exactly one selected singleton and are transversal. Hence 4×105=420 of the old 735 line/cap×g-matching partitions are NOT represented by the fixed q-hub family; the other 3×105=315 are. Additional q-hub matchings yield many mixed odd-g tests omitted by the old g-only family.

### Lift freedom: four singleton q-vertices are not independent Fano obstructions

Conversely, any prescribed values V_0,V_1,V_2,V_3∈G all with parity q can be realised as sums of these four q-pseudo singleton groups: set s_q=V_0; choose each s_r arbitrarily with its named parity r, and take s_{r+q}=V_l−s_r for the corresponding coset. Its parity is q+r, as required. Thus the q-hub pseudo-value matching equations alone impose NO extra relation between V_0,...,V_3 beyond their common parity. The four transverse Fano lines depend on the individual chosen s_r and are precisely where the individual original indices re-enter.

## 2. Explicit 59-original-position hostile countermodel (CLM-0220)

The following is an **actual G=C20^3 zero-sum 59-index collection**, with every original pair parity nonzero and with ALL q-hub matching H28 sequences minimal, which nevertheless has a proper original G zero-sum subset. This refutes any argument claiming the (N−1)!! atom equalities/edge potentials and t_i≠0 by themselves prove a contradiction. It is NOT a minimally zero-sum T59 or a zero-sumfree G58 counterexample.

Let e1,e2,e3 be standard basis elements of G=C20^3, and use the same symbols for the standard basis of H=C10^3 when referring to H. Set q=π_G(e3). For any m∈{0,1,2,3}, make m of the 22 original pair blocks equal to the ORIGINAL pair (e3,e3). The remaining 22−m pairs are assigned H kernel sums
U^(m)=e1^9 e2^9 e3^(3−m) (e1+e2+e3).
For each of these unsplit pair blocks of H sum u choose ORIGINAL a=e1 and b=2u−e1 in G. Both original members have nonzero parity π_G(e1), while the pair sum is iota(u). The m split pairs have nonzero member parity q. There are 22 original pairs, all 44 positions distinct as labels even where values repeat.

Take all eight original g_j=e3. Take seven singleton values, with their indicated original Q parities:
s_e3=e3,
s_e1=−e1, s_(e1+e3)=e3+e1,
s_e2=e2, s_(e2+e3)=e3−e2,
s_(e1+e2)=e1+e2, s_(e1+e2+e3)=e3−e1−e2.
Each of the three q-coset PAIRS sums to e3, as does s_q. The 8 g originals and 4 singleton q-superblocks therefore supply twelve q vertices, ALL with actual G value e3. Add the 2m split original members, each e3, to obtain N=12+2m q-hub vertices ALL with value e3. Every possible matching edge has original G sum 2e3=iota(e3), so every matching produces the SAME 28-term H sequence by value:
U^(m) e3^(6+m) = e1^9 e2^9 e3^9 (e1+e2+e3).

This 28-term H sequence is indeed MINIMALLY zero-sum, by an elementary argument independent of the historical D(H) bound. A zero-sum subset omitting the diagonal term must select 0 or 10 copies of EACH ei; at most9 are available, so it must be empty. A zero-sum subset containing the diagonal must select exactly9 copies of EACH ei, and so is the WHOLE 28-term sequence. This proves all (11+2m)!! matching partitions simultaneously yield actual indexed H atoms with exact matching edge-potential compatibility.

The 59-term G original collection has TOTAL ZERO: the unsplit pair sums yield iota((4−m)e3) because 9e1+9e2+e1+e2 vanish modulo10; all N q-hub values sum to (12+2m)e3=iota((6+m)e3), totalling iota(10e3)=0.

But the ORIGINAL Fano line L={e1,e2,e1+e2} has three singleton values adding to 2e2∈G. Combine those THREE singleton original positions with the NINE UNSPLIT original pairs whose H sums are e2; the sum is 2e2+9·2e2=20e2=0 in G. This proper indexed zero subset occupies exactly 3+18=21 original positions. Even more directly, one ORIGINAL member a=e1 of a pair and the original singleton s_e1=−e1 sum to zero. These subsets are absent from the fully grouped q-hub matching tests, which never cut a singleton q-coset PAIR or an unsplit pair.

This model is a decisive **no-go for the specific proposed inference**: an arbitrary huge number of coherent simultaneous, source-independently proved H28 matching atoms, coupled edge potentials, correct q≠0 and all t_i≠0, do NOT force the original T to be minimal or give an impossibility theorem. It is NOT a no-go for a theorem using the remaining transversal outsider and split-pair conditions. In particular it does not realise all 735 original Fano line/cap atoms; the exhibited L already fails, and no such claim is made.

## 3. Sustained attempts at the decisive bridge; actual boundary

**Route A: exhaustively strengthen matching switches.** In place of eight g originals only, incorporate the unique canonical four q-singleton superblocks and m eligible split original q-pairs. This gives a globally coupled N-vertex additive-potential family, (N−1)!! maximal H atom partitions, and many genuine original mixed odd-g tests. Apply S058 CLM-0216 symbolically to any quartet of these supervertices: fixing a matching of the other N−4 vertices gives 26 common H positions, and (conditionally on SOURCE_STATED D_3(C5³)=25) the identical common-25-position three-block binary basis and three complement-pair projected atoms. At m=0 there are binom(12,4)·7!!=51,975 labelled quartet matching TRIADS. These do not give independent bases across unrelated triads. The constructed model passes ALL such matching configurations, proving that no contradiction can follow from universal matching-saturation and S058's necessary consequences ALONE.

**Route B: transversals that break the q-pairs.** Exactly 2,048 proper original outsider parity-zero choices are excluded from the q-hub index algebra, including four Fano lines avoiding q. Their individual singleton values s_r matter even after the four grouped q-vertex sums have been fixed. In the explicit model one such line yields an ACTUAL 21-index G zero sum, so the original-index transversal constraints decisively distinguish valid and invalid candidates. But this model supplies NO proof that every possible arbitrary U22 and arbitrary singleton lift must fail one such transversal. The earlier S052 mod2 tensor and S057 exact Fano lift show why asserting independent Fano line values is unsound. Prior S050 excludes one slab family, not arbitrary U22.

**Route C: split-pair transport.** For any selected m with t_i=q, its original member values can be included as disjoint q vertices and all mixed perfect matchings remain extremal. For m up to3 the explicit example still passes the entire enlarged family, while failing original transversal/split conditions. Thus t_i=q cannot be ruled out from perfect-matching compatibility alone. For other t_i, or multi-splits involving differing parities, there is no claimed complete construction or exclusion. The genuine S055/S056 4,096 one-sided tests per pair and all |I|≥2 must still be checked, and exact E(U\I) rather than E(U) must be used.

**Route D: projection/extension inverse.** The S058 common 25-block basis and C≤11 three-switch projected atoms remain correct conditional statements. Our model even supplies all required 28-term H atoms (so every necessary projected consequence holds whenever SOURCE_STATED D_3 is invoked), but original mixed cuts invalidate the T assumption. Attempting to force contradiction solely from 51,975 necessary common-basis triads is therefore logically impossible: this example satisfies their H-atom premises. One must deduce a restriction using FULL original-index overlap across the q-coset singleton pairs, and likely U one/multi-splits. No P11 actual affine-span inverse or universal transport lemma was proved.

## 4. Exact unresolved mathematical bridge

For **arbitrary** allowed U22, eight g values of common nonzero q, seven coherently lifted singleton original values, all 22 original nonzero-parity pairs, and all surviving noncanonical quotient configurations, no verified universal contradiction has been derived. Even the reduced **canonical q-hub-plus-transversal** statement remains unproved:

> Under total-zero and q≠0, t_i≠0, does q-hub matching-atom compatibility for every q-member pair split, together with the 2,048 q-transversal original outsider E(U22) tests and the 4,096 original one-sided tests for each i (plus higher pair splits), force a proper original zero sum for EVERY assignment of original group values?

This is posed as an OPEN task, not a new theorem or equivalent solved problem. A sharper proof route would show that universal q-hub compatibility forces K(W,U) into a proper affine parity coset while the four transversals demand the S052 full binary tensor, or else directly construct a mixed original zero sum from the shared projected bases. Neither implication follows from the present evidence. Universal coverage of three-hub, (0,4),(0,6),(1,7) profiles remains outstanding even if this conditional canonical profile were resolved.

## 5. Reverse audit / source integrity

- All constructed singleton groups are disjoint ORIGINAL index blocks. They become indivisible ONLY for the matching-family subproblem; treating them as indivisible when claiming full T minimality is precisely the invalid step exposed by the countermodel.
- A matching H edge iota inverse exists because its two vertices have equal NONZERO q. There is no nonexistent G=C2^3⊕C10^3 splitting or illicit division of one odd-parity G term by 2.
- The 28 H atoms are proved directly, not postulated or numerically searched. The historic D(H)=28 is needed only to call these atoms maximal relative to the Davenport constant, and remains SOURCE_STATED.
- The conditional CLM-0216 extension uses SOURCE_STATED SRC-0015 D_3(C5³)=25; it is NOT an independently verified computational theorem.
- The (N−1)!! matching count, 2,048 versus 4,096 index-fibre count, and 3-versus-4 Fano line count are closed formulas; not mathematical numerical search, enumeration, SAT/ILP or generation of zero-free counterexample candidates.
- The constructed G T59 collection contains an explicit proper 21-position zero sum and explicit two-position zero sum; it is deliberately a COUNTERMODEL TO AN INFERENCE, not a new Davenport counterexample.
- The 12-hub subgroup alone does not include the 420 non-q original Fano partitions; no false claim that ALL 735 simultaneous atoms have been realized.
- SOURCE_STATED SRC-0008/0015/0023 statuses unchanged; original 30 frontier rows and 28 source objects untouched, no D20 equality, candidate, source promotion, external review, Lean or Palomar.
