# S046 — a genuine decorated two-block exchange on every hostile A_k window (CLM-0180)
13 October 2026. Pure symbolic indexed CRT argument. No mathematical search, full composite lift, or assumption that quotient-only packing gives a contradiction.

Let Q=C5^3 with symbols X=e1,Y=e2,Z=e1+e2, and use the S042/S044 A_k indexed quotient sequence (k>=2):
  A_k=e1^(5k-6) e2^4 e3^4 Z^3 (e1+e3)^2 (e2+e3)^2.
It splits into k-2 disjoint pure five-blocks P_i=X^5, one seven-block B=X^2 Z^3 Y^2, and leftover L=X^2 Y^2 e3^4(e1+e3)^2(e2+e3)^2 (12 positions). S045 proves every W_t=B+L+P_1+...+P_t has exactly t+1 disjoint Qzero blocks at most, so quotient-only forcing fails. Distinguish FULL A_k length5k+9 from the actual n=5m zero-sumfree target length5k+8, k=D(C_m^3)=3m-2; deleting ONE indexed X from L gives A_k' length5k+8, L' length11, and preserves all relevant zero-free packing obstructions. Full A_k is a HOSTILE quotient model, A_k' is a possible quotient skeleton only, NOT a known G-zero-sumfree lift.

## General exact indexed H tests
Let G=Q\oplus H via CRT, with H=C_m^3 and D(H)=k when known/assumed. In ANY hypothetical indexed zero-sumfree G lift of these quotient blocks, V=(b,p_1,...,p_(k-2)) is an H zero-sumfree sequence of length k-1, where b and p_i are exact H sums of the ORIGINAL disjoint blocks. For any indexed Q-zero replacement W of B contained in B+L, disjoint from all untouched P_i, one MUST have h(W) in E(V\{b}); this is necessary AND sufficient for zero-freeness restricted to unions of W and entire unchanged P_i. It does NOT test G subsets using only parts of P_i or the leftover.

In FULL A_k, choose r=1 or2 distinct Z positions from B and r distinct X positions and r distinct Y positions from L. Form W=(B\Z_selected)+X_selected+Y_selected; since X+Y=Z, W is Qzero, with b'=b+delta where delta is the sum of the new H decorations minus removed ones. These are 3*2*2=12 labelled r=1 and C(3,2)=3 labelled r=2 exchanges: FIFTEEN distinct indexed Qzero block replacements, all requiring b' in E(V\{b}). In A_k' (one X deleted from L) only SIX r=1 replacements remain. Values b' may coincide in H; no cardinality lower bound on E is inferred.

## Genuine TWO-BLOCK cross-window exchange
Fix one pure block P_i, a distinct ORIGINAL X index x in it (5 choices), an X index y in L (2 in full A_k, 1 in A_k'), a Y index q in L (2), and a Z index d in B (3). Replace the pair of original quotient-zero blocks by
  B'=(B\{d}) union {x,q},   P_i'=(P_i\{x}) union {y}.
They are mutually disjoint indexed Qzero blocks, also disjoint from the k-3 OTHER intact pure blocks. B' has 8 terms; P_i' has5. Their H decorations (write h_x for the ORIGINAL individual H entry) are
  b'=b+h_x+h_q-h_d,   p_i'=p_i-h_x+h_y,
  b'+p_i'=b+p_i+h_y+h_q-h_d.
The last sum differs from the original b+p_i by a new, generally NONZERO L-to-B exchange contribution. Let U=V\{b,p_i}, a zero-sumfree sequence of k-3 exact H block sums. Then absence of a Gzero that is a union of B',P_i' and selected intact other P_j is EQUIVALENT to the THREE independent membership tests
  b' in E(U),  p_i' in E(U),  b'+p_i' in E(U).
Indeed, zero sums among the unchanged U alone are excluded; a zero using B' alone, P_i' alone or BOTH corresponds respectively to one of these E violations (including the empty U selection). The third is not automatically implied by the first two, because b'+p_i' CHANGES. This differs fundamentally from the conserved-sum three-hub n20 critical extension (CLM-0178).

For a given full W_t window there are 5*2*2*3=60 original-index test tuples PER retained P_i, i=1..t, hence 60t labelled genuine two-block tests, in addition to fifteen B-only tests. Across A_k' the counts are 5*1*2*3=30t two-block tests and six B-only. All counts use labelled DISTINCT positions in each test but do NOT assert distinct H sums or independent information. In a genuine n15 or n20 target-sized lift of A_k', t=k-2 gives respectively k=7: 150 two-block tests, or k=10:240; neither supplies a contradiction without an H inverse that excludes one required triple-membership family.

## Hostile and conditional boundaries
The sharp A_k quotient window is still compatible with the EXISTENCE OF MANY alternative quotient-zero blocks: maximal packing is about DISJOINT simultaneous Qzero blocks, not uniqueness. Replacement B' and P_i' overlap original B/P_i but are disjoint FROM EACH OTHER, so the correct test is an H extension test, never a quotient packing contradiction. We have not supplied any G decoration satisfying all test families, nor shown that no such decoration exists. H=C3^3 and C4^3 equalities are prime-power internal/historical inputs; H=C6^3=16 and p5 multiwise UPPER are SOURCE_STATED. The exact new indispensable lemma must exclude the triple E(U) test for EVERY possible maximal decoration V and genuine A_k'-like original skeleton, or force an explicit disjoint G-zero partition not captured by a hostile quotient example. No composite equality, no candidate, no novelty.
