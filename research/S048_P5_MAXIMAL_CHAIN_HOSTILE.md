# S048 — maximal changing-total chain survives all subset tests (CLM-0188)
13 October 2026. Symbolic hostile configuration for ONE maximal ordered p5 chain, NOT a G-lift or all-chain theorem.

Let H=C_m^3 with m=3 (k=D(H)=7, n15) or m=4 (k=10, n20), with basis f1,f2,f3. Use the target-length A_k' quotient skeleton of S047 (not full A_k). It has t=k-2 pure X^5 blocks P1,...,Pt, the B=X²Z³Y² quotient-zero block, residual L' with a unique X position y and a Y position q, and at least one Z position d in B.

For a chosen ordered chain through ALL t pure blocks, prescribe OLD H block decorations
 b=f1+f2,
 (p1,...,pt)=f1^(m-2) f2^(m-1) f3^(m-1)
as a multiset in any order. The count t=(m-2)+(m-1)+(m-1)=3m-4 is 5 when m3 and 8 when m4. The OLD sequence V=(b,p1,...,pt), length t+1=3m-3=k-1, is H zero-sumfree: without b the coordinate counts each lie below m; with b, a zero would need m-1 copies of f1 but only m-2 occur.

Fix one selected ORIGINAL X index x_j from every pure block and assign its H label 0, also assign H(y)=H(q)=0, H(d)=f2. Distribute the rest of each pure block's total p_j among its other four original X indices, and distribute the remaining B total b-f2=f1 among B's six untouched indices. This is an honest assignment to ORIGINAL positions in Q⊕H; unmentioned residual decorations may be set 0, with no full G-zero-free claim.

Apply the EXACT S047 r=t chain: the new B decoration is β0=b+0+0-f2=f1, and every new P decoration is β_j=p_j (all individual chain transfers are 0). The changed TOTAL is Δ=-f2 ≠0. The new maximal H block decoration sequence is
 f1^(m-1) f2^(m-1) f3^(m-1),
which is H zero-sumfree because no coordinate count reaches its order m. Since U is empty for r=t, ALL 2^(k-1)-1 nonempty subset memberships of this maximal chain hold: 63 at m3 and 511 at m4. This is not a fake conserved-sum example: old and new totals differ by nonzero -f2.

The construction is scoped to ONE chosen ordered maximal chain and its selected ORIGINAL indices, not all 6*5^t*t! possible chains, not all B-only and cross-window replacements, not all quotient-zero subsets of A_k', and not a certified zero-sumfree C15³/C20³ target. It disproves the naive idea that ONE maximal changed-total chain alone must necessarily contradict a maximal H decoration. A future successful p5 attack must couple different index choices or chains genuinely.