# S039 — Continued A/B/C attack and precise proof-obstruction dossier

2026-10-13. This is the continued geometry component of the SAME S039 session, after the independent multiwise endpoint in `S039_MULTIWISE_DEFICIT_REMOVED.md`. It records substantive attempts on A, B and C, including joint synthesis, failed strengthening and reverse-direction tests. The independent D route succeeds; the balanced-only Psi route does not close. No mathematical instance search, CAS, solver, candidate/orbit enumeration or author code was used.

## Standing hypotheses and statuses

For p>=7 prime, N=3p=2b+1, b=(3p-1)/2, a=b-1, s=(-1)^b, t=(p+s)/2. Assume an ACTUAL indexed zero-sum Z=(z_i) in F_p^3 with no nonempty zero sum of <=a positions. F is the COMPLETE indexed b-zero-sum family, m=kp>=2p, F_i its neighbourhood at i, r_i=t+p j_i, lambda and tau its pair/triple codegrees. Critical Psi is the actual polynomial coefficient, not an abstract freely assigned tensor. Previous proved identities: Psi_ijk=-1/2+s(lambda_ij+lambda_ik+lambda_jk-2tau_ijk), scalar pair sum s(lambda_ij-t), vector pair sum 0, star -1/8, total triple sum 0, and four-index exchange. Every nonempty pair support has >=3 active projective directions, by S037. No universal positive lambda, strict three-deletion CW or blanket noncancellation is assumed.

## Front B: equal-weight rows also have equal VECTOR sums

A contained adjacent-level pair F_i subset F_j with r_j-r_i=p leaves exactly p additional distinct b-blocks, all containing j and avoiding i. On the other N-2 positions their incidence rows have common weight b-1 and common vector sum -z_j. If h columns vary, strip the constant columns; the p distinct variable row subsets have a single common weight w, 1<=w<=h-1, AND a common sum C. Psi_ijk=s mu_k, where mu_k counts extra rows containing k, so variable columns are exactly active witnesses. This holds for any m, provided the contained degree gap is exactly p.

S038 used only equal weight; equal vector sum plus the S037 direction condition gives stronger small-boundary restrictions.

## CLM-0145 — contained adjacent pairs need six / seven witnesses, with actual mixed-support sandwiches

**Theorem, local part.** At p7 any such contained adjacent pair has h>=6 active third-index witnesses; at p13 it has h>=7. Thus for the m=2p low/high census, writing F_c for the number of mixed containment pairs, W_mix for NONZERO Psi triples meeting both levels, and W for all NONZERO triples,

   2 W_mix >= 3LH+3 F_c       (p7),
   2 W_mix >= 3LH+4 F_c       (p13),
   W >= W_mix.

Consequently p7 W>=156+ceil(3F_c/2), and p13 W>=570+2F_c. With F_c=0 the previous 156/570 unconditional bounds remain; this is not a new opposing upper or a contradiction.

**Proof at p7.** S038 already gives h>=5. If h=5, weights 1 or4 admit at most five distinct row subsets; weight3 reduces by complementation in the variable columns to weight2, without changing equality of sums. So seven distinct pairs of five labelled variable positions must have one vector sum C. All five vector VALUES cannot be equal: all active witnesses would then be in one projective direction, contradicting S037. Choose two positions with different vectors u and v, leaving three labelled others.

At most three pairs use neither u nor v; at most one uses both. For each of the other three positions, at most one of its pairs with u and v can have sum C (otherwise u=v). Hence at most 3+1+3=7 equal-sum pairs. To achieve seven, all three pairs among the other positions must occur, forcing their vectors to be the same r and C=2r. The pair {u,v} must occur, so u+v=2r. Any required cross pair forces u+r=2r or v+r=2r, thus u=r or v=r and therefore both are r, contradiction. The maximum is <=6. Seven distinct rows are impossible; h>=6. No ordering or positivity on field values is used.

**Proof at p13.** S038 gives h>=6. At h=6, weights 1 or5 have <=6 possibilities; weights 2 or4 have <=11 if two vector values u!=v occur: classify by neither/both/exactly one, obtaining 6+1+4=11. All-equal values are excluded by S037 as above. It remains w=3. Choose differing u,v and leave four labelled other vectors. At most four triples contain neither u nor v, at most four contain both, and at most six contain exactly one (at most one for each pair of the four others). Thirteen equal-sum triples would require at least seven from the first two categories, so one category has all four and the other at least three. Having all four in EITHER category forces the four remaining vector values to equal r: either subtract their triple sums or compare their singleton contributions alongside u,v. The other category, being nonempty, then gives C=3r and u+v=2r. But any exactly-one triple would require u+2r=3r or v+2r=3r, forcing u=v=r. Thus that category is empty, contradicting thirteen triples. So <=12 possibilities; h>=7.

The mixed-incidence count is EXACTLY 2 W_mix: a mixed triple has exactly two mixed edges and a monochromatic triple has none. Other mixed pairs have >=3 witnesses by S038/S037. Sum their requirements and the improved contained-pair requirements. QED.

**Hostile reverse test / sharpness of LOCAL row conditions.** These six/seven minima cannot be improved solely from common row weight, common vector sum, nonzero values, three projective directions and no short zero sum inside the variable columns. This is a proved local countermodel, NOT a complete Z or Davenport candidate. Take independent u,v.

At p7 use six labelled columns with vectors u,u,u,u,u+v,u-v. The six pairs among the four u-columns plus the pair {u+v,u-v} give exactly seven distinct weight-two rows with sum 2u. Every column varies: each u-column occurs in three of the seven rows; each special column in one. Three projective directions occur. A functional with ell(u)=1, ell(v)=0 gives value 1 at each column, so every nonempty subset of these six columns has nonzero functional sum (its length is 1..6, less than 7).

At p13 use seven columns u,u,u,u,u,u+v,u-v. Ten triples among the five u-columns and five triples consisting of the two special columns and one u-column all have sum 3u. Keep all five latter triples and any eight of the former ten: thirteen distinct weight-three rows. Every u-column occurs at least once and at most seven times; each special column occurs five times, so all seven columns vary. The same functional excludes every nonempty zero sum on these seven columns since 7<13, and three directions occur. These witnesses only refute a stronger LOCAL variable-row minimum. A full indexed b-block family, constants, total Z and exclusion of every mixed short zero sum are not supplied. No lift is claimed.

## Front A: derive an opposing bound on the SAME mixed quantity

**Theorem, upper part of CLM-0145.** For m=2p use the actual low/high partition. For each projective functional X, H_X={i:<X,z_i>=0}, h=|H_X| and r=|H_X intersect LOW|. Define C(h,r) as the number of mixed deletion triples containing H_X:

| Zero-fibre | C(h,r) |
|---|---:|
| h=0 | LH(N-2)/2 |
| h=1,r=1 | H(L-1)+binom(H,2) |
| h=1,r=0 | L(H-1)+binom(L,2) |
| h=2,r=2 | H |
| h=2,r=1 | N-2 |
| h=2,r=0 | L |
| h=3,r=1 or2 | 1 |
| h=3,r=0 or3 | 0 |
| h>=4 | 0 |

Then W_mix<=U_mix:=sum_X C(h_X,r_X). Also let ell_alpha and h_beta be the sizes of equivalence classes of identical block neighbourhoods within LOW and HIGH. Then

   W_mix <= T_twins
     := H[binom(L,2)-sum_alpha binom(ell_alpha,2)]
        +L[binom(H,2)-sum_beta binom(h_beta,2)].

Thus at p7/p13 the genuine joint necessary condition is

   (3LH+(h_star-3)F_c)/2 <= W_mix <= min(U_mix,T_twins),
   h_star=6 at p7 and 7 at p13.

**Proof.** S032's exact projective coefficient sum has a nonzero term only when H_X is contained in the three deletions; a NONZERO Psi implies at least one such term. Count mixed triples containing each ACTUAL H_X. For h0 use binom(L,2)H+L binom(H,2). For a singleton low, the other two are either one other low and one high, or two highs; the high singleton case is symmetric. Two lows need a third high, two highs need a third low, a mixed pair accepts any third position. At h3 only the fibre itself can qualify and it must be mixed. At h>=4 none qualify. Taking the union bound proves U_mix, with overlaps and F_p cancellation potentially reducing support; the converse nonvanishing inference is NOT used.

For twins F_i=F_j, S038 gives Psi_ijk=0 pointwise for all k. A mixed triple is a pair of lows and a high or a pair of highs and a low. Its same-level pair cannot be twins if Psi is nonzero. Count all allowed same-level pairs and choices for the opposite-level third position, yielding T_twins. Mixed twins cannot occur because their degrees differ. The lower is the already proved incidence count, so precisely the SAME W_mix is sandwiched. QED.

**Attempted endpoint and failure.** Neither the scalar/vector/star moments, direction cap c_d<=p-1 nor four-index exchange bounds the actual U_mix or T_twins below these lowers. A light fibre of size zero or one contributes a large capacity, and the known deficit identity sum_X(3-h_X)=3 does not bound their counts sufficiently. Twin sparsity makes T_twins large rather than small. No proved premise forces sufficiently many twins or sufficiently few mixed light fibres. Thus we derived a valid actual-Z-dependent upper but did not establish a conflicting numerical upper for ALL Z. S032's U>=p^2+10p-8 is a lower on a coarse-capacity number and was never reversed.

**Four-index exchange continuation.** For four distinct positions the retained-factor Psi values are a linear functional of their four z-values. Its dependence coefficients need not be 0/1 or nonnegative integers. A relation among three active collinear directions therefore yields a WEIGHTED dependence, not a forbidden zero sum of original positions. For a concrete reverse-direction check, u,v,u+v (independent u,v over p>=7) are three projectively collinear directions with a nontrivial linear dependence u+v-(u+v)=0, but no nonempty 0/1 subset sums to zero: its u/v coefficients belong to 0..2 and cannot vanish unless all choices are zero. The four-index relation is consequently useful structure but does not by itself supply the required unsigned support contradiction. This example refutes that attempted implication only, not any complete no-short Z.

## Front B continuation: full matrix, swaps and value support

Every b-block incidence row R_B has R_B z=0 and R_B 1=b. Row differences consequently lie in the kernel of both the coordinate map and the cardinality map. This signed kernel property does not force any binary vector of weight <=a in the kernel, as the preceding example demonstrates. An attempted inference that many equal-weight zero rows must give a short unsigned zero sum fails at this conversion; the small local equal-sum row countermodels above give a stronger hostile test.

If z_i=z_j, the COMPLETE block family is invariant under transposition of i,j, so r_i=r_j. Mixed low/high positions cannot have the same vector VALUE. If such equal-value positions also have identical neighbourhoods, no b-block can contain just one of them. Conversely a block distinguishing them has its transposed companion, so its columns are not twins. This distinguishes value classes from neighbourhood classes; neither implies a universal mixed containment count F_c>0. The orbit observation does not by itself control all scalar multiples or all zero-block profiles.

## CLM-0147 — every no-short Z has affine span three and >=5 vector values

**Theorem.** Under the standing hypotheses, the vectors z_i have linear rank three, affine span of dimension three, and at least FIVE distinct vector VALUES. This concerns all m=kp, not only m2p; it does not assert >=5 projective directions.

**Proof.** If their linear rank were <=2, embed their span in F_p^2. Programme-proved CLM-0091 eta(C_p^2)<=3p-2 applies to a 3p-2 subsequence and supplies a nonempty zero sum of <=p<=a original positions, contradiction. So the rank is three. A proper affine plane containing all z_i would be ell(z_i)=c for a nonzero linear functional ell. If c=0 the linear rank is <=2, already impossible. If c!=0, any b-zero-sum block B (which exists by S029) would give 0=ell(sum_B z_i)=bc, impossible because b=-1/2!=0 in F_p. Thus the affine span is three.

Suppose there are at most four distinct vector values v_1,...,v_d. The direction cap implies the multiplicity c_j of each value is positive and <=p-1. If d<=3, their total multiplicity is <=3(p-1)<3p, impossible. If d=4, the 3-by-4 matrix of the v_j has rank three, hence a one-dimensional kernel. Its nonzero vector c=(c_j modp) lies in that kernel because Z sums to zero. Also sum_j c_j=3p=0 modp, so every kernel vector has coordinate sum zero. But the value-count vector q=(|B intersect value_j| modp) of a b-zero-sum block also lies in this kernel, while sum_j q_j=b=-1/2 modp is nonzero. Contradiction. Thus >=5 values. QED.

This gives an all-layer structural exclusion of small value support; it does not resolve five-plus values or imply a bound on k. Treating it as an exclusion of all four projective directions would be false: distinct values can lie on the same direction. The rank-three matrix has a kernel on VALUE counts, not arbitrary independent direction counts.

## Front C: all layers and two extreme adjacent cuts

## CLM-0146 — complete level constraints and adjacent boundary support

**Theorem.** Put n_u=# {i:j_i=u}, u=0..k-1. Then

   sum_u n_u=3p,
   sum_u u n_u=kb-3t.

For i at level u and j at level v, u<=v,

   max(0,2t+(u+v-k)p) <= lambda_ij <= t+up.

Every pair at levels 0/1 has nonempty Psi support and >=3 projective witness directions. The same holds for every pair at levels (k-2)/(k-1). If either such pair is nonexceptional, its lower-level neighbourhood is contained in the upper one and the gap leaves EXACTLY p extra blocks, so CLM-0145's six/seven witness improvement applies at p7/p13.

**Proof.** The census is S030's exact incidence identity sum_i r_i=mb, expanded by levels. The codegree interval is inclusion-exclusion for two subsets F_i,F_j of an m=kp member family and the smaller-degree upper bound. At levels0/1 the only integer in 0..t congruent to t modp is t itself, so a nonexceptional pair is contained. At the top adjacent levels the lower interval endpoint is 2t+(k-3)p=(k-2)p+s. The next candidate residue below r_i=t+(k-2)p is t+(k-3)p, smaller than that endpoint by p+s-t=t>0. Hence again only lambda=r_i can be nonexceptional, which is exactly containment with degree gap p. Exceptional pairs have nonzero scalar moment and >=3 directions by S037; contained adjacent pairs have nonempty variable-row support by S038, and CLM-0145 sharpens its p7/p13 counts. QED.

For k3 this gives a rigorous whole-layer composition. If F_adj counts contained 0/1 and1/2 pairs, and h_star has the values above,

   2W >= 3 n_1(n_0+n_2)+(h_star-3)F_adj.

Indeed the graph joining adjacent levels is the path 0--1--2; any three indexed vertices contain at most two edges of this graph (even a triple with one vertex at each level contains only its 0/1 and1/2 edges). Count supported pair/triple incidences. This is NOT the two-level L/H formula transplanted to k3.

**Exact k3 census:** for s=+1, n_2-n_0=-3, so n_0=n_2+3 and n_1=3p-3-2n_2; for s=-1, n_2=n_0 and n_1=3p-2n_2. Thus at p7 the extreme-only census (n0,n1,n2)=(12,0,9) is arithmetically allowed; at p13 the all-middle census (0,39,0) is arithmetically allowed. They are NOT actual Z constructions. They make the adjacent-cut lower vacuous and prevent it from being an all-k elimination proof.

**Serious attempted k3 elimination.** Try to replace adjacent cuts by ALL unequal-level pairs. A nonexceptional 0/2 pair would have containment with TWO p extra rows, not one p. Its variable-column counts range 0..2p; variable columns with mu=p now have Psi=s mu=0, unlike the adjacent case. Consequently the p-row argument cannot force support. Try instead to eliminate the all-middle k3 case by the rank of its square b-regular incidence matrix (p13:39 rows/columns, degree19). Its rows annihilate all three coordinate columns, so rank<=N-3; regularity only supplies the nonzero eigenvector 1, not nonsingularity on its complement. No proved lower rank exceeds N-3, and no determinant or binary-kernel argument was established. These are specific failed elimination candidates, not assertions that all elimination methods fail.

**Reverse test for the two-p-row extrapolation.** At p7, take six variable columns all equal to a nonzero u; select seven complementary pairs of distinct weight-three subsets of these six positions, giving fourteen distinct equal-weight rows. Such seven pairs exist since the twenty weight-three subsets form ten complementary pairs. Each column occurs in exactly seven of the fourteen rows, so every column varies while mu=7=0 mod7 at every column. Every row has vector sum 3u; no nonempty subset of the six variable columns sums to zero since their size is <7. This is a selected LOCAL row family, not the complete equal-sum family (the latter has all twenty rows), and not a Z lift. It proves exactly that DISTINCT zero-sum/equal-weight row conditions alone do not extend the p-row support equivalence to 2p rows. Completeness and global no-short conditions are indispensable to any valid all-layer repair.

## Cross-front endpoint synthesis and shortest remaining dependencies

1. A+B composition yields the genuine mixed-support sandwich, stronger local containment counts, value-versus-twin distinction and a proved local limit on those counts. It does NOT force the upper below the lower. First exact missing Psi lemma: actual complete b-block geometry must force min(U_mix,T_twins) below [3LH+(h_star-3)F_c]/2, or supply a different unsigned short-zero-sum contradiction. Neither scalar/vector/star moments nor the raw projective deficit currently prove that lemma.
2. B+C composition excludes all no-short Z with <=4 VALUES, and proves all boundary-adjacent pair support for any k, including the explicit k3 path incidence count. It does NOT exclude m2p, k3 escape censuses, or arbitrary higher k. The first unresolved middle-layer step is completeness-sensitive cancellation at a two-p neighbourhood gap or a rank/binary-kernel obstruction in regular incidence families.
3. D closes the requested two-position saving independently of EVERY Psi layer. CLM-0142/0143/0144 prove D2<=5p-3 and D_(2p-4)<=M-(p-3). Therefore continuing to require strong short extraction as a prerequisite for that comparison would now be an incorrect dependency. Strong extraction itself remains an independent research target; it is not a necessary bridge for the repaired multiwise route.
4. History audit: S004 CLM-0068 and S005 section1 already had the weaker conditional base D2<=5p-2 and the weak-coefficient bypass, subject to then-imported classical/CW/eta inputs. Later S025-S038 correctly computed M+2 for THEIR inferior safe-recursion base but incorrectly treated a D2 saving as globally unestablished. S039 freshly reconstructs the prime D1 premise, strengthens the D2 base by ONE further position, and restores the actual dependency graph. No novelty or priority claim follows. Historical files remain immutable; current authority corrects the obsolete blockers.

All A/B/C registered attempts were continued to their endpoint consequences and at least one distinct follow-up, rather than ending at a single lower bound. No claim of exhaustive mathematical exploration is made. The shortest consequential next route is a hostile independent reconstruction of the new D2 lifted argument, then composing it with the general large-prime eta plane proof and the ACTUAL downstream induction; it should not spend another session trying to fix an already-bypassed M+2 deficit. S040 is future only. Strong extraction, arbitrary composite rank-three Davenport equality/counterexample, and five frontier intervals remain unresolved. Frozen original30 row objects/full ordered Markdown rows, original28 sources/access, Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED and blocked CAM-0001 remain intact.
