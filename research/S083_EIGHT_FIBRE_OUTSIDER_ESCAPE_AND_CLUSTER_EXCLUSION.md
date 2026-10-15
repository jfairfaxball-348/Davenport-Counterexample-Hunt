# S083 — exact eight-fibre outsider escape calculus and exclusion of clustered residual patterns

15 October 2026. Owner invocation "Run next arson" followed by "Session" is treated as **Run next session**, exactly S083. Entry merged main **092806b528c5da36b11d666fb7719d6c989c8393**, actual root Git tree **96011577de55d5424dee9680deaa64f52216b11d**, S082 authored c474e1308d8a300d0848736601f3e2d7026bcb3b with one parent c55614a875640a75387d5999d7459273c8200bed; S082 merge 092806b528c5da36b11d666fb7719d6c989c8393 has two parents c55614a875640a75387d5999d7459273c8200bed and c474e1308d8a300d0848736601f3e2d7026bcb3b. Results are **INTERNAL SAME_EXECUTOR**, symbolic, no numerical mathematical search, CAS, SAT, ILP, code enumeration, Lean, Palomar, campaign, source promotion, external certification or publication.

## 1. The true original-index setting and extension-completion rule

Take G=(Z/20)^3, H=(Z/10)^3 and the even-subgroup isomorphism iota(h)=2h, **not** G=Q plus H. Fix the source-conditional canonical total-zero *actual 59-original-position* family: twenty-two pairs of equal nonzero quotient parity with full-pair H sums U*=e1^8 e2^8 e3^6, eight separate original g positions of parity q, and seven separate singleton original positions, one in each nonzero C2^3 parity. The three pairs (X_i,Y_i) of six non-q singleton original positions have genuine pair-group sums V_i=X_i+Y_i of parity q; along with s_q and the eight g these give twelve **disjoint genuine original q-supervertex groups** z_1,...,z_12. Pair-grouping does not identify or merge individual original indices.

The indexed U* subset sums form [0,8] x [0,8] x [0,6] in H. Put
- E=H\(-Sigma(U*))={h:h1=1 or h2=1 or h3 in {1,2,3}};
- P=C5^3; E5=pi5(E)={x:x1=1 or x2=1 or x3 in {1,2,3}};
- C={(a,b) in C5^2:a=1 or b=1};
- c5=(2,2,4)=half-projected sum of all twelve q-supervertices.

For each genuine group z_j, define its half mod-5 projection y_j=(1/2)pi5(z_j), using inverse two **only in C5**. For every proper nonempty EVEN collection I of q-supervertex labels, its real G sum is even and gives h(I)=iota^-1(sum_I z_j) in H, with pi5(h(I))=sum_I y_j. **If sum_I y_j is outside E5, there is a literal original proper G zero:** since h(I) lies outside E, some truly indexed B subset of the 22 original full pairs sums to -h(I); select *both* original members of every pair in B and *all* original member indices in each group I. This indexed original selection is nonempty and proper because a q group is omitted. The full twelve-group selection is excepted: its c5 third coordinate is 4 and it can be completed only to all 59 positions. This completion is the only passage from projected obstructions to G; E5 membership is necessary but NOT sufficient for real H gate passage.

By CLM-0288, no half-projected fibre can contain nine labels. This session handles the boundary case of **exactly eight** in one fibre and four individually labelled outsiders, without presuming anything about which labels correspond to g, s_q or V_i.

## 2. CLM-0290 — exact mod-5 parity-matched escape calculus for eight repeated groups

**Theorem (necessary, original-index).** Suppose eight y_j equal y=(y1,y2,t) and the remaining four outsider values are b_1,...,b_4 in P. If the canonical axial original T59 has NO proper q-only G zero, then:

(A) t is nonzero in C5. In fact the four pure-fibre tests for 2y,4y,6y,8y show: t=1 requires y1=4 or y2=4; t=2 requires y1=3 or y2=3; t=3 requires y1=2 or y2=2; t=4 requires y1=1 or y2=1.

(B) Define **horizontal residual outsider vectors**
  w_i=b_i-(b_{i,3}/t)y=(w_{i,1},w_{i,2},0), considered as points of C5^2.
For EVERY nonempty even outsider support J of size two or four, the horizontal residual sum w_J is in C. In particular, for all six i<j: w_i+w_j in C, and W=w_1+w_2+w_3+w_4 in C.

(C) For EVERY odd outsider support J of size one or three: **if w_J is outside C, then the sum of the actual outsider third projections must equal t**:
  w_J notin C  =>  sum_{i in J} b_{i,3}=t in C5.
In particular:
  w_i notin C => b_{i,3}=t;
  W-w_i notin C => b_{i,3}=4-4t.
The second formula uses the real total c5: sum of all four outsider third coordinates is 4-8t=4-3t. Hence no i may simultaneously have w_i outside C and W-w_i outside C, as that would force t=4-4t, i.e. 0=4 in C5.

**Proof.** For t=0, S082's pure 2/4/6 sieve already forces a proper original zero. For nonzero t, let J be outsider labels, k=|J|. An eligible repeated-group count r must satisfy 0<=r<=8 and r+k even. If k is even, counts r=0,2,4,6,8 each have a distinct residue modulo5. Exactly one such r makes r t+sum_J b_{i,3}=0. Then the full projected sum is (w_J,0), so its first two coordinates must fall in C; otherwise the completion rule gives a proper ORIGINAL G zero. The k=4,r=8 possibility would use all twelve groups, but cannot occur for this third-zero selection: the actual full c5 has third coordinate4. For k=2 any r<=8 is proper.

If k is odd, r=1,3,5,7 range over precisely the residue classes 1,3,0,2 modulo5, omitting ONLY 4. If sum_J b_{i,3} is not t, then the unique solution r=-sum_J b_{i,3}/t mod5 is not 4 and one of those four genuine odd counts exists. Its selected group number is even and at most 10, so proper. Thus if w_J lies outside C, the only escape is sum_J b_{i,3}=t. Finally total third outsider projection is 4-8t=4-3t and subtraction yields (C)'s two displayed individual consequences. All selected q groups are genuine disjoint original-labelled groups, and the projected-zero-to-real-original cancellation is the exact indexed U* rule of section1. QED.

**Important limitation.** (A)-(C) are NECESSARY projection conditions, not a sufficient S060 gate: they do not check other z3 layers, full H E, any of the 2048 real Fano outsider cuts, nor E(U\I) split gates. In particular they do not claim that w_i satisfying them define a real survivor.

## 3. CLM-0291 — ANY three outsiders in one affine y-line are impossible

**Theorem.** In any such eightfold y-fibre hypothetical q-only survivor, the four residual w_i have NO value repeated three or more times. Equivalently, among the four projected outsiders, no three are on the **same affine line parallel to y** in P (their third-normalised horizontal residuals cannot coincide). This excludes all multiplicity patterns 4 and 3+1 independently of full H torsion, original q label roles and Fano values.

**Proof.** Suppose w_1=w_2=w_3=w and w_4=v. From the outsider pair J={1,2}, 2w is in C, while J={1,4} and J={1,2,3,4} force w+v and 3w+v to be in C. We use the odd singleton/triple escape implication (C).

If w itself lies in C, the simultaneous membership w and 2w in C forces w=(1,3) or (3,1): a coordinate of w must be1, and (possibly its other) coordinate must be3, which cannot be the same coordinate. Swap horizontal coordinates to set w=(1,3). Then 3w=(3,4) lies OUTSIDE C. The genuine outsider triple J={1,2,3} is bad, so b_{1,3}+b_{2,3}+b_{3,3}=t. Also w+v in C means v1=0 or v2=3, and 3w+v in C means v1=3 or v2=2. Both hold only for v=(0,2) or v=(3,3). In either case v is OUTSIDE C, so the genuine fourth singleton outsider requires b_{4,3}=t. But the true full third-coordinate identity says b_{4,3}=(4-3t)-t=4-4t. Thus 5t=4 in C5, absurd.

Otherwise w is outside C. Each of its three genuine singleton outsider supports is bad, forcing b_{1,3}=b_{2,3}=b_{3,3}=t. If 3w were also outside C, the three-outsider triple would demand 3t=t, impossible for nonzero t. So 3w lies in C. Because 2w lies in C, one horizontal coordinate of w equals 3 and the other equals 2. Swap coordinates to w=(3,2). From w+v in C: v1=3 or v2=4. From 3w+v=(4+v1,1+v2) in C: v1=2 or v2=0. The only solutions are v=(3,0) or (2,4), both OUTSIDE C, hence b_{4,3}=t. Yet the triple J={1,2,4} has residual 2w+v, equal to (4,4) or (3,3), outside C. Its genuine third outsider projection is b_{1,3}+b_{2,3}+b_{4,3}=3t, not t. This violates (C). Therefore three equal residuals are impossible. Every forbidden (C) case already constructs a proper literal original G zero as in section2. QED.

## 4. CLM-0292 — a two-plus-two residual outsider partition is also impossible

**Theorem.** With eight repeated y groups, the other four cannot have residual pattern w_1=w_2=u and w_3=w_4=v with u!=v. Thus a hypothetical eight-fibre original q-only configuration must have outsider residual multiplicity pattern **2+1+1 or 1+1+1+1**. It need not have four distinct original mod-20 group values; this is a statement strictly about quotient P/<y>.

**Proof.** The six outsider pair tests imply 2u,2v,u+v lie in C. The four-outsider test requires 2(u+v) in C. A vector h and its double 2h both in C must be h=(1,3) or (3,1). Swap horizontal coordinates to assume u+v=(1,3).

Since 2u in C, one of u's coordinates equals3, and similarly for v. If u1=3, then v1=1-u1=3. If neither has first coordinate3, both must have second coordinate3, giving (u+v)2=1 rather than3, contradiction. Thus write u=(3,a) and v=(3,3-a), some a in C5.

Their true residual triples are
  2u+v=(4,a+3), in C exactly when a=3;
  u+2v=(4,1-a), in C exactly when a=0.
Moreover u itself is in C exactly when a=1 and v is in C exactly when a=2.

For a=0,3,4, **both** u and v are outside C, so all four genuine outsider third-coordinate values are forced to equal t. At least one of 2u+v, u+2v is then outside C (indeed both for a=4), but every corresponding three-outsider support has third sum 3t!=t, contradicting (C).

For a=1, v is outside C but u is inside; and BOTH kinds of triple residual are outside C. Let third coordinates of the two u outsiders be d1,d2 and of the two v outsiders e1=e2=t. The triples {one u, both v} require d1=d2=-t. The triples {both u, one v} would then have third coordinate -t-t+t=-t, not t, contradicting (C) because t!=0 in C5. For a=2, exchange the roles of u and v. These are all five C5 values of a, a complete small symbolic case split, not a computer search. All contradictions force a true projected forbidden even q selection and hence a **proper actual original** G20 zero using selected indexed full U* pair members. QED.

## 5. Hostile original-index checks and honest frontier

The proof NEVER treats four Fano triples as disjoint (they share the same six original singleton labels); in fact it uses only even q-supervertex groups, so no extra fictitious Fano constraint is needed. The third-coordinate normalisation divides only by nonzero t in C5. The count r of repeated original groups is always physically available and parity-matched. For four-outsider J and r=8 the all-twelve exception is ruled out by the actual total c5 third coordinate4, not hand-waved away. Original U* contains real labelled full pairs so every point outside E5 produces a proper real G original zero. None of the three claims uses hidden rank-three Davenport conclusions or independent checking.

**Result and boundary.** In axial U* any q-only-compatible twelve projected groups have max fibre<=8 (S082). If a fibre has eight groups, quotient-normalise the four outsiders along its nonzero third direction: the four horizontal w_i MUST have either four distinct residual values or exactly one doubled residual and two singletons. We have removed ALL 4,3+1,2+2 outsider coset arrangements for arbitrary original lifts and all original q roles. This is a strict additional necessary obstruction, but does **not** show no 2+1+1 or four-distinct configuration exists. No complete 59-index q-only S060-gated model exists in our evidence, and there is no proof of its impossibility; all max-fibre<=7 spectra also remain.

Further unresolved obligations: full P=C5^3 twelve-index proper even-subset classification with sum c5; true H torsion E rather than E5; 2048 indexed outsider/Fano cuts and SAME-six-original 4-line C/Delta; every q split I/alpha with E(U\I), all 26 q hubs; non-q original split signed w_i/tau_eps, FULL8/exact12/13/14/>=15, original overlap carry and three-hub/P26 alternatives. Arbitrary zero-free U22, a G58 zero-sumfree sequence and D(C20^3)=58 remain **UNPROVED**. The 29 source objects and 30 original frontier rows were not changed; Phase1 IN_PROGRESS, CAM-0001 BLOCKED, CI ABSENT_NOT_PASS.
