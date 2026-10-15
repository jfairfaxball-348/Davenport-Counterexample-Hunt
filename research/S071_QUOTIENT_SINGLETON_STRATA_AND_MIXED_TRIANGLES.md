# S071 — original parity-signature theorem and mixed Fano bridge obstruction

15 October 2026. INTERNAL SAME-EXECUTOR Phase-1 symbolic investigation, owner-invoked exactly S071. Source-conditional 22-pair + eight g + seven singleton original canonical G59; not a proof of D(C20^3)=58 or a G58 zero-sumfree counterexample. No mathematical numerical search, CAS/SAT/ILP, model/orbit generation, Lean/Palomar or external proof certification. All 59 indices are actual labelled ORIGINAL positions, and full group arithmetic is in G=(Z/20)^3, never a false splitting G=H⊕Q.

## 1. Genuine data and the previously missing singleton stratum

Assume the *actual* S060 canonical total-zero T of 59 original indices: 22 equal-parity pairs (a_i,b_i) with t_i=pi(a_i)=pi(b_i)≠0, eight g_j of parity q≠0, and seven singleton original indices s_r for each r∈Q\{0}, Q=F2^3. Let P_q={i:t_i=q}, N={i:t_i≠q}, m=|N|. The U22 pair sums u_i in H=C10^3 are H-zero-sumfree; all q-only H28 matchings, E(U\I), four true Fano x_eps, full sum C, mod2 Delta, original outsider transversals and proper-complement tests are assumed. No claim that such T actually exists.

As in S060, label the six singleton originals other than s_q by three disjoint q-coset pairs (X_j,Y_j) with pi(X_j)=r_j, pi(Y_j)=r_j+q for j=1,2,3, where [r_1],[r_2] form a basis of V=Q/<q>≅F2^2 and [r_3]=[r_1]+[r_2]. For ANY literal original index subset Z, define its non-q pair-split mask M(Z)⊆N and the three-bit *singleton split signature* h(Z)∈F2^3, where h_j(Z)=1 iff Z contains EXACTLY ONE of X_j,Y_j. A singleton coset pair with h_j=0 is either fully included or absent, regardless of its q parity contribution. Define

  Phi(M)=sum_(i∈M) [t_i] in V,
  R(h)=h_1[r_1]+h_2[r_2]+h_3[r_3] in V.

These are actual quotient maps; neither is a torsion colour v∈Q nor the epsilon choice of a true Fano transversal. Crucially, an arbitrary non-q torsion witness is NOT necessarily a Fano transversal. Its six singleton positions can have one, two or three q-coset pairs split.

## 2. CLM-0252 — exact original singleton-signature quotient obstruction

**Theorem.** For any ORIGINAL subset Z, independently of its sum modulo5,

  [pi(sum_G Z)] in Q/<q> = Phi(M(Z)) + R(h(Z)).           (S71.1)

In particular, if sum_G Z lies in G[2]=10Q, then

  Phi(M(Z))=R(h(Z)).                                    (S71.2)

For a fixed M, the admissible h-signatures for *zero quotient parity modulo <q>* are exactly TWO bitstrings h0 and h0⊕111. If Phi(M)=0 they are 000 (grouped singleton coset pairs) and 111 (a genuine Fano transversal, either parity of epsilon); if Phi(M)≠0 they are the one-split pattern {j} and its two-split complement {1,2,3}\{j}, where [r_j]=Phi(M). This is an exact parity/quotient classification, NOT sufficient for a G[2] subtotal or for any S060 q gate. One can algebraically correct any remaining quotient q-bit by selecting one g_j, but this does not correct modulo5.

**Proof.** Every selected full pair a_i+b_i has even quotient parity 0, and neither selected endpoint contributes 0. Exactly one selected member of a pair i contributes t_i. Thus non-q split originals contribute sum_(M)t_i, q pair splits only multiples of q. Every selected g_j or s_q contributes q. For a singleton q-coset pair (X_j,Y_j), selecting neither has parity 0, both gives r_j+(r_j+q)=q, and exactly one gives r_j+epsilon_j q. Modulo the line <q>, the last contribution is precisely h_j[r_j]. These exhaust the original 59 positions, giving (S71.1). The map R:F2^3→V has kernel {000,111} because [r_1],[r_2] are a basis and [r_3]=[r_1]+[r_2]. Each fibre is therefore exactly the two indicated complementary bitstrings. If sum_G Z∈10Q, its parity pi is zero, hence (S71.2). QED.

**Scope warning.** If Phi(M) is NONZERO, there is *no actual torsion witness with mask M* whose six singleton positions form a three-index Fano transversal; nor can those positions be entirely grouped. A mixed one-vs-two split pattern is mandatory, whether or not x_000,x_011,x_101,x_110 satisfy the S060 gate. The q-only Fano gate does not supply or re-select the missing mixed-mask witness.

## 3. CLM-0253 — sharp Fano-compatible mask kernel and two-pair no-go

**Theorem.** An actual parity-even Fano-transversal witness with non-q split mask M must lie in the linear subspace

  K_Fano=ker(Phi:F2^N→V).                                (S71.3)

If m>0, every [t_i]∈V is NONZERO because t_i∈Q\{0,q}, so rank(Phi) is 1 or 2. Thus dim(K_Fano)=m-rank(Phi); three distinct nonzero Fano-admissible masks A,B,A△B require dim(K_Fano)≥2. In particular:

(a) For m=1, NO nonempty mask is Fano-admissible.

(b) For m=2, NO three distinct nonempty masks A,B,A△B can all have Fano-transversal torsion witnesses, regardless of U, q-matchings, four Fano x values, C or Delta. If [t_1]≠[t_2], NONE of {1},{2},{1,2} is Fano-admissible; if [t_1]=[t_2], ONLY {1,2} is.

(c) For m=3, the rank-two kernel has dimension 1 and again supplies no complete A/B/A△B Fano triangle. Such a triangle of masks can be quotient-admissible only if rank(Phi)=1, equivalently ALL THREE [t_i] equal, when the possible three nonempty masks are {1,2},{1,3},{2,3}. The latter is merely parity admissibility and does NOT guarantee any torsion witness.

(d) More generally partition the non-q indices into the three nonzero classes c1=[r1],c2=[r2],c3=[r3] of V. Writing p_j(M) for the parity of the number of selected indices in class c_j, the condition Phi(M)=0 is EXACTLY

  p_1(M)=p_2(M)=p_3(M) in F2.                             (S71.4)

In particular every nonempty Fano-admissible mask has at least two non-q pair indices, unless it includes at least one from each of the three classes (in which case size≥3).

**Proof.** Fano transversals mean h=111 and R(111)=0, so (S71.2) gives Phi(M)=0. Since each non-q t_i is nonzero and different from q, [t_i] is a nonzero element of V. Rank-nullity yields (S71.3) and dimension statement. With m≤2, rank≥1, nullity≤1, so no two independent nonzero A,B can lie in the kernel. For m2 if the two classes differ they are a basis of V, kernel0; otherwise kernel is span(11). For m3, rank1 iff all three columns are the same nonzero class, then kernel is the even-weight plane, whose three nonzero vectors are 110,101,011. Finally c3=c1+c2, so Phi(M)=(p1+p3)c1+(p2+p3)c2, which vanishes iff the three parities agree. QED.

**Consequence for EXACT12, not its elimination.** In m=2 the exact12 cover necessarily has the three masks {1},{2},{1,2}. The two singleton-mask danger colours might be witnessed by *mixed* singleton patterns, but **cannot be witnessed by true Fano-transversal torsion subsets**. Thus the strong S071 primary method of selecting THREE true EVEN-Fano witnesses from abstract D_A,D_B,D_C has a direct unavoidable original parity obstruction for every m2 profile; merely choosing their torsion colours to sum zero cannot rectify it. This does NOT prove the exact12 configuration impossible or construct a real S060-feasible G59.

## 4. CLM-0254 — mixed-support cross-mask triangle admits exactly grouped/Fano XOR strata

**Theorem.** Take ANY three actual G[2] witnesses Z_A,Z_B,Z_C with non-q masks A,B,C=A△B, not necessarily Fano individually, and their actual singleton signatures h_A,h_B,h_C. Their original XOR X=Z_A△Z_B△Z_C satisfies

  M(X)=∅,   h(X)=h_A⊕h_B⊕h_C∈{000,111}.                 (S71.5)

If h(X)=000, X uses none or BOTH of each original q-coset singleton pair; the *grouped* q-hub matching gate excludes a zero sum for any nonempty proper X. If h(X)=111, X selects precisely one ORIGINAL singleton in each coset pair; it is automatically nonempty proper and the TRUE q-split Fano/E(U\J) gate excludes a zero, using complement for an odd Fano epsilon. If X=∅ or X=T, only h(X)=000 is possible; it is not a contradiction and is not silently discarded.

**Proof.** Original pair split membership under XOR is XOR-linear, so A⊕B⊕C=∅ and X has no non-q pair split. Similarly for each singleton pair, the parity of the number of its two selected endpoints is the XOR of its three separate status parities, so h(X)=h_A⊕h_B⊕h_C. Each witness has even quotient parity, hence pi(sum_G X)=0 (the difference between XOR and ordinary summation is an even multiple of G labels), and (S71.1) for M(X)=∅ yields R(h(X))=0. Thus h(X) is 000 or111. The q-only original-index gate CLM-0221/0222 handles both types exactly, but only for proper nonempty X. For h=111 the selected singleton triple proves properness (three selected and the three complementary singleton indices omitted). For h=000, q-hub grouping is literal original-index full/empty Fano coset pairs, not an invented H edge; an empty or full XOR is allowed. QED.

**Exact12 colour-zero refinement.** Pick true witnesses with v_A+v_B+v_C=0 as S070 guarantees. The majority K and XOR X still obey sum_G X=−2sum_G K. Equation (S71.5) now reveals two *genuinely different* routes:
1. If h_X=111, properness is free even though NONE of the three individual witnesses need be Fano. One still has to FORCE lambda_G(sum X)=0 and pi(sum K)=0; neither follows from the signature.
2. If h_X=000, the gate protects a proper X, but one must additionally force X to be proper. Distinct non-q masks do NOT ensure it for a triple; a disjoint-set union Z_C=Z_A△Z_B has X=empty and can have distinct masks and nonzero torsion sums.
The XOR status h_X cannot be changed by replacing any selected original witness with its original full complement: complement preserves the split/unsplit status of every pair, although it changes endpoint orientations and takes X to its complement. Therefore complement choice alone does not select the Fano branch.

## 5. An explicit *symbolic* mixed-m2 table (not a 59-label model)

Assume m=2 and [t1]≠[t2], so Phi({1}),Phi({2}),Phi({1,2}) are precisely the three nonzero classes of V. Relabel q-coset singleton pairs so they correspond to {1},{2},{3}. Then a torsion witness with mask {1} has signature 100 or011; mask {2} has 010 or101; mask {1,2} has 001 or110. These are EXACT necessary singleton split patterns for the original data, not discretionary Fano choices. Selecting the one-split representatives 100,010,001 produces h_X=111 (proper q-only Fano XOR); selecting 100,010,110 produces h_X=000 (potentially empty/full XOR). These are allowed parity patterns ONLY; no matching U/G subset, true C5-zero sum, or all-S060-gate-passing witness is asserted. Even when 16 abstract colour-zero triangles exist, colours alone do not ensure any given pattern is available as a real original support.

For the m2 same-class case, {1},{2} still require mixed signatures for the same nonzero quotient class, while {1,2} may be grouped 000 or Fano 111. Consequently the original S071 demand that all three zero-colour witnesses be even-Fano fails on quotient grounds even in this case.

## 6. Aggressive proof attempts and hostile failure analysis

**Attempt A: force all three S070 exact12 witnesses to be true even Fano by re-selecting original supports.** Impossible for m≤2 by CLM-0253. For m≥3 the mask kernel may have dimension at least2, but no S060 or D-set theorem forces any mask's torsion colour to have Fano support. Quotient-admissible is NOT witness-realised.

**Attempt B: use zero-colour a+L,b+L,a+b+L to tune mixed singleton signatures.** The zero-colour selection chooses one among actual witnesses with a specified 10v subtotal. The D_M definition forgets h(Z); there is no justified inference that the 4 genuine colours in a mask realise both h and h⊕111. This is the precise missing *support-type extension theorem*. Complements preserve h, and paired 10theta gauges preserve all singleton indices/h. The 16 available colour combinations therefore do not imply a true Fano-XOR branch without a new coupling argument.

**Attempt C: force majority parity and C5-zero projection.** Even in the improved mixed-Fano X branch, the identity sum X=−2sum K plus q-gate only yields S070's order-four escape. Neither Phi-h data (a quotient mod2 condition) nor zero-colour torsion sums determine lambda_G(sum X), which depends on genuine original intersections. For a majority K that itself selects one singleton per q-coset pair, if K∈G[2] its non-q split mask E must satisfy Phi(E)=0; this is a necessary filter, not a newly forced fourth mask. No false C5 carry is promoted.

**Attempt D: full-eight, extra-cover or 59-label hostile example.** CLM-0252 applies to each actual D-mask witness in FULL8 or 13/14/≥15 covers as well: it gives its *two possible* original singleton split strata, but not their mod5 support counts. No contradiction to FULL8, exact12, enlarged13/14, ≥15 no-full, any Delta rank, or m≥3 emerges. We have not built any actual 22-pair+8-g+7-singleton C20³ total-zero model simultaneously passing S060 q-H28 matchings, E(U\I), 2048 transversals, true four Fano C/Delta and U22 zero-freeness with a first non-q zero. Do not recycle the S059 matching-only nonminimal model (it fails F_*). No computation has been run or claimed.

**Adversarial scope.** The stratification is exact quotient arithmetic for the fixed q canonical profile, not a proof the profile occurs for every hypothetical 59-term atom. All 26 possible q hubs, three-hub options and alternate P26 profiles (0,4),(0,6),(1,7) require separate global exclusion. No claim of a 58-term zero-sumfree sequence or D(C20³)=58 or general D((Z/n)^3)=3n−2 follows. Internal review is same executor; no external validation, no hosted CI pass. Original30 frontier rows and all29 source records untouched; SRC-0008/0015/0023/0029 remain source-stated as before.

## 7. Real bridge after S071

To close the exact12 case, target a REAL colour-zero triangle across the **correct Phi-MIXED singleton strata**, not an unjustified all-Fano triangle. Prove, with original full-pair B, non-q split endpoints, q-split J, g/S outsider membership and actual six singleton labels, that either (i) at least one colour-zero triangle has h_X=111 and both lambda_G(sum X)=0 and pi(sum K)=0; (ii) grouped h_X=000 has nonempty proper X with these properties; (iii) a true majority K has G[2] sum and a new non-q mask E; or (iv) FULL8/12+/all hubs are eliminated by another complete original bridge. Otherwise supply a fully labelled fully q-gated original hostile G59 with first exact non-q zero and complement. These obligations are NOT met by S071.

**Verdict:** CLM-0252–0254 INTERNAL PROGRAMME_PROVED conditional exact original quotient algebra. The restricted *three true even-Fano-witness* primary approach is proven impossible for m≤2, but the genuine mixed-stratum original-index contradiction is OPEN. Phase1 IN_PROGRESS, not PASS.
