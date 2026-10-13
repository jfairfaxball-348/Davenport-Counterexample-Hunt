# S049 — full eight-point plus Fano line/cap kills S048 n20 hostile (CLM-0189)
13 October 2026. Fully symbolic indexed proof, INTERNAL same-executor, conditional on specified paired core. **No D(C20³)=58 proof.**

## Honest setup, non-split and original indices
In an assumed **minimally zero** augmented T of **59 distinct original indexed positions** in G=C20³, suppose that 22 disjoint parity pairs have H=2G≅C10³ sums U=(f1 repeated 9, f2 repeated 9, f3 repeated 4); eight OTHER original positions g1,...,g8 lie in one nonzero mod2 parity class, as in CLM-0187: gi=G_f3+2di with di∈span(f1,f2), so each has third C20-coordinate 1 (di may be distinct, as in S048); and the remaining seven ORIGINAL singleton positions s_r represent exactly once each nonzero r∈F2³. The 22 pair blocks, eight points and seven singleton positions account for 44+8+7=59 ORIGINAL indices. Each external pair has even total in G; it gives one H decoration in U. The embedding iota:H→G is doubling, iota(h)=2h, an isomorphism onto 2G; we do NOT split G as C2³⊕C10³.

A subset C of the seven singleton positions has even G parity iff the XOR of the corresponding r is 0. Define h_C=iota^{-1}(Σ_{r∈C}s_r)∈H for such C. The seven Fano lines L (3 parity vectors r with XOR0), their seven complements L^c (4 parity vectors with XOR0 because XOR all seven nonzero vectors is0), and the full set V (7 vectors with XOR0) give the 15 nonzero codewords of the [7,4,3] Fano/Hamming parity kernel. Only lines and caps are needed below. Original representatives may have arbitrary C20 lifts of the required parities.

## A two-test forcing lemma using the entire eight-point set
For a Fano line L or complementary cap L^c, C has length3 or4. As T is minimally zero, **every** union of this nonempty quotient-zero C with ANY of the 22 disjoint pair blocks is a PROPER, nonempty, G-nonzero subset; hence h_C∈E(U), where E(U)=H\(-Σ(U)) includes the empty subset in Σ. The FULL set I of all eight same-parity points also has quotient parity0 and is disjoint from C and the 22 pairs, hence every union of C∪I with any external pairs is PROPER (max |C|+8+44=56<59); consequently h_C+v∈E(U), where v=iota^{-1}(Σ_i gi)=4f3+Σ_i di. These are genuine original-index quotient-zero subsets; the two membership tests are NOT a fictitious 28-block counting inequality.

Since U=f1⁹ f2⁹ f3⁴, its negative subset sums fill arbitrary first and second H coordinates and third coordinates 0,6,7,8,9. Thus
E(U)={h∈H : third coordinate ∈ {1,2,3,4,5}}.
Write t=third(h_C)∈{1,2,3,4,5}. The second membership requires t+4 (mod10)∈{1,2,3,4,5}. As t+4∈{5,6,7,8,9} with no wraparound, **t=1**. Therefore EVERY one of the seven lines AND seven complementary caps has third H-coordinate exactly1.

## Fano incidence contradiction over Z/10
For any line L, the disjoint indexed line and its complement cover all seven singleton positions, so h_L+h_{L^c}=h_V. The projected third coordinate of h_V is therefore 1+1=2 mod10 (same for each line).

Every nonzero r∈F2³ belongs to EXACTLY THREE Fano lines. Since iota is an injective homomorphism, the indexed total of the seven line decorations obeys
Σ_{L line} h_L = iota^{-1}(3 Σ_{r∈V} s_r)=3h_V
in H: the middle sum is even because Σ_V s_r is even. Project to the third C10 coordinate. The left side is 7·1=7, and the right side is 3·2=6 modulo10. This gives 7≡6 (mod10), contradiction.

**Verdict:** NO arbitrary choice of seven singleton C20 lifts can complete the S048 exact 22-pair U=f1⁹f2⁹f3⁴ and eight gi=G_f3+2di family into a G-minimally-zero T59. This strictly defeats CLM-0187's all-127-matching-tests hostile; it does so even if the di are repeated, so in particular the eight-distinct/two-dimensional example fails. It uses a fuller cross-class Fano family and proper indexed unions, NOT an exhaustive numerical search or an independently certified Gzero-free witness.

## Scope and hostile audit
1. The argument depends decisively on the special *slab* E(U) third=1..5 and on every selected gi having third C20-coordinate1 (so v third=4). It does NOT exclude other 22-pair cores, other 8-point labels, other 28-block partitions or profiles (0,4),(0,6),(1,7).
2. We never demand E(U) for I=8 and C=all7, since U22+I+all7 could equal the FULL 59-point T, which legitimately has total zero. Every line/cap C used is a strict subset, so the size56 properness check prevents this invalid leap.
3. The 7+7 parity codewords are not 14 independent linear checks. The precise complement and 3-incidence identities, rather than a raw count, force the contradiction.
4. Total-zero of T is part of the hypothetical minimally-zero context but was not needed to manufacture any invalid proper subset. Historical D(C10³)=28, BSP ternary cases and finite p5 upper remain SOURCE_STATED, untouched. No inference to the 58-term counterexample conjecture.
