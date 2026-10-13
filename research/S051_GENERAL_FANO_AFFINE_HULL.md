# S051 — indexed Fano extension-set affine-hull obstruction (CLM-0195)
13 October 2026. ONE Phase1 direct hand proof, INTERNALLY checked only. No universal C20 conclusion and no computation.

## Exact hypotheses
Let G=C20³, H=C10³, iota(h)=2h mapping H isomorphically onto 2G (NOT a direct product C2³×C10³). Suppose T is a 59-term **minimally zero-sum** original-index sequence divided into:
(1) 22 distinct-index parity-zero pairs, whose iota-inverse sums form an arbitrary indexed U=(u1,...,u22) in H;
(2) eight other **original** indices g1,...,g8 whose parities are identical (possibly parity 0);
(3) seven final original singleton indices s_r, precisely one from each nonzero r in F2³.
These account for 44+8+7=59 positions. No special slab assumption, multiplicity restriction, or coordinate split.

Define the inclusive H-subset-sum set Σ(U), and E(U)=H\(-Σ(U)); zero is never in E(U) since the empty subset has sum zero. Let v=iota^-1(sum of all eight g_i). For every EVEN subset J of the eight ORIGINAL g indices (including empty) put w_J=iota^-1(sum_{j∈J}g_j). This is defined since parity(J)=0, and W={w_J: |J| even}. In general W has at most 128 distinct H VALUES, and labels can repeat; no 763 matching tests are counted independently. Define
K(W,U)=intersection_{w∈W}(E(U)-w).
In particular K(W,U)⊆K_v(U):=E(U)∩(E(U)-v), since 0,v∈W.

## The universal affine-hull obstruction
For any Fano line L (three distinct nonzero vectors with XOR zero), and its four-element complementary cap Lc, define h_L=iota^-1(sum_{r∈L}s_r) and h_Lc analogously. They exist because each original parity sum is zero. For EACH even J, union of line/cap originals, the J originals, and ANY subset of 22 disjoint pair blocks is nonempty and PROPER: size at most 4+8+44=56<59. T-minimality therefore implies h_L+w_J and h_Lc+w_J lie in E(U). Hence all fourteen h_L,h_Lc lie in K(W,U), and thus also in K_v(U).

Write V for all seven singleton indices. Since every nonzero F2³ point occurs in exactly THREE of the seven Fano lines, and since each L/Lc partitions V,
  Σ_{L line} h_L = 3h_V,    h_L+h_Lc=h_V.
Fix any particular line L0. Subtraction gives the exact **integer-affine identity**
  0 = (Σ_{L line} h_L) - 3 h_L0 - 3 h_L0c,
whose integer coefficients have total 7−3−3=1.
For a nonempty subset K of any finite abelian H, define aff_Z(K)={Σ_i n_i k_i: k_i∈K, n_i∈Z, Σ_i n_i=1}. This equals k0+⟨K−K⟩ for any k0∈K. The displayed identity proves
  **NECESSARY: K(W,U) is nonempty and 0∈aff_Z(K(W,U)).**
The weaker but more practical condition 0∈aff_Z(K_v(U)) follows immediately. Thus if K_v is empty, or is contained in a coset a+D of a subgroup D with a∉D, this entire indexed 22+8+7 completion is impossible. For any homomorphism φ:H→A, if φ(K_v) is a SINGLE nonzero value c, then applying φ to the integer-affine identity gives 0=(7−3−3)c=c, contradiction. No appeal to field-linear geometry or unit inverses is needed.

## New broad corollary: any projected five-residue core
Let φ:H→Z10 be any homomorphism and suppose, for an ARBITRARY U22, φ(E(U))⊆{1,2,3,4,5}. If φ(v)=4 then φ(K_v)⊆{1}; if φ(v)=6 then φ(K_v)⊆{5}, simply by intersecting the five-residue set with its translate. Both singletons are NONZERO in Z10. Therefore **neither φ(v)=4 nor φ(v)=6 permits the specified T59 completion**, regardless of the eight individual G values and regardless of U's other two coordinates. Empty intersection also precludes completion. The old fixed slab f1^9 f2^9 f3^4 with φ=third coordinate and v-third4 is only one instance; this theorem does NOT say all 22-pair cores have such a φ or that φ(v) must be 4 or6.

## Audit, limitations
- We NEVER require membership for the full 59-index union. Every used line/cap union has ≤56 positions.
- The eight-index tests are even ORIGINAL subsets. A hypothetical matching-of-pairs quotient is NOT substituted for an indexed G subset.
- The identity is in H for even-parity sums; no illegal C2×C10 splitting or division of odd G elements.
- The affine hull condition is NECESSARY, not sufficient. If aff_Z(K_v) contains0, there may still be no lifts or total-zero constraint satisfaction. The 26 hub pairings, eligible (0,4)/(0,6)/(1,7) profiles, and arbitrary U22 classification remain entirely OPEN.
- All evidence is internal mathematical hand reasoning; no numerical search, exhaustive proof, certification or D(C20³)=58 theorem.
