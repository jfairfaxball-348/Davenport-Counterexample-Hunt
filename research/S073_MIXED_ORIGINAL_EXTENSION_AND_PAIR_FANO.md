# S073 — exact original mixed-mask extension fibres and genuine same-mask Fano differences

15 October 2026. Owner-invoked EXACTLY S073. Internal, same-executor, symbolic Phase 1 mathematics, not an independent certification. The target is the rank-three Davenport conjecture; here the canonical 59-original-position C20^3 case is **source-conditional**. This manuscript neither constructs a full S060-gated 59-position hostile model nor proves D(C20^3)=58, nor exhibits a zero-sumfree 58-position counterexample.

## 1. Original labels, groups and frozen prerequisites

G=(Z/20)^3; H=(Z/10)^3; Q=(F2)^3. Write iota:H→2G, h↦2h; pi:G→Q reduction modulo 2; rho:H→Q reduction modulo 2; lambda:H→(Z/5)^3 reduction modulo 5. Embedded 10Q⊂G and 5Q⊂H are the actual order-two subgroups. **G=Q⊕H is false** and is never assumed.

Work with one hypothetical actual ORIGINAL labelled total-zero T59 consisting of 22 ORIGINAL pairs (a_i,b_i) with common nonzero quotient t_i=pi(a_i)=pi(b_i), 8 individually labelled q-parity g_j, q≠0, and 7 labelled singletons s_r for r∈Q\{0}. Set u_i=iota^{-1}(a_i+b_i)∈H and require the indexed U22=(u_i) to be H-zero-sumfree. Partition indices into P_q={i:t_i=q} and N={i:t_i≠q}. The six singletons other than s_q are the three original q-coset pairs (X_j,Y_j), j=1,2,3, with quotient labels r_j, r_j+q, and [r_3]=[r_1]+[r_2] in Q/<q>. For an ORIGINAL subset Z, M(Z)⊆N is the non-q pair split mask; h(Z)∈F2³ has bit j=1 iff Z selects exactly one member of (X_j,Y_j). The frozen S071 quotient map is Phi(M)=∑_{i∈M}[t_i], R(h)=∑h_j[r_j], so torsion witnesses require Phi(M)=R(h).

Assume *only conditionally* that the exact S060 all-q original no-zero gates have passed: all q-supervertex matching atoms, all q-pair one/multi-splits using true E(U\I), all 2048 labelled outsiders, and the four coupled TRUE Fano values x_000,x_110,x_101,x_011∈S060 F_* obeying original full-H C and Delta equations. NO construction of such globally feasible T is asserted.

A torsion danger D_M^h consists of v∈Q for which some proper nonempty ORIGINAL Z with M(Z)=M, h(Z)=h, sum_G Z=10v exists. Let D_M=∪_h D_M^h. For M≠empty properness is AUTOMATIC because an original pair is split. For M=empty do not silently assume properness; the S060 gate handles the proper-original exception.

## 2. CLM-0258 — exact ALL original mixed-mask mod5/parity extension gate

**Theorem (symbolic exact formula, for every nonempty M⊆N and h∈F2³).** For every q-split mask I⊆P_q choose ONE member alpha_i∈{a_i,b_i} at each index i∈M∪I. Choose an actual labelled outsider subset R_out of the original 8 g plus 7 singletons, and require h(R_out)=h. Put

  c(M,I,alpha,R_out)=∑_{i∈M∪I}alpha_i + ∑_{z∈R_out}z ∈ G;
  J=[22]\(M∪I);
  Sigma(U_J)={∑_{j∈B}u_j : B⊆J}, with original indices retained.

Use ONLY choices with pi(c)=0, so b=iota^{-1}(c)∈H really exists. Define
  A_{M,h}= ⋃_{I,alpha,R_out, pi(c)=0, h(R_out)=h} (b+Sigma(U_J)) ⊆ H.

Then EXACTLY
  D_M^h = {v∈Q : 5v∈A_{M,h}}.                             (73.1)

Equivalently,
  D_M^h = {rho(w) : w∈A_{M,h} and lambda(w)=0}.           (73.2)

If Phi(M)≠R(h), all permitted choices vanish and D_M^h=empty. For each M with admissible h, its other admissible h is h+111, and no other h is possible (S071). Formula (73.1) is NOT a computed feasible instance: it is an exact original-label finite-group identity, with ALL eight g, all seven singleton choices, both members of each split non-q and q pair, unsplit full-pair indexed sums, and true modulo20 arithmetic retained.

**Proof.** Any ORIGINAL Z with non-q split mask M has a unique additional q split mask I⊆P_q, unique actual chosen split members alpha, a unique selected outsider index set R_out, and a unique subset B of the un-split ORIGINAL full pair indices J. Thus sum_G Z=c+∑_{j∈B}(a_j+b_j)=c+iota(∑_B u_j). A sum 10v necessarily has parity zero, so pi(c)=0 and c=iota(b). Now 10v=iota(5v), whence by iota injective b+∑_B u_j=5v in H. This is precisely membership in (73.1); conversely any witnessed membership constructs Z with sum 10v and split mask M, and M≠empty guarantees proper and nonempty ORIGINAL Z. Because 5Q is the subgroup of H of elements reducing to zero mod5 and rho(5v)=v (5 is odd), (73.1) and (73.2) coincide. The S071 quotient identity proves the Phi/R necessity: full original pairs have zero pi, so pi(c) modulo <q> is Phi(M)+R(h), independent of I,alpha and q-outsider choices. QED.

**Nontrivial diagnostic use.** D_M^h is NOT an arbitrary 4-colour plane. Its four required colours are parities of actual **projected-zero mod5 subset sums**, all constrained to ONE singleton status h (or a prescribed affine switch of h). It is incorrect to declare four parity values feasible merely from quotient compatibility, or to replace U_J with U under a split, or to use synthetic H matching edges as disjoint ORIGINAL indices. All no-q original tests must still be passed by the chosen 59 original values, not by formal A_{M,h} sets guessed independently.

**Complement involution.** If total(T)=0 and Z is a torsion witness, complement Z^c has the SAME non-q mask, SAME h and SAME torsion colour: each pair's split status is unchanged, each singleton q-coset split status is unchanged, and sum_G Z^c=−10v=10v. It is a second ORIGINAL witness except if Z is empty/full, excluded for M≠empty. Complement does NOT change h, cannot supply the missing opposite stratum, and cannot be used as a source of independent colour values.

## 3. CLM-0259 — same-mask Fano pair forcing in no-Fano triangle alternative

Assume genuine S064 exact12 full-cover equality with three masks A,B,C=A△B, D_A=a+L, D_B=b+L, D_C=a+b+L and |L|=4, and ALL sixteen colour-zero ACTUAL cross-mask triangles are in S072's no-Fano branch. S072 then PROVES unique witnessed status h_P(w)=h_P^0+[chi(u)+beta_P]111 at each torsion colour w=z_P+u∈D_P, with SAME linear chi:L→F2 and beta_A+beta_B+beta_C=1. Here P∈{A,B,C}; no claim the exact12 hypothesis occurs in a real fully feasible T.

**Theorem.** For ANY distinct u,u'∈L, take genuine ORIGINAL witnesses Z_{P,u}, Z_{P,u'} of two different colours z_P+u,z_P+u' in the SAME mask P. The ORIGINAL XOR
  X=Z_{P,u} △ Z_{P,u'}
has empty non-q split mask and
  h(X)=chi(u+u')·111.                                   (73.3)
It is AUTOMATICALLY nonempty and proper; no grouped/full exception. If chi(u+u')=1, X is a TRUE ORIGINAL Fano-transversal q-only subset (one of the eight genuine transversal endpoint choices, possibly the odd-complement form) and must pass the **actual S060** F_*/E(U\I_X) gate, with its true q split I_X, original selected alpha/g/s_q and indexed remaining U blocks. If chi(u+u')=0 it is a TRUE grouped q-only proper subset and must pass the original q-supervertex matching gate.

For the FULL ORIGINAL G intersection J=Z_{P,u}∩Z_{P,u'}, put d=u+u'≠0. Exactly
  sum_G X=10d−2sum_G J.                                (73.4)
Therefore the q-only zero prohibition yields the necessary original overlap restriction
  sum_G J NOT≡5d (mod 10), componentwise.                (73.5)
This does NOT force a contradiction: the intersection is not known to lie in 5Q modulo10, and q-only gates prohibit only ZERO, not nonzero Fano H values.

If chi≠0, EACH of A,B,C forces FOUR unordered pairs of differing colours with chi(d)=1, hence twelve **labelled pairwise Fano tests** across the three masks; the remaining two unordered colour pairs per mask (six total) have grouped XOR. These count **witness pairs/tests**, not necessarily distinct resulting X or independent F_*/C/Delta conditions. If chi=0, all 18 unordered within-mask colour pairs are grouped, and the Fano-pair route yields no forced Fano. Both possibilities remain consistent at support-signature level.

**Proof.** For a singleton q-coset pair, the bit h_j(Z) equals the parity of its two ORIGINAL endpoint membership bits; consequently h is additive under symmetric difference. Since the same non-q mask P appears twice, the mask of X is P△P=empty. Subtraction of the unique affine statuses gives h(X)=(chi(u)+chi(u'))111=chi(u+u')111. Suppose X=empty: then the two ORIGINAL subsets coincide, so have equal G sums, contradicting distinct colours. Suppose X=T (all 59 ORIGINAL indices): the subsets are complements; since total(T)=0 and their G sums have order two, complement witnesses have equal colours, again contradicting distinct colours. Thus X is proper nonempty in BOTH cases chi(d)=0 and chi(d)=1. For any pair of index sets, sum_G(Z△Z')=sum_G Z+sum_G Z'−2sum_G(Z∩Z'). Here 10(z_P+u)+10(z_P+u')=10d because 2z_P=0 over Q and 10·2z_P=0 mod20, proving (73.4). Vanishing iff 2sum_G J=10d iff sum_G J≡5d modulo10, which S060 forbids for this TRUE q-only proper X, gives (73.5). A nonzero linear functional on L≅F2² partitions its four elements into two fibres of two; unordered cross-fibre pairs number 2×2=4, within-fibre pairs number 2, per mask. QED.

**Novel vs old results.** S064 already gave the general same-mask intersection no-zero law, and S072 gave the affine 3-mask status rule; DO NOT claim either as discovered here. The NEW scoped deduction is their ORIGINAL-index *within-one-mask* combination: if chi≠0, twelve specifically Fano original pair tests are mandatory, independently of whether any zero-colour three-mask XOR is Fano. A no-Fano *triangle* DOES NOT mean absence of q-only Fano XORs elsewhere. This is a conditional reduction, not a refutation of exact12.

## 4. Applying the mixed-mask gate to exact12 and testing the ambitious target

For each P∈{A,B,C}, z_P+L must be witnessed in the exact original extension gate (73.1). Under the S072 no-Fano branch, writing h_P(u)=h_P^0+[chi(u)+beta_P]111, each u∈L must satisfy
  5(z_P+u) ∈ A_{P,h_P(u)},                         (73.6)
while the OPPOSITE admissible status h_P(u)+111 must satisfy
  5(z_P+u) ∉ A_{P,h_P(u)+111}.                     (73.7)
Both are genuine *full original data* conditions. This is now an exact finite additive existence/exclusion statement in H (not a guessed quotient assignment): selected g/S original positions, all q and non-q split alpha choices, and one indexed U complement J in each term. In particular a constant chi=0 must realise FOUR different 5Q parities from C5-projected-zero mixed subsets with the SAME selected singleton signature for each P, and no opposite-status witness at any of those values. Nonconstant chi adds the twelve mandatory true Fano same-mask XOR tests of §3. None of (73.6)/(73.7) has been proved impossible for arbitrary source-conditional U22.

**Attacking the 16 zero-colour triangles.** Their existence and shared affine signatures DO NOT control the full-G original majority intersection. For three original torsion witnesses with zero colour, S070 says sum_G(X)=−2sum_G(K). For a TRUE proper Fano X, projected-zero X is equivalent to projected-zero majority K, but even parity of K is additional data. If X has nonzero H sum in 5Q, an order-four odd K can realise the zero-colour but nonzero-original-X escape. Conditions (73.1) constrain each witness's individual mixed subset projection but do NOT fix intersections among THREE separately selected witnesses; (73.4) constrains PAIRS but does not imply a triangle's weighted original carry vanishes.

**Endpoint operations.** Genuine b_i−a_i=10d_i switch operations only exist under that full G equality, not just same endpoint parity. Such an endpoint flip preserves the corresponding h and translates torsion colour by d_i if the split index is selected. S072 chi|W_P=0 follows. No amount of endpoint switches or simultaneous non-q 10theta gauge creates an opposite singleton status of the SAME original witness; the gauge preserves true original XOR/carry for fixed supports (S070). No legitimate universal mixed-status-reversal operation identified.

**Full8 and high danger.** A full D_M=Q would require all eight parity values 5Q in the union of its true mixed gates (73.1), with at least one true actual witness per value, respecting q-only XOR no-zero; S072's 3-mask affine theorem DOES NOT apply. For no-full covers ≥13, and for m≥3 even at equality12, extra actual masks/strata cannot be ignored; S067's 13→12 subcover does not imply exact12 exclusivity. For m=0 S060 only tests the canonical q-only subproblem; for m=1 any failure needs a full8 mask (S064), and m=2 both full8 and exact12 or more remain unexcluded. All 26 q hubs, three-hub choices, alternate P26 (0,4),(0,6),(1,7), and the source-conditional canonicality itself remain separate obligations.

## 5. Hostile review of tempting false conclusions

1. **False:** No Fano zero-colour *triangle* means there is no genuine Fano *pair*. In fact chi≠0 forces twelve pairwise tests (§3). Even these do NOT guarantee a zero X.
2. **False:** Twelve genuine Fano pair tests contradict S060. Its q-only exclusion is ONLY of zero sums; all twelve can in principle be nonzero, and tests might coincide.
3. **False:** Four torsion colours z_P+L may be chosen independently by a quotient/F2 colouring. The true extension gate (73.1) demands twelve actual subset-sum mod5 cancellations with exactly prescribed parity and status; no globally feasible original instance has been built.
4. **False:** The XOR of different torsion-colour ORIGINAL subsets can be empty or full, as for the 3-witness grouped case. In a SAME mask, different colour forces XOR proper by the complement argument; that argument CANNOT transfer to three different witnesses.
5. **False:** A proper Fano pair XOR implies sum_G(X)=0. Equation (73.4) still has an unconstrained full original intersection. Same for majority K in the 3-witness bridge.
6. **False:** The S060 four TRUE Fano x values with sum C and Delta can be independently assigned to each of the twelve new mixed-mask pair differences. Their actual singleton endpoints, q split I, g choices, and full-pair B vary and remain coupled to one global T.
7. **False:** Complete-pair 3-rank order-two blocks can be assumed in U22. S066 PROVED that impossible; the historical D2(C5³)=20 remains merely SOURCE_STATED. No such input used here.
8. **False:** A support-only formal affine pattern is a genuine labelled hostile G59. We produced NO 22 original pairs+8 g+7 singleton values passing F_*, no first fully gated non-q original zero, and no G58 candidate.

## 6. Mathematical conclusion and next precise gap

**INTERNAL PROGRAMME_PROVED scoped claims:** CLM-0258 exact original mixed-mask H-extension/5Q gate; CLM-0259 mandatory proper within-mask original XOR and nonconstant-chi twelve genuine Fano pair tests. These are finite original-index theorems, CONDITIONAL on the pre-existing canonical/exact12 framework, not numerical Davenport proofs.

The strict next bridge is to combine (73.6)/(73.7) and the twelve within-mask TRUE Fano XOR gates WITH the SAME global S060 actual four-Fano C/Delta and U22 zero-free constraints, and either (a) forbid all affine status choices including chi0, or (b) force a genuine proper original zero-colour triangle X with lambda(sum X)=0 and majority parity even, or (c) give full 59 labelled passing G data plus its first non-q original zero. At present no such bridge is proved; no new original zero, no full-gate hostile model, no G58 sequence, no D(C20³)=58, and certainly no universal rank-three conjecture resolution.
