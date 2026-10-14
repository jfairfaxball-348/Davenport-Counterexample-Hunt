# S057 — EXACT full C10³ Fano-line realisation (CLM-0212)
14 October 2026. One symbolic, original-index proof in the conditional C20 setup. Completes the isolated seven-singleton value-realisation question; NOT a T59 or composite Davenport proof.

Let G=(Z/20)^3, H=(Z/10)^3, iota(h)=2h, Q=(F2)^3. The seven DISTINCT ORIGINAL singleton positions s_r (r in Q\{0}) have prescribed quotient parities r. Label the seven Fano lines L_ell={r !=0 : ell(r)=0} by ell in Q*\{0}. For any desired SEVEN FULL H values y_ell in H, ask for iota(y_ell)=sum_{r in L_ell}s_r. Let bar(y) denote mod2 in H. Define the tensor T(y)=sum_ell bar(y_ell) tensor ell in End_F2(Q).

**IFF theorem.** There exist seven original C20 singleton values s_r with the prescribed individual quotient parities and ALL seven full H line sums y_ell if and only if
    T(y)=I_Q.                                                    (1)
This is precisely the S052 CLM-0198 NECESSARY coherent tensor condition, here upgraded to SUFFICIENCY for the isolated singleton subsystem. It does not make that condition sufficient for pair blocks, g-outsiders, H28 atoms or full G minimality.

Proof. Take each r's fixed coordinatewise 0/1 lift tilde(r) in G. Each line has binary XOR zero, so coordinatewise the ordinary INTEGER sum over its three tilde(r)'s is even. Put k_ell=(sum_{r in L_ell}tilde(r))/2, an integral 0/1 vector, interpreted in H. Every original s_r with quotient r is uniquely s_r=tilde(r)+2x_r for x_r in H. Thus y=k+Nx in H^7, with Fano 7x7 point-line incidence N_{ell,r}=1 iff ell(r)=0.

Modulo5, N^T N=2I+J and JN=3J, hence N^{-1}=3N^T-J over F5 as proved in S056 CLM-0211: NO mod5 obstruction. Modulo2,
    (Nx)_ell = sum_r x_r + ell(sum_r x_r r),
an affine-linear function of ell (coordinatewise). The image consists of ALL restrictions to the seven nonzero ell of affine-linear functions: constants come from three original point indices r1,r2,r3 with r1+r2+r3=0 and all three x coefficients 1; any linear form ell(v) comes from two different nonzero r1,r2 with r1+r2=v, their coefficients 1. Hence the F2-rank of N is 4 per coordinate.

For scalar-valued seven-tuples z_ell define F(z)=sum_ell z_ell ell in Q*. Its rank is 3 because the seven ell span Q*. Every affine-linear z_ell=a+ell(v) lies in ker F: sum_ell ell=0 and sum_ell ell_i ell_j=0 over F2 (four appearances for diagonal, two off-diagonal). Therefore im N=ker F, both dimension4. Coordinatewise for Q-valued seven-tuples, im N is EXACTLY ker T.

For canonical k, the four lines not containing any fixed q≠0 each include every point r≠q twice and q zero times. Thus sum_{ell(q)=1} k_ell = sum_{r≠q}tilde(r) as integer vectors, and mod2 this is q (the XOR of all seven nonzero r is0). Therefore T(k)(q)=q for every q, i.e. T(k)=I. Consequently the mod2 equation Nx=y-k is soluble exactly when T(y)=I. Combine its mod2 solution with the UNIQUE mod5 solution via CRT for x mod10. Finally set original s_r=tilde(r)+2x_r modulo20. This proves BOTH directions without identifying G with Q direct-sum H.

**Exact fibre statement.** For EACH admissible y there are precisely 2^9 distinct labelled original seven-singleton choices s_r: the kernel of N modulo2 has dimension3 PER H coordinate, while its kernel modulo5 is zero. There are 2^12*5^21 attainable full seven-line H tuples (7 line slots, 3 coordinates), all and only those satisfying (1). These are linear rank counts, NOT numerical/orbit/candidate enumeration.

**Hostile audit.** Identity (1) is essential; seven independently chosen mod5 values alone are not enough. Complementary cap values are forced by the total singleton H sum. Actual s_r are distinct INDEX POSITIONS even if values collide. The proof uses s_r=tilde r+2x_r and CRT only in H=C10, NOT a false splitting C20=C2 direct-sum C10. The four-line moment in S052 is prior necessary content and is not claimed new. Neither U22, g_j, all 4096 one-split tests, 2048 mixed odd-J, all |I|>=2, 735 atom tests nor three-hub patterns are addressed by the singleton realisation alone. INTERNAL symbolic proof, no original-source access change.