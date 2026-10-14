# S056 — independent mod-5 freedom of seven Fano line block values (CLM-0211)
14 October 2026. Original-index, symbolic matrix inversion. This isolates why the seven Fano line/cap H-valued gates do not themselves impose a new mod5 relation. NOT an inverse theorem for extremal H28 atoms, nor a C20 Davenport endpoint.

Let Q=F2³, and let the seven original singleton positions s_r∈G=C20³ be indexed by the seven r∈Q\{0}, with π_G(s_r)=r. Let L range over the seven three-point Fano lines. Each line sum lies in iota(H)=2G, so define h_L=iota⁻¹(Σ_{r∈L}s_r)∈H=C10³. Reduction H→F5³ will be denoted by overbar.

**Theorem: the seven mod-5 vectors (h_L mod5) can be prescribed ARBITRARILY and INDEPENDENTLY, while fixing each original quotient parity π_G(s_r)=r.** More precisely, for any seven desired y_L∈F5³, there are original G positions with these specified parities and overline(h_L)=y_L. There is no implication that such choices satisfy U22 extension/minimality requirements.

**Proof.** Index the seven original singleton classes and the seven Fano lines and form the 7×7 incidence matrix N, N_{Lr}=1 when r∈L and 0 otherwise. Each line has 3 points; two distinct lines intersect in precisely one nonzero point; every point belongs to 3 lines. Consequently NᵀN=2I+J and JN=3J, where J is the all-ones matrix. Over F5 we have
  (3Nᵀ−J)N=3(2I+J)−3J=6I=I.
Thus N is invertible over F5 with inverse 3Nᵀ−J. The line equations reduced mod5 read N(overline(s_r))_r = (2 y_L)_L, since iota(h)=2h in original G. There is a UNIQUE solution
  overline(s_r)= 3 Σ_{L∋r}2y_L − Σ_L2y_L
               = Σ_{L∋r}y_L +3Σ_L y_L    (mod5).
Choose each coordinate of original s_r mod20 to have this mod5 value and its prescribed mod2 value r. Such a choice exists by the ordinary CRT for the **two congruences mod5 and mod2**, since they are coprime. We do not split C20 as C2⊕C10; only residues of original G elements are specified. By construction every line sum is even and has mod5 value 2y_L, so overline(h_L)=y_L. QED.

**Coherence still remaining.** Let S=Σ_r s_r=iota(c_s) (seven distinct nonzero parities sum 0). The complementary cap value is h_{Lᶜ}=c_s−h_L, so fourteen line/cap values are NOT independent. Further, for any hub parity r, the THREE lines through r use its original index three times and the six other originals once. Consequently
  Σ_{L∋r}h_L=c_s+(s_r mod10) in H.                       (5)
Reducing mod2 shows the seven line values must satisfy the Fano pencil/tensor constraint already recorded in S052 CLM-0198; mod5 alone cannot supply its replacement. This illustrates a clean separation: seven arbitrary mod5 line values can be realised in the original indexed singleton subsystem, while mod2 coherence, the eight-g edge normal form and the actual H-extremal atom/one-and-multi-split tests are still genuinely coupled.

**Reverse check.** The inverse formula is a finite FIELD-LINEAR identity, not computational enumeration. It does NOT assert arbitrary FULL H line values (mod10), arbitrary fourteen line/cap values, or existence of a zero-free G58 or minimally zero-sum T59. S052's earlier mod2 coherent tensor is acknowledged rather than claimed as new. No original source proof inspected; no D(C15³)=43/D(C20³)=58 outcome.
