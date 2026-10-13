# S042 — Non-split Fano lift reconstruction and affine-span obstruction

13 October 2026. One internal Phase-1 symbolic proof session continuing S041 CLM-0151/0152. The group C20^3 is NOT C2^3 direct-sum C10^3: the exact sequence 0 -> C10^3 -> C20^3 -> C2^3 -> 0 is non-split. Historical D(C10^3)=28 remains SOURCE_STATED.

## CLM-0158 — exact, parity-TWISTED K4 lift compatibility

Let G=C20^3, K=2G, identify K with H=C10^3 by the isomorphism iota(h)=2h (coordinates modulo20). A putative n20 58-position zero-sumfree sequence has six residual SINGLETON original terms s_ij in G whose mod2 classes are the six nonzero vectors of F2^3 other than w. Index them by the six edges ij of K4 so that the four Fano triples avoiding w are K4 stars and the three Fano quadruples are the K4 crosscuts. Write c_ij= s_ij mod2; c_ij are SIX DISTINCT nonzero Fano classes, the four star sums vanish, the three opposite-edge sums equal w, and sum of all six c_ij=w.

Define t_i in H by iota(t_i)=sum_{j != i}s_ij in G; define q_{ij|kl} in H by iota(q)=s_ik+s_il+s_jk+s_jl, with split ij|kl equal to 12|34,13|24,14|23. These are well-defined because each corresponding collection has even mod2 sum.

Set T=sum_i t_i, Q=q_12+q_13+q_14. Double-incidence in ORIGINAL G gives T=Q in H and, critically,

  d_ij := t_i+t_j-q_{ij|kl} = s_ij (mod 10) in H.

The right-hand identity is obtained by applying iota: iota(d_ij)=2s_ij in G. It is NOT 2a_ij for some arbitrary edge a_ij in H. Thus the correct conditions in H/2H=F2^3 are

  bar(d_ij)=bar(t_i)+bar(t_j)+bar(q_split)=c_ij,

for all six specified labelled edge classes, and T=Q. In particular bar(T)=bar(Q)=w, NOT ZERO. Treating the original singleton edge as a C10^3 kernel element would incorrectly drop the non-split carry, create false 'even' constraints and an invalid seven-class conclusion.

**Exact converse for the Fano equations only.** Fix the six edge parity classes c_ij as above. Given seven proposed values t_i,q_split in H, there exist six original singleton elements s_ij in G with these parity classes and producing EXACTLY those seven Fano kernel sums if and only if (1) T=Q and (2) bar(d_ij)=c_ij for every edge. Necessity was proved above. For sufficiency, choose s_ij in G reducing modulo10 to d_ij (possible with parity c_ij by (2)). Since sum_j d_ij=3t_i+(T-t_i)-Q=2t_i modulo10, the discrepancy Delta_i=iota(t_i)-sum_j s_ij in G lies in {0,10}^3, the order-two subgroup. All star sums have even mod2 because the c-star is a Fano line. Sum_i Delta_i=iota(T)-2sum_edges s_ij=0, because sum_edges d_ij=3T-2Q=T modulo10. Add Delta_i to edge s_i4 for i=1,2,3. Each chosen edge remains in the required mod10 class and has the same mod2 class. The vertex 1,2,3 star sums are corrected, and the vertex4 sum is corrected because Delta_1+Delta_2+Delta_3=-Delta_4=Delta_4 in the order-two subgroup. Then all four star sums give the desired t_i; each crosscut q follows from iota(q)=iota(t_i+t_j)-2s_ij and d_ij=t_i+t_j-q. QED.

This is a necessary-and-sufficient realization of the SEVEN labelled quotient-block equations by six residual original singletons; it does NOT realize the 26 parity pairs, nor prove the complete 58-term lift zero-sumfree.

## CLM-0159 — the valid affine-span theorem for n20 extensions

Continue S041 conditional n20 pairing: zero-sumfree P26 in H=C10^3 and seven values t_i,q_split in E(P)={x: P*x zero-sumfree}. Define bar E as the mod2 image in H/2H=F2^3.

**Theorem.** If such an S58 existed, the AFFINE span of bar E would be all F2^3. In particular bar E spans the full three-dimensional VECTOR space and contains at least FOUR distinct residue classes. This is necessary, NOT a proof that such an extension set exists or a Davenport equality.

Proof. By CLM-0158, all six prescribed nonzero edge classes c_ij are sums of three elements in bar E: c_ij=bar(t_i)+bar(t_j)+bar(q_split). The six c_ij span F2^3, so the linear span of bar E must be F2^3.

If the affine span of bar E were a proper affine subspace, it would lie in some affine hyperplane chi(x)=epsilon for a nonzero linear chi:F2^3->F2, epsilon in F2. If epsilon=0, bar E lies in ker chi, contradicting full linear span. If epsilon=1, then chi(bar T)=4*1=0, while chi(bar Q)=3*1=1, contradicting T=Q. Hence its affine span is full. At least four affine-independent elements are necessary in a three-dimensional affine space. QED.

**Sharp parity reverse test, not an actual E(P).** Choose independent A,B,C in F2^3, omitted w=A+B+C, and label
 c12=A, c13=B, c23=C, c14=A+B, c24=A+C, c34=B+C.
Set three q residues all equal to w, and four star residues
 beta1=w, beta2=A, beta3=B, beta4=A+B.
For every edge, beta_i+beta_j+bar(q_split)=c_ij; both the four-beta sum and three-q sum are w. The set {w,A,B,A+B} has just FOUR nonzero residue classes but affinely spans F2^3. It satisfies ALL labelled mod2 compatibility conditions. Therefore the tempting assertion 'if 0 is absent, all seven nonzero classes must occur' is FALSE. Do NOT carry that claim forward. Actual C10-valued t/q and a zero-sumfree P are NOT asserted by this parity-only test.

**Another hostile check:** in a split, artificial K4 system one would get T in 2H and q=t_i+t_j modulo2, but here the correct T parity is the omitted Fano residue w !=0. Any proof which forgets the original C20 singleton lifts loses the carry and is invalid.

**Remaining inverse premise:** Rule out every affinely spanning bar E(P), or show the actual seven labelled H-valued elements cannot meet the SIX congruences plus exact T=Q for any eligible P26. A mere 4E(P) intersect 3E(P) is not sufficient to realize those labelled equations, and the new affine-span criterion alone is not contradictory.
