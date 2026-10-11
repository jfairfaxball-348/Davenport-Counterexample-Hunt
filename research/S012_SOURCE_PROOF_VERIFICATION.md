# S012 — complete p=7 Lemma 5.2 hand proof and original dependency audit

2026-10-11. Entry main `eb47980a78c1298e557202b4b63fe45459bdb87b`. ONE preregistered Phase-1 primary-source-only pass. No mathematical numerical/computational search, SAT/ILP, orbit enumeration, candidate generation, author code, Lean, campaign, manuscript, contact, outreach or publication. The tables below are hand-derived symbolic case proofs, not program outputs. Source statements and conditional deductions retain their assumptions.

## 1. Common hypotheses and counting

Read the definitive publisher offprint SRC-0021, BSP2012 Lemma5.2 printed pp29–30. Assume for contradiction that A has 15 indexed terms in F7², no NONEMPTY zero-sum subsequence of length AT MOST SEVEN, and at most two terms on each cyclic line. Zero cannot occur. There are eight lines. If a are occupied twice and b once, then 2a+b=15 and a+b<=8, giving a=7,b=1. Every line is occupied.

CLM-0076 replaces x,2x by x,x preserving these hypotheses and decreasing support until no such pair remains. The complete S010 hand proof CLM-0081 then gives at most one mixed line. Hence at least SIX distinct lines contain two copies of a single vector. CLM-0083, independently rechecked in S011, supplies distinct such doubled x,y,z with x+y in <z>. Distinct occupied lines ensure x,y are independent; their sum cannot lie on either input line. The invertible linear map sending x,y to u=(1,0),v=(0,1) sends z to d=(t,t), t nonzero. It preserves positions, multiplicities, cyclic capacity, x,2x absence and all sums/lengths. No affine translation or independent rescaling of a third vector is used.

The remaining task is to exclude t=1,2,4. CLM-0078 already gives available short sums for t=3,5,6 (and zero for t=0). All previous CLM-0075–0079,0081,0083 retain their original narrow scopes; the complete result below is a NEW composed claim.

For doubled anchors u,v,d, any extra term w=(a,b) with a,b nonzero admits a forbidden sum w+kd+Au+Bv whenever a,b belong to S_k=-kt-{0,1,2}, k=0,1,2. Choose A,B in {0,1,2} with a+kt+A=b+kt+B=0 mod7. The length is 1+k+A+B<=7, with every anchor position available. A term on a full anchor line is already excluded by capacity. When excluding a doubled w, all tables use exactly TWO copies of w; transposing coordinates gives the corresponding transposed witness because u,v are equally available and d is fixed.

## 2. CLM-0084: t=2, exhaustive alternatives and actual availability

Here d=(2,2). The forbidden coordinate sets are S0={0,5,6}, S1={3,4,5}, S2={1,2,3}. Membership signatures of residues 1,2,3,4,5,6 are respectively {2},{2},{1,2},{1},{0,1},{0}. An extra term's coordinate signatures must be disjoint. The unordered coordinate pairs left are exactly

{1,4},{1,5},{1,6},{2,4},{2,5},{2,6},{3,6},{4,6}.

These are obtained directly by comparing the six displayed signatures; equal coordinates share a signature. Thus the list and its transposes include every possible extra term. Five pairs cannot occur doubled:

| Doubled w | Available forbidden sum | Integer sum | Length |
|---|---|---|---:|
| (1,4) | 2w+2d+u+2v | (7,14) | 7 |
| (1,5) | 2w+2d+u | (7,14) | 5 |
| (2,5) | 2w+d+u+2v | (7,14) | 6 |
| (2,6) | 2w+d+u | (7,14) | 4 |
| (3,6) | 2w+u+2v | (7,14) | 5 |

Consequently the ONLY further doubled alternatives are E={(1,6),(6,1),(2,4),(4,2),(4,6),(6,4)}, exactly the printed list. The three transposed pairs are mutually exclusive EVEN as singleton values:

(1,6)+(6,1)=(7,7), length2;
(2,4)+(4,2)+u+v=(7,7), length4;
(4,6)+(6,4)+2d=(14,14), length4.

At least six pure doubled lines exist; the three anchors account for three, so at least THREE further doubled values occur. They must therefore select exactly one from each of these three pairs. Interchange coordinates if needed to make a=(6,1) the doubled member of the first pair. Then (6,4) cannot occur, since a+(6,4)+d=(14,7), length3. Nor can (4,2), since a+(4,2)+2d=(14,7), length4. Hence (2,4) and (4,6) ACTUALLY occur twice, as forced by the count, not by the printed assertion alone. The available sum

2a+(2,4)+v=(14,7), length4,

is forbidden. This closes the entire t=2 doubled-anchor case. Printed 2(6,1)+(1,6)+u=(14,8) remains NONZERO and uses an excluded term; it is not rehabilitated. CLM-0075 remains conditional in its own statement, while this new proof establishes its required availability in the present case.

## 3. CLM-0085: t=1 and the omitted 8-x argument

Here d=(1,1). S0={0,5,6}, S1={4,5,6}, S2={3,4,5}. Among pairs with neither coordinate 1, the single-term test leaves only (2,b),(b,2), b=3,4,5,6, and (3,6),(6,3). Coordinates on full axes or diagonal are excluded. The doubled points (2,4),(4,2) are excluded by the already proved t=2 case in the basis (v,d), respectively (u,d): they equal 2(v+d), respectively 2(u+d). These bases are independent and their anchors really occur twice. The remaining possibilities have the following doubled witnesses, and their transposes:

| Doubled w | Available forbidden sum | Integer sum | Length |
|---|---|---|---:|
| (2,3) | 2w+d+2u | (7,7) | 5 |
| (2,5) | 2w+2d+u+2v | (7,14) | 7 |
| (2,6) | 2w+d+2u+v | (7,14) | 6 |
| (3,6) | 2w+d+v | (7,14) | 4 |

Thus every further doubled value has at least one coordinate equal to 1. At least three further doubled values exist. Assign each to a coordinate equal to 1; by pigeonhole and coordinate interchange at least TWO have the form (1,r),(1,s), distinct from u and d. Let B={0,1,r,s}; these four distinct second coordinates each have TWO available positions with first coordinate 1.

We now justify the printed 8-x bound without importing a sumset theorem. Let E_B be sums of TWO DISTINCT members of B. Among six unordered pairs, an equal pair sum must use disjoint inputs. There are only three complementary-pair equalities; any two would force repeated members of B after subtraction in odd characteristic. Hence at most one equality occurs and |E_B|>=5. For any two subsets of F7 with total cardinality >7, their sumset is F7: for a requested sum c the first subset intersects c minus the second. Consequently B+B=F7, B+E_B=F7, and E_B+E_B=F7. Partition the eight available positions into two copies of B. These identities supply EVERY second-coordinate residue using respectively 2,3,4 distinct positions. Taking complements in the eight positions supplies every residue using 5 positions as well.

If any other term w=(x,y) has 2<=x<=5, select 7-x positions from these eight whose second coordinates sum to -y. Together with w their sum is zero, and their length is 8-x in {3,4,5,6}. They are disjoint from w because its first coordinate differs from 1. Thus all terms except the two v positions have first coordinate 1 or6; first coordinate0 is on the already full v-axis.

Let P,Q be the sets of second coordinates of support points with first coordinate1,6. Capacity two gives support size>=8, so |P|+|Q|>=7 (v is the one remaining support value). If Q is nonempty, absence of a zero-sum pair or a zero-sum triple using v says Q is disjoint from (-P) union (-1-P). A nonempty proper subset P of the cyclic group F7 satisfies |P union (P+1)|>=|P|+1: equality with |P| would make it translation-invariant, hence all of F7. P cannot be all of F7 if Q is nonempty. Thus |P|+|Q|<=6, contradiction. If Q is empty, |P|>=7, so all seven (1,j), j=0,...,6, are available; taking each once gives (7,21)=0, length7. This also contradicts the hypothesis. No asserted extra multiplicity or all-length zero-sumfreeness was used. The complete t=1 case is closed.

## 4. CLM-0086: t=4 and every final antidiagonal term

Here d=(4,4). S0={0,5,6}, S1={1,2,3}, S2={4,5,6}. Single-term avoidance forces one coordinate in {1,2,3} and the other in {4,5,6}. For a doubled value outside H=<(1,-1)>, the following cases and transposes are eliminated:

| Doubled w | Available forbidden sum | Integer sum | Length |
|---|---|---|---:|
| (1,4) | 2w+d+u+2v | (7,14) | 6 |
| (1,5) | 2w+d+u | (7,14) | 4 |
| (2,6) | 2w+2d+2u+v | (14,21) | 7 |
| (3,6) | 2w+u+2v | (7,14) | 5 |

The ONLY further doubled values outside H are (2,4),(4,2),(3,5),(5,3). At least three further pure doubled lines are needed; at most one is H, so at least TWO are from this list. These points occupy just two lines: (2,4),(5,3) on slope2; (4,2),(3,5) on slope4. The transposed pairs cannot both occur, because

(2,4)+(4,2)+u+v=(7,7), length4;
(3,5)+(5,3)+d+2u+2v=(14,14), length7.

Thus exactly one point on each of these two lines is doubled; their values are either (2,4),(3,5) or (5,3),(4,2). Interchange coordinates to take c=(5,3) and b=(4,2), BOTH doubled.

Every line is occupied. The line L=<(3,1)>, of slope5, has the six possible nonzero points (1,5),(2,3),(3,1),(4,6),(5,4),(6,2). All except (1,5) are excluded even singly:

| Singleton w on L | Available forbidden sum | Integer sum | Length |
|---|---|---|---:|
| (2,3) | w+d+u | (7,7) | 3 |
| (3,1) | w+d+2v | (7,7) | 4 |
| (4,6) | w+2d+2u | (14,14) | 5 |
| (5,4) | w+2d+u+2v | (14,14) | 6 |
| (6,2) | w+2c+d+u+2v | (21,14) | 7 |

(1,5) cannot be doubled by the preceding table. Thus L is the unique singly occupied line. In particular H is occupied (indeed twice). Every possible singleton w on H gives an actually available short sum:

| w on H | Available forbidden sum | Integer sum | Length |
|---|---|---|---:|
| (1,6) | w+2b+d+u | (14,14) | 5 |
| (6,1) | w+b+d | (14,7) | 3 |
| (2,5) | w+b+u | (7,7) | 3 |
| (5,2) | w+2b+u+v | (14,7) | 5 |
| (3,4) | w+b+v | (7,7) | 3 |
| (4,3) | w+2b+2u | (14,7) | 5 |

Hence H cannot even be occupied, contradiction. This proves the entire t=4 case with all normalizations and multiplicities justified.

## 5. CLM-0087: composed complete BSP2012 Lemma5.2

Supposing a counterexample, the terminating CLM-0076 replacement produces one with no x,2x pair. CLM-0081 and the 15-term/eight-line count give six pure doubled lines. CLM-0083 gives distinct doubled x,y,z with x+y in <z>. Their valid GL2 normalization produces u,v,(t,t). CLM-0078 excludes t=0,3,5,6; sections2–4 exclude t=2,1,4. These exhaust F7. Therefore every 15-term sequence over C7² without a NONEMPTY zero sum of length AT MOST SEVEN has a cyclic subgroup containing at least THREE indexed terms. This is a complete composed hand proof of Lemma5.2, PROGRAMME_PROVED, with no numerical/computational enumeration and no strengthened all-length hypothesis.

This does NOT independently prove eta(C7³)<=116: the rank-three plane argument still needs its rank-two eta/Property C inputs. Nor does it prove the stronger BSP2012 Lemma2.3 coefficient. Historical narrower claims are not broadened retrospectively.

## 6. Original GG1999: actual pages, extraction and terminal condition

SRC-0026 original 33-page article: the requested ResearchGate PDF is recognized by the web reader but direct download gives fresh S012 HTTP403; web screenshots yield text placeholders, not usable images in this session. A lawful AUTHOR-HOSTED mirror was independently authenticated from the author's current publications list, reached via the university homepage redirect:

https://geroldinger.github.io/publications.html item[38] -> https://geroldinger-0836a9.gitlab.io/38.long-minimal-zero-sequences.pdf

This download returned HTTP200, 1,147,605 bytes, SHA256 a60f6192235fa25ac9161dbb689032de1c67d0d8684e3c703cb469f8681ee42f. Printed p185 Lemma4.3, pp202–203 Proposition10.4/Cor10.5 and pp204–208 Lemma10.6/Theorem10.7 were rendered and visually inspected; OCR was a reading aid, never a proof or source-program run. Source PDF copies remain outside the repository.

The original Lemma4.3(2) states that a length3p-2 sequence has a p- or2p-term zero sum; (3) states that a zero-sum sequence of length>=2p has a nonempty zero sum of length<=p. Printed p185 refers their proofs externally to [Ol2,Lemma1.1] and [Ga4,Lemma7], respectively. This is the FIRST remaining original prerequisite without a complete independent reconstruction in this pass; reading the original does not remove these external dependencies.

Conditional on these inputs, the printed extraction is valid: append one zero to a short-free length3p-3 S and use (2). Deleting the appended zero if used leaves a zero block of length p-1,p,2p-1 or2p. Short-freeness eliminates the first two, and (3) eliminates 2p. The remaining length2p-1 block is minimal: a proper zero block and its nonempty complement would have total2p-1, so one has length<=p-1. Property B is about maximal MINIMAL zero-sum sequences of lengthD(Cp²)=2p-1; the classical exact D input is needed, not an unproved assumption that any block of that length is automatically maximal.

For an element b with p-1 copies in S, translating every position by -b preserves absence of p- and2p-term zero sums, because these lengths are multiples of p. The translated p-1 zero positions imply that the remaining 2p-2 positions are all-length zero-sumfree: a zero block of lengthr=1,...,2p-2 could be padded with at most p-1 of those zero positions to lengthp or2p. Appending minus their total creates a minimal length2p-1 zero sum. These translation and padding steps are legitimate uses of the original no-short hypothesis plus (3); arbitrary translation does not preserve general short-freeness.

The Cor10.5(2) structure used in the proof can be verified directly for its relevant rank-two part. If a minimal length2p-1 zero sequence contains p-1 copies of nonzero e1, project its other p terms to the quotient by <e1>. Any proper quotient zero block could be lifted by 0,...,p-1 available e1 copies to a proper zero block, impossible. Thus its quotient is minimal of lengthp and all its p terms equal one nonzero quotient generator. To see the cyclic assertion without another imported theorem, remove one position from a minimal lengthp cyclic zero sequence. For a zero-free sequence of lengthp-1, the p-1 successive partial sums in ANY ordering are nonzero and distinct and exhaust the nonzero group elements. Swapping any adjacent terms changes just one partial sum; the other p-2 values stay fixed, so the changed value must equal the old value. The two adjacent terms are equal. Any pair can be made adjacent, proving all p-1 terms equal; total zero forces the last term equal too. Choose a lift e2 of the quotient generator. Then the original block has form e1^(p-1) product(a_i e1+e2), with sum a_i=1 modp. The converse minimality follows by first taking the quotient sum. This verifies the specific Cor10.5(2) input, not all Cor10.5(1),(3) or its higher-rank dependencies.

Printed p207's actual terminal assertion (**) is, for EVERY t-subset I of the p indices:

either sum_{i in I} x_i=1 modp, OR all x_i in I equal1, OR all x_i in I equalm-1,

where 3<=m<=p-1, 2<=t<=p-2, and t(m-1)=1 modp. It is NOT the universal assertion that all t-subset sums equal1: an all-1 subset has sumt, and t!=1. S011's last inference was explicitly conditional on a stronger universal premise; it cannot justify replacing the actual trichotomy by that premise.

**CLM-0088, complete actual terminal combinatorial implication.** Suppose three x values are distinct. Fix t-1 indices outside those three, possible because t-1<=p-3, and form the three t-subsets by adding one distinguished index each. Their sums are pairwise distinct. By (**), any nonconstant subset has sum1; a constant all-(m-1) subset also has sum1; a constant all-1 subset has sumt. Hence these three sums have at most two possible values, contradiction. Thus at most two distinct x values occur.

If the two values x!=x' each occur at least twice, write their counts u>=v>=2, u+v=p. For t>=3, choose u0 in[2,u-1], v0 in[1,v-1], u0+v0=t. Such integers exist because these sum intervals cover[3,p-2], which contains t. Both count patterns (u0,v0) and (u0-1,v0+1) are mixed, available t-subsets; (**) makes both sums1, yet they differ by x'-x!=0. Contradiction. For t=2, a mixed pair gives x+x'=1. Since 2x and2x' then differ from1, the available homogeneous pairs force x,x' in{1,m-1}; distinctness gives x+x'=m, contradiction to3<=m<=p-1. Thus all but at most one x_i equal the same x. With the already established constant x_i+y_i=m, at least p-1 FULL vector terms coincide. Lemma10.6 would finish the original theorem. CLM-0088 is conditional on the real (**) and constant-coordinate-sum setup, not an unconditional B=>C proof.

Lemma10.6's inspected argument uses the same no2p input, a change to basis(e1-e2,e2), the maximal cyclic zero-free assertion, a t-subset minimal length2p-1 zero block, Property B, and the relevant Cor10.5(2) projection. Availability requires positive representatives in{1,...,p}, with zero coordinates separately handled, not arbitrary integer representatives. The full internal argument and Reiher's entire Property B proof are NOT certified here. CLM-0082 remains SOURCE_STATED. Inspection of Cor10.5 and transparent selected inferences is not a declaration that all prerequisites have complete hand proofs.

Reiher2010 SRC-0025 Thm10.2 printed p26: cases from Lem9.2, with cloudiness excluding(a), Cor2.5 excluding(b), Props5.1/6.2/8.1 handling(c)–(f), and Lem9.6/Prop10.1 handling(g); support<=3 uses Lem7.2. These clauses and selected subsidiary statements are read, but their complete algebraic/geometric proof chain remains unrebuilt. Printed p27 explicitly cites ORIGINAL GG1999 Thm10.7, not the 2006 survey. Separately, BSP2012 p31 ref[10] is the DIFFERENT 2003 Gao–Geroldinger article, On zero-sum sequences in Z/nZ⊕Z/nZ; do not silently identify that bibliography entry with GG1999.

## 7. Plane averaging and exact coefficient, kept conditional

For rank3, let N=3p²-4p-3=(p+1)(3p-7)+4, and m be maximal occupied-line multiplicity. The p+1 planes through a fixed maximal line partition all positions outside it, so one plane U has at least m+ceil((N-m)/(p+1)) positions. Equivalently it has at least ceil(3p-7+m+(4-m)/(p+1)). Assume rank-two eta(Cp²)<=3p-2 and Property C at length3p-3. Every line has m<=p-1 by the cyclic partial-sum bound D(Cp)=p. If m>=5, the displayed lower bound exceeds3p-3 (already at m5 and then increases), contradicting eta. Thus m<=4. At m4 the bound is3p-3; at m3 integrality gives3p-3. Property C on a chosen3p-3 subsequence supplies a point repeatedp-1>4, contradiction for p>=7. Hence m<=2, and |A intersect U|>=3p-6 while capacity gives<=2(p+1). This is impossible for p>=11. At p7, U has>=15 terms with line capacity2, now independently excluded by CLM-0087. Consequently BOTH rank3 reductions are complete deductions CONDITIONAL on the rank-two inputs. eta(C7³)<=116 is not unconditionally upgraded while those original inputs remain insufficiently independently proved.

BSP2012 Lem2.1/2.3 printed pp22–23: splitting a zero3p block gives ONLY R=(3p-1)/2; it does not give3(p-1)/2. Lem2.3 omits its rank3 proof. CLM-0068 still assumes eta(Cp³)<=3p²-4p-3 and the recorded classical p-group/Chevalley–Warning inputs. Closing Lem5.2 does not discharge these separate obligations or prove the stronger coefficient.

## 8. Other original sources and current read-only access

BSP2007 SRC-0008/0019 Prop1 p3, Prop8 pp10–11 and diagram pages6–10 reread. The k-2 sentence does not prevent deriving the correct k-3 monochromatic-triple capacity in its lower construction: multiplicities2+3kappa_i permit floor((2+3kappa_i)/3)=kappa_i disjoint triples, totaling sum kappa_i=k-3. This is a restricted arithmetic reconciliation; the diagrams, total-subsum classification and upper induction are not fully independently proved. Subscript multiwise D3(C3³)=15,D4=18 remains distinct from superscript at-most-three threshold17.

Official Sheikh2017 full137-page Chapter4 PDF attempted ONCE freshly in S012: web open explicitly reports(403)Forbidden. This is a fresh S012 HTTP403, separately recorded from S011403,S010403,S009 internal fetch error. Full Chapter4/Remark4.3.11 not read. Exactly-three-free does not imply at-most-three-free; the indexed example's zero-sum pair prevents applying its warning to the latter premise.

GHST2007 SRC-0024 original Prop5.6 pp16–17 reread; authentic historical C53.html code AND output were sought read-only at the printed pointer. Current tool says the HTTPS-resolved location is inaccessible. Neither original bytes nor output authenticated; no source execution.

Yiu2609.04950v1 SRC-0015 §§2.3,5,8 and original abstract/source locator reread. M1 generation repetitions98,622/230,983 are not a repeat of the FINAL three-disjoint-zero-sum test; M2 s<=6=24 and M3 s<=7=19 have different predicates. Current source-bundle member list and hashes are in SOURCE_MANIFEST; no authentic computational implementation/log/certificate found among the retrieved records. Non-discovery is not global absence. No author code run.

## 9. All thirty frontier applications and honest gate

Both thirty-row mirrors retain every numerical endpoint. n1 is trivial. Prime powers n2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29 use source-stated Olson equality. Original II Cor4.3 gives source-exact n6,10,14,18,22,26; III Cor1.5 familyVIII gives n6,12,24; Schmid2011 Thm4.1(2) independently states n6=16. Their original source statements were checked afresh; full long proofs remain scoped, and published exactness is not demoted. The five conditional arithmetic intervals remain n15 43..45=3*13+6 upper, n20 58..59=2*28+3, n21 61..63=3*19+6, n28 82..83=2*40+3, n30 88..90=3*28+6. Bounded current primary-literature queries authenticate no new individual exact theorem; they do NOT prove present-day openness. All lower endpoints are3n-2. No endpoint requires the new p7 lemma.

**Phase1 IN_PROGRESS/PASS withheld.** Complete hand proof CLM-0087 closes BSP2012 Lem5.2. Remaining original rank-two inputs, GG/Reiher full dependencies, exact stronger coefficient, BSP2007 full diagrams, Sheikh access, GHST/Yiu records and historical long proofs remain. Phases2/3 NOT_STARTED. CAM-0001 PROPOSED/NOT RUNNING, activation BLOCKED by published n6=16; no replacement target/candidate/certificate. Inherited14/17,+5,43/699/5553 quarantined. No hosted CI PASS: actual workflows/runs/checks absent. Stop after S012; S013 is strictly FUTURE UNEXECUTED.
