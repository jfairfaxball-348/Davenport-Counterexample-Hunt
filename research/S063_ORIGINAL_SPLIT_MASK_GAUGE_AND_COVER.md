# S063 — Original non-q split-mask torsion gauge, exact finite-cover obstruction

14 October 2026. One owner-invoked sustained Phase-1 **SYMBOLIC** C20³ session. INTERNAL same-executor mathematics, conditional on the actual S060 canonical original 22+8+7 data, all true q-matchings, every q-split E(U\\I) with both original member choices, full-H four-Fano values satisfying the SAME c mod5 and three Delta identities, mixed odd g, and total T=0. No numerical mathematical search, CAS/SAT/ILP, orbit/candidate enumeration, Lean, Palomar, manuscript or correspondence. No proof of D(C20³)=58, no indexed G58 zero-free candidate, no surviving S060-gate passing actual G59 model.

## 1. The missing freedom: independently twist BOTH original members of each non-q pair

Let G=(Z/20)^3, Q=G/2G=(F2)^3, H=(Z/10)^3, iota(h)=2h. This is a nonsplit extension; 10Q=G[2] is the exact order-two subgroup of G. Fix actual 59 original indices W: 22 labelled equal-parity pairs (a_i,b_i), eight q-parity g_j, seven parity-distinct singleton s_r. Put t_i=pi(a_i)=pi(b_i); q nonzero and total_G(W)=0. The original pair sums 2u_i=a_i+b_i are fixed, as are all g_j, S=s_q, V_k=X_k+Y_k and all four q-avoiding Fano H values, with every S060 requirement assumed truly met. Define N={i in [22]:t_i != q}, m=|N|. We do not assume m>0.

For each i in N and theta_i in Q simultaneously replace
    a_i -> a_i + 10 theta_i,   b_i -> b_i + 10 theta_i.           (1)
These are labelled-original changes, not synthetic H-block swaps. Since twice 10theta_i is zero in G, (1) preserves a_i+b_i EXACTLY in G; it also preserves pi(a_i), pi(b_i). It preserves total(W), U, all q hub values and q-pair members, **every** S060 matching including all I subset P_q, every E(U\\I) shift with selected original members, all mixed odd-g selections, all six original singleton values and all four true Fano values. Thus the entire S060 q-only gate is unchanged for **all 8^m** choices of theta. This is a torsion subfibre of permitted ORIGINAL labelled configurations, not a classification of all possible configurations.

For an ORIGINAL indexed subset Z define its non-q split mask
    M(Z)={ i in N : |Z intersect {a_i,b_i}|=1 } subset N.
Write theta_M=sum_{i in M} theta_i in Q. Every ORIGINAL full-G subset sum transforms by the exact identity
    sum_G(Z;theta)=sum_G(Z;0)+10 theta_{M(Z)}.                 (2)
If Z has odd parity, it cannot become zero. Only parity-even reference subtotals in the actual order-two subgroup G[2] can threaten any twist. No division by iota before checking original G parity is performed.

## 2. CLM-0227: singleton 64-lift freedom is a gauge redundancy for zero-sum tests

S061 independently allows original singleton shifts X_k,Y_k -> X_k+10eta_k,Y_k+10eta_k with eta_1+eta_2+eta_3=0, corresponding to ell in Hom(K,Q), K=Q/<q>. On a parity-even ORIGINAL Z, S061's exact formula is +10ell(sigma(Z)), where sigma(Z)=[sum_{all split i}t_i]. The q split indices vanish in K, so
    sigma(Z)=sum_{i in M(Z)}[t_i].
By F2-linearity, ell(sigma(Z))=sum_{i in M(Z)}ell([t_i]). Combining singleton ell and pair theta therefore gives
    sum_G(Z;theta,ell)
       =sum_G(Z;0,0)+10 sum_{i in M(Z)}(theta_i+ell([t_i])).   (3)
Set phi_i=theta_i+ell([t_i]); the phi_i are again freely and independently assignable in Q for all i in N. Thus as far as **the existence of a proper zero subset** is concerned, the full (64)(8^m)-point combined labelled lift space has EXACTLY the same attainable zero-sum test patterns as the 8^m pair-twist space with ell=0. The physical original singleton labels can differ; this is equivalence of zero-sum predicates, not equality of original labelled sequences. If m=0, all q-only tests already cover all original splits and the singleton 64 lifts cannot change any parity-even proper sum; S060's exact q gate then certifies the fixed total-zero T as minimal **conditionally on a feasible gate**. Such feasibility for arbitrary U is not established.

In particular, sigma=0 is not a fully lift-invariant danger class once the valid non-q pair twists are admitted: a Z splitting two non-q indices i,j with [t_i]=[t_j] has sigma(Z)=0 but is shifted by 10(theta_i+theta_j). Hence treating 0 in S061 C_0 as an unavoidable obstacle in the enlarged family is INVALID. It is unavoidable only on a fixed-original-pair 64-point singleton slice.

## 3. CLM-0228: exact danger-set criterion and sharp eight-condition cover threshold

For EACH ORIGINAL non-q split mask M subset N set
 D_M={v in Q: some nonempty proper ORIGINAL parity-even Z has M(Z)=M and sum_G(Z;0)=10v}.
Complementary actual original positions are not identified as subsets (although complement gives the same torsion v and mask). Different witnesses may yield the same pair (M,v). Let A_M=Q\\D_M.

**Exact iff.** For the fixed genuine four-Fano reference and its 8^m order-two original pair twists, at least one minimally zero-sum T59 exists iff
    0 notin D_empty
and there are phi_i in Q (i in N) with
    sum_{i in M} phi_i in A_M  for EVERY nonempty M subset N. (4)
Proof: (2) says a zero subset at theta must have reference sum 10v and satisfy v=theta_M; the converse uses the same actual original Z. For M=empty a zero is invariant under every pair twist. The full S060 q-only original-index IFF excludes all proper zeros with NO non-q split pairs, so in a genuinely S060-compatible configuration 0 notin D_empty is ALREADY guaranteed. Any reference subtotals outside G[2] cannot become zero under (1). This proves both implications including actual original complement/full exclusions.

**Sharp covering threshold (not a claim that witnesses exist).** If every one of the 8^m twists is nonminimal and 0 notin D_empty, then the total number
    N_danger=sum_{nonempty M} |D_M|
of DISTINCT mask/value obstructions is at least 8. If N_danger=8, a UNIQUE nonzero mask M_0 must satisfy D_(M_0)=Q and all other nonempty D_M must be empty. In particular if no D_M is all eight Q values, a full obstruction requires at least N_danger>=9. These are actual indexed reference witnesses if the sets are nonempty; the theorem does not infer their existence from S060.

Proof: The group of twists Q^m has cardinality 8^m. For each nonempty M and v in D_M, the forbidden cylinder
    E_(M,v)={theta in Q^m:sum_{i in M}theta_i=v}
has EXACTLY 8^(m-1) points since the linear form is surjective. Fewer than eight distinct cylinders cannot cover Q^m. If exactly eight cover, equality in the union bound forces them pairwise disjoint. For distinct masks M!=M' (both nonempty), their F2 indicator rows are linearly independent; consequently the map theta->(theta_M,theta_M') is onto Q^2, and E_(M,v) and E_(M',v') intersect in 8^(m-2)>0 points. Therefore all eight covering cylinders have the SAME mask, and disjointness plus cover forces all eight v in Q. Conversely D_(M0)=Q alone covers all pair twists. For m=0 q-gate supplies minimality as above; no nonempty masks exist. QED.

**Important qualifier:** this eight-threshold applies to the *total number of distinct (mask,v) conditions in the full pair-twist subfibre*, not to the old aggregated C_sigma values. It is NOT the S062 three-colour 8-or-12 theorem and does not rule out 9,10,11-condition nonparallel covers. A complete nonlinear bound for all m is still missing.

## 4. CLM-0229: one- and two-pair exact reductions; full-G intersection audit

If m=1, S060 gives 0 notin D_empty, and some pair twist produces a minimal T59 iff D_{1}!=Q. Thus any genuinely S060-feasible dataset with one non-q pair either has all EIGHT genuine reference torsion values for that exact original split mask, or admits a full indexed minimal T59 via a permissible original torsion twist. This is a CONDITIONAL dichotomy, not an exhibit of such data.

If m=2, there are masks 1,2,12. With B_1=Q\\D_1, B_2=Q\\D_2, B_12=Q\\D_12, (4) is exactly
    exists a in B_1, b in B_2 with a+b in B_12.            (5)
The S062 three-colour counting proof now applies to these THREE EXACT ORIGINAL MASKS: if all pair twists fail, either some D_M=Q or, when all three are proper, their sizes sum to at least12; equality requires common four-point affine coset geometry. This holds regardless of whether [t_1] and [t_2] are equal in K; if they are equal, mask12 has sigma0 but is STILL adjustable by theta_1+theta_2. For m>=3 (4) has 2^m-1 nonempty mask equations and cannot be replaced by three aggregate C_sigma constraints.

For any two actual parity-even original torsion witnesses Z,Z' with reference sums 10v,10w, masks M,M', J=Z intersect Z', D=Z triangle Z', original indicator parity gives
    M(D)=M triangle M'
and original full-G arithmetic gives
    sum_G(D)=10(v+w)-2sum_G(J).                              (6)
If sum_G(J)=5d modulo10 coordinatewise and D nonempty proper, then v+w+d in D_(M triangle M'). If M=M' and d=v+w, (6) would give a forbidden proper original ZERO of empty non-q split mask, directly contradicting the assumed S060 gate; the identical Z=Z' (D empty) and actual complements (D full) are the mandatory exceptions. This is a genuine support/carry prohibition, but neither eight witnesses for one mask nor twelve across three masks has yet been shown to force the congruence on an actual ORIGINAL intersection.

## 5. Hostile stress tests and why the central goal remains open

**Eight-label aggregated-colour trap.** As a purely ABSTRACT mask/value system, suppose four non-q pair parities have the same nonzero image s in K. Their eight ODD-cardinality masks M_1,...,M_8 all have the same sigma=s. Assign exactly one D_(M_j)={v_j} per mask, the v_j running bijectively over Q, and every other D_M empty. Aggregation gives C_s=Q: all 64 singleton-only lifts fail, despite C0 empty. But all eight forbidden cylinders have DIFFERENT masks and intersect pairwise, so by the exact eight-cover equality proof their union is strictly smaller than Q^4. At least one pair twist avoids them ALL. This is NOT a real original G59 construction: no actual U, g, S, original pair members, E(U\\I), four-Fano tuple or intersection-carry constraint has been realised. It rigorously kills the invalid logical step 'one full aggregate C_sigma necessarily blocks all permitted original-label torsion changes'.

**Failed direct universal collision route.** S062's eight-or-twelve aggregate torsion values do not determine original masks or original subset intersections. Equation (6) forces a q-only zero only when actual same-mask witnesses have the exact 5(v+w) overlap carry and a proper symmetric difference; nothing in pure forbidden-value counting supplies this. The m=1 full D_M, m=2 full/equality cases, and higher-mask covers remain genuine conditional boundary cases.

**Failed concrete model route.** S059's total-zero NONMINIMAL all-q-hub matching model is not an S060-gate survivor: its genuine four-Fano gate fails by the previously documented S050/S051 slab. Twisting non-q pair members preserves this failure; it cannot repair the missing Fano feasibility. No actual fully labelled total-zero nonminimal G59 passing S060's every q matching, every selected original q pair split and TRUE four-Fano F_* gate was constructed here.

**Scope/provenance hostile test.** Canonical 22+8+7 from 26 equal-parity pairs needs S041 CLM-0151 and historical SOURCE_STATED SRC-0023. This does NOT exclude three-hub pencils or P26 parity (z,r)=(0,4),(0,6),(1,7), and historical SRC-0015 D3(C5³)=25 remains SOURCE_STATED unauthenticated. No claim about D(C20³)=58, counterexample G58, general rank-three conjecture, mathematical search, source upgrade or independent certification follows.

## 6. Exact next obligation

For every REAL S060-feasible canonical dataset, analyse the complete mask-level original witness sets D_M. Prove that no pair-twist assignment satisfies (4), ideally from forced same-mask indexed intersections/carries (6) or actual coupled Fano/H data; OR actually exhibit one **fully labelled total-zero NONMINIMAL** G59 passing every S060 q-only gate and identify its first original non-q zero split, clearly separated from an extremal counterexample. Triage m=0,1,2 first with honest feasible-U evidence; then arbitrary m. Never treat an abstract mask assignment as an actual C20 construction. Preserve all original labels and the full n20 profile obligations. Same-executor INTERNAL review only.
