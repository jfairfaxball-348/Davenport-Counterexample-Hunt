# S061 — The 64 singleton lifts form a three-class order-two obstruction triangle

14 October 2026. **INTERNAL Phase-1 original-index SYMBOLIC mathematics**, restricted to the conditional canonical C20³ 22+8+7 configuration of S060. CLM-0223 and CLM-0224. Not a universal nonexistence theorem; no numerical mathematical search, CAS, SAT/ILP, orbit/candidate generation, Lean, Palomar, source promotion, paper or contact.

## 1. Exact existing data and new target

Write G=(Z/20)^3, H=(Z/10)^3, Q=G/2G=(F2)^3; iota(h)=2h identifies H with the even subgroup 2G. Fix the 22 **original indexed** (a_i,b_i), U=(iota^{-1}(a_i+b_i)), eight original g_j of parity q!=0, original S=s_q, and the q-coset singleton totals V_i=X_i+Y_i (i=1,2,3), where pi(X_i)=r_i, pi(Y_i)=r_i+q, and r_3=r_1+r_2 in Q. The r_i images form the three nonzero elements of K=Q/<q> (an F2-vector space of dimension two). Fix full total(T)=0.

Fix an ACTUALLY FEASIBLE four-tuple (x_0,x_12,x_13,x_23) of q-avoiding Fano H line values satisfying BOTH S060 CLM-0222's full-H sum and three binary differences. Choose one original singleton realization T^0, leaving all non-singleton original labels/values fixed. There are precisely 2^6 other-or-same original singleton realizations with the same four values, fixed individual parities, and fixed V_i. Their effect on the otherwise unresolved non-q pair-split tests is the subject of this theorem. A feasible four-tuple in F_* means q-split tests additionally pass IF S060 matching premises hold, but this paper does NOT assume they imply any non-q test.

## 2. CLM-0223: the exact linear order-two action on original subsets

**Theorem (lift fibre action).** All 64 original singleton lifts of the fixed four-tuple are *uniquely* indexed by eta_1,eta_2 in Q, setting eta_3=eta_1+eta_2. At lift eta replace BOTH original singleton values X_i,Y_i by X_i+10 eta_i, Y_i+10 eta_i in G (coordinatewise, viewing 10eta_i as an order-two element). No other original value is changed. Each V_i and all four genuine Fano line totals remain **exactly** fixed in G; their H values are unchanged. Conversely every realization of the fixed four-tuple arises in this way.

For any nonempty proper set Z of the 59 ORIGINAL labelled positions whose G-parity is zero, let I(Z) be the original pair indices i for which Z selects exactly ONE of a_i,b_i; put
  sigma(Z) = [sum_{i in I(Z)} t_i] in K,  t_i=pi(a_i)=pi(b_i).
Then, for one uniquely determined F2-linear map
  ell_eta: K -> Q,
with ell_eta([r_1])=eta_1, ell_eta([r_2])=eta_2 and ell_eta([r_3])=eta_1+eta_2, the original G-subset sum at lift eta is
  sum_G(Z;eta) = sum_G(Z;0) + 10 ell_eta(sigma(Z))       (in G).       (A)
Thus all parity-even proper indexed subset sums in the **same split-parity class** sigma change by the same order-two G translation. Every Z with sigma(Z)=0 is INVARIANT across all 64 lifts, even if I(Z) contains non-q pairs whose parities cancel modulo <q>. In particular every q-only split test is invariant, as demanded by CLM-0221, but q-only splits are not the whole sigma=0 class.

**Proof.** S060's map from three H singleton adjustments z_i to the four H Fano line adjustments has mod-5 kernel zero and mod-2 kernel z_1+z_2+z_3=0, dimension six. Its kernel therefore consists exactly of z_i=5eta_i in H, eta_i in Q with eta_1+eta_2+eta_3=0. Changing X_i by iota(z_i)=10eta_i changes Y_i by its negative, equal to +10eta_i because 10eta_i has order at most two. Both fixed totals V_i are unchanged; each Fano triple contains one singleton from every coset, hence changes by 10(eta_1+eta_2+eta_3)=0 in G. The 64 choices are distinct original index-labelled lifts, and S060's exact kernel proves exhaustiveness.

For a selected original subset Z write m_i in F2 for whether precisely one of X_i,Y_i occurs in Z. The only changing values are these six, so its G-sum changes by 10 sum_i m_i eta_i. Reduce the ORIGINAL parity equation pi(sum_G(Z))=0 modulo <q>. Every selected full original pair has parity zero; each selected split original contributes t_i; every g_j, S, and every two-selected q-coset singleton group contributes 0 modulo <q>; an exactly-one-selected singleton in coset i contributes [r_i]. Therefore
  sum_i m_i [r_i] = [sum_{i in I(Z)} t_i] = sigma(Z)  in K.
Because [r_1]+[r_2]+[r_3]=0 is the ONLY linear relation among these three K classes and eta_1+eta_2+eta_3=0, the sum_i m_i eta_i equals ell_eta(sigma(Z)), proving (A). This uses actual original parity before any division by two. QED.

## 3. CLM-0224: exact torsion-danger sets and three-set triangle test

Let W be the full 59 original positions. For each sigma in K define the **indexed forbidden torsion subset**
  C_sigma = {v in Q : exists NONEMPTY PROPER Z subset W with pi(sum_G(Z;0))=0,
               sigma(Z)=sigma, and sum_G(Z;0)=10v in G}.
Values of different Z and repeated G coordinates are NOT conflated with original-index subsets. Only elements in the order-two subgroup G[2]={10v:v in Q} can occur here. This definition is a symbolic finite set, not a mathematical instruction to enumerate candidates. Let B_sigma=Q\C_sigma for the three nonzero sigma.

**Theorem (full original minimality on a fixed Fano four-tuple).** Among the 64 legitimate original singleton lifts, a minimally zero-sum original T59 EXISTS if and only if BOTH:
 (i) 0 is not in C_0;
 (ii) there exist a in B_[r1], b in B_[r2] with a+b in B_[r3].
Equivalently B_[r3] intersects B_[r1]+B_[r2] in Q. This test covers **ALL** one/multi original pair splits of EVERY nonzero t_i, not just t_i=q, and every original singleton/g configuration; it is conditional on the fixed four-tuple and other original values, not a universal existence assertion.

**Proof.** Adding 10ell_eta(sigma) never changes any subset sum modulo 10 in G. If an original proper parity-even Z has sum not in G[2], it is impossible for it to become zero in ANY lift; conversely every zero sum at some lift comes from a reference sum 10v, necessarily v in C_sigma. For such Z, equation (A) reads 10(v+ell_eta(sigma)). It vanishes EXACTLY when v=ell_eta(sigma) in Q. For sigma=0 this happens for every lift precisely when 0 belongs to C_0. For each nonzero sigma, avoiding all zeros is equivalent to ell_eta(sigma) lying in B_sigma. A linear map K→Q is freely determined by a=ell_eta([r1]) and b=ell_eta([r2]) (8 choices each); its third value is a+b. Every such pair corresponds to exactly one of the 64 legitimate lifts. Hence (i),(ii) are jointly necessary and sufficient for **no nonempty proper original G zero subset**. The fixed total(T)=0 is preserved by the lift, so this is exactly minimality. QED.

**Complement hostile audit.** Because sum_G(W;0)=0, the nonempty proper ORIGINAL complement W\Z has the same split index set I(Z), the same sigma, and opposite G sum. For torsion witnesses -10v=10v, so Z and its original complement witness the SAME element v of C_sigma. Properness and index disjointness are preserved. This validates complementary exclusions without treating the empty or full original set as forbidden.

**Immediate sharp structural consequences.**
* Modulo-10 invariance: ONLY reference proper subsets summing to 0 modulo 10 in G can ever threaten any of the 64 lifts; a non-torsion even subtotal is harmless for this specific fibre question. This does not assert those dangerous sets are few.
* One reference witness in class sigma!=0 at torsion value 10v forbids precisely those eight of 64 lifts with ell_eta(sigma)=v. One class-zero proper sum=0 forbids ALL 64 lifts; class-zero nonzero torsion subtotal never changes to zero. Multiple witnesses must be combined by the triangle condition, not added as independent costs.
* A universal obstruction certificate for all 64 lifts is exactly: (a) 0 in C_0 OR (b) B_[r3] disjoint from B_[r1]+B_[r2]. If the latter holds, every eta yields a genuine original proper zero witness belonging to at least one of the three nonzero split classes. Neither alternative was proved to hold for arbitrary allowed U22.
* If |B_[r1]|+|B_[r2]|>8 and B_[r3] is nonempty, the triangle condition **automatically holds**, by the pigeonhole identity B1+B2=Q. This is only a useful conditional sufficiency test and does not construct compatible F_* data or resolve Davenport.

## 4. Full H parity stratification of S060's four-point gate

As a second exact reformulation, let rho:H→Q be reduction mod2 and let p_ij=Delta_ij from S060, with p_0=0. For c in Q define F_c={h in F_*:rho(h)=c}, and let M_c be their images in H/5? **Use the correct mod-5 projection** lambda:H→(Z/5)^3, which is bijective when restricted to each fixed parity fibre F_c (by CRT). Set A_c=lambda(F_c). Write d=lambda(overline(V1+V2+V3)). Then the original S060 four-point feasibility gate is exactly:
  There exists c in Q with
    d in A_c + A_(c+Delta12) + A_(c+Delta13) + A_(c+Delta23)  in (Z/5)^3.      (B)
The mod2 parity of the required full-H sum is automatically right because
  Delta12+Delta13+Delta23
   =rho(iota^-1(V1+V2)+iota^-1(V1+V3)+iota^-1(V2+V3))
   =rho(overline(V1+V2+V3)),
and each of the four selected fibre parities sums to that value (4c=0). Hence CRT makes (B) both necessary and sufficient for the exact H sum and all Delta differences, not just for a coarse fourfold sum inclusion. Unlike the earlier independent-line shortcut, (B) enforces the SAME base c across all four fibres. No such Minkowski sum was shown universally empty, and the source-stated extremal matching implications alone cannot justify its emptiness.

## 5. Boundary, attempted inference killed and exact future bridge

This session tried to push S060's common F_* constraint to an arbitrary-U22 contradiction through (B), the S058 source-conditional common 25-index kernel basis and the expanded q matching family. No universal inverse classification of E(U\I) or bound proving (B) empty followed. The S059 q-matching-only model already demonstrates why matching extremality by itself cannot force a contradiction, and its fixed V_i fibre is already killed by the S050/S051-type slab; this is NOT a new example and NOT a general argument.

The new genuinely indexed action (A) and triangle criterion are exact for all non-q splits, but they do **not** eliminate C_0's mixed split cancellations or force the forbidden sets to cover K→Q. They clarify the exact remaining proof target: for EVERY arbitrary canonical actual dataset obeying every S060 q-hub matching and F_* affine gate, prove 0∈C_0 or B_[r3]∩(B_[r1]+B_[r2])=empty; OR rigorously exhibit an actual indexed total-zero G59 nonminimal model passing the q-only conditions, localise its first offending mixed split, and do not pass it off as a Davenport counterexample. Independently, proving canonical profile coverage from all hypothetically minimal T59 still requires treating three-hub and alternate (0,4),(0,6),(1,7) quotient profiles. No universal theorem, D(C20³)=58 proof, or G58 zero-free candidate was obtained.

All counts are **closed finite-group algebra**, not numerical mathematical search. Sources SRC-0008/0015/0023 stay SOURCE_STATED as recorded, in particular computational D3(C5³)=25 remains unverified; original source28 and frontier30 records unchanged. Same-executor internal adversarial proof review only.
