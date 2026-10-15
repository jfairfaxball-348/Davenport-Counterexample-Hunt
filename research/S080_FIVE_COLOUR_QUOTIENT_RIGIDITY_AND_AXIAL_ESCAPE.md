# S080 — five-colour cyclic quotient obstruction, total-free rigidity, and a genuinely broad-spectrum axial escape

15 October 2026. Owner invoked precisely S080 with "Run next session". Main before work: \`a24b40bf03910ca80dc783238414a3dc9793bd38\`; TRUE Git root tree \`c9bbca5b436f82ad2c2feab2ea6a7a116cec7c9c\`. S079 authored head \`362272e59c955bce5acff9ce93f7627d6cf9bbc0\` has ONE parent \`a57fe97fd7a79cefc1275c70b87ac7e39618b8b2\`; ordinary S079 merged main has precisely these TWO parents. Entry open PR 0, hosted Actions runs 0, both predecessor combined-status contexts 0 (ABSENT_NOT_PASS), rulesets 0, branch protection 403 UNKNOWN.

All results below are symbolic INTERNAL SAME-EXECUTOR mathematics under the SOURCE-CONDITIONAL canonical original 22+8+7 profile. No mathematical numerical search, orbits, candidates, CAS, SAT, ILP, code execution, historical source promotion, Lean, Palomar, independent certificate, arXiv or correspondence. No D(C20^3)=58, G58 zero-free sequence or rank-three resolution.

## 1. Genuine original-index setup

Let G=(Z/20)^3, H=(Z/10)^3, iota:H→2G, h↦2h. **G is not Q⊕H** for Q=G/2G=F2^3. Let T be an actual total-zero 59-position sequence: 22 distinct original equal-nonzero-parity pairs (a_i,b_i) with even sums iota(u_i), eight distinct labelled original g_j of parity q≠0, and seven distinct original singleton positions s_r, one per nonzero parity r. Duplicate group *values* are allowed, but the original *indices* are distinct. Assume U=(u_i) is zero-sumfree in H. Put Σ(U)={Σ_{i∈B}u_i:B⊆[22]} (including empty) and E(U)=H\\(-Σ(U)).

The six singleton indices other than s_q are the genuine X_i,Y_i with parities r_i,r_i+q, i=1,2,3 and r_3=r_1+r_2 in Q/<q>. Their actual grouped sums V_i=X_i+Y_i have parity q. The 12 mutually disjoint ORIGINAL q-supervertices are eight separately labelled g_j, the singleton s_q, and the three actual two-original-singleton groups V_i. Every perfect matching of THESE twelve groups yields six disjoint even-G groups c_j∈H after iota^-1. Each NONEMPTY PROPER subcollection of matching groups, plus any selection of complete ORIGINAL U pairs, is a nonempty proper original subset. If T has no proper original zero in the S060 q-only class, all nonempty proper indexed subsums of the c_j belong to E(U). The full sum of all six matching blocks, however, is c=−Σ_i u_i; it must **not** be required to lie in E(U).

## 2. CLM-0278 — sharp five-term growth / six-block rigidity without prescribed total

**Elementary growth lemma.** In any finite abelian group A, let b_1,...,b_k be an indexed zero-sumfree sequence, with subset sums Σ_j for its first j terms, including zero. Then |Σ_j|≥|Σ_{j−1}|+1. Indeed, if Σ_{j−1}+b_j=Σ_{j−1}, its translation orbit containing 0 contains −b_j, so an indexed subset of earlier terms plus b_j would sum to zero. If two terms b_i,b_l are DISTINCT, then zero-freeness makes {0,b_i,b_l,b_i+b_l} four distinct two-term subset sums, and ordering these two first gives |Σ_k|≥4+(k−2)=k+2. Thus if k=5 and |Σ_5|≤6, ALL five terms must be equal.

**Six-block lemma, no sum hypothesis.** Let b_1,...,b_6∈C10, and A⊆C10\\{0} with |A|≤5. Suppose *every nonempty proper indexed subsum* b_J belongs to A. Choose ANY five of the six indices. They are zero-sumfree as scalars, since all their nonempty subset sums are in A and 0∉A. Their subset-sum set lies in {0}∪A, of size≤6. The growth lemma forces |A|=5 and these five terms all equal; varying the omitted index forces ALL SIX terms equal some b. The scalar values b,2b,...,5b are nonzero, pairwise distinct, and exhaust A, so ord(b)>5. In C10 this means b is a UNIT b∈{1,3,7,9}, A={b,2b,3b,4b,5b}, and the otherwise-unconstrained full scalar sum is automatically 6b. In particular |A|≤4 is impossible. This subsumes the CLM-0276 integer-prefix lemma without assuming scalar full total 6, and holds for non-interval A as well.

For a fixed A as above, b is uniquely determined: the four possible units have pairwise different values of 6b mod10 (6,8,2,4). In any matching on the same 12 ORIGINAL q-supervertices the full scalar block sum is the SAME φ(c), so any scalar b appearing in a different matching satisfies 6b=φ(c) and hence is the same b.

## 3. CLM-0279 — universal at-most-five zero-avoiding character exclusion with an actual original witness

**Theorem.** In the canonical total-zero original 59-index configuration of §1, if there is ANY homomorphism φ:H→C10 for which
    0∉φ(E(U)) and |φ(E(U))|≤5,                       (80.1)
then T possesses a NONEMPTY PROPER ORIGINAL G-zero subset already in the S060 q-only class. No assumption φ(−ΣU)=6, no preselected five-residue interval, no source-stated D_3(C5^3) and no G≅Q⊕H splitting is used.

**Proof, including literal original-index extraction.** Assume no proper original q-only zero. Set A=φ(E(U)), and choose any perfect matching of the twelve genuine original q-supervertices. For each matching, every proper nonempty subcollection J has c_J=Σ_{j∈J}c_j∈E(U): if not, there exists an ACTUAL indexed B⊆[22] with Σ_{i∈B}u_i=−c_J, and the union of selected disjoint ORIGINAL q-supervertex groups with BOTH ORIGINAL endpoints of each pair in B is a nonempty proper G-zero. Hence all proper scalar sums lie in A. By CLM-0278, |A|=5, and all six matching block scalar values equal a unit b, with A={b,2b,3b,4b,5b}; each matching has the SAME b because its full scalar sum φ(−ΣU)=6b is independent of matching.

Choose a true mod20 lift F:G→C20 of integer coefficients of φ, so F(iota(h))=2φ(h). ANY two distinct original q-supervertex groups z,z' may be paired in a perfect matching; hence F(z)+F(z')=2b modulo20. Comparing partners shows ALL twelve true original group values have the SAME F scalar a; 2a=2b mod20 means a∈{b,b+10}, so a≡b mod10. In particular each actual g_j and each true V_i has that scalar.

For each of the four ACTUAL parity-even Fano transversal triples ε=000,110,101,011, choose one of the same six original X_i/Y_i labels per coset and let x_ε=iota^-1(sum of its three original singleton G values)∈H. Selecting this original triple plus ANY 2k of the eight labelled original g_j, k=0,1,2,3,4, is nonempty and proper because the complementary singleton positions are omitted. Thus φ(x_ε)+kb∈A for ALL k=0,...,4. Since b is a unit and A={b,2b,3b,4b,5b}, intersecting the five translates A−kb forces φ(x_ε)=b for each of the FOUR actual ε; thus φ(Σ_ε x_ε)=4b.

But EACH of the six actual X_i/Y_i singleton ORIGINAL positions occurs in exactly TWO of the four even Fano triples. Their exact G sums are 2x_ε, and Σ_ε(2x_ε)=2(V_1+V_2+V_3) in G. Passing through the even-subgroup isomorphism iota, Σ_ε x_ε equals the reduction of V_1+V_2+V_3 modulo10 in H. Consequently applying φ gives Σ_ε φ(x_ε)=F(V_1+V_2+V_3) mod10=3a mod10=3b, contradicting 4b because b has order10.

**Constructive witnesses, not synthetic overlaps.** If any matching's proper scalar subsum falls outside A, choose its nonempty proper set J and a real indexed B with Σ_B u=−c_J; its literal original zero consists of the selected q-supervertex original groups and both endpoints of B. If all matching proper scalar subsums are inside A, the previous argument forces some true ε and k with φ(x_ε)+kb∉A; choose the actual 2k labelled g indices and a real indexed B cancelling x_ε+shift. The forbidden original zero consists of the THREE true singleton indices in ε, those 2k real g indices and BOTH endpoints of the complete original U pairs in B. Omission of complementary singleton indices guarantees properness, even when B contains all 22 indices. At no point are overlapping different Fano triples artificially combined as disjoint original subsets.

**U-only spectral necessary condition.** Any hypothetical canonical S060 survivor must satisfy, for EVERY φ:H→C10: either 0∈φ(E(U)), OR |φ(E(U))|≥6. This is only a necessary H-core sieve, not a full-gate sufficiency criterion.

## 4. CLM-0280 — an entire six-parameter diagonal-core family has no original S060 lift

For any α,β∈C10 and integer t∈{1,2,3,4,5,6} set
    U_(α,β,t)=e1^9 e2^9 e3^3 (α e1+β e2+t e3)∈H^22.
This indexed 22-term U is zero-sumfree: without the last term, third-coordinate sums lie 0..3 and sum zero forces empty; with it, third-coordinate sum lies in {t,...,t+3}⊆{1,...,9} and cannot be zero. The first two coordinate sums independently run through ALL of C10 whether or not the last term is selected. Hence
    Σ(U)=C10² × R_t,  R_t={0,1,2,3}∪{t,t+1,t+2,t+3}.
For φ=third-coordinate, φ(E(U))=C10\\(−R_t). The six exact possibilities are:
    t=1: {1,2,3,4,5};
    t=2: {1,2,3,4};
    t=3: {1,2,3};
    t=4: {1,2};
    t=5: {1,6};
    t=6: {5,6}.
All are ≤5 residues, none zero. CLM-0279 therefore excludes EVERY possible actual labelled original total-zero canonical T59 lift of EVERY one of these U cores, for ALL α,β and all invertible H coordinate changes. In particular t=2,3,4 have φ(−ΣU)=−(3+t)≠6, so their elimination is NOT obtained from S079's old full-total6 hypothesis. No claim is made that these are all zero-sumfree U22 or that arbitrary U22 has a thin character spectrum.

## 5. CLM-0281 — precise broad-spectrum original feasibility obstruction (not a survivor)

The axial H-only core U_*=e1^8e2^8e3^6 is an actual indexed zero-sumfree 22-term sequence: each coordinate subset sum stays in [0,8],[0,8],[0,6], and no nonempty subset can sum zero modulo10. Its exact extension set is
    E(U_*)={h:h1=1 OR h2=1 OR h3∈{1,2,3}}.           (80.2)
This is the complement of −([0,8]×[0,8]×[0,6]); in particular E contains EACH complete coordinate hyperplane h_i=1, with the other two coordinates free.

**Theorem.** For EVERY homomorphism φ:H→C10 (including nonsurjective and zero maps), φ(E(U_*))=φ(H). In particular 0∈φ(E(U_*)) ALWAYS: the S080 five-colour zero-avoiding character criterion does not apply to this completely explicit, rigorous H-zero-free U22.

**Proof.** Write φ(h)=a1h1+a2h2+a3h3 modulo10. Let d=gcd(10,a1,a2,a3), so φ(H)=dC10. Because 10 has precisely two prime divisors 2 and5, one can choose at most two of the coefficients whose gcd with10 is already d: choose one attaining the minimum 2-adic valuation (capped at v2(10)), and one attaining the minimum 5-adic valuation (possibly the SAME coefficient). Call these two FREE coordinate directions i,j; if they coincide choose any other as the second. Their additive images generate φ(H). Let k be the remaining coordinate. Equation (80.2) includes the FULL genuine H hyperplane h_k=1, on which h_i,h_j vary freely. Its φ-image is a_k+〈a_i,a_j〉=a_k+φ(H)=φ(H), since a_k∈φ(H). Thus the image of E is all φ(H); reverse inclusion is tautological. This includes zero homomorphism. QED.

This is a **counterexample to the proposed universal thin-character bridge**, not an actual original 59-index S060 gate survivor. In particular, the 12 true q groups, 2048 outsiders, the 26 q-hubs, every E(U\\I) split, the same SIX ORIGINAL singleton Fano C/Delta conditions, and all non-q signed fibres may still rule U_* out. None have been realised or verified for this core. No mathematical numerical search was conducted.

## 6. Aggressive cross-gate audit and exact first unresolved obstruction

- Six-block lemma is independent of φ(−ΣU) and of interval shape, but **requires 0∉φ(E(U))**. If 0 lies in the image, scalar zero may be an H-nonzero actual extension, and the zero-free scalar growth argument FAILS. U_* proves this escape cannot be removed by asserting a character always avoids0.
- The five-colour proof uses m=0 original q supervertex matchings plus real coupled original Fano triples and true 0,2,4,6,8 original g shifts. These are necessary across m0/m1/m2/m≥3, but are NOT all S060 q one/multisplit conditions. It is legitimate to rule out a U core from one necessary gate; it is NOT legitimate to certify an arbitrary other U as a gate survivor.
- The all-atom/full-original matching selection is correctly excluded from E(U). All complement and properness exceptions are explicit. F maps from ACTUAL C20 original values to C20, while φ maps H to C10, with F(2h)=2φ(h); no invalid direct G=Q⊕H decomposition.
- No actual fully labelled 59-position total-zero T passing every S060 q-only gate has been produced. No first literal non-q proper zero/complement in such a survivor can be reported. Signed w_i(Z) at split non-q pairs remain the true endpoint difference, four tau_ε(Z) share original singleton values, and neither χ=0 K_ε occupation nor χ≠0 three-point fibre nor an original overlap/majority carry is forced.
- FULL8, exact12 χ0/χ≠0, 13,14,≥15 distinct danger sets; m0/m1/m2/m≥3; ALL 26 q-hubs, three-hub profiles and P26 (0,4),(0,6),(1,7), remain unresolved. Historical SRC-0015 D3(C5³)=25 stays unauthenticated SOURCE_STATED. Original 29 sources and 30 frontier row objects are unchanged.

**First hard gap:** for a broad-spectrum H-zero-free core such as U_*, prove incompatibility of the *actual* original 12 q supervertices with the 2048 outsider/Fano and all true E(U\\I) gates, or construct one completely S060-gated original labelled total-zero T59 and identify its literal first non-q zero. The S080 five-colour character result cannot perform this step alone. An H-only spectral escape is emphatically NOT a full original survivor.

**Outcome:** CLM-0278–0281 INTERNAL PROGRAMME_PROVED in the indicated self-contained/conditional scopes, no C20³ theorem, G58 or campaign. 281 claims; source29/frontier30 untouched; Phase1 IN_PROGRESS, CAM-0001 BLOCKED, hosted CI ABSENT_NOT_PASS, review INTERNAL SAME_EXECUTOR.