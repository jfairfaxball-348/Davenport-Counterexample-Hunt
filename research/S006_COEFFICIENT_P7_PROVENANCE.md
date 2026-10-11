# S006 — Remaining coefficient, p=7, auxiliaries and provenance (2026-10-11)

One bounded **source-only** Phase-1 pass, no mathematical numerical search, SAT/ILP, campaign, author code execution, candidate or Lean. Phase 1 **IN_PROGRESS**, Phases 2/3 **NOT_STARTED**. Source-stated results and independent symbolic checks are distinguished.

## BSP2012 Lemma2.1/2.3 printed pp.22–23

Original publisher offprint: https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf . Lemma2.1's statement yields a short zero sum of length at most R=(3p−1)/2; its proof's split of a 3p-term zero sum cannot justify the strictly smaller 3(p−1)/2, since min(t,3p−t)≤floor(3p/2)=(3p−1)/2 for odd p. The p-term alternative does not repair the 3p case. Lemma2.3's rank-three proof is omitted while its exact multiwise coefficient is the smaller 3(p−1)/2. Neither a complete repair nor counterexample to the statement has been supplied.

The independently derived CLM-0068 remains a narrower **CONDITIONAL** alternative: assuming the classical p-group/Chevalley–Warning inputs and η(Cp³)≤M=3p²−4p−3 for p≥7, let R=(3p−1)/2, D₂≤5p−2 and D_j≤5p−2+(j−2)R. With j=2p−4, D_j≤3p²−5p+1 and M−D_j≥p−4>0; short-block extraction gives D_k(Cp³)≤pk+p²−3 for k≥3p−2. Neither η7 nor the printed stronger Lemma2.3 coefficient has thereby been independently certified.

## New bounded p=7 local subcase repair, not a whole lemma proof

Published BSP2012 Lemma5.2 printed p.29 asserts 2(6,1)+(1,6)+(1,0) is a zero sum. It is instead (14,8)=(0,1) modulo 7, and the narrative excludes (1,6) in that subcase. But the same printed subcase stipulates TWO copies of (6,1), TWO of (2,4), and at least one (0,1). Therefore 2(6,1)+(2,4)+(0,1)=(14,7)=(0,0) modulo 7 is a valid FOUR-term zero sum (CLM-0075). A second valid conditional identity is 2(6,1)+2(4,6)+(1,0)=(21,14)=0 modulo 7. These symbolic checks repair ONE contradicted subcase. The earlier without-loss normalizations, other discarded candidate vectors and remaining case completeness are neither spelled out exhaustively nor independently proved. Lemma5.2 (length 15 over C7², no zero sum ≤7 implies three terms in a cyclic subgroup), its large-prime application and η(C7³)≤116 therefore stay source-stated, not PROGRAMME_PROVED.

## Prime Property B/C and BSP2007 classification

Reiher 2010 original https://www.math.uni-rostock.de/math/pub/preprints/preprint/2010/pre10_01.pdf Theorem10.2 and printed p.27 assert every prime Property B, and refer to Gao–Geroldinger Theorem10.7 for B⇒C. Internal classification lemmas and the original independent proof of Theorem10.7, as well as the BSP2012 p≥11 averaging argument on pp.29–30, were not completely independently reconstructed.

BSP2007 original https://www.mathematik.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Davenport333d.pdf Proposition1 p.3: D₂(C3³)=11, and D_k(C3³)=3k+6 for k≥3 (so D₃=15, D₄=18). Superscript D³=17 is the **at-most-three** zero-sum threshold, not a multiwise value and not exactly-three. Proposition8 pp.10–11 relies on diagrams/classifications pp.6–10 whose every case, and a k−2 versus k−3 narrative count, are not fully reconstructed. Full Sheikh2017 thesis Chapter4 and Remark4.3.11: university portal https://pure.royalholloway.ac.uk/en/publications/the-davenport-constant-of-finite-abelian-groups/ readable, full PDF https://pure.royalholloway.ac.uk/files/28262990/The_Davenport_Constant_of_Finite_Abelian_Groups.pdf returned HTTP403. Indexed example has pair (1,0,0)+(2,0,0)=0 and cannot counter the distinct at-most-three-free premise merely because it is exactly-three-free. No claim that the entire thesis is read.

## GHST2007 and Yiu2026 unverified computational sources

GHST2007 original https://www.math.univ-paris13.fr/~schmid/personal/schmid_16.pdf printed pp.16–17 Prop5.6 reports s(C5³)=37 and Property D based on a recursive computer classification; its printed historical purported full source/output is http://www.combinatorics.net.cn/homepage/hou/C53.html . This locator is seen in the original paper but actual code/output are NOT inspectable in this pass. Its source-stated theorem yields η(C5³)=33; nothing was executed, no COMPUTED_EXACT claim.

Yiu arXiv2609.04950v1 manuscript https://arxiv.org/html/2609.04950v1 describes M1 D₃(C5³)=25, with AUTHOR-REPORTED 98,622 normalized generators and 230,983 extensions reproduced independently only at the **candidate generation** stage; the final three-disjoint-zero-sums predicate is implemented once according to the author, not independently checked here. M2 s_{≤6}(C5³)=24 and M3 s_{≤7}(C5³)=19 are DISTINCT predicates with author-reported independent reimplementations. They do not constitute independent external certificates. S004 downloaded source bundles contained only five TeX/bibliography files each, no code or logs; current targeted public-location attempts did not authenticate executable M1/M2/M3 source, detailed logs or certificates. This is an access limitation, not evidence of universal absence. Nothing run.

## All 30 frontier rows and historical exact-family proof limitations

Original Schmid2011 https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i1p33/pdf/ Theorem4.1(2), printed p.27, states D(C6²⊕C6t)=D* for t≥1; n6=16. Its dependencies Thm3.13, Prop4.2/Lemma4.3 and omitted subsums are not fully reconstructed. Original van Emde Boas II https://ir.cwi.nl/pub/7240/7240D.pdf Theorem2.8 → Theorem4.2/Cor4.3 printed pp33–35 yields D(C(2p^a)³)=6p^a−2, and report III https://ir.cwi.nl/pub/7217/7217D.pdf Lemma1.2 (computational structural input), Lemma1.3 (sketch), Theorem1.4/Cor1.5 yields D(C(3·2^a)³)=9·2^a−2. These are SOURCE_STATED exact families notwithstanding incomplete original dependency proofs. Olson p-group cases remain source-stated; n=1 is trivially proved.

For EVERY n=1..30 there are unchanged 25 exact/trivial **source-stated** rows and FIVE conditional intervals:
- n15: 43..45, upper 3×13+6.
- n20: 58..59, upper 2×28+3.
- n21: 61..63, upper 3×19+6.
- n28: 82..83, upper 2×40+3.
- n30: 88..90, upper 3×28+6.
All lower bounds 3n−2. No fresh primary exact result was authenticated for these five by bounded targeted checks, **without asserting present-day openness**. Inherited 14/17 multiwise, tripling +5 and 43/699/5553 orbit counts remain quarantined.

## Outcome and named gaps

Phase-1 PASS withheld: BSP2012 p23 exact coefficient, pp29–30 all p7 omitted cases and rank-three averaging, Reiher/GG Theorem10.7 full original proof chain, BSP2007 diagram/Prop8 case exhaustion, inaccessible Sheikh thesis, GHST C53 code/output, Yiu M1 final predicate and M2/M3 certificates, full Schmid/1969 sources, and primary results for the five intervals all incompletely independently verified. No mathematical counterexample or certified negative. CAM-0001 stays PROPOSED / NOT RUNNING with activation blocked by published D(C6³)=16. No replacement target, no Phase2/3. S007 is a FUTURE UNEXECUTED prompt. STOP after S006.
