# S005 — Remaining primary proofs and corrected n≤30 frontier

Date 2026-10-11. **Phase 1: IN_PROGRESS. Phases 2 and 3: NOT_STARTED.** One source-only S005 session, no mathematics computation/search, campaign, candidate, SAT, orbit enumeration, author program execution, Lean, manuscript or outreach. Proof-read scope is not source-independent certification.

## 1. Definitive BSP2012 coefficient: unproved strengthening

The actual publisher offprint, Contemporary Mathematics 579 (2012) printed pp.22–23, gives Lemma2.1's statement short zero-sum length R=(3p−1)/2 at 6p−3 terms in C_p³. Its written 3p-block split on printed p.23 instead says 3(p−1)/2. For odd p, a split of any 3p-block into two nonempty zero-sum blocks gives min(size,3p−size)≤floor(3p/2)=(3p−1)/2; the strictly smaller 3(p−1)/2 does **not** follow. The p-term alternative is short enough but does not repair the 3p alternative. Lemma2.3 p.23 asserts the coefficient 3(p−1)/2 in D_k ≤ max(5p−2, 3(p−1)k/2+2p+5) and explicitly omits the rank-three proof; its higher-rank induction repeats the unshown shorter step. No counterexample to the lemma or definitive refutation is claimed. The exact imported stronger axiom remains unverified.

Independently checked S004 weaker *conditional* route: use R=(3p−1)/2, D₂≤5p−2 and D_j≤5p−2+(j−2)R for j≥2; at j=2p−4, D_j≤3p²−5p+1. For M=3p²−4p−3, M−D_j ≥p−4>0 at p≥7. Conditional on η(C_p³)≤M and the underlying classical/Chevalley–Warning facts, the extraction lemma yields D_k≤M+p[k−(2p−4)]=pk+p²−3 for k≥3p−2. The threshold j≤k is satisfied. This **does not** prove the exact stronger Lemma2.3 statement and is not an unconditional repair of η's source proof. CW alternating signs vs printed plus signs must be tracked when checking full proof; S004's specialized congruences remain conditional on the absence of forbidden block lengths.

## 2. Published Lemma5.2 p=7: concrete arithmetic failure

At printed p.29 of the original offprint, Lemma5.2 assumes a length-15 sequence over C_7² with **no zero sum of length at most 7**, and concludes some cyclic subgroup contains three terms. The narrative briefly calls an assumed counterexample 'zero-sum free', a stronger hypothesis not provided. Several reductions are asserted 'without loss' or 'easily ruled out' with neither a complete case list nor proof.

A direct arithmetic check of a displayed alleged zero sum gives
  2·(6,1)+(1,6)+(1,0)=(14,8)≡(0,1) in C_7²,
so it is NOT a zero sum. This is CLM-0073, a check of a printed local inference, not a disproof of the stated lemma. Another printed alleged zero sum (5,4)+(6,1)+(3,1)+(0,1)=(14,7)≡(0,0) is arithmetically valid **if those terms are available**; the preceding (1,6)/(6,1) subcase and multiplicity assumptions are insufficiently transparent to independently establish availability. The proof's exhaustive p7 case claim remains open to audit. The last paragraph printed p.30 reduces rank three's p7 η bound to this lemma, so imported η(C_7³)≤116 is still SOURCE_STATED, not independently proved here.

## 3. Original rank-two Property B/C for p≥11

The primary Christian Reiher 2010 proof 'A proof of the theorem according to which every prime number possesses property B' (SRC-0025) title/abstract and printed p.27 were inspected. It proves prime Property B and explicitly states that its implication to Property C comes via Gao–Geroldinger Theorem10.7; thus every prime has Property C. Published BSP2012 printed p.29 invokes this chain for Lemma5.1. This settles *identification and original-statement provenance*, not a reconstruction of each Reiher/Gao–Geroldinger argument, nor every step of the plane-averaging proof at p.30. The p7 proof and large-prime η are not thereby independently closed.

## 4. BSP2007 Proposition1/8, Sheikh and scope differences

The original 2007 BSP paper Proposition1 printed p.3 asserts D₂(C_3³)=11 and D_k(C_3³)=3k+6 for k≥3, so D₃=15 and D₄=18. Distinct superscript D³=17 refers to the length threshold for a zero sum of length **at most** 3. Proposition8 printed pp.10–11 uses earlier diagrammatic classifications and treats repeated-triple removals and a 17-to-14-term argument. Its lower construction partitions k−3 extra triples, while one sentence instead says 'at most k−2' short zeros; the subsequent count uses k−3. That latter estimate is not repaired by a full case-by-case verification here. The p.9–10 diagrams and all auxiliary classification cases remain not independently reconstructed; the published multiwise formula is SOURCE_STATED.

The Royal Holloway 2017 Sheikh doctoral-thesis portal is readable but full 137-page Chapter4 PDF remains HTTP403. An accessible 2016 Sheikh seminar/slides file is not the doctoral thesis. The university-indexed Remark4.3.11, printed p.41, concerns a **no exactly-three-term** assertion; the example contains a two-term zero sum, hence does not satisfy the different **no at-most-three-term** premise of the earlier BSP proposition. This scoped distinction stands, not a claim of full Chapter4 inspection.

## 5. GHST2007 computational base: paper and original pointer

Original GHST2007 *On Short Zero-Sum Subsequences II*, Prop5.6 printed pp.16–17, reports s(C_5³)=37 and Property D via a recursive program. The printed algorithm description restricts a candidate to a fixed 16-term fourfold affine-basis seed and at least one other multiplicity-four term, and uses 25a+5b+c as encoding. The actual original **advertised complete code and detailed output location** is http://www.combinatorics.net.cn/homepage/hou/C53.html (printed p.17). This is a verified *printed pointer*, not verified present accessibility or source provenance: page content/code/logs were NOT retrieved and nothing was executed. Thus η(C_5³)=33 via GHST Theorem1.7 retains SOURCE_STATED, not COMPUTED_EXACT.

## 6. Yiu2609.04950 code/logs/certificates

S004 directly read the 13-page author manuscript and two source bundles; both bundles had only README, bibliography and TeX source, with no advertised computational source/log/certificate. S005 scoped public-location searches found no inspectable official M1/M2/M3 implementation, logs or independently checkable certificates. In particular repeated candidate generation does not independently repeat M1's final predicate; the author's scope distinction between M1 and repeated M2 remains binding. The unresolved artifact locator is not evidence of global nonexistence, and the numerical author claims remain SOURCE_STATED. No code, solver or paper source archive program ran.

## 7. Historical exact proof hierarchy and all 30 frontier rows

Schmid2011 Theorem4.1(2) printed p.27 states D(C_6²⊕C_{6t})=D* for all t≥1: with t=1 this is D(C_6³)=16. Its Theorem3.13, Proposition4.2 and Lemma4.3 dependencies include omitted long subsum cases, so it is an exact PUBLISHED theorem but not a complete programme reconstruction. Original van Emde Boas report II Theorem2.8 supplies the p-group ν input for Theorem4.2 / Corollary4.3 printed pp.33–35, yielding D(C_{2p^a}³)=6p^a−2. Original report III Lemma1.2 (finite/computational structural input), Lemma1.3 (sketch), Theorem1.4 (proof printed pp.12–13) and Corollary1.5 family VIII yield D(C_{3·2^a}³)=9·2^a−2. The entire historical proof dependencies were NOT reconstructed; their **source-stated exactness remains**, without demotion. Distinguish historical λ=D−1 from D.

Recheck of EVERY n≤30 row from lower 3n−2, p-group exact theorem, and these original exact families preserves 25 exact/trivial source rows and five conditional intervals:

| n | 15 | 20 | 21 | 28 | 30 |
|---|---|---|---|---|---|
| Lower | 43 | 58 | 61 | 82 | 88 |
| Upper | 45 | 59 | 63 | 83 | 90 |
| Reason | 3·13+6 | 2·28+3 | 3·19+6 | 2·40+3 | 3·28+6 |

The remaining 25 rows are n=1 trivial, prime powers n=2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29, and original-family n=6,10,12,14,18,22,24,26. Targeted current-source searches for exact values at n=15,20,21,28,30 yielded no newly authenticated primary exact result in THIS bounded pass. This is NOT an assertion of present-day openness; it cannot downgrade any published exact theorem. The JSON/Markdown tables remain numerically identical to S004. Neither Yiu nor Grinsztajn conditional inputs are needed for these endpoints.

## 8. Gate, exclusions and remaining exact tasks

**Phase-1 IN_PROGRESS, PASS withheld.** Remaining pages and blockers: BSP2012 Lemma2.3 printed p.23 missing exact short coefficient proof; BSP2012 Lemma5.2 printed pp.29–30 p7 invalid displayed zero sum, unjustified availability and omitted cases; Reiher Property B/Gao–Geroldinger Property C full original proof chain and BSP p≥11 averaging not independently closed; BSP2007 Lemmas1/2/diagrammatic p.6–10 and Proposition8 p.10–11 classification incomplete; full Sheikh 2017 Chapter4/Remark4.3.11 inaccessible; GHST2007 Prop5.6 original C53 source/output not inspected; Yiu M1/M2/M3 artifacts not located; original Olson/1969 historical chains only partly reconstructed; no verified current exact values for five intervals. Gaps are not mathematical counterexamples.

The inherited subscript 14/17, tripling +5 and 43/699/5553 orbit counts remain quarantined as inherited/unverified. CAM-0001 remains PROPOSED / NOT RUNNING and **activation BLOCKED by published n6 equality**. No replacement target/campaign selected; Phase 2/3 NOT_STARTED, no certified candidate or numerical negative result. No external/owner-action blocker prevents administrative S005 closeout; S006 is a future unexecuted prompt only.
