# S088 — complete sevenfold projected q-fibre exclusion for the canonical axial original profile

16 October 2026. **INTERNAL SAME_EXECUTOR, symbolic hand proof, not independent verification.** Entry live main 0b4825905541b212ecb3e8f4e21000f1ed25f863, true original Git root tree 8f4fb20ff7699da483b838f93c4db4984d41364d; S087 authored one-parent 34ff67cc820f203f393989386e999aaf2d78d504 and ordinary two-parent merge 0b4825905541b212ecb3e8f4e21000f1ed25f863. No mathematical numerical search, orbit enumeration, CAS/SAT/ILP, Lean, Palomar, independent reviewer, source upgrade, or candidate construction.

## 1. Exact original-index setting and the only permissible promotion

Work conditional on S060/S081–S087's actual canonical total-zero 59-index T in G=(Z/20)^3: twenty-two separately indexed complete original pairs whose sums divided by two give U*=e1^8 e2^8 e3^6 in H=(Z/10)^3, eight individually indexed original g, one actual s_q, and the SAME six original X_i,Y_i positions forming three genuine disjoint V_i=X_i+Y_i. The latter twelve disjoint real q-supervertices each have parity (0,0,1); their half-sum projections into P=F5³ total (2,2,4). The full-pair extension E(U*) in H has projected image E5={x in P:x1=1 or x2=1 or x3 in {1,2,3}}. If any **nonempty proper even set I of genuine q groups** projects OUTSIDE E5, take its actual H half-sum h(I), and choose k_l=(-h(I)_l mod10) of the distinct indexed complete U* pairs of type e_l (capacity 8,8,6 respectively). Select both ORIGINAL endpoints of each such pair and every true original position represented by I. The sum in G is exactly zero; nonempty I and at least one omitted q group make this an actual nonempty PROPER original-index zero. No all-twelve q selection, synthetic Fano values, independent X/Y choices or fictional original indices enter any witness.

S085 forces any seven equal projected q half-values to have third coordinate t=3 (and their seven true G third coordinates all equal 1 or all 11). S086/S087 eliminate every sevenfold horizontal v=(a,b) with ab=0. We now eliminate all sixteen ab≠0 by the exactly equivalent five-singleton/ten-pair NECESSARY proper-support sieve of S087 CLM-0304; no stronger or sufficient condition is assumed.

Put c=1-3a and d=1-3b in F5, so c,d≠1. Define
- C0={ (x,y):x=1 or y=1 }; C4={ (x,y):x=c or y=d };
- A=(1,d), B=(c,1), P2={A,B}, W=(2,2)-3(a,b)=A+B=(c+1,d+1).
- Five individually labelled outsider third ratios e_i and residual horizontals w_i satisfy sum e_i=1, sum w_i=W.

A singleton with e∈{0,2,3} is **strong** and has w∈P2. A weak e=1 singleton has w∈C4; weak e=4 has w∈C0. For any outsider pair with e_sum=0 it needs C0, with e_sum=2 it needs C4, and with e_sum∈{1,3,4} it needs BOTH and hence P2. Each tested singleton/pair is physically available by selecting a parity-compatible count of the seven REAL repeated q groups; the S086 proof checks properness. S087 complement duality supplies the corresponding triple/quartet tests without treating the five-outsider/full-twelve set as a proper subset.

## 2. CLM-0307: the weak-only multiset (1,1,1,4,4) never passes

Let u,v be the two e4 residuals and z1,z2,z3 the three e1 residuals. Their e4+e4 pair has e_sum=3, so u+v∈P2. Their sum plus z1+z2+z3 is W=A+B. By interchanging the two horizontal coordinates, it suffices to consider u+v=A and z1+z2+z3=B. Each u,v belongs to C0; each z_i and z_i+z_j belongs to C4; and **every** z_i+u,z_i+v belongs to C0 since 1+4=0.

If d≠2, any two C0 points summing to A=(1,d) must, up to order, be u=(1,d-1), v=(0,1). For any z=(x,y) among the three e1 outsiders, mixed pairs with v and u demand respectively (x=1 or y=0) and (x=0 or y=2-d). If x=0 then y=0. If x=1 then y=2-d, but membership z∈C4 would require c=1 or 2-d=d; the former contradicts a≠0, the latter gives d=1 and contradicts b≠0. If x is neither 0 nor 1, the mixed pairs force y=0=2-d, contradicting d≠2. Thus every z_i=0, contradicting sum z_i=B whose second coordinate is 1.

If d=2, both e4 singles have second coordinate 1, say u=(s,1) and v=(1-s,1). An e1 residual z=(x,y) with y=0 must have x=c by C4. If y≠0, its two mixed pairs require x+s=x+1-s=1, hence s=3 and x=3; membership C4 then requires x=c or y=2. If c=3, all three z_i have x=3, so their total first coordinate is 9=4, not B_1=c=3. If c≠3, the nonzero-y e1 residuals are exactly (3,2); all others are (c,0). To total B_2=1, their count n∈{0,1,2,3} must obey 2n=1 in F5, so n=3. But a pair of them sums to (1,4), outside C4 (since c≠1 and d=2). Contradiction. Interchanging coordinates proves the case u+v=B. **No zero-strong five-outsider configuration passes.**

## 3. CLM-0308: one or two strong outsiders never pass the proper cross gates

Write D=B-A when the strong point is A, or D=A-B when it is B. Both D and -D are nonzero. If a weak e1 is paired with a strong point S, then e_sum∈{1,3,4}, so w_e1∈{0,D}∩C4. If a weak e4 is paired with a strong e0 or e2, its residual belongs to {0,D}∩C0, and 0∉C0 forces it to equal D.

### Exactly one strong label

The exact e_total=1 congruence gives only three multisets: (0,4,4,4,4), (2,1,1,1,1), (3,1,4,4,4).

**(0,4^4).** All four e4 residuals equal D. Every e4+e4 pair has e_sum=3 and must obey 2D∈P2. If strong S=A, this means either B=2A (only (a,b)=(3,1)) or 2B=3A (only (a,b)=(4,4)); for S=B the symmetric possibilities are (1,3) and (4,4). At (4,4), D is (3,2) or (2,3), outside C0, so no weak e4 singleton passes. At (3,1) the possible D=A, and at (1,3) D=B; all five residuals therefore coincide and sum to 0, contradicting W=A+B≠0. No case survives.

**(2,1^4).** Let m∈{0,1,2,3,4} of the four e1 residuals equal D, the rest being zero. From S+mD=W, for S=A one obtains m(c-1)=c and m(1-d)=1. Necessarily m∈{2,3,4}, giving respectively (c,d)=(2,3),(4,4),(3,2); by symmetry S=B exchanges the coordinates. At (2,3), 0∉C4, so all four e1 would have to be D, inconsistent with m=2. At (4,4) D=(3,2)∉C4 and 0∉C4. At (3,2) D=(2,4)∉C4 and 0∉C4. Contradiction in every case.

**(3,1,4^3).** Let S∈P2 be the e3 strong residual, z the e1 residual, and r1,r2,r3 the e4 residuals. Then z∈{0,other(S)-S}. Each r_i∈C0; each e4+e4 pair has sum in P2. Up to relabelling the three e4 indices, their three pair-sums are AAA, BBB, AAB or BBA. Elementary halving in F5 gives the **complete symbolic classification**:

| pair-sum pattern | necessary parameter | sum r1+r2+r3 |
|---|---|---|
| AAA | d=2 | 4A |
| BBB | c=2 | 4B |
| AAB | (c,d)=(2,4) | A+3B |
| BBA | (c,d)=(4,2) | B+3A |

To check: AAA forces each r_i=3A, whose C0 membership needs 3d=1; similarly BBB. For AAB the individual points are A-3B,3B,3B. Membership 3B∈C0 forces c=2; then A-3B∈C0 forces d=4; the BBA case is symmetric. Now impose S+z+sum r=W=A+B. For AAA, S=A demands z=W and S=B demands z=2A. Neither lies in {0,other(S)-S}: any equality would force A+B=0, which occurs only at c=d=4, incompatible with d=2; or force A=0. BBB is symmetric. For AAB, at c=2,d=4 one has A=(1,4), B=(2,1). If S=A, the demanded z=-A-2B=(0,4), different from 0 or B-A=(1,2). If S=B, z=2B=(4,2), different from 0 or A-B=(4,3). BBA is symmetric. All exactly-one-strong cases fail.

### Exactly two strong labels

Outside the exceptional parameter pairs S087 already forces each strong-strong e pair to have e_sum∈{0,2}. For such compatible pairs, the exact five-label e_total=1 multisets are (0,0,1,1,4), (0,2,1,4,4), (2,3,1,1,4). The arguments below also exclude those specific multisets **at exceptional parameters**.

**(0,0,1,1,4).** The e4 weak label must pair in BOTH layers with both e0 strong labels. As 0∉C0, their strong points must coincide S∈P2, and the e4 residual is D=other(S)-S. Each e1 residual belongs to {0,D}. Since W=2S+D+z1+z2=W+z1+z2, we have z1+z2=0. With only values 0,D, and D nonzero in characteristic 5, this forces z1=z2=0. Their C4 singleton gate needs c=0 or d=0. The strong0+strong0 pair (e_sum=0) requires 2S∈C0: d=3 if S=A, c=3 if S=B. The e4 singleton D∈C0 requires (c=2 or d=0) if S=A, or (c=0 or d=2) if S=B. These three necessities are incompatible.

**(0,2,1,4,4).** Each of the two e4 weak labels pairs in BOTH layers with both strong labels, so both strong points must coincide S, and both e4 residuals are D=other(S)-S. The sole e1 residual z∈{0,D}. But W=2S+2D+z=2other(S)+z forces z=S-other(S)=-D, neither 0 nor D. Contradiction.

**(2,3,1,1,4).** Each e1 weak label pairs in BOTH layers with the strong e2 and e3 labels. If their strong points differ, both e1 residuals must be 0, and the e4 weak residual must be D2=other(S2)-S2 because it pairs in both layers with e2. Then the total is S2+S3+D2=2S3, inconsistent with W=S2+S3 since S2≠S3. Thus the two strong points coincide S. The e4 residual is D; both e1 values are 0 or D and must sum 0 by the same W identity as the (0,0,1,1,4) case, hence both are 0. Their C4 gate requires c=0 or d=0; the strong2+strong3 pair has e_sum=0 so requires 2S∈C0; the e4 singleton D needs C0. The same three incompatible conditions finish the proof.

## 4. CLM-0309: the three exceptional horizontal parameters also fail

S087 establishes that, for any other ab≠0 parameter, at most two strong outsiders occur. Thus sections 2–3 already exclude thirteen of the sixteen values. It remains to eliminate (4,4), (3,1) and (1,3); the last two are symmetric.

**(4,4).** Now c=d=4, B=-A, W=0, and the strong residuals are ±A. Neither 0 nor ±2A belongs to C0 or C4. Therefore no weak e1 can coexist with any strong label, and no weak e4 can coexist with a strong e0 or e2. If a strong e0 or e2 exists, all five labels are strong. Any two strong labels requiring BOTH crosses must sum into {±A}, impossible for pairs of ±A (their sums are 0,±2A). Hence every strong e pair must have e_sum 0 or2. The ONLY permitted unordered e types among {0,2,3} are (0,0),(0,2),(2,3). Five pairwise-compatible strong values are then either all0 or four0 plus one2, giving e_total 0 or2, never1. If no e0/e2 exists but a strong e3 does, all remaining labels are e3 or weak e4 (weak e1 is impossible). Their total condition forces exactly four e3 labels, but any e3+e3 pair needs BOTH crosses and cannot sum into {±A}. Finally with no strong label the weak-only lemma applies. Thus (4,4) is impossible.

**(3,1).** Here c=2,d=3, B=2A, W=3A. The two crosses intersect exactly at {A,2A}; the points 0,-A,3A,4A all lie outside BOTH C0 and C4, whereas A and 2A lie inside both. A strong point is A or2A. A strong paired with ANY weak e1 forces both the strong and weak residual to equal A: for strong 2A, both possible differences (0,-A) miss C4; for strong A, only difference A meets C4. A strong e0/e2 paired with a weak e4 likewise forces both to equal A, by C0.

If at least one weak e1 and at least one strong e0/e2 exist, all five residuals are A (the other strong labels also meet weak e1), contradicting sum W=3A, since five A sum0. If weak e1 exists and ALL strong labels are e3, write k=#e3, p=#e1≥1, q=#e4, k+p+q=5. The third-total equation 3k+p+4q=1 is equivalent to k+3p=4 mod5, whose positive possibilities are (k,p,q)=(1,1,3) or (3,2,0). For (3,2,0), all residuals are A and the proper e3 triple has residual 3A outside the compulsory C0 (its e_sum=4). For (1,1,3), the strong e3 and weak e1 both have residual A. Each e4 outsider r satisfies r+A∈C4 from the (3,4) pair (e_sum=2) and r+A∈C0 from the (1,4) pair (e_sum=0). Hence r∈{0,A}, and its e4 singleton C0 forces r=A. Total five A=0 again contradicts W=3A.

If no weak e1 but a weak e4 AND any strong e0/e2 occur, the latter and each e4 have residual A. Every other strong e3 must also be A: its pair with e0 has e_sum=3 requiring both crosses, and with e2 has e_sum=0 requiring C0, while A+2A=3A lies outside both. Thus all five residuals A, contradiction. If no weak e1, a weak e4 exists and all strong labels are e3, the e total forces exactly four e3 labels. Their pairs have e_sum=1 and require BOTH crosses; among {A,2A}, only A+A=2A lies in {A,2A}. All four strong residuals equal A, and their proper triple has sum 3A outside the required crosses. If all five labels are strong, any mixed A,2A pair sums to 3A outside both crosses, hence all strong residuals coincide. All A fails a proper triple, and all 2A fails a proper pair (sum4A lies outside both). If no strong label, section2 applies. Hence (3,1) fails; exchanging horizontal coordinates proves (1,3) fails.

## 5. CLM-0310: the genuine original-index conditional consequence

**Theorem (S088, internal).** In the actual source-conditional S060/S081 canonical axial T59 with 22 indexed U*=e1^8 e2^8 e3^6 full original pairs and twelve true disjoint q-supervertices (including the original eight g, s_q and three paired V_i from the SAME six original X_i/Y_i), if every nonempty PROPER original G-subset is nonzero, then no projected half-value of those twelve q supervertices occurs seven times. Together with S082–S084's exclusion of eight or more repeats, the maximum multiplicity in the twelve projected q half-values is **at most six**.

Proof: For seven repeats, S085 forces common third3. S086/S087 exclude every a=0 or b=0 horizontal parameter. S087 limits strong count to at most two outside the three named exceptions. Sections2–3 exclude every allowable zero/one/two-strong multiset without a numerical mathematical search; section4 excludes all three exceptions, including strong count≥3. Hence no five-outside-residual configuration passes even the *necessary* fifteen proper two-layer gates. Every obstruction is some physically available singleton/pair gate or its proper complement triple, and section1 converts it to a literal proper original G zero by full original index choices. The only excluded outsider all-five support never supplies a witness. QED.

**Rigorous scope.** This is a universal sevenfold q-fibre **NO-GO ONLY FOR THE FIXED AXIAL U*** source-conditional canonical profile, not a twelve-q impossibility for fibres≤6. It is not a proof that any arbitrary U22 or alternative 26-profile fails, not an S060 all-original Fano/2048/q-splits/signed mixed theorem, not a certified 59-original minimality obstruction in the unrestricted group, not a length58 zero-sumfree counterexample, and not D(C20³)=58 nor D(C_n³)=3n-2. S089 should attack the true sixfold e-total/cross exceptional t=2,3 cases and unrestricted horizontal projections, with the same original-index discipline. Phase1 IN_PROGRESS; CAM-0001 PROPOSED NOT_RUNNING BLOCKED; original 29 sources/30 frontier rows frozen; hosted CI ABSENT_NOT_PASS; INTERNAL SAME_EXECUTOR.
