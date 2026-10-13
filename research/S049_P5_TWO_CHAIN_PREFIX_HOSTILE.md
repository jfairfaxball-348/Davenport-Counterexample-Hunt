# S049 — two genuinely changed original-index CRT chains survive EVERY prefix (CLM-0190)
13 October 2026. Symbolic OLD/NEW zero-free H proof for a larger family than S048's ONE chain, not a Gzero-free C15/C20 candidate.

## The target-sized A_k' only
Use S047's indexed Q=C5³ quotient skeleton A_k' of exact length 5k+8 (NOT the 5k+9 A_k): B=X²Z³Y², t=k-2 disjoint pure P_i=X⁵, and residual L' with original y∈X and q∈Y. Fix an original d∈B of class Z. Take H=C_m³, with m=3,k=7,t=5 or m=4,k=10,t=8 and basis f1,f2,f3. Assign h(B)=b=f1+f2 and h(d)=f2, plus h(y)=h(q)=0, realisable by assigning total f1 to the other six B positions. Prescribe the multiset of pure block decorations as
P=(f1)^(m-2) (f2)^(m-1) (f3)^(m-1), length (m-2)+(m-1)+(m-1)=3m-4=t.
Choose ONE distinguished block P*=X⁵ with total p*=f2. It contains two different ORIGINAL X indices a and a' having h(a)=0 and h(a')=f3. Assign a third distinct original X index the H label f2-f3, and other two zero, making total f2. For every other pure P_i assign at least one selectable original X index with label0 and distribute the prescribed p_i onto another index; leave others0. Choose an ordering of all t blocks with P* first and one designated 0-labelled X index selected in each subsequent block.

## Two distinct choices and ALL r=1,...,t
Chain A chooses x1=a; chain B chooses x1=a'. For every prefix 1<=r<=t, perform the honest S047 original-index replacement from B through P1,...,Pr to residual y using q,d. All selected x2,...,xr and y,q are 0, and h(d)=f2. The NEW block decoration list together with untouched P_{r+1},...,P_t has EXACTLY the same multiset for every prefix:
- Chain A: f1^(m-1) f2^(m-1) f3^(m-1).
- Chain B: (f1+f3)(f2-f3) f1^(m-2) f2^(m-2) f3^(m-1).
In particular the chosen indices a≠a' and their H labels are not equal, and the B and first P new decorations differ (f1 vs f1+f3, f2 vs f2-f3). These generate genuinely different single-block E(U) tests, although some total and union tests are duplicated. The changing TOTAL in either chain is Δ=h(y)+h(q)-h(d)=-f2≠0, independently of r.

## Direct H zero-free proof, no hidden enumeration
OLD list V=(f1+f2) f1^(m-2) f2^(m-1) f3^(m-1) of length k-1=3m-3 is H-zero-free: if a zero subset contains b, its f1-coordinate would require m-1 additional f1 copies, but only m-2 exist; if b absent, coordinate basis counts stay <m. Chain A's NEW list is H-zero-free since every coordinate coefficient can be 0..m-1 and cannot vanish except when all are zero.

Chain B's NEW list is H-zero-free: the f1-coordinate of any subset is between0 and m-1, so to be 0 it MUST omit the (m-2) f1 basis terms and f1+f3. Then the f2-coordinate among remaining terms lies 0..m-1, forcing omission of f2-f3 and all m-2 f2 basis terms. The remaining f3^(m-1) is zero-free. This applies to m3 and m4.

For every prefix r, its r+1 changed blocks plus t-r untouched blocks form the corresponding full k-1-term zero-free H list. Therefore EVERY of the 2^(r+1)-1 nonempty changed-block subset sums avoids -Σ(U), exactly as required by CLM-0184. Unlike S048, this simultaneously passes all prefix lengths for TWO actual differing original-index choices with different single-block tests and unchanged nonzero Δ.

## Strict limitations
Other orders putting P* later, other chosen indices including the third with h=f2-f3, other choices of d or q, and other B-only exchanges are NOT shown compatible. This is NOT all chains/all original pairs, no full quotient-wide G zero-freeness, no S58/S43 witness, and no new upper or lower Davenport value. Claim is a materially larger hostile local family against an easy two-chain/prefix contradiction only.
