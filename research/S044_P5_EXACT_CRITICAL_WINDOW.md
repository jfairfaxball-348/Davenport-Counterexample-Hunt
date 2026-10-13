# S044 — exact sharp C5³ one-block replacement and twelve-term residual

13 October 2026. CLM-0170, entirely symbolic. C5³ basis e1,e2,e3. Retain the S042 independently proved A_k family for every k>=2:
A_k=e1^(5k-6) e2^4 e3^4 (e1+e2)^3 (e1+e3)^2 (e2+e3)^2, length5k+9, with NO k pairwise disjoint nonempty zero-sum blocks.

Split precisely k-2 indexed pure-e1 blocks P_j=e1^5, using5k-10 copies, from the original 5k-6 pure-e1 positions. Exactly FOUR pure e1 indices remain. Next select the seven distinct-index original positions
B=e1^2 (e1+e2)^3 e2^2.
Its integer coordinate sums are (5,5,0), so B is a Q=C5³ zero-sum block. Of the remaining positions form
L=e1^2 e2^2 e3^4 (e1+e3)^2 (e2+e3)^2,
exactly twelve distinct indexed positions. Its C5³ sum is not assumed zero.

L is Q-zero-sumfree by elementary coordinate bounds: coordinate2 contributions in L come ONLY from its two e2 and two (e2+e3) terms, so any subset has integer second-coordinate sum in [0,4]; a Qzero subset must choose none. After omitting those, coordinate1 contributions come ONLY from two e1 and two (e1+e3), again in [0,4], so none of those can occur. Only at most four pure e3 remain, never yielding nonempty zero modulo5. Thus L is zero-sumfree, length12=D(C5³)-1.

The one-block replacement window B union L has 7+12=19 positions. If it admitted two disjoint nonempty Qzero subsets W,W', those, together with the k-2 pure-e1 blocks P_j, would form k disjoint zeros in A_k, contradicting the standalone S042 CLM-0160 A_k non-k-packing proof. Hence **B union L of length19 has no two disjoint zeros**, and SOURCE_STATED D2(C5³)=20, if assumed, has sharp upper threshold19. This also supplies an independent length19 lower-bound witness for D2>=20.

k=4 is exactly the original 29-position critical A4: P1,P2 both length5; B length7; L length12. The deletion A4' (28 positions) can remove one of L's pure e1 positions, leaving L11, and still has 3 Qzero blocks and no fourth. Index overlap is zero throughout. This is a local quotient countermodel, **not** a lift to C15³/C20³, not an assertion that source-stated D2<=20 has been proved, and not a refutation of the rank-three Davenport conjecture.

Therefore attempts to save a required position by strengthening CLM-0166's universal local |B_i|+|L|<=19 to <=18 are FALSE even in this structured critical family. A winning n15/n20 proof must use cross-block H decorations, different quotient choices or inverse constraints on actual complete original S.
