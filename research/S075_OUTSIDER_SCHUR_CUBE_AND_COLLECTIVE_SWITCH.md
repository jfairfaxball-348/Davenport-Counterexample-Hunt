# S075 — original outsider additive cubes and mixed signed Fano-fibre constraints

15 October 2026. Exactly S075, from independently read GitHub main \`5689584fed22fcd140f84dafbcd25f2dd87b8b8c\` with true root tree \`b6b4691fe039f1220eaee5a417e2cddb63321280\`. INTERNAL symbolic Phase1 research. No numerical search, CAS/SAT/ILP, generated orbits/candidates, Lean/Palomar, arXiv, outreach, or source proof promotion. ALL statements about T59 are conditional on the previous SOURCE-CONDITIONAL canonical original C20³ configuration, not independent evidence such a full S060-gated model exists.

## 1. Original 59-index setting and what is being attacked

Let G=(Z/20)^3, H=(Z/10)^3, iota:H→2G, h↦2h; lambda:H→C5³ and Q=F2³. G is NOT Q⊕H. The 59 ORIGINAL indices are 22 actual labelled pairs (a_i,b_i), eight actual g outsiders sharing nonzero parity q, and seven original singleton positions s_r in every nonzero parity r. Let u_i=iota^-1(a_i+b_i) and U=(u_i) an indexed H-zero-sumfree 22-term sequence. Let Sigma(V) include the empty indexed subset and E(V)=H\(-Sigma(V)). The S060 original q-only gate states that every nonempty proper original subset splitting only q-parity original pairs must have NONZERO full G sum.

For an ACTUAL mixed non-q-mask torsion witness Z with split mask P, S074's signed Fano switch bases tau_eps(Z) come from the SAME six original singletons for eps=000,110,101,011. The signed full-pair increments w_i(Z) equal +u_i or -u_i at unsplit original pair indices, and actual endpoint differences iota^-1(b_i−a_i) or its negative at split indices; these differences are NOT unconditionally 5Q. The exact fibre K_eps(Z)=(tau_eps(Z)+Sigma((w_i(Z))))∩5Q satisfies, under the S064 exact12 and S072 no-Fano affine alternative, K_eps(Z)⊆{5e:e∈L,chi(e)=1}, dim(L)=2. Consequently chi=0 makes K empty, and chi≠0 allows at most TWO distinct points per slice. The key missing bridge is FORCE OCCUPANCY of a real fibre or create a literal true original zero.

## 2. CLM-0263 — exact zero-free length-22 core with a MISSING projected layer

Let e1,e2,e3 be the coordinate basis of H=C10³ and consider the indexed 22-term sequence

    U = e1^9 e2^9 e3^3 (e1+5e3).                         (75.1)

Every subset sum is uniquely of the shape (k+t)e1 + l e2 + (m+5t)e3, for k,l in {0,...,9}, m in {0,...,3}, and t∈{0,1} indicating whether the special LAST original H term is included. If t=1, its third H coordinate is one of 5,6,7,8, never 0 modulo10. If t=0, sum0 forces m=0, l=0, k=0, the EMPTY subset. Therefore U is rigorously H-zero-sumfree.

For each fixed t, k and l independently traverse all of C10; hence exactly

    Sigma(U) = C10 e1 + C10 e2 + {0,1,2,3,5,6,7,8} e3,
    E(U)     = C10 e1 + C10 e2 + {1,6} e3.               (75.2)

Here the second identity uses E=H\(-Sigma), so the two missing negatives are 1 and 6. Under lambda to C5³, Sigma(U) has third coordinate only 0,1,2,3, missing layer4. The projected terms nevertheless span ALL of C5³. Deleting any terms cannot ADD the missing layer. This is an explicit self-contained mathematical disproof of a proposed blanket assertion 'every length22 H-zero-free U saturates projected C5³', including after any ≤2 indexed deletions. No actual 59-labelled S060-gated model is supplied by this U.

## 3. CLM-0264 — ORIGINAL outsider Schur triple and the eight-outsider four-pair cube

**Theorem.** If a canonical ORIGINAL 59-index T passes the S060 q-only no-zero gate, then ANY four distinct actual q-parity outsider indices g1,g2,g3,g4 satisfy, with true H shifts

    b12=iota^-1(g1+g2),  b34=iota^-1(g3+g4),
    b12 ∈ E(U), b34 ∈ E(U), b12+b34 ∈ E(U).             (75.3)

**Proof.** The SAME q parity makes each selected two-g sum even, so the indicated iota inverse is defined and additive. Any subset of complete ORIGINAL pairs has full G sum iota(sum_B u_i). Select (a) original g1,g2; (b) g3,g4; (c) all four original g, optionally along with ANY subset of the 22 original complete pair indices. Every such literal original subset is NONEMPTY and PROPER because at least the seven singleton originals are omitted. If b12 or b34 or b12+b34 were in −Sigma(U), a choice of original complete indexed pairs would cancel the indicated original g selection to give a FORBIDDEN proper full G zero sum. Thus all three belong to E(U). Note the FOUR g choice is literally disjoint union of the first two pairs, so their H values add: this is not the forbidden artificial G=Q⊕H splitting. QED.

More strongly partition all EIGHT original g labels into FOUR fixed disjoint original pairs, let b_j=iota^-1(g_{2j−1}+g_{2j}) for j=1..4. Every NONEMPTY indexed subset sum Σ_{j∈J}b_j (all 15 nonempty J⊆[4]) must lie in E(U), by the same genuine original subset construction. The resulting 15 values are NOT asserted distinct. This is the mandatory *original eight-g subset-sum cube*.

In particular E(U) CANNOT be sum-free, because (75.3) supplies a TRUE x,y,x+y in E(U). Nor can the projection lambda(E(U)) lie wholly in any nonzero affine linear level {v:f(v)=c} of C5³ where f linear and c∈F5 is NONZERO: its three actual points would have values c,c,2c, impossible. This statement is a genuine restriction on every fully S060 q-only-gated original model, not merely an abstract colouring of an independently chosen extension set.

**Exclusion of the non-saturating core (75.1).** Equation (75.2) puts lambda(E(U)) entirely in the NONZERO third-coordinate layer v3=1. This contradicts the just-proved compulsory original b12,b34,b12+b34 triple (1+1=2, not 1). Thus there is NO FULL original S060 q-only-passing T59 whose 22 original complete pair sums are U of (75.1), irrespective of actual eight g values, singleton values, q-pair multi-splits and Fano C/Delta. This is a positive structural elimination of an explicit projected nonsaturating zero-free escape core, NOT a proof all other nonsaturating cores are excluded.

## 4. CLM-0265 — true signed equal-projection exchange restriction at an OCCUPIED Fano fibre

Fix a genuine torsion mixed-mask ORIGINAL Z, actual even Fano eps and actual B⊆[22] for which tau_eps(Z)+Σ_{i∈B}w_i(Z)=5e∈K_eps(Z). Let i∈B, j∉B and lambda(w_i(Z))=lambda(w_j(Z)). Then w_j−w_i∈5Q; write w_j−w_i=5d for its unique d∈Q. Replace B by B'=(B\{i})∪{j}: this changes ONLY two ORIGINAL full-pair toggle index sets in the S074 literal symmetric-difference construction. The resulting original switched subset is still nonempty proper (mixed mask P remains split), has the SAME reversed singleton status, and has H increment 5(e+d). Therefore BOTH e and e+d must lie in L and satisfy chi=1 by S074. Necessarily

    d ∈ L ∩ ker(chi).                                  (75.4)

If chi≠0 the allowed intersection is a ONE-dimensional subspace (two points). Thus at ANY occupied fibre B every genuine equal-projection selected/unselected exchange must have d=0 or lie in ONE common nonzero torsion direction. An exchange outside this line, or two independent exchange differences, disproves the particular occupied original fibre. This is an original-index necessary restriction, with arbitrary real signed split-pair w retained. It does NOT create an occupied B or refute all exact12 configurations.

## 5. CLM-0266 — collective 9-fold ORIGINAL order-two return with no individual order-two pair sums

Suppose NINE original pair indices that are UNSPLIT in a true torsion witness Z all have the SAME order10 H pair sum u. Each of their S074 signed increments is ±u, since each original pair is either fully selected or absent in Z. If r of nine are −u, their indexed subset sums yield every consecutive multiple −ru, (1−r)u,...,(9−r)u: choose a positive terms and b negative terms; a−b runs through the whole interval. The ten consecutive residues are all of 〈u〉≅C10. Hence Σ of the true signed original pair increments contains the FULL cyclic subgroup 〈u〉, not merely one 5Q colour.

Independently, among nine actual unsplit original full pairs at least FIVE are identically fully selected or identically absent in Z. Toggling precisely those five original full pairs preserves the mixed split mask and every singleton status, and shifts the original G sum by iota(±5u)=iota(5u)∈10Q, a NONZERO original order-two increment. This is a **collective** original witness stabiliser even though each individual u has order TEN rather than TWO. For any actual torsion witness at mask P, it produces another same-mask same-status torsion witness at colour translated by e_u∈Q with 5e_u=5u.

If TWO disjoint unsplit nine-fold blocks have independent order10 H values u,v, their signed indexed subset sums contain 〈u,v〉≅C10². Thus every nonempty signed Fano slice K_eps(Z) contains all four distinct translates by {0,5u,5v,5(u+v)}⊂5Q; it therefore contradicts S074's 0-or-2-point no-Fano exact12 bound. Further, if exact12 holds, original collective torsion toggles put independent directions e_u,e_v inside its common plane L and S072's affine no-Fano singleton status uniqueness forces chi(e_u)=chi(e_v)=0, hence chi=0. This alone does NOT force slice occupancy; the all-empty escape remains. It is wrong to assume two nine-blocks must exist, or lie outside an arbitrary actual P.

## 6. Hostile self-review

1. The U of (75.1) is an H-only ZERO-FREE sequence, NOT a labelled original G59 model. In fact the S060 q-only four-g test rigorously REJECTS it, so it cannot refute universal projected saturation under *all* genuine original S060 gates.
2. (75.3) uses exactly four original g positions of SAME nonzero q parity, and complete original indexed pairs; each selected union is proper regardless of hidden H pair duplications. Four-pair subset sums need not be distinct. No unverified C/Delta or external D2 historical theorem is used.
3. Sum-free E(U) exclusion is necessary, not sufficient, for q-only S060 passing; no full converse and no global classification of E(U) is established.
4. Signed exchange requires an already OCCUPIED mod5-zero original fibre B, with exact signed w_i from selected real endpoints. A duplicate projected pair increment is not an automatic collision, and equal projection does not mean w_i themselves belong to 5Q.
5. Collective five-full-pair toggling is at nine UNSPLIT indices and uses majority sign pigeonhole; if a pair is split the increment changes and proof fails. Two independent nine-blocks are rare conditions, not forced in arbitrary U22. No new global D(C20³) theorem.
6. Four SAME signed tau_eps retain S074 C/Delta; no independently selected Fano lines. Original full majority carry, S060 q multi-splits E(U\I), 2048 outsider transversals, all 26 q hubs, FULL8/exact12/13+/P26 and all non-q masks still require their original constraints. A necessary four-outsider additive cube is not a full signed-fibre 5Q proof.
7. No fully S060-gated original 59-label model, non-q full original zero, G58 zero-free sequence, D(C20³)=58 or rank-three Davenport proof/refutation was obtained. No numeric mathematical search, formal certification, source promotion, or external review. CI absent is ABSENT_NOT_PASS.

## 7. Honest S075 outcome

CLM-0263 disproves blanket projected saturation at the critical H-zero-free U22 length; CLM-0264 goes decisively beyond that negative point and excludes the SAME concrete U from the actual ORIGINAL S060 constraints using only four of the eight outsider indices. CLM-0265 and CLM-0266 introduce signed-fibre restrictions driven by the SAME original pair data, conditional on an occupied fibre and disjoint unsplit repetitions. The still missing mathematical bridge: show that EVERY globally S060-compatible true U22 / witness Z forces a nonempty forbidden signed Fano fibre, or a true projected-zero Fano majority with even parity, or another genuine proper original zero. No such global conclusion follows from these proofs. Phase1 IN_PROGRESS.
