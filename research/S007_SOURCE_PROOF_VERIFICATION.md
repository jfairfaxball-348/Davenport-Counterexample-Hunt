# S007 — Remaining primary source-proof gate and first p7 normalization

Date 2026-10-11. One bounded **source-only** Phase-1 verification, entry main `f1a52c99abd03e66f612a4aa16b2bfb48ec77795`. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED. No numerical/computational search, author source code, SAT/ILP, orbit enumeration, campaign, candidate, Lean, manuscript, contact or publication. PROOF_INSPECTED means selected text read, not every dependency independently proved.

## 1. Publisher BSP2012 stronger coefficient remains unproved

Original published offprint SRC-0021 https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf printed Lemma2.1/2.3 pp.22–23. A zero-sum 3p block partitioned into two zero-sum blocks only guarantees the shorter length ≤floor(3p/2)=(3p−1)/2 for odd p; the printed stronger 3(p−1)/2 does not follow. Lemma2.3 reuses the stronger coefficient without its rank-three proof. No independent complete published correction located; this is a gap in printed inference, not a counterexample to its statement. CLM-0068 remains distinctly CONDITIONAL: assuming classical p-group/Chevalley–Warning inputs and eta(Cp³)≤M=3p²−4p−3 for p≥7, R=(3p−1)/2 and D₂≤5p−2 imply D_j≤5p−2+(j−2)R; at j=2p−4 this is ≤3p²−5p+1, which is M−(p−4)<M. Extraction then gives D_k≤pk+p²−3 for k≥3p−2. This does not prove eta7 or exact smaller source coefficient unconditionally.

## 2. New independent restricted proof — CLM-0076

Printed BSP2012 Lemma5.2 p.29 hypothesizes a 15-term A⊂C₇² with no zero sum of length ≤7 and at most two terms in any cyclic subgroup. Suppose A contains both x and 2x. They occupy all two subgroup slots, one copy each. Replace 2x by x, making A'. Subgroup occupancy and length are unchanged.

If A' contained a zero-sum subsequence T of length ≤7: with zero x copies in T, the original positions are unchanged; with exactly one copy, use the original x position instead of the changed 2x position; with both copies, replace their 2x total by the ONE original 2x term, reducing the subsequence length by one. In all cases the other terms remain available and the original A has a zero sum of length ≤7, contradiction. Hence A' preserves the hypothesis. Since 2x disappears from the support and x was already present, the support shrinks. Repeat until no x,2x pair exists. This JUSTIFIES ONLY the first printed 'without loss' normalization, not later subgroup reductions or full case enumeration.

Printed alleged contradiction 2(6,1)+(1,6)+(1,0)=(14,8)=(0,1) modulo7 is NONZERO (CLM-0073). S006 conditional subcase identity 2(6,1)+(2,4)+(0,1)=(14,7)=0 modulo7 uses available multiplicities and repairs ONE subcase (CLM-0075). The printed text also casually calls A 'zero-sum free', stronger than its actual short-zero-sum-free assumption. Remain unproved: later 'at most one subgroup containing two different terms' reduction, all later coordinate normalizations, omitted vector configurations and multiplicity availability, final case-exhaustion conclusion. Thus Lemma5.2 and eta(C₇³)≤116 are SOURCE_STATED, not programme-proved.

## 3. Property B/C and BSP2007 classifications

Reiher original SRC-0025 https://www.math.uni-rostock.de/math/pub/preprints/preprint/2010/pre10_01.pdf Theorem10.2 invokes Lemma7.2, Lemma9.2, Cor2.5, Prop5.1/6.2/8.1/10.1 and Lemma9.6; printed p27 invokes Gao–Geroldinger Theorem10.7 for Property B⇒C. Dependency located, NOT full independent proof reconstruction or BSP p≥11 plane averaging on pp29–30. BSP2007 SRC-0008/0019 https://www.mathematik.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Davenport333d.pdf Prop1 p3 states subscript D₃(C₃³)=15 and D₄=18; superscript D³=17 is zero sum of length AT MOST three. Prop8 pp10–11 uses pp6–10 diagrams/cases; an earlier k−2 sentence conflicts with the later k−3 construction count. No exhaustive diagrammatic reproof or ambiguity repair established.

Official Sheikh2017 137p dissertation full-PDF URL discovered: https://pure.royalholloway.ac.uk/files/28262990/The_Davenport_Constant_of_Finite_Abelian_Groups.pdf (SRC-0013/0020). University index identifies Chapter4/Remark4.3.11; direct full PDF returned HTTP403, so Chapter4 was NOT read in full. Indexed exactly-three-free remark's example has a two-term zero sum and does not meet the different NO at-most-three premise. No source-status upgrade.

## 4. GHST/Yiu provenance (read-only only)

Original GHST2007 SRC-0024 https://www.math.univ-paris13.fr/~schmid/personal/schmid_16.pdf Prop5.6 pp16–17's computational C₅³ base refers to historical http://www.combinatorics.net.cn/homepage/hou/C53.html for complete code/output; actual bytes not retrievable/inspected. Eta(C₅³)=33 remains SOURCE_STATED; no COMPUTED_EXACT.

Yiu v1 https://arxiv.org/html/2609.04950v1 SRC-0015: M1 D₃(C₅³)=25 uses author-reported repeated GENERATION of 98,622 generators and 230,983 extensions, but its FINAL three-disjoint-zero-sums predicate is singly implemented, so the generation repeats do NOT independently certify it. M2 s_≤6(C₅³)=24 and M3 s_≤7(C₅³)=19 are distinct predicates with author-reported independent reimplementations, not externally authenticated here. S004 source bundles comprised only five TeX/bib members; S007 retrieved no authenticated ancillary code/log/certificates. Absence from inspected records is not global proof of nonexistence; no source program run.

## 5. All n1..30 and original proof hierarchy

n1 trivial; prime-powers source-stated Olson D=3n−2. Schmid2011 SRC-0022 Theorem4.1(2), p27, source-states D(C6³)=16, with longer structural lemmas/omitted subsums not independently closed. Original 1969 report II SRC-0023 Theorem2.8→Theorem4.2/Cor4.3 source-states D(C(2p^a)³)=6p^a−2: n6,10,14,18,22,26. Report III SRC-0002 Lemma1.2 (computational structural dependency), sketched Lemma1.3, Theorem1.4/Cor1.5 family VIII states D(C(3·2^a)³)=9·2^a−2: n6,12,24. Source-stated exact values are NOT downgraded due to incomplete long independent proof reconstruction.

Every n1..30 lower 3n−2 checked, with 25 source exact/trivial and 5 still conditional intervals: n15=43..45 (3×13+6), n20=58..59 (2×28+3), n21=61..63 (3×19+6), n28=82..83 (2×40+3), n30=88..90 (3×28+6). Targeted primary-source checks for each found no newly AUTHENTICATED exact theorem IN THIS BOUNDED PASS; this does NOT assert these are currently open. Historical inherited 14/17 multiwise, tripling +5 and 43/699/5553 orbit claims remain quarantined. No numeric endpoint changes.

## 6. Gate / stop

Phase-1 **IN_PROGRESS**. Exact coefficient and complete eta7 remain unresolved, as do Reiher/GG full dependency, BSP2007 diagrams, Sheikh Chapter4 HTTP403, GHST original code, Yiu M1 final predicate and M2/M3 ancillary verification, and historic long proofs. Phases2/3 **NOT_STARTED**, CAM-0001 PROPOSED / NOT RUNNING, activation BLOCKED by published n6=16; no replacement target. No counterexample or exhaustive negative. Stop after this one bounded source pass and administrative S007 closeout; S008 FUTURE UNEXECUTED.
