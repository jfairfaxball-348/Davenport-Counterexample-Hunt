# S009 — p=7 printed omitted-eight-vector subcase and primary-dependency audit

2026-10-11. Entry LIVE main 74130b059940a3bf4dbe4e75bb7fee40a7cdea49. ONE bounded primary-paper-only Phase-1 pass; no mathematical numerical search, exhaustive enumeration, author program execution, solver, campaign, candidate, Lean, correspondence or publication. Phase1 IN_PROGRESS, Phase2/3 NOT_STARTED. No proof-status upgrade from inspection alone.

## 1. Published BSP2012 Lemma2.1/2.3, pp.22–23: coefficient not repaired

Original publisher offprint SRC-0021: https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf (Contemporary Mathematics 579, 2012, pp.21–31). The 3p-term zero-sum splitting yields min(r,3p−r)≤floor(3p/2)=(3p−1)/2, not the subsequently printed 3(p−1)/2. The stronger Lem2.3 rank-three coefficient is not supplied by the omitted 'easier' proof, and no full independent repair is authenticated. CLM-0068 remains valid only CONDITIONAL on classical Chevalley–Warning/p-group inputs and eta(Cp³)≤M=3p²−4p−3 for p≥7: with R=(3p−1)/2, j=2p−4, one gets Dj≤5p−2+(j−2)R=3p²−5p+1<M (slack p−4), and Dk≤pk+p²−3 for k≥3p−2. This conditional theorem does not prove eta7 or the original stronger coefficient.

## 2. NEW complete conditional hand proof CLM-0079: BSP2012 Lem5.2 p29 (5,5)-twice branch

Assume EXACTLY the published contradiction context: A is a multisequence of 15 indexed terms in F7²; it has NO NONEMPTY zero-sum subsequence of length at most 7; no cyclic subgroup contains more than TWO indexed terms. Grant the conditional previous CLM-0077 normalisation of TWO different mixed cyclic subgroups: the four occupied axis elements are u=(1,0), U=(3,0), v=(0,1), V=(0,3), each once because the axes are full. Now consider ONLY the printed alternative that d=(5,5) occurs TWICE. The diagonal line is full. There are NINE other indexed terms.

Every other term w=(a,b) is neither on the full axes nor the full diagonal; hence a,b∈{1,2,3,4,5,6} and a≠b. The four axis terms generate in EACH coordinate precisely the possible subsequence sums B={0,1,3,4} (empty, 1, 3, 1+3); the x/y choices are independent. If there is k∈{0,1,2} such that BOTH coordinates a,b belong to S_k=−5k−B (mod 7), the term w, k available copies of d, and a subset of at most all four axis terms form a NONEMPTY zero sum of length at most 1+2+4=7, forbidden. Explicitly:

- S0={0,3,4,6}; S1={1,2,5,6}; S2={0,1,3,4}.
- For values 1..6, membership in these S sets is: 1:{1,2}, 2:{1}, 3:{0,2}, 4:{0,2}, 5:{1}, 6:{0,1}.
- To avoid any forbidden k, a and b must have DISJOINT membership sets. The only possible ordered pairs join {2,5} and {3,4}, giving precisely E={(2,3),(2,4),(3,2),(3,5),(4,2),(4,5),(5,3),(5,4)}. These are exactly the source's eight printed but unproved omitted candidates.

Nine remaining indexed terms draw from just these eight values. Thus at least one element of E occurs TWICE. Here are exhaustive E-indexed explicit nonempty forbidden short sums, with arithmetic displayed in Z² and each coordinate divisible by 7 (all axis terms once; d available twice):

| Repeated term w | Available zero-sum subsequence | Integer-coordinate sum | Length |
|---|---|---|---|
| (2,3) | 2w+(3,0)+(0,1) | (7,7) | 4 |
| (2,4) | 2w+2d+(0,3) | (14,21) | 5 |
| (3,2) | 2w+(1,0)+(0,3) | (7,7) | 4 |
| (3,5) | 2w+(1,0)+(0,1)+(0,3) | (7,14) | 5 |
| (4,2) | 2w+2d+(3,0) | (21,14) | 5 |
| (4,5) | 2w+2d+(3,0)+(0,1) | (21,21) | 6 |
| (5,3) | 2w+(1,0)+(3,0)+(0,1) | (14,7) | 5 |
| (5,4) | 2w+2d+(1,0)+(0,3) | (21,21) | 6 |

Every summand's availability follows from the explicit conditional hypotheses, and each length is ≤7; no all-length zero-sumfree hypothesis or program is used. This PROVES the (5,5)-multiplicity-two branch impossible, including all eight vectors. It DOES NOT prove that (5,5) is present twice, NOR the (5,5) zero/one-copy alternatives. The first still-unclosed inference for the advertised at-most-one-mixed-line statement is the published transition from this restricted alternative to ALL remaining multiplicity cases. Do not call Lemma5.2, eta7 or the entire p7 argument verified.

Prior status distinctions still apply: CLM-0075 repairs only one printed false short-sum subcase; CLM-0076 only the first x,2x replacement; CLM-0077 conditional normalization only; CLM-0078 only t=0,3,5,6 with three already-available doubled vectors. Unproved further cases include the two-copy intersection x+y∈<z>, the further forbidden triples, availability of displayed vectors, and the t=1,2,4 exclusions; the printed phrase 'zero-sum free' cannot strengthen the actual no-zero-sum-of-length-≤7 hypothesis.

## 3. Property B/C, plane averaging, BSP2007, Sheikh, computational provenance

Reiher2010 original SRC-0025 https://www.math.uni-rostock.de/math/pub/preprints/preprint/2010/pre10_01.pdf Theorem10.2 p26 cites Lemmas7.2,9.2,9.6, Cor2.5, Props5.1,6.2,8.1,10.1. Its p27 cites Theorem10.7 of reference [6], identified on p29 as Gao–Geroldinger, On Long Minimal Zero-Sum Sequences in Finite Abelian Groups, Periodica Mathematica Hungarica 38 (1999), 179–211, DOI 10.1023/A:1004854508165 (new SRC-0026, CLM-0080). The original GG1999 article is NOT the GG2006 survey. A publisher bibliographic preview was reachable but the original Theorem10.7 proof text was NOT, so the B⇒C premises and derivation remain unverified. Reiher's entire cited internal proof chain also not independently re-proved. BSP2012 p≥11 plane-counting yields m≤4 and then m≤2 only CONDITIONAL on Lem5.1 and the rank-two Property C/short-sum input; previously checked integer ceilings do not close original Property B⇒C.

BSP2007 SRC-0008/0019 https://www.mathematik.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Davenport333d.pdf original Prop1 printed p3 and Prop8 pp10–11 with diagrams pp6–10: subscript D3(C3³)=15, D4(C3³)=18, whereas superscript D³=17 means zero sum of length AT MOST THREE, not multiwise D3 and not exactly-three. The earlier 'at most k−2 triples' versus later k−3 bound is not independently reconciled with every underlying diagrammatic case, so Prop8 auxiliary proof remains partly source-inspected, not programme-proved.

The university official Sheikh2017 137-page full thesis URL https://pure.royalholloway.ac.uk/files/28262990/The_Davenport_Constant_of_Finite_Abelian_Groups.pdf remains unread: prior direct PDF HTTP403; current retrieval returned an internal fetch error, NOT evidence of another fresh HTTP403. The indexed Chapter4/Remark4.3.11 available excerpt addresses exactly-three-free; the example contains a two-term zero sum, so it does not satisfy the stricter no-AT-MOST-three hypothesis. Full Chapter4 is not inspected.

GHST2007 SRC-0024 https://www.math.univ-paris13.fr/~schmid/personal/schmid_16.pdf Prop5.6 pp16–17 points to original FULL code and detailed output http://www.combinatorics.net.cn/homepage/hou/C53.html; HTTP/HTTPS historical page retrieval failed to supply content. Neither source nor output read, no historical program run or independent exact computational claim. The source-stated eta(C5³)=33 stands as literature statement.

Yiu2026 v1 SRC-0015 https://arxiv.org/html/2609.04950v1 reports M1 D3(C5³)=25 with generation of 98,622 normalized generators/230,983 extensions repeated independently but FINAL three-disjoint-zero-sum predicate implemented just once; generation agreement does NOT independently verify final predicate. M2 s≤6(C5³)=24 and M3 s≤7(C5³)=19 check different forbidden lengths. Author-reported independent M2/M3 implementations are distinct from this programme obtaining complete logs, code and certificates. Prior S004 two arXiv source bundles had five TeX/bib files, no authenticated ancillary code/logs; focused S009 read-only source checks found none authenticated, which does not establish universal absence. No source code executed or mathematical enumeration.

## 4. All n=1..30, exact-value source level and five focused intervals

Every integer n=1..30 checked individually against lower 3n−2 and both mirrors: rows below record values, NOT new finite-group searches. Exact source-stated prime powers come via Olson/GG; n1 follows from definition. Schmid2011 SRC-0022 printed Thm4.1(2) p27 states D(C6³)=16, independently corroborated by van Emde Boas II SRC-0023 exact rank-three 2p^a family, values n6,10,14,18,22,26; original III SRC-0002 exact 3·2^a family gives n6,12,24. Original source long dependencies (Schmid's omitted subsums; II Theorem2.8; III Lemma1.2 structural/computational input and sketched Lemma1.3) not completely independently reconstructed. Source-stated exact results are not downgraded.

| n | D* | source-audited D bound | evidence class |
|---|---|---|---|
| 1 | 1 | 1 | source-stated exact/trivial |
| 2 | 4 | 4 | source-stated exact/trivial |
| 3 | 7 | 7 | source-stated exact/trivial |
| 4 | 10 | 10 | source-stated exact/trivial |
| 5 | 13 | 13 | source-stated exact/trivial |
| 6 | 16 | 16 | source-stated exact/trivial |
| 7 | 19 | 19 | source-stated exact/trivial |
| 8 | 22 | 22 | source-stated exact/trivial |
| 9 | 25 | 25 | source-stated exact/trivial |
| 10 | 28 | 28 | source-stated exact/trivial |
| 11 | 31 | 31 | source-stated exact/trivial |
| 12 | 34 | 34 | source-stated exact/trivial |
| 13 | 37 | 37 | source-stated exact/trivial |
| 14 | 40 | 40 | source-stated exact/trivial |
| 15 | 43 | 43..45 | conditional interval |
| 16 | 46 | 46 | source-stated exact/trivial |
| 17 | 49 | 49 | source-stated exact/trivial |
| 18 | 52 | 52 | source-stated exact/trivial |
| 19 | 55 | 55 | source-stated exact/trivial |
| 20 | 58 | 58..59 | conditional interval |
| 21 | 61 | 61..63 | conditional interval |
| 22 | 64 | 64 | source-stated exact/trivial |
| 23 | 67 | 67 | source-stated exact/trivial |
| 24 | 70 | 70 | source-stated exact/trivial |
| 25 | 73 | 73 | source-stated exact/trivial |
| 26 | 76 | 76 | source-stated exact/trivial |
| 27 | 79 | 79 | source-stated exact/trivial |
| 28 | 82 | 82..83 | conditional interval |
| 29 | 85 | 85 | source-stated exact/trivial |
| 30 | 88 | 88..90 | conditional interval |

Focused primary exact-result checks for n15=43..45 (3·13+6), n20=58..59 (2·28+3), n21=61..63 (3·19+6), n28=82..83 (2·40+3), n30=88..90 (3·28+6) found no independently authenticated newly exact theorem IN THIS PASS. NON-DISCOVERY is not evidence of present-day openness. Five intervals remain and 25 exact/trivial rows stand. Inherited multiwise 14/17, tripling +5, GL-orbit counts 43/699/5553 are quarantined.

## 5. Honest gate

**Phase1 IN_PROGRESS, PASS withheld**: at-most-one-mixed-line other multiplicity alternative; x+y intersection and later triples/t values, published stronger coefficient, eta7, original GG1999 B⇒C and dependent Reiher, BSP2007 diagrams, full Sheikh thesis, GHST original code/output, Yiu independently certified final tests and incomplete historical source chains. Phases2/3 NOT_STARTED. CAM-0001 PROPOSED / NOT RUNNING activation BLOCKED by published n6=16; no replacement. No mathematical numerical search, source code run, campaign, candidate, certificate or exhaustive negative. Source accessibility limits do not demote published exact frontier results. Real hosted checks absent: local ADMIN checks are NOT CI PASS.
