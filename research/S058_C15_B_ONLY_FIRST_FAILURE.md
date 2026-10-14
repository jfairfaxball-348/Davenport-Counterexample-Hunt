# S058 — first B-only original-index CRT window and a sharp slab-rigidity obstruction (CLM-0218)
14 October 2026. INTERNAL pure symbolic, NOT a complete C15 test or a G43 candidate.

Use exactly the ORIGINAL indexed target-sized quotient skeleton A'_k of S047 with Q=C5^3, B=X^2Z^3Y^2 and t=k-2 disjoint pure P_i=X^5, residual L' with unique X index y and TWO distinct Y indices q_1,q_2. There are THREE original Z indices d_1,d_2,d_3 in B. Take H=C_m^3, m=3 for n15 (k=7,t=5), or m=4 for the analogous n20 calibration (k=10,t=8); this is CRT G=C5^3⊕H (coprime), unlike the invalid C20=C2⊕C10 split.

**B-only zero-quotient exchange (r=0).** For ANY original Z index d and ANY original residual Y index q, replace the old 7-index B by B'=(B\\{d})∪{y,q}, of length8. Q(B')=Q(B)-Z+X+Y=0. The new residual (L'\\{y,q})∪{d} remains Q-zero-free by S047's coordinate argument, while all t ORIGINAL pure 5-index blocks remain unchanged. Write b=h(B), P=(p_1,...,p_t) their old H decorations and a=h(d), h_y=h(y), h_q=h(q). The new H decoration is
   beta_B=b+Delta(d,q),     Delta(d,q)=h_y+h_q-a.
In any genuine original G-zero-sumfree lift with P zero-free, **beta_B∈E(P)** for all 3×2=6 labelled (d,q) choices: otherwise B' and a subset of original disjoint P blocks form a proper nonempty G-zero-sum subset. This is an original-index necessary condition, not a claim of sufficiency.

**Exact first-character failure in the S049/S052 saturated OLD decoration.** Let f_1,f_2,f_3 be an H basis. Suppose the OLD pure-block TOTAL list is
 P=f_1^(m-2) f_2^(m-1) f_3^(m-1)
and old b=f_1+f_2 (the fixed S049/S052 setting). Write phi for the f1 coordinate in Z/m. Indexed subset sums of P have f1 coordinates 0,...,m-2, and their f2,f3 coordinates run over all residues independently. Thus
   E(P)={x∈H:phi(x)=1}.
Each one of the six distinct-original-index B-only exchanges is therefore admissible **IFF**
   phi(h_y)+phi(h_q)-phi(h_d)=0 mod m.
If this equality fails, beta_B has phi-coordinate in {0,2,...,m-1}; choose m-phi(beta_B) copies of f1 when phi(beta_B)≠0, or none when it is0, and independently choose f2/f3 blocks to cancel the remaining two coordinates. This explicitly gives a proper original G zero sum from B' plus selected pure ORIGINAL 5-blocks; this is not just a vague extension-membership screen.

The six equations FORCE all THREE phi(h_d) to be identical and both phi(h_q) identical, with phi(h_d)=phi(h_y)+phi(h_q). Repeated H values remain separate original positions; there are six labelled windows but fewer independent scalar equations. The S052 fixed decoration h_y=h_q=0 and h_d∈{0,f2} **satisfies** all of them; its Delta remains 0 or -f2. Hence this is a precise genuine first-failure restriction on *other* original decorations, NOT a contradiction for the current fixed family, and NOT an all-window global test. The remaining r≥1 mixed changed-block paths, every alternative original index, and full G43 zero-freeness remain open.
