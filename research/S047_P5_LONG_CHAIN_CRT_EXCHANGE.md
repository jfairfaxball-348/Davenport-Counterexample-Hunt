# S047 — arbitrarily long changing-total CRT chains in A_k' (CLM-0184)
13 October 2026. Original-index symbolic proof; not numerical search, composite lift, or new multiwise upper.

Use S046 notation X=e1, Y=e2, Z=X+Y in Q=C5^3. The target-length hostile quotient skeleton A_k' (k>=3) contains the indexed B=X^2Z^3Y^2, t<=k-2 disjoint pure blocks P_i=X^5, and residual L' from S044's L=X^2Y^2e3^4(X+e3)^2(Y+e3)^2 with exactly one X removed. L' has exactly one indexed X position y and TWO Y positions q. A_k' has length 5k+8 and remains a QUOTIENT MODEL, not a G zero-sumfree candidate.

Choose r with 1<=r<=t and an ORDERED list of r distinct pure blocks P_{i_1},...,P_{i_r}. In each block select one of its five ORIGINAL X indices x_j. Choose d one of the THREE original Z indices of B; choose q one of the TWO Y indices in L'; let y be its unique X index. Define NEW indexed blocks:
  B'=(B\{d})∪{x_1,q};
  P'_{i_j}=(P_{i_j}\{x_j})∪{x_{j+1}} for 1<=j<r;
  P'_{i_r}=(P_{i_r}\{x_r})∪{y}.
Each new P' consists of five X quotient terms so sums0. B' sums_Q B -Z+X+Y=0, has eight ORIGINAL indices, and is disjoint from all the new P'_i and the untouched P_j. There is no reused position: selected x_j moves one link left, q moves into B', and y enters last P', while d moves into the remaining residual. The new residual is L''=(L'\{y,q})∪{d}; its Q contents are Y e3^4(X+e3)^2(Y+e3)^2 Z. It is itself Q-zero-sumfree: second coordinate total is 1+2+1=4, so no zero subset can include any term having second coordinate1; then first coordinate contributes at most2 from (X+e3)^2, and finally at most4 pure e3 terms remain. Thus the chain preserves local residual sharpness.

Let h denote genuine ORIGINAL CRT H=C_m^3 component (m=3 or4, or source-stated m6 when appropriately conditional). Denote b=h(B), p_j=h(P_{i_j}), and individual h_xj,h_y,h_q,h_d. The r+1 new disjoint Qzero block decorations are:
  β_0=b+h_x1+h_q-h_d;
  β_j=p_j-h_xj+h_x(j+1)  for 1<=j<r;
  β_r=p_r-h_xr+h_y.
The telescoping identity is
  β_0+...+β_r = b+p_1+...+p_r +h_y+h_q-h_d.
This total CHANGES by Δ=h_y+h_q-h_d, independent of chain length, order or chosen pure-block individual H decorations. Unlike the conserved n20 hub grid, no completion involution can eliminate arbitrary joint subset sums.

Let U consist of the other t-r intact P decorations, and in the complete maximal k-1 block system of ALL A_k' let U include all k-2-r untouched P decorations. U is H-zero-sumfree in every genuine G-zero-sumfree lift. For this fixed chain, absence of a zero G subset that is a union of any of the r+1 changed blocks and some U blocks is EXACTLY equivalent to
  sum_{j in J} β_j ∈ E(U) for EVERY nonempty J⊆{0,...,r}.
Proof: each subset sum β_J cancels a subset of U iff β_J∈-Σ(U), and every such selected union is on mutually disjoint ORIGINAL Qzero blocks. Nonempty U-only zero subsets are excluded separately by U zero-freeness. This gives 2^(r+1)-1 simultaneous extension memberships per chain. For r=1 it is S046 CLM-0180's b',p',b'+p' tests; r=2 demands seven memberships; for all r=k-2, U is empty and they demand that the k-1 newly decorated blocks themselves remain H-zero-sumfree.

Among t named pure P blocks there are (t)_r=t!/(t-r)! orders, 5^r labelled selected X positions, three d and two q and one y, i.e. 6*5^r*(t)_r labelled chains in A_k'. These may generate duplicate H values or constraints. Full A_k would have an additional choice for y, but is one position LONGER than target and not substituted. For k7 (n15) and k10 (n20) all r up to5 or8 respectively become available on their corresponding hypothetical target-sized A_k' lifts. NO result says a maximal C3^3 or C4^3 decoration violates these constraints. Needed next: an authentic H inverse theorem that forces a particular chain-sum into -Σ(U), or a genuine 43/58-position G-zero-sumfree construction with independent certification.
