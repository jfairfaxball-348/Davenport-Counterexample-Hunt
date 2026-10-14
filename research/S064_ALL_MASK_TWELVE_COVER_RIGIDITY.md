# S064 — All-mask twelve-cover theorem and exact original carry obligations

14 October 2026. Phase 1, one owner-invoked extended original-index SYMBOLIC session. INTERNAL same-executor proof and hostile audit. No mathematical numerical/computational search, CAS/SAT/ILP, orbit enumeration, candidate generation, Lean/Palomar, outreach or publication. The results are conditional structural lemmas for an ACTUAL S060-compatible canonical total-zero C20^3 59-position configuration, NOT an assertion that such data exist.

## 1. Exact reference and what was attacked

Use G=(Z/20)^3, Q=(F2)^3, the embedded torsion subgroup G[2]={10v:v in Q}, and 22 genuinely original labelled pairs (a_i,b_i), eight original q-hub positions g_j, seven genuine singleton positions, and their exact total zero. Preserve every q-matching H28 atom, every I subset P_q, every selected original member alpha, E(U\I), every mixed odd-g choice, and four **actual** Fano H values satisfying the SAME full-H sum and three mod2 differences, as in S060 CLM-0221/0222. For N={i:t_i!=q}, m=|N|, twist BOTH members of pair i by 10theta_i; original full pair sums, parity, q-gate and Fano data stay unchanged.

For nonempty proper ORIGINAL subsets Z with reference G sum 10v and non-q split mask M(Z), set
  D_M={v in Q : there exists such an actual Z with M(Z)=M}.
On an original pair twist theta, that proper zero condition is precisely theta_M=v, theta_M=sum_(i in M)theta_i. The actual S060 q-only gate ensures 0 notin D_empty; no extra assumption that D_empty is empty. The covering problem is: can the finite union of cylinders E_(M,v)={theta in Q^m:theta_M=v}, nonempty M, cover all Q^m? Count **distinct** (M,v), N_danger=sum_(M!=empty)|D_M|, not individual original subsets or the old aggregated C_sigma.

S063 proved an eight-condition union bound, with equality only one full D_M=Q; it left nine, ten, eleven and general high-m equality geometry open. We attack those cases here, independently of original witness support assumptions. This gives a real strengthening but does not by itself force an original-index contradiction.

## 2. CLM-0230 — all-m twelve-cover stability theorem

**Theorem.** Let V=(F2)^m with m>=1 and Q=(F2)^3. For every nonzero vector M in V let D_M subset Q, and write
 E_(M,v)={theta in Hom_F2(V,Q):theta(M)=v}.
Put N=sum_(M!=0)|D_M|. If these cylinders cover Hom_F2(V,Q), then EITHER

(A) a nonzero M has D_M=Q (all eight values; its eight parallel cylinders already cover), OR

(B) no D_M is full and N>=12.

If (B) holds with N=12, then there are EXACTLY THREE nonempty D sets, indexed by A,B,A+B for two independent nonzero A,B in V, each of cardinality four. Their allowed complements B_A=Q\D_A, B_B, B_(A+B) are cosets of ONE common four-point subgroup L<=Q, and B_(A+B) is the opposite L-coset to B_A+B_B. Equivalently, for suitable a,b in Q,
 D_A=a+L, D_B=b+L, D_(A+B)=a+b+L,
all other D_M empty. Conversely these three four-point forbidden cosets cover every linear theta, making the abstract bound sharp for m>=2; a full mask is the only cover with N=8. For m=1 only (A) can hold.

**Proof of the two-dimensional case.** For m=2 the only three masks are A,B,C=A+B. Let T_A=Q\D_A and similarly T_B,T_C. If any T is empty, (A) holds. Otherwise full obstruction means (T_A+T_B) cap T_C is empty. For any c in T_C, T_A and c+T_B are disjoint, hence |T_A|+|T_B|<=8. Cycling proves |T_A|+|T_C|<=8 and |T_B|+|T_C|<=8. Therefore sum |T|<=12, N=24-sum|T|>=12. At equality each |T|=4 and |T_A+T_B|=4. Translation invariance forces all three T to be cosets of one common four-element subgroup L; T_C is the other L-coset relative to T_A+T_B. Passing to complements gives the displayed D-cosets and D_C=D_A+D_B. This also proves the converse. The same conclusion for m=1 is immediate because there is only one nonzero mask.

**Induction for arbitrary m>=3.** Assume the theorem for m-1. Suppose all D_M proper yet their cylinders cover and N<=12. Choose a mask A with nonempty D_A, write k=|D_A| (1<=k<=7), and fix ANY a in Q\D_A. Restrict to the affine slice theta(A)=a, naturally a copy of Hom(F2^(m-1),Q). The k A-conditions vanish; every other nonzero mask descends to a nonzero mask modulo <A>, possibly with a translated forbidden value. At most N-k<=11 original cylinders remain, so by the induction hypothesis a full eight-value quotient-mask class MUST occur on this slice. The same quotient-mask class can arise from only TWO original masks B and A+B. Consequently
 |D_B|+|D_(A+B)|>=8
for some B independent of A (even if some induced RHS values coincide). Define the two-dimensional span P=<A,B>. The original conditions with masks in P number at least k+8>=9; therefore at most 12-(k+8)<=3 conditions have masks outside P.

Suppose the P-conditions do NOT cover all (theta(A),theta(B)) in Q^2. Choose a pair (a0,b0) avoiding every P-condition. In the fibre theta(A)=a0,theta(B)=b0, an outside-P mask is a nonzero linear functional of the remaining m-2 variables, hence EACH one of its individual forbidden-value cylinders contains exactly 1/8 of this fibre. At most three such cylinders cannot cover it, by the union bound. This contradicts the assumed full cover. Thus P-conditions alone cover Q^2. By the already proved two-dimensional theorem, with no full D_M, they require at least 12 distinct values and, at equality, exactly the three common-coset masks. Our global N<=12 then forces N=12 and NO conditions outside P, with precisely the asserted triple-coset geometry. This completes the induction. Note that the induction never assumes a common two-dimensional coefficient subspace at entry; it **forces** such a subspace when N<=12.

**Boundary audits.** Different nonzero masks A and B are F2-linearly independent; the restricted fibre counts use Q-valued linear surjectivity and have density 1/8 exactly, regardless of whether their original pair parities t_i have the SAME class modulo <q>. Affine RHS offsets on theta(A)=a are allowed and do NOT affect cardinality. If no mask is populated then no cover exists. No "one-test per session" or numerical case search was used. The pure abstract m=2 4+4+4 example is a sharpness model, NOT an actual original G59 construction.

## 3. Application to genuine original masks

**Corollary (CLM-0230 application).** For EVERY genuinely S060-compatible original labelled T59 with all original q-only tests passed, either at least one 8^m non-q pair twist is a minimal total-zero original G59, OR its ORIGINAL reference D_M conditions exhibit one nonempty full eight-value mask, OR they contain at least TWELVE distinct (M,v) conditions. At EXACTLY twelve with no full mask all conditions must live on three split masks A,B,A triangle B and have aligned four-point cosets. This improves the predecessor's "at least nine" alternative to "at least twelve" for ALL m, not only m=2. It does not certify any actual minimal T, prove existence of feasible initial data, or prove the Davenport conjecture.

For m=0 the S060 q-only gate already tests every split and conditionally gives minimality if its initial full data exist. For m=1 the full-eight-versus-surviving-twist dichotomy is exact. For m=2 the theorem is precisely the S062/S063 additive-triangle obstruction. For m>=3, a twelve-condition cover must collapse to a two-dimensional **mask** plane even if its original parity classes aggregate differently; any nonempty fourth mask at N=12 supplies a surviving twist. In the equality case each of the twelve distinct mask/value pairs needs at least one genuine indexed ORIGINAL witness, and its complementary original proper subset is distinct with the same pair/value: at least 24 individual original proper subsets are forced. A full-eight case forces at least 16. These are necessary original-index obligations, not the existence of matching witnesses.

## 4. CLM-0231 — original intersection-carry restriction at equality

Assume the exact twelve non-full case is realised by genuine G witnesses, so D_A=a+L, D_B=b+L, D_C=a+b+L for C=A triangle B, |L|=4. For any two ACTUAL original parity-even torsion witnesses Z,Z' of two DIFFERENT masks P,P' from {A,B,C}, with full G sums 10v,10w, put J=Z intersect Z' and X=Z triangle Z'. Because P!=P', X cannot be empty; and because the complement of Z has the SAME mask as Z, X cannot be all 59 original positions. Thus X is automatically a nonempty proper original subset, with mask P triangle P' equal to the third one.

The exact full-G identity is
  sum_G(X)=10(v+w)-2sum_G(J).
If and ONLY IF the actual coordinatewise G intersection satisfies sum_G(J) congruent to 5d modulo10 for some d in Q, X has G torsion sum 10(v+w+d). In that case v+w+d MUST lie in D_(P triangle P') to agree with the exact D mask definition. But the prescribed equality cosets satisfy D_P+D_P'=D_(P triangle P'), and v+w is ALREADY in that latter coset. Hence necessarily
  d in L.                                                (carry condition)
In words: whenever a cross-mask witness overlap is 5Q-valued mod10, the overlap's normalized carry lies in the unique four-point subgroup L. Any actual cross-mask pair with d outside L destroys the asserted twelve-cover equality configuration. The sum must be computed in full original G before mod10; the hypothesis "intersection is 5Q-valued" is NOT automatic from mere parity or mask counts. Same-mask pairs obey the earlier S063 forbidden congruence sum_G(J) != 5(v+w) modulo10 whenever their symmetric difference is proper. Both genuine tests preserve original complementary and identical exceptions.

This gives a sharper **testable necessary support/carry law**, not a proof that the forbidden overlap exists. Moreover, for equality12 any mask outside the 2-plane has D_M=empty; an actual original torsion witness of ANY fourth mask immediately falsifies equality12, raising the danger budget to at least13 if the fibre nevertheless remains covered without a full mask.

## 5. Sustained priority A/B attack and precise limits

**Eight-full branch.** Suppose some D_M=Q. It demands eight distinct torsion values, hence eight actual nonempty proper original mask-M witnesses and their eight distinct complements (at least16 indexed subsets). For two witnesses at v,w, the proper symmetric difference has empty non-q mask, and S060 forbids it from having full G sum zero. The exact necessary condition is sum_G(Z_v intersect Z_w) !=5(v+w) mod10 (unless identical/complementary). The eight-value hypothesis alone provides no forced overlap congruence. This branch remains OPEN; an artificial assignment of D_M=Q is not a real Fano-compatible sequence.

**Twelve-distributed branch.** The theorem eliminates 9–11 FULL covers abstractly and forces any exact12 full cover into a 2-mask span and aligned four-point cosets. Original-index Fano/CRT constraints have not been proved to forbid those cosets. The true carry restriction above only fires if real overlaps are 5Q-valued mod10. It is invalid to impose that congruence on all pairs. Hence equality12 is a precise residual geometric obligation, not an established contradiction.

**Actual S060-gate survivor route.** The only known S059 fully indexed total-zero matching-only model still FAILS the true S060 four-Fano F_* / SAME-c CRT gate (S050/S051 five-residue slab). The abstract three-mask affine cover and S063 eight odd-mask example specify NO actual labelled G59 or original Fano data, so they do NOT qualify as survivors. We found no properly witnessed S060-feasible canonical original nonminimal G59 and no unexpected minimal G59. Thus neither a G58 zero-free counterexample nor D(C20³)=58 follows.

**Scope and evidence.** Original 30 frontier row objects and 28 historical SRC objects unchanged. Historical SRC-0008/0015/0023 remain SOURCE_STATED, especially unauthenticated computational D3(C5³)=25 from SRC-0015. The canonical display and its extremal H atoms retain their SOURCE_STATED assumptions. All 26 q hubs, three-hub pencils and P26 parity alternatives (z,r)=(0,4),(0,6),(1,7) still demand universal treatment. No Phase2/3, no mathematical search, no source promotion, no independent audit or hosted CI PASS.

## 6. Next exact theorem obligation

Use the theorem's forced dichotomy, not the obsolete nine-condition slack: for EVERY actual source-conditionally canonical S060 q-gate configuration, prove **(i)** full D_M=Q cannot be realised by true original supports/Fano data, **(ii)** any >=12 nonfull cover (starting with the EXACT12 aligned-coset equality obstruction) must trigger an actual q-only zero via original intersection carries, OR construct an actual fully labelled total-zero nonminimal G59 satisfying ALL genuine q-matchings and all four true Fano F_* constraints, locate its first non-q proper zero split and rigorously verify it. The unconditional full general n20 parity-profile proof is further downstream. All original labels, mixed odd g, E(U\I), six-singleton SAME-c CRT, complements and full G arithmetic remain mandatory.
