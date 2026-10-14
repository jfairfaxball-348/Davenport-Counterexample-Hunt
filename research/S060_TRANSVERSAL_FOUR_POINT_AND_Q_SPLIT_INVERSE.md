# S060 — Exact transversal four-point inverse, including all q-parity original pair splits

14 October 2026. **INTERNAL SYMBOLIC** Phase-1 mathematics, not independently certified. No claim of D(C20³)=58, a minimally zero-sum 59-index original sequence, or a 58-index zero-sumfree counterexample. This session attacks the actual-original-index missing bridge, building on S053/S052/S057/S059; no CAS, SAT, enumeration, solver, computational campaign, Lean, Palomar or external correspondence. Statements CLM-0221 and CLM-0222 are source-independent finite-group proofs, conditional on the canonical 22+8+7 profile, not universal to all C20³ sequences.

## 1. Set-up and original-index partition

Let G=(Z/20)^3; H=(Z/10)^3; iota:H→2G be iota(h)=2h, an isomorphism onto the even subgroup. It is **not** a splitting of G as C2³⊕H. Let Q=G/2G=F2³ and pi be quotient parity. Let T consist of 22 distinct labelled pairs (a_i,b_i) of original positions, u_i=iota^{-1}(a_i+b_i) in H, eight original g_j with pi(g_j)=q≠0, and original singleton positions s_r with pi(s_r)=r for every r≠0 in Q. All 59 positions are distinct *as indices*, with duplicate values allowed. Assume total(T)=0. Put U=(u_1,...,u_22), E(V)=H\{-sum(V_B): B a subset of the indexed V, including empty}. For a possible minimal T, U must be H-zero-sumfree.

Relative to q the six singleton positions other than s_q form three disjoint original pairs indexed by cosets of <q>. Choose r_1,r_2 independent modulo <q>, take r_3=r_1+r_2, and put
X_i=s_{r_i}, Y_i=s_{r_i+q}, V_i=X_i+Y_i in G (i=1,2,3); S=s_q.
Each V_i and S has parity q. The 12 q-supervertices from S,V_1,V_2,V_3 and the eight individually labelled g_j are disjoint ORIGINAL groups, just as in S059.

For eps∈{0,1}³, put T_eps=sum_i (X_i if eps_i=0, else Y_i). Its parity is (eps_1+eps_2+eps_3)q because r_1+r_2+r_3=0. The FOUR eps of even Hamming weight are 000,011,101,110 and precisely describe the four q-AVOIDING Fano lines. Write x_eps=iota^{-1}(T_eps)∈H for these four. The other four eps give q-parity three-singleton transversals, not individually divisible by 2.

Let P_q={i∈[22]:pi(a_i)=pi(b_i)=q}. For each I⊆P_q and each choice alpha=(alpha_i∈{a_i,b_i}:i∈I), set
U_I=U\{u_i:i∈I} (retaining original indices), A_alpha=sum_{i∈I}alpha_i in G.

Define the 256-label shift family (values may repeat)
B_{I,alpha}={ iota^{-1}( A_alpha + delta S + sum_{j∈J}g_j ):
delta∈{0,1}, J⊆[8], delta+|J| ≡ |I| (mod2) }.
The argument of iota^{-1} has EVEN G parity, so every shift is legitimate. Define the **exact transversal gate**
F_{I,alpha} = intersection_{b∈B_{I,alpha}} (E(U_I)-b) ⊆H,
and the simultaneous original q-split gate
F_* = intersection_{I⊆P_q} intersection_{alpha∈{a_i,b_i}^I} F_{I,alpha}.
For I=empty this is the 256-shift gate F_0, made of 128 even-g shifts and 128 (S+odd-g) shifts. The family is a symbolic finite intersection, NOT permission to enumerate or run a mathematical search. In particular these are E(U_I), never the invalid substitution E(U).

## 2. CLM-0221: exact four-transversal / all q-split original-index equivalence

**Theorem.** Suppose total(T)=0 and U is H-zero-sumfree. The following are equivalent:

(A) There is NO nonempty proper zero-sum subset of the 59 ORIGINAL positions whose set of split original pairs (exactly one of a_i,b_i selected) is contained in P_q.

(B) For EVERY I⊆P_q, split precisely the pairs in I into their two original q-members, and retain all other pairs as U_I. Every perfect matching of the N=12+2|I| disjoint q-supervertices yields a minimally zero-sum 28-block H sequence (the S059 condition); AND all FOUR genuine original Fano line H values x_000,x_011,x_101,x_110 belong to the SAME F_*.

This is an exact equivalence for the entire original-index family which splits only q-parity pairs; it is not an elimination or a theorem about split pairs of parity t_i≠q. H-atom minimality here is proved directly; identifying its 28 terms as maximal uses the separate historical SOURCE_STATED D(H)=28.

**Proof of (A⇒B).** Every H block of every described matching is the genuine iota-preimage of the sum of a disjoint even-parity set of original G positions. Their 28 blocks partition T. If a proper nonempty subcollection of blocks had H sum zero, it would be a proper nonempty original G zero subset, contrary to (A). Hence each matching is an H-atom. Now fix I, alpha, even eps, and an allowed delta,J in B_{I,alpha}. Select exactly the three ORIGINAL singleton indices specified by eps, delta copies of the ORIGINAL s_q position, the ORIGINAL g indices J, exactly the alpha_i selected originals from split pairs i∈I, and any subset B of the UNSPLIT full original pairs outside I. This subset is nonempty and proper (three Fano original indices are used, and at least their three complementary q-coset positions are omitted). Its sum is iota(x_eps+b+sum_{i∈B}u_i). By (A) this never vanishes, for any B. Hence x_eps+b∈E(U_I), for every labelled b. Thus x_eps∈F_{I,alpha} for every I,alpha, and x_eps∈F_*.

**Proof of (B⇒A).** Let Z be a nonempty proper original zero-sum subset with split pair set I⊆P_q, selecting member alpha_i on each i∈I and some full unsplit pair indices B⊆[22]\I. On the seven singleton original positions there are only two disjoint patterns compatible with the Q quotient after adding q-parity g and split members:

(i) Select NONE or BOTH from EACH of the three q-coset singleton pairs. The chosen outsider originals are then unions of whole S,V_i and g_j q-supervertices. Together with the chosen alpha_i original q vertices, their parity zero means their total number of selected q-supervertices is EVEN. Pair all selected vertices internally and all unselected vertices internally to extend them to a perfect matching on N vertices. Such an extension exists because N and the selected count are even. The chosen original Z becomes an H-block subcollection of that matching atom (including selected full U_I pairs). For I≠empty it is automatically a proper nonempty block subcollection since at least one alpha_i is selected and its mate omitted. For I=empty, the empty/full q-vertex cases are handled separately by U zero-freeness and total(T)=0 exactly as in S059: only Z=empty or Z=T can sum zero. Therefore there is no prohibited Z of type (i).

(ii) Select EXACTLY ONE from EACH of the three q-coset singleton pairs. If the choice eps has EVEN weight, the selected Fano triple itself has parity zero, and the rest has parity zero iff delta+|J|≡|I| (mod2). Its H sum is x_eps+b+sum_B u_i with b∈B_{I,alpha}. Since x_eps∈F_{I,alpha}, this is never zero. If eps has ODD weight, pass to the complement of Z within ALL 59 ORIGINAL positions: total(T)=0 implies this complement is also zero-sum, it is still nonempty and proper, its split set remains I but the chosen members become their mates alpha^c, all g and S choices are complemented, and its transversal eps^c has EVEN weight (three binary choices). The already proved even-eps case for alpha^c rules it out. This complementary argument is why ONLY four even-weight Fano triples are needed, despite eight possible three-singleton cuts. QED.

**Counting and interpretation.** At I=empty S059 matchings cover exactly 2046 proper grouped outsider tests. The remaining 2048 proper indexed outsider parity-zero tests are represented by four even-weight line values, each subject to 256 genuinely labelled shifts in F_0 (1024 labelled conditions); the other 1024 are automatically equivalent by original COMPLEMENT and E(U)=(-sum U)-E(U). No claim of 1024 independent H values. For I nonempty the same four-line F_{I,alpha} checks plus S059 split matching conditions likewise give *complete* coverage of the q-split-only original-index class. The total 59-index problem retains every t_i≠q split and the three-hub/alternate quotient profiles.

## 3. CLM-0222: precise four-value original-lift realisation, not free matching data

Fix U, the actual g_j, S, the actual original pair member values, and the THREE q-coset original group sums V_i∈G with pi(V_i)=q, subject to total(T)=0. Regard the six individual X_i,Y_i as variables with fixed named quotient parities pi(X_i)=r_i, pi(Y_i)=r_i+q and X_i+Y_i=V_i. Let overline(v) denote reduction of a G element modulo10, lying in H. Let rho:H→H/2H=Q denote coordinate reduction modulo2. For i≠j let d_ij=iota^{-1}(V_i+V_j)∈H, well-defined since both have parity q, and define Delta_ij=rho(d_ij)+r_i+r_j in Q.

**Exact realisation theorem.** A four-tuple (x_0,x_12,x_13,x_23) of H values is realised by such SIX original singleton values at the four even-weight transversals (x_0=x_000, x_12=x_110, x_13=x_101, x_23=x_011) **if and only if**
(1) x_0+x_12+x_13+x_23 = overline(V_1+V_2+V_3) in H;
(2) rho(x_ij-x_0)=Delta_ij in Q, for ij=12,13,23.
There are exactly 2^6 distinct original labelled (X_i,Y_i) choices per feasible H four-tuple. Consequently, with the fixed other data and matching prerequisites of CLM-0221, existence of an original singleton lift passing ALL no-q/nonzero-q pair-respecting plus ALL q-parity one/multi-split original tests is **equivalent** to existence of a four-tuple IN F_* satisfying (1) and (2). This is the precise remaining mathematical *feasibility* gate for the canonical q-split-only subproblem; it does not establish emptiness for arbitrary U.

**Proof, necessity.** Each of the SIX original X_i,Y_i occurs in exactly TWO of the four q-avoiding Fano transversal triples. Summing all four genuine G triple sums gives 2(V_1+V_2+V_3), which after iota-inverse gives (1). For ij, the transversal changing i and j from X to Y differs in G by (V_i-2X_i)+(V_j-2X_j). Thus
x_ij-x_0 = iota^{-1}(V_i+V_j)-overline(X_i)-overline(X_j)
and reducing mod2 proves (2), since rho(overline(X_i))=r_i. This is a full original-index mod20 calculation, not a guess that four H line values are independent.

**Proof, sufficiency and exact fibre.** Choose ANY reference lifts X_i^0 of parity r_i and set Y_i^0=V_i-X_i^0, of the required opposite q-coset parities. Every possible other labelled lift has X_i=X_i^0+iota(z_i), Y_i=Y_i^0-iota(z_i), with z_i∈H. Changes in the four H transversal values are the linear map H³→H⁴ whose matrix, in order (000,110,101,011), is
  B = [[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1]].
The four rows add to zero. Modulo5 the first three rows have determinant ±4 (unit), so im(B mod5) is EXACTLY the hyperplane whose four coordinates sum0. Modulo2 all four rows equal (1,1,1), hence im(B mod2) consists EXACTLY of four equal binary values. Applying CRT coordinatewise in the THREE H coordinates proves that the changes realised by B are precisely those with zero total in H and equal parity among all four components. The target (1) has the baseline total, while (2) says every target-minus-baseline component has the same parity; together they are exactly the image conditions. The modulo5 kernel is zero; the modulo2 kernel has dimension2 per H coordinate, giving 2^(2·3)=2^6 original labelled lifts for each feasible tuple. QED.

**Usable immediate necessary test.** Put A=rho(F_*)⊆Q. A permissible lift must contain FOUR members x_0,x_ij∈F_* with prescribed parity differences Delta_ij AND exact full H sum overline(sum V_i). In particular overline(sum V_i)∈F_*+F_*+F_*+F_*; this coarse fourfold sumset inclusion is NECESSARY but emphatically not SUFFICIENT: the mod2 differences must match and the four H elements must be the actually coupled original-lift values. This upgrades the old all-even g set K(W,U) test by incorporating s_q+odd g AND every q-parity original pair split, including multi-splits and E(U\I).

## 4. Hostile test: S059 saturated matching model and first genuine original zero

The real S059 hostile model has V_1=V_2=V_3=S=g_1=...=g_8=e3 in G and U=e1^9 e2^9 e3^3 (e1+e2+e3) in H, for every m=0,1,2,3, regardless of which m e3-pairs are explicitly split. Direct indexed subset-sum algebra gives E(U) = {h∈H: third-coordinate(h)∈{1,2,3,4,5}}: without the diagonal, third subset sums run0..3 and horizontal first/two coordinates run all residues; with the diagonal, third sums run1..4 and horizontal sums again all residues. This is the same five-residue SLAB phenomenon previously exploited by S050/S051 for another core; do NOT claim a novel independent slab obstruction.

For every even-weight Fano line value x_eps, taking 0,2,4,6,8 ORIGINAL g positions gives five necessary memberships x_eps+k e3∈E(U) for k=0..4. Hence third(x_eps)=1 mod10, for ALL four lines. But the full original-index four-line sum identity from section3 gives
third(x_000+x_110+x_101+x_011)=third(overline(V_1+V_2+V_3))=3 mod10,
whereas four values each having third coordinate1 would sum to4 mod10. Contradiction. This proves **EVERY lift of the fixed S059 q-coset group totals fails a real ORIGINAL transversal test**, not just the named lift already exhibited by S059. It remains a SPECIAL-CORE exclusion already within the scope of S050/S051-style slab mathematics, not an arbitrary-U22 proof.

The FIRST forced genuine original zero has an explicit INDEX-SET FORM: at least one of the four q-avoiding Fano line triples L and some k∈{0,...,4} has third(x_L+k e3) outside {1,...,5}; because the ENTIRE H complement of E(U) is exactly the set with those other third residues, an indexed subset B of the 22 U pair blocks satisfies sum_B u=-(x_L+k e3). The ORIGINAL G zero subset consists of the THREE singleton positions of L, ANY 2k of the eight ORIGINAL g positions, and BOTH original members of every pair indexed by B. It is nonempty proper, using at most3+8+44=55 original positions. For the concrete S059 lift X_1=s_e1=-e1, X_2=s_e2=e2, X_3=s_(e1+e2)=e1+e2, take L={e1,e2,e1+e2}, k=0 and B the nine e2-pairs: 3+18=21 original indices have sum 2e2+18e2=20e2=0. This is not a zero-free candidate.

## 5. Attempted universal implication and exact boundary

One would like to prove **for every** permissible source-conditional canonical U22, actual eight g_j, actual S,V_i and original pair member values with all t_i≠0 and total0, the q-hub all-matchings conditions force the S060 exact affine four-tuple feasibility set in F_* to be EMPTY. We did NOT prove this. The predecessor S059 model refutes the stronger mistaken inference that q-hub matching conditions alone are inconsistent; this session isolates the additional full-original-data inverse condition they omit. The S050/S051 slab examples kill special U22 and do not establish an arbitrary-U theorem. Even a canonical q-split-only impossibility would not cover t_i≠q original splits, 26 three-hub pencils, or alternate (0,4),(0,6),(1,7) profiles. Historical SRC-0008 D(C5³)=13, SRC-0015 D3(C5³)=25, SRC-0023 D(C10³)=28 remain SOURCE_STATED, and none were promoted.

**Strongest false shortcut killed:** treating any four individually admissible E-extension values as independently choosable Fano lines, or treating the fourfold sumset inclusion alone as a sufficient original lift, is INVALID. The original modulo2 difference pattern (2) and full modulo10 sum (1) are both mandatory; the exact converse proves no other singleton-only restrictions exist once fixed V_i and original parities are respected. Similarly, omitting E(U\I) in split constraints or identifying synthetic edges across different matchings with a common original set invalidates the statement.

**Precise new next theorem obligation:** prove the intersection F_* admits no four elements satisfying (1),(2) whenever the full S059 q-hub matching-atom hypotheses hold for arbitrary canonical actual group data; OR exhibit a fully indexed actual G59 TOTAL-ZERO nonminimal countermodel meeting BOTH those families and locate its first t_i≠q or noncanonical original zero. Do not assert either result without direct proof. All mathematics remains Phase1 INTERNAL.
