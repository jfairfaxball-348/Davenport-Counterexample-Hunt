# S052 — all-even-subset COMMON Fano kernel parity moment (CLM-0198)
13 October 2026. Phase1 original-index symbolic proof, internally checked only. **No D(C20³)=58 proof or actual length58 zero-free witness.**

## Setup and why this sharpens S042
Use exactly S051's 59 distinct indexed positions in G=C20³: 22 disjoint pairs (44 originals) with H=C10³ decorations U=(u1,...,u22); eight further originals g_i all in the SAME residue class mod2; and seven other original singleton indices s_r for every nonzero r∈Q=F2³. The injection iota:H→G is iota(h)=2h, an isomorphism onto 2G, NOT a splitting of G. T is assumed minimally zero-sum. Define c=-Σ_i u_i∈H; v=iota^{-1}(Σ_i g_i)∈H; h_V=iota^{-1}(Σ_{r≠0}s_r)∈H. T-total zero implies h_V=c-v. For each even subset J of the eight ORIGINAL indices, including the empty and full subsets, set w_J=iota^{-1}(Σ_{j∈J}g_j), W={w_J}, E=H\(-Σ(U)), K=∩_{w∈W}(E-w). Equal H sums do not create independent restrictions. For each of the seven three-element Fano lines L, let h_L=iota^{-1}(Σ_{r∈L}s_r), and h_{L^c} analogously. All h_L and h_{L^c} lie in K: every union of the corresponding 3/4 singleton original indices, any even J and arbitrary full U pairs is NONEMPTY and PROPER, size at most 4+8+44=56<59. This is precisely S051 CLM-0195 and needs no full-T test.

## The four-line moment — FULL PARITY RANK IN THE COMMON K
Let π:H=C10³→H/2H=Q be mod2 reduction of the H coordinates. Fix any nonzero q∈Q. Exactly FOUR of the seven Fano lines do NOT contain q. Each other singleton parity r≠q occurs in exactly TWO of those four lines, whereas q itself occurs zero times. Hence in G, without illicitly dividing an odd sum,
 iota(Σ_{L: q∉L}h_L)=Σ_{L:q∉L}Σ_{r∈L}s_r=2Σ_{r≠q}s_r.
Since iota identifies H with 2G, taking the unique iota inverse shows Σ_{L:q∉L}h_L equals the coordinate reduction of Σ_{r≠q}s_r modulo10. Reducing once more modulo2 gives the **exact indexed parity identity**
 π(Σ_{L:q∉L}h_L)=Σ_{r≠q}r=q.
The last equality holds because the XOR of all seven nonzero elements of F2³ is zero. Thus each q≠0 is represented by a FOURFOLD sum of values in the COMMON K. Zero also belongs to 4π(K), by four repetitions of one element. Therefore
 **4π(K)=Q** (ordinary fourfold sumset, repetitions allowed),
and, more strongly, the SAME seven line choices give all seven q's simultaneously.

For the affine-span consequence, choose k0∈K. In Q any fourfold sum equals Σ_i(π(k_i)-π(k0)), since 4π(k0)=0. Thus 4π(K) is contained in the vector span of the pairwise differences of π(K). Because 4π(K)=Q, that span is all Q:
 **aff_F2(π(K))=F2³.**
In particular π(K) must contain at least four affinely independent residues. This improves the older necessary full span of π(E(P26)) in S042 CLM-0159: K requires the extension to survive **all 128 labelled original even-subset expressions at once**, rather than only a chosen 26-block pairing. It is necessary, not sufficient, and does NOT exclude every U22 core.

## Coherent 3×3 tensor identity
Label each Fano line L as ker ℓ_L\{0} for the unique nonzero linear form ℓ_L∈Q*. The condition q∉L is equivalent to ℓ_L(q)=1. The seven identities above say
 Σ_L ℓ_L(q) π(h_L)=q for all q∈Q.
Equivalently, as endomorphisms of Q,
 **Σ_L π(h_L)⊗ℓ_L = I_Q**.
This is a coherent original-index moment constraint, not seven independent cardinality claims. It may rule out particular candidate sets K even when their affine span is full; no theorem says it always does.

## Reflection symmetry and sharper residue lower bound
For any indexed zero-free U, the standard complement bijection gives E(U)=c-E(U), where c=-ΣU. Since complementing an even subset of eight originals sends w_J to v-w_J, W=v-W. Therefore, exactly as sets,
 K=∩_{w∈W}(E-w) = (c-v)-K = h_V-K.
Project to Q. Writing A=π(K), t=π(h_V), reflection becomes A=t+A (characteristic two).

If t=0, full affine span already demands |A|>=4. If t≠0, A is a disjoint union of two-element translation orbits {a,a+t}; one orbit spans at most a line, two orbits have at most two independent affine differences (t and b-a), hence cannot affinely span Q. At least THREE translation orbits are required, so **|A|>=6**. Both 4 and 6 are sharp as ABSTRACT parity-set thresholds: an affine basis of four points for t=0, and three independent t-pairs {0,t,a,a+t,b,b+t} for t≠0. Such abstract parity sets do NOT realise the C20 T59.

## Hostile audit and outstanding obligation
- Four nonincident Fano lines really do count every singleton except q twice. The modulo10 equality follows from the group isomorphism iota, not a C2⊕C10 split; the last mod2 parity of Σ_{r≠q}s_r is exactly q.
- Every use of E(U) arises from a proper original-index subset; max size56, never the full 59.
- 4π(K)=Q allows repeated K values as a SUMSET; the actual seven h_L are still shared/coherent and cannot be chosen independently.
- K reflection uses complement of eight **original** indices and exact total-zero h_V=c-v; all W can have repeated values.
- If K projects to a proper affine subspace, or to <=3 parity values (<=5 when πh_V!=0), the specified completion is impossible. Conversely, 4/6 classes are NOT sufficient; 26 hub pencils, other parity profiles, arbitrary U22 and mixed odd-index Fano kernels remain unresolved.
- This is an internally reasoned new necessary obstruction. It may overlap historical inverse literature; NO novelty/priority claim or original-source proof promotion. S042 already had affine-span of the larger E(P26), so do not relabel that as new.
