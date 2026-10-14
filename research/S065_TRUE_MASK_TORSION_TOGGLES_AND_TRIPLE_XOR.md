# S065 — Exact original-mask extension gates, order-two pair toggles, and triple-witness collisions

14 October 2026. Owner-invoked one sustained Phase-1 ORIGINAL-INDEX symbolic C20³ investigation. **INTERNAL mathematical proofs and same-executor hostile review**; no CAS/SAT/ILP, numerical/computational mathematical search, orbit generation, Lean, Palomar, campaigns, manuscript, outreach or certification. Claims CLM-0232–0234. These results hold conditionally in the S060 canonical source-conditioned 22+8+7 original-position setting, NOT for all 59-term configurations. **No full-eight or ≥12 real obstruction excluded universally, no fully S060-gate-passing nonminimal original G59 constructed, no D(C20³)=58, no original zero-free G58.**

## 1. Exact original data and decisive obstruction

Let G=(Z/20)^3, H=(Z/10)^3, iota(h)=2h∈G, Q=(F2)^3=G/2G and G[2]={10v:v∈Q}. All identities of labelled original sums are initially in G, never in an alleged C2³⊕H splitting. T is the ACTUAL total-zero 59-position sequence: 22 distinct indexed original pairs (a_i,b_i), each with equal nonzero quotient parity t_i and u_i=iota^{-1}(a_i+b_i)∈H; eight original q-parity g_j; seven distinct indexed singleton positions s_r for all r≠0, with q≠0. N={i:t_i≠q}, m=|N|, P_q={i:t_i=q}. Assume every S060 q-only gate genuinely passes: U22 is H-zero-sumfree, every original q H28 matching atom for every I⊆P_q and selected original members, every E(U\\I), all four real Fano H values in SAME F_* satisfying full modulo10 sum and three modulo2 differences, every mixed odd-g shift. No unsupported arbitrary-U feasibility assertion.

For any nonempty proper ORIGINAL index subset Z with even full-G parity and G subtotal 10v, define its precise non-q split mask M(Z)⊆N (i∈M iff exactly one of a_i,b_i occurs). For nonempty M⊆N let D_M={v∈Q: such a Z with M(Z)=M}. The S063 order-two pair gauges θ∈Q^m change the subtotal by 10∑_{i∈M}θ_i. A gauge survives iff every θ_M avoids D_M, because M=∅ actual zero is forbidden by S060. S064: every-gauge failure implies one full D_M=Q or ≥12 distinct (M,v), and equality12 without a full mask forces precisely A,B,C=A△B with D_A=a+L,D_B=b+L,D_C=a+b+L, |L|=4, all other nonempty D empty.

## 2. CLM-0232 — all genuine forbidden masks are exact indexed E(U\\I) failures

**Theorem.** For EVERY nonempty M⊆N and v∈Q, v∈D_M IF AND ONLY IF the following genuinely original-index data exist:

* a subset J⊆P_q and I=M∪J;
* a choice α_i∈{a_i,b_i} of exactly one ORIGINAL member for each i∈I;
* a subset R of the FIFTEEN labelled outsiders O={g_1,...,g_8}∪{s_r:r∈Q\\{0}}, satisfying the actual quotient equation ∑_{i∈I}t_i+π(∑_{z∈R}z)=0 in Q;
* a subset B⊆[22]\\I of the unsplit original full pairs;

such that, with b_{I,α,R}=iota^{-1}(∑_{i∈I}α_i+∑_{z∈R}z)∈H,
    b_{I,α,R}+∑_{i∈B}u_i = 5v  in H.           (1)

Equivalently, if ℒ_M denotes the EXACT original allowed labelled (I,α,R) shifts above, then
    D_M={v∈Q: there is (I,α,R)∈ℒ_M with b_{I,α,R}+5v NOT IN E(U\\I)}.   (2)
Here E(U\\I)=H\\{−∑_{i∈B}u_i:B⊆[22]\\I}, with EVERY original index retained.

**Proof.** For any original subset with precise mask M, its q-parity split pairs are some J⊆P_q, its chosen split members are α, its selected full unsplit pairs B, and its selected outsiders are R; these determine Z uniquely. All pairs in B have even G sum 2u_i. The parity equation is necessary and sufficient for ∑α+∑R to be even, so iota^{-1} exists. The full G subset sum is precisely 2(b+∑_B u_i). Equality with 10v in G is precisely (1) in H. Conversely these four original-index choices construct Z with mask exactly M and parity even. Since M is nonempty, Z is automatically nonempty (one selected member) and proper (its mate unselected), even at extreme B,R. The E complement identity is: (1) iff ∑_B u_i=5v−b iff −∑_B u_i=b−5v=b+5v, because 5v=−5v in H. Hence (2). Original complement corresponds to mates α^c, R^c, complement B^c and has the SAME mask and 10v subtotal, since total(T)=0. QED.

**Interpretation.** This is a REAL indexed E(U\\I) test for EVERY non-q mask; no abstract free mask/colour assignment can be mistaken for a survivor. A FULL eight mask means all eight distinct order-two values 5Q are hit in the exact union (2), and exact12 means three masks each hit exactly one prescribed four-point affine L-coset and NO fourth mask hits even one. This does NOT show those hits occur for any actual U22. It does not replace the SAME-c four-Fano feasibility gate or the 26-hub/three-hub/P26 alternatives.

## 3. CLM-0233 — order-two unsplit original-pair toggle rigidity, a true additional bridge

Let R_2={i∈N : u_i=5e_i for some nonzero e_i∈Q}. They are non-q ORIGINAL pair indices whose COMPLETE original two-member sum is 10e_i in G; no endpoint is treated as a synthetic H matching edge.

**Theorem (real support-toggle invariance).** For EVERY nonempty mask M⊆N define
    L_M=span_{F2}{e_i : i∈R_2\\M} ≤ Q.
Then
    D_M+L_M=D_M.                                      (3)
Thus every nonempty D_M is a UNION of L_M-cosets and |D_M| is a multiple of 2^{dim L_M}. If dim L_M=3, ANY original torsion witness of mask M alone forces D_M=Q (the eight-full obstruction).

**Proof.** For i∈R_2\\M, the ORIGINAL pair i is unsplit in every Z of mask M: either neither of a_i,b_i occurs or both occur. Toggle membership of BOTH original indices. The mask stays M, and the original G sum changes by +10e_i in the empty→full case or −10e_i in the full→empty case; these are identical because 10e_i has order two in G. Since M≠∅, some different pair remains split, so the toggled Z is still nonempty proper. Consequently v∈D_M implies v+e_i∈D_M, and this involution can be repeated for all indices outside M in R_2. Hence (3). No q pair is silently toggled: q-pairs may be split in the original witness and are excluded from R_2 by definition. QED.

**Theorem (new exact12 exclusion).** If a genuine exact12/no-full S064 obstruction D_A=a+L,D_B=b+L,D_C=a+b+L with C=A△B exists, then
    span{e_i:i∈R_2} ≤ L.                              (4)
In particular, THREE linearly independent u_i=5e_i among NON-q original pair indices make the exact12 obstruction IMPOSSIBLE. Any all-twist failure under that hypothesis must instead have a full-eight D_M=Q or at least THIRTEEN distinct (M,v) conditions.

**Proof.** Fix any i∈R_2. Since the indicator of i in C equals its indicators in A and B added mod2, it cannot belong to ALL THREE masks A,B,C. Choose a supported mask P among them with i∉P. By (3), D_P is invariant under addition of e_i. But D_P is a nonempty single affine coset of L, whose translation stabilizer is precisely L. Therefore e_i∈L. This holds for every i∈R_2, proving (4). Since dim L=2, rank-three R_2 contradicts it. This argument uses the THREE actual supported ORIGINAL split masks, not a falsely assumed common coefficient-parity subspace. QED.

**Independent rank audit.** S060 assumes U=(u_i) is H-zero-sumfree. Any nonempty F2-dependence among the order-two terms u_i=5e_i would be an indexed U-zero subset, so the e_i of ALL order-two U terms are linearly independent in Q. In particular |R_2|≤3, and if |R_2|=2, equality12 forces L=span(e_i:i∈R_2). Nothing establishes that |R_2|=3, or even R_2 nonempty, in arbitrary S060-feasible data. Thus the new exclusion is genuine but CONDITIONAL, not the missing universal bridge.

**Hostile full-eight no-go for simple collision counting.** If an actual mask-M reference torsion witness Z exists and THREE independent order-two non-q pair blocks lie OUTSIDE M, toggling them produces precisely eight ORIGINAL mask-M witnesses with all eight values v+span(e_1,e_2,e_3)=Q. For distinct toggles their ORIGINAL symmetric difference consists exactly of a nonempty set of those complete pair blocks, with G sum 10(e_{i_1}+⋯+e_{i_k})≠0. Therefore **these eight values alone do NOT force even a pairwise S060 q-only zero**. This is a conditional original-index mechanism, not a full 59-position S060-gate survivor; it destroys a proposed counting-only contradiction in the full-eight branch.

## 4. CLM-0234 — triple-mask original XOR: a collision test without any pairwise 5Q hypothesis

**Theorem.** Suppose Z_A,Z_B,Z_C are ACTUAL nonempty proper original torsion witnesses of masks A,B,C=A△B, with G subtotals 10v_A,10v_B,10v_C. Put J_AB=Z_A∩Z_B, J_AC=Z_A∩Z_C, J_BC=Z_B∩Z_C, K=Z_A∩Z_B∩Z_C, and X=Z_A△Z_B△Z_C. Then:
    M(X)=∅,
    sum_G(X)=10(v_A+v_B+v_C)
             −2(sum_G(J_AB)+sum_G(J_AC)+sum_G(J_BC))
             +4sum_G(K)                             (mod20).       (5)
If X is nonempty proper, the right side CANNOT be zero in G under the actual S060 q-only gate, EVEN IF no individual pairwise overlap lies in 5Q mod10. At exact12, v_A+v_B+v_C∈L; hence an observed triple whose weighted overlap
    Ψ=2(∑ sum_G J_pairs)−4sum_G K
equals 10(v_A+v_B+v_C) in G, with X proper nonempty, disproves that actual equal12 witness system.

**Proof.** For original membership bits x,y,z∈{0,1}, the XOR bit is x+y+z−2(xy+xz+yz)+4xyz. Sum this identity weighted by each ORIGINAL G element. Every pair's split-membership bit is F2-linear under symmetric difference, so M(X)=A△B△C=∅. Every ORIGINAL pair with non-q parity is therefore either fully present or fully absent from X; all split pairs of X, if any, belong to P_q. Its original G parity is zero because the three torsion subsets each have parity zero. S060 CLM-0221 excludes any nonempty proper zero such X. Empty or full X are necessary and explicit exceptions; full original T has total0 and must NOT be counted as a proper zero. At exact12, coset arithmetic gives (a+L)+(b+L)+(a+b+L)=L, and (5) gives the asserted direct triple-collision certificate. QED.

**Why this differs from S064's pair-carry:** Each pairwise overlap can have arbitrary residues modulo5, while the weighted combination of all three overlaps and the triple intersection might equal the torsion target. There is no logical need to first prove that a particular pair intersection is 5d mod10. Conversely, the mere existence of three masks with four values each does NOT force the weighted equality: it requires ACTUAL common original support arithmetic. This remains a concrete proof obligation rather than a claimed contradiction.

## 5. Extensive attack log and limits

**Real exact12 route.** The new ORIGINAL order-two block symmetry (3) and three-mask parity relation force the global inclusion (4), excluding exact12 WHEN independent non-q 2-torsion block rank is three. For rank0, rank1 or rank2, exact12 remains viable as an abstract covering certificate. No valid argument extracted a mandatory rank3 from all H28 q matchings, U22, every E(U\\I), mixed odd g or SAME-c Fano gate. Such a claim would need an inverse theorem for arbitrary U22, and source-stated D(C10³)=28 is not that inverse theorem.

**Real full8 route.** The three-independent-toggles witness gadget demonstrates how eight different REAL mask-M torsion labels could arise from one base witness WITHOUT a pairwise zero carry. It is not a total-zero S060-compatible 59-label example. For a full mask lacking rank3 order-two toggles, the missing constraint is a genuinely forced forbidden overlap among its eight different labelled values. No such overlap was forced.

**≥13 cover route.** S064's exact12 rigidity does not classify nonfull 13+ covers. The new masked E-gates impose real data, and (3) puts subgroup-divisibility requirements on each danger D_M; nevertheless no general upper bound N≤12, reduction of a 13+ cover, or universal original collision follows. Do not count 12 conditional witnesses as an automatic exhaustive list.

**Small m.** m=0: q-only S060 clearance would imply minimality if the entire 59-label dataset existed, but no actual feasible dataset was produced. m=1: full-eight remains the sole way all legal pair gauges fail. m=2: existing additive triangle remains; if two non-q order-two block directions e1,e2 are independent, any exact12 common L MUST equal span(e1,e2). No small-m feasibility was inferred from the formulas.

**Hostile construction.** The S059 matching-only total-zero G59 example still fails true S060 four-Fano F_*; it cannot be advertised as a fully-gated hostile survivor. In this session no independently verified labelled total-zero G59 satisfies ALL genuine S060 gates with its first non-q proper zero identified. No minimal G59 was verified, and no G58 zero-sumfree counterexample was found.

**Scope.** Original30 frontier row objects/28 source objects unchanged; SRC-0008, SRC-0015, SRC-0023 SOURCE_STATED, especially unverified historical D3(C5³)=25. The canonical display uses published-source statements, not an unconditional theorem. All 26 hubs, three-hub and P26 (z,r)=(0,4),(0,6),(1,7) profiles still open. No numerical mathematical search, no formal kernel/certification, no external review.

## 6. Exact next research obligations

S066 should attempt to prove from EVERY genuine arbitrary-U22 S060 q-matching+Fano original configuration either: (i) three independent non-q order-two pair sums (thereby ruling out exact12) AND separately eliminate full8/≥13; OR (ii) a different forced real full-eight/equality12/13+ original collision using the explicit masked E(U\\I) theorem, 2-torsion toggle symmetry, and triple-XOR weighted intersection certificate; OR (iii) exhibit a fully labelled genuine S060-gate-passing total-zero nonminimal G59 with exact first non-q original zero and complement. Do not assume condition (i) is true; it could be false for genuine maximal H atoms. Genuine proof failure must be recorded plainly; preserve original labels, actual full-G arithmetic, and all noncanonical parity profiles.
