# S101 — Physical Fano horizontal rescue and surviving C3=1/3 constraints

16 October 2026. **CLM-0343: INTERNAL SAME_EXECUTOR, conditional hand proof; not independent or formal verification.** Entry main `7da04f8dc90d3653a45b79eeeaced4c67fbaa735`, genuine Git root tree `55865480c7151ed4ba732a65f15059be586192c0`. S100 was a genuine ordinary two-parent GitHub PR #103 merge, with exactly one authored PR commit `2ce4720c27c4176291580ccb3b30134badbd6388`. No numerical mathematical search, solver/CAS/SAT/ILP, Lean, Palomar, campaign, source promotion, external contact or publication.

## 1. SAME 59 physical original positions, not a detached parity picture

Work in `G=(Z/20)^3`, `H=(Z/10)^3`, with iota(h)=2h, `q=(0,0,1)` in the original quotient `G/2G`. Retain 22 ACTUAL labelled pairs with half-sums `U*=e1^8 e2^8 e3^6`, eight ACTUAL individual `g_j`, the original singleton `S=s_q`, and six ACTUAL singleton positions `X_i,Y_i` for i=1,2,3, with `V_i=X_i+Y_i`. Each V is a q-GROUP of TWO original singleton indices. The twelve pair-respecting q groups are S, eight g and three V; their total original G20 sum is (4,4,8). No V is appended to a Fano transversal: every Fano transversal contains one of its two original members.

Use the S098 exceptional exactly-five-flat case `z,z,z,z,z+2`, z=1 or11 in full G20, and assume ALL FIVE q flats are actual distinct FREE singleton q originals from `{S,g_1,...,g_8}`, disjoint from all six X/Y originals. Call the exceptional original e and the four ordinary originals f1,...,f4. Their actual horizontal G20 values are 0 or10, giving F2² colours `c(e)=D` and `c(f_i)=(A,A,B,C)`, with A,B,C pairwise distinct. Put `m=D+A` in F2² (binary addition); for h=1,2 set `K_h=6-5m_h` in H10, so `K_h=6` if m_h=0 and `K_h=1` if m_h=1.

The four genuine even Fano original transversals are `L_0={X1,X2,X3}`, `L_12={Y1,Y2,X3}`, `L_13={Y1,X2,Y3}`, `L_23={X1,Y2,Y3}`. Their legitimate even-G original half-sums `x_L=(sum L)/2∈H` obey S060 exact SAME-data identities `sum_L x_L=C=overline(V1+V2+V3)` in H, and `rho(x_ij-x_0)=Delta_ij=rho((V_i+V_j)/2)+r_i+r_j` in F2³. Here use the actual parity representatives `r1=(1,0,0), r2=(0,1,0), r3=(1,1,0)` (choice of the X/Y naming); none of these identities invents independent Fano values. The horizontal `C_1,C_2` are EVEN mod10 since each genuine V has q parity.

The E gate for genuine original Fano plus even subsets R of these five physically DISJOINT original free q positions is

`x_L+(sum_{r in R}r)/2∈E(U*)={h∈H: h1=1 OR h2=1 OR h3∈{1,2,3}}`.   (F)

Every failed (F) is a literal original 59-index proper zero by the complete-indexed-U-pair completion specified in §5. This is a NECESSARY part of 2048 Fano outsider tests and is not the 2046 pair-respecting q-group gates.

## 2. Exact five-free-flat Fano extension classification at t=0/1

S100 already proves that, if all the displayed genuine original Fano cuts (F) pass, each SAME physical `t=(x_L)_3` belongs to `{0,1}`. Here is a NEW exact classification of ALL even R chosen from those five originals, at each of these two residues.

Each nonempty even R is exactly one of: two ordinary leaves (third H shift1), exceptional+one leaf (shift2), four ordinary leaves (shift2), or exceptional+three leaves (shift3). This is true in full original G20 because z is 1 or11, so (2z)/2=z=1 mod10, (2z+2)/2=2, (4z)/2=2 and (4z+2)/2=3. For a 0/10 horizontal flat sum, the H horizontal shift is exactly 5 times its F2² XOR colour.

* If `t=0`, ALL nonempty even R have vertical H coordinate 1,2 or3 and are automatically admitted into E(U*). The EMPTY R has third0 and is admitted **if and only if** `x1=1 OR x2=1` in H10.
* If `t=1`, EMPTY R, two ordinary leaves, exceptional+one leaf, and four ordinary leaves have vertical coordinate1,2,3,3 and automatically pass. ONLY exceptional+three distinct ordinary leaves have vertical4 and need horizontal rescue. Their actual horizontal XOR colours form `T=D+(B+C)+{A,B,C}`. Because the one unoccupied colour among {A,B,C} is A+B+C, the unique missing colour of T is exactly `D+(B+C)+(A+B+C)=D+A=m`.

For fixed horizontal `x=(x1,x2)`, let `H_x={v∈F2²:x1+5v1=1 OR x2+5v2=1 mod10}`. This set has at most three colours. To contain T (three distinct colours), H_x must be exactly the complement of {m}, so for each coordinate its single rescuing bit must be `1-m_h`, requiring `x_h=1+5(1-m_h)=K_h`. Conversely with x_h=K_h, H_x is exactly the complement of {m}, so every e+three shift passes.

**Exact LOCAL iff:** conditional on the S100 restriction t∈{0,1}, all even genuine free-five Fano extension cuts (F) pass at L **iff** either `t=0 and (x1=1 or x2=1)`, or `t=1 and (x1,x2)=K`. This is not an iff for any of the OTHER free original g/S positions, V-overlaps, q matchings, pair splits or full G59.

## 3. A new whole physically original C3=3 exclusion family

Since all four genuine t lie in {0,1} and `C3=(V1+V2+V3)_3 mod10` is odd, the only S100 residues are C3=1 (exactly ONE t=1) or C3=3 (exactly THREE t=1). Suppose C3=3.

All THREE genuine Fano L with t=1 must have the SAME horizontal pair K (exactly, mod10), by §2. The ONE line L* with t=0 has horizontal
`x_{L*,h}=C_h-3K_h mod10` for h=1,2 by the SAME physical S060 C identity. Its EMPTY genuine Fano cut requires `x_{L*,1}=1 OR x_{L*,2}=1`. Thus for at least one h,
`C_h=1+3K_h mod10`.
But C_h is EVEN mod10, whereas `1+3K_h` is `9` when m_h=0, and `4` when m_h=1. Thus necessarily

`(m1=1 AND C1=4 mod10) OR (m2=1 AND C2=4 mod10)`.       (H)

This is exact full-mod20-original-data arithmetic reduced only AFTER the legitimate halves; C is the sum of the THREE ACTUAL V original pair totals, not an arbitrary horizontal variable. In particular if `D=A` (so m=00) AND C3=3, a proper original zero is unavoidable irrespective of all other V coordinates. More generally every true C3=3 datum violating (H) is excluded.

A SECOND INDEPENDENT necessary condition uses all three genuine S060 Delta parity equations. Put `v_i=(V_i)_h/2∈H10` for each horizontal coordinate h (legitimate, since V_i is horizontal-even G20), and `eta_i=( (V_i)_1/2 mod2, (V_i)_2/2 mod2 )+(r_i)_horizontal∈F2²`. Then the horizontal part of `Delta_ij=eta_i+eta_j`. Any THREE equal horizontal Fano parity values among the four force the FOURTH equal too, because the sum of four horizontal parities equals rho(C_horizontal)=00. Thus all three Delta horizontal vectors vanish and

`eta_1=eta_2=eta_3`.                                        (D)

If the TRUE physical V data violate (D), at least one t=1 genuine Fano line has horizontal x≠K, so an exceptional+three REAL free-singleton cut fails (F). No fictitious independent Fano values were used.

**CLM-0343(a):** In the exceptional all-five-original-free (2,1,1) physical class, C3=3 together with failure of EITHER concrete (H) or (D) forces a nonempty PROPER original G20 zero by §5. This removes further C3=3 subfamilies genuinely beyond CLM-0342, including **ALL** C3=3 data with D=A. The residual C3=3 family satisfying BOTH (H),(D) is OPEN, not asserted feasible.

## 4. C3=1: a further actual Delta parity-square necessary condition, NOT a universal contradiction

If C3=1, EXACTLY one of the same four actual Fano lines has third1 and horizontal K, so its horizontal parity vector is precisely m (as K_h is odd iff m_h=1). The remaining three actual lines have third0 and must each have at least one horizontal coordinate equal to1 by §2, hence each has NONZERO horizontal parity vector. Their three horizontal parity vectors sum to m in F2², since rho(C_horizontal)=00.

In the especially transparent physical subfamily `m=00` (the exceptional horizontal colour D equals repeated ordinary colour A), the three nonzero vectors summing to0 MUST be exactly `01,10,11`, in some order. Hence the FOUR real Fano horizontal parity vectors must be the ENTIRE square F2², and the actual S060 pair-difference vectors `Delta12_horizontal,Delta13_horizontal,Delta23_horizontal` must be precisely the three distinct nonzero vectors. Equivalently the three TRUE `eta_1,eta_2,eta_3` must be pairwise distinct.

**CLM-0343(b):** If C3=1, D=A and two real eta_i coincide, the five-free-flat Fano gates fail, giving a real proper original zero as in §5. With m≠00, any actual t=0 Fano line having horizontal parity00 likewise fails the empty original Fano cut. **If eta_1,eta_2,eta_3 are pairwise distinct, the m=00, C3=1 parity-square escape survives these local necessary tests.** No claimed actual complete G59 model, full q matching, exterior slab or signed split feasibility follows.

## 5. Literal original indexed zero selection and failure audit

For any excluded true 59-original datum, identify the real Fano L whose §2 exact local condition fails. In the (H) obstruction at C3=3, the unique t=0 L* has neither horizontal coordinate1, so R=EMPTY itself fails. In the (D) obstruction, one of the three actual t=1 Fano L has horizontal x≠K, so choose one of its FOUR ACTUAL e+three-distinct-ordinary-leaf original-index sets R with XOR colour outside H_x; such an R must exist by the exact three-colour covering argument, and its vertical resulting coordinate is4. In the C3=1 eta-repetition obstruction, one of the three true t=0 lines has horizontal parity00 and therefore neither horizontal coordinate1: again take R=EMPTY.

In every case R consists of ZERO or FOUR actual free S/g singleton original indices, disjoint from the three actual X/Y original indices of L. Put `h=x_L+sum(R)/2` in H, outside E(U*); define `k_j=-h_j mod10` represented in 0..9. Since h∉E(U*), `0<=k1<=8, 0<=k2<=8, 0<=k3<=6`. Take BOTH actual original endpoints of k1 of the first eight indexed e1 pairs, k2 of the next eight e2 pairs and k3 of the final six e3 pairs. Then the genuine original-index support
`W=L ∪ R ∪ ⋃ selected {a_i,b_i}`
has total G20 sum `2h+2∑k_j e_j=0`, contains L and hence is nonempty, and omits the three original X/Y complements of L and hence is proper. It has at most `3+4+44=51<59` distinct original positions.

**Hostile boundary:** (H) and (D) are only NECESSARY, not jointly sufficient for 2046 proper q grouped tests, 2048 original Fano residual tests, full S060 F_*/P_q/I/alpha deletion E(U\\I), original non-q endpoint/signed multi-splits, seven p channels plus p000, 26 hubs/P26, FULL8/exact12/13+, arbitrary U22/G59, G58 zero-free or D(C20³)=58. All stay OPEN. V-overlap still prohibits appending V to L; no overlap case was solved. The local iff in §2 does NOT upgrade to global original-model feasibility. Phase1 HOLD, CAM-0001 PROPOSED NOT_RUNNING BLOCKED; source29/frontier30 immutable; CI ABSENT_NOT_PASS.