# S045 — n15 exact six-class ternary residual inverse (CLM-0173, CLM-0174)

13 October 2026. Independent symbolic quotient argument **not using** the historical SOURCE_STATED D11=39 or D12=42 or BSP2007 diagrams. Uses the internally reconstructed prime values D(C3³)=7 and D(C5³)=13 (S039), plus the minimal-zero augmentation of a hypothetical zero-sumfree S43 in C15³. No full composite theorem or candidate.

## CLM-0173 — at least SIX quotient classes, and an exact eleven-point six-class obstruction

Let T=S*z have 44 distinct indexed terms and sum0, where z=-sum S is a new position. T is G-minimal zero-sum (complement argument). Let Q=C3³, H=C5³ by CRT. If T could be split into 14 disjoint nonempty Q-zero blocks, among any 13 H decorations a zero subcollection exists by D(H)=13, and it omits the nonempty 14th block; this gives a forbidden proper G zero. Thus T has **no 14 disjoint Q-zero blocks**.

For each distinct quotient value v appearing in T with indexed multiplicity m_v, strip a_v=floor(m_v/3) disjoint **monochromatic triples of original indices**. They are quotient-zero because 3v=0. Leave r_v∈{0,1,2} distinct indexed positions, and put R=sum r_v. Since 44=sum 3a_v+R, necessarily R≡2 (mod3). All stripped triples are pairwise index-disjoint. The residual R-position multiset is quotient-zero as T is. If there are at most FIVE different quotient values, R≤10, so R∈{2,5,8}:
- R=2: (44-2)/3=14 disjoint monochromatic Q zeros already, impossible.
- R=5: 13 disjoint monochromatic Q zeros plus the ENTIRE nonempty quotient-zero residual five-block produce14, impossible.
- R=8: 12 disjoint monochromatic Q zeros. Reserve any one residual index. The other SEVEN positions contain a nonempty Qzero subset by D(Q)=7. The leftover complement contains the reserved index, is nonempty, and is Qzero because R's total is0. They supply TWO more disjoint quotient zeros, making14, impossible.

Hence the quotient support of T has at least SIX distinct classes (no SOURCE_STATED multiwise premise required).

If it has EXACTLY six classes then R≤12 and R∈{2,5,8,11}; the first three cases are impossible by the same argument. Thus R=11 and the six remainders are EXACTLY (2,2,2,2,2,1), each strictly positive. Label their six distinct quotient values v1,...,v5,u, where u is the singleton-residue class. The quotient-zero total of the eleven residual positions gives
  2(v1+...+v5)+u=0 in F3³, or **u=v1+...+v5**.

The eleven-point residual CANNOT contain any nonempty quotient-zero subcollection W of size 1,2,or3. Otherwise after removing W, the remaining quotient-zero residual has size≥8. Reserve one of its indices, apply D(Q)=7 to seven of the others, then take the Qzero nonempty complement. This produces THREE pairwise disjoint Qzeros in the residual plus the eleven stripped triples =14 in T. Contradiction. In particular none of the six support values is zero, none is antipodal to another, and no three DISTINCT support values sum to0. In characteristic3 three distinct affine-collinear points have sum0; hence these six values form an affine six-cap (no three collinear), with no opposite pair and the distinguished relation u=sum v_i. Such a geometric six-cap relation is **a necessary surviving model, not proved impossible**. If a hypothetical T has exactly six support classes, it has NO quotient-zero opposite pair anywhere, stronger than S044's at-most-one disjoint-pair condition.

## CLM-0174 — forced canonical 11+2 quotient circuit structure and H inverse

Continue EXACTLY the six-class boundary above. Eleven original-index monochromatic triples have been stripped, leaving the rigid 11-point residual, which is quotient-zero and has no zero sum of length≤3. Reserve any one of the eleven residual positions; by D(Q)=7, a nonempty zero subcollection W of some seven of the other ten exists, so 4≤|W|≤7. Since total of residual is0, its indexed complement W'=R\W is nonempty Qzero with 4≤|W'|≤7. Therefore the residual splits into TWO disjoint quotient zeros with size pattern **(4,7) or (5,6)** (up to order), and T has a canonical 13-block Qzero partition:

  11 monochromatic triples + TWO residual mixed blocks of sizes (4,7) or (5,6).

Both residual blocks are Q-minimal: if either contains a proper nonempty Qzero subcollection, splitting it yields THREE disjoint zeros inside R and hence14 in T, impossible. The original eleven triples are minimal as their residual value is nonzero and characteristic3. The H=C5³ decorations of all 13 blocks form a length13 **minimal zero-sum** sequence, from T minimal; the first eleven are exact H-decorations of ORIGINAL indexed triples, and the two remaining decorations are exact H-sums of disjoint mixed residual circuits. This is a much narrower inverse-normal form than the 44-term arbitrary-anchor partition. It is not a proof that the two H decorations cancel properly: their full 13-term H sum is already zero and no proper subcollection is.

**Hostile gates.** Remainder multiplicities are mod3 counts, not full 44-term counts; a six-class residual cap is not an actual C15 zero-sumfree lift. Quotient block reallocations overlap unless distinct **original indices** are retained. An 11-point residual minimality bound alone does not certify the unknown affine cap relation impossible, and full-length H maximal-minimal sequence classification has NOT been reconstructed. No source-stated D11/D12 has been silently upgraded; their availability remains conditional for S043/S044 anchored lemmas. A decisive next lemma must rule out this precisely decorated six-cap canonical partition or force a disjoint exchange across two such index choices.
