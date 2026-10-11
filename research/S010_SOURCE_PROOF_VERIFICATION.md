# S010 — complete intermediate p=7 mixed-line hand proof; original 1999 B⇒C proof accessible

Date 2026-10-11. Entry main 4d93334fd6335397f1c3df8113b7b3e86f0bd839. One bounded Phase-1 primary-paper source-only hand-proof/provenance pass. NO numerical mathematical search, SAT/ILP, orbit enumeration, source code, candidate generation, certificate, Lean, manuscript, contact or campaigns. Phase1 IN_PROGRESS.

## 1. CLM-0081: complete HAND PROOF of the at-most-one-mixed-cyclic-subgroup intermediate assertion

Assume the *actual* BSP2012 Lemma5.2 p29 contradiction hypotheses: a multisequence A of 15 **indexed** terms in F7², no NONEMPTY zero sum of length at most 7, and at most two indexed terms in any cyclic subgroup. The CLM-0076 replacement x,2x -> x,x preserves the no-short-zero-sum and capacity conditions, so suppose henceforth no line contains simultaneously x and 2x. If there were two distinct occupied *mixed* cyclic subgroups (two different elements in each), CLM-0077's justified GL₂(F7) change of basis gives exactly one copy of each u=(1,0), U=(3,0), v=(0,1), V=(0,3), filling the two axes. Axis subset sums in either coordinate independently give B={0,1,3,4}. Zero itself is impossible, a forbidden length-one zero sum.

There are exactly eight one-dimensional subgroups in F7². The other SIX lines, including diagonal Δ=<(1,1)> and anti-diagonal H=<(1,−1)>, have capacity 2 each. If Δ were empty, at most 4+5·2=14 terms would occur, contradicting 15. Thus Δ contains one or two terms. Any diagonal element d=(t,t) can have only t∈{1,2,5}: t=0 is a singleton zero, while for t=3,4,6 the value −t lies in B; then d together with available axis subsets gives an explicitly available ≤5-term zero sum. Two distinct diagonal values in {1,2,5} are impossible: (1,1) and (2,2) form a forbidden x,2x pair after CLM-0076; (2,2)+(5,5)=(7,7) is zero of length 2; and (1,1)+(5,5)+u+v=(7,7) is zero of length 4. Consequently Δ either contains ONE d=(t,t) or TWO copies of the same d, with t∈{1,2,5}.

**Two-copy branch.** For t=2, 2(2,2)+U+V=(7,7) is a forbidden zero sum length 4. For t=5, 2(5,5)+u+U+v+V=(14,14) is forbidden length 6. For t=1, let w=(a,b) be any of the OTHER 9 indexed terms (not on full axes or diagonal). It has a,b nonzero, a≠b. If both a and b lie in S_k=−k−B modulo 7 for k∈{0,1,2}, w plus k available diagonal copies and coordinate-independent axis subsets yields a NONEMPTY zero sum of length ≤1+k+4≤7. Explicitly S0={0,3,4,6}, S1={2,3,5,6}, S2={1,2,4,5}; membership signatures of 1,2,3,4,5,6 are {2},{1,2},{0,1},{0,2},{1,2},{0,1}. Disjoint signatures force (a,b) among (1,3),(3,1),(1,6),(6,1). These four points occupy exactly THREE cyclic subgroups (slopes 3,5,−1); capacity2 per line accommodates at most 6 of the necessary NINE further indexed terms. Contradiction. This does NOT presuppose anything about multiplicity-two patterns on the other lines. Thus ALL possible two-copy diagonal branches are eliminated.

**One-copy branch.** Suppose Δ contains exactly one d=(t,t), t∈{1,2,5}. There are 15−4−1=10 other indexed terms and five other cyclic subgroups, all capacity2. Hence EVERY one of the five lines, including H=<(1,−1)>, must contain exactly TWO indexed terms. Nonzero candidates on H are (1,6),(6,1),(2,5),(5,2),(3,4),(4,3). If both coordinates of an off-axis term lie in S0=−B={0,3,4,6} or S1(t)=−t−B, that term, up to one available d, and axis subset choices give a nonempty zero sum of length ≤6. The pair (3,4)/(4,3) is forbidden via S0 for ALL t. The pair (2,5)/(5,2) is forbidden via S1(1)={2,3,5,6}, S1(2)={1,2,4,5}, or S1(5)={1,2,5,6}. For t=5, the pair (1,6)/(6,1) is ALSO forbidden via S1(5), so H cannot contain even one term, contradicton. At t=1 or2 only (1,6) and (6,1) remain on H. They are negatives and cannot BOTH occur (short zero sum of length2), so the two available indexed terms on H must be copies of the SAME point. Interchanging x/y coordinates, choose w=(6,1) twice, without changing axis availability:
t=1: 2(6,1)+(1,1)+(1,0)+(0,1)+(0,3)=(14,7), length6.
t=2: 2(6,1)+(2,2)+(0,3)=(14,7), length4.
Both are available NONEMPTY zero-sums modulo7, forbidden. This eliminates ALL one-copy diagonal branches.

No other diagonal occupancy is possible. So with printed 15-term short-zero-sum/capacity hypotheses after the earlier valid replacement, **at most one cyclic subgroup has two different occupied values**. This is a complete PROGRAMME_PROVED intermediate sublemma CLM-0081, not a proof of subsequent doubled-element classification, entire Lemma5.2, eta(C7³), or stronger Lemma2.3 coefficient. S009 CLM-0079 remains true within its narrower hypotheses; its twice-(5,5) case now also has the immediate displayed length-six witness.

## 2. FIRST downstream unproved BSP2012 p29–30 transition

Following the mixed-line assertion, printed Lemma5.2 p29 claims that there are three distinct doubly occurring elements x,y,z satisfying x+y∈<z>, because otherwise six elements on separate cyclic lines have their pairwise sums in two fixed lines, which 'easily gives a contradiction'. The existence/geometry implication and purported short zero-sum are not supplied or independently recovered in this ONE pass. **FIRST DOWNSTREAM GAP** is this printed six-line/pair-sum inference. All subsequent forbidden triples, further coordinate normalisations, multipicity-two alternatives and terminal t=1,2,4 are UNPROVED here. CLM-0075 remains one local conditional arithmetic repair, CLM-0078 only shows t=0,3,5,6 under extra doubled-anchor availability.

For t=1,2,4 the mere three doubled anchors 2(1,0),2(0,1),2(t,t) cannot yield a nonempty zero sum: choice coefficients 0≤a,b,c≤2 with a+tc=b+tc≡0 imply a=b=−tc. For c=1,2 and t=1,2,4, the residues −tc lie outside {0,1,2}; c=0 forces a=b=0. Extra terms whose multiplicities must be actually established are necessary. The source's false printed p29 sum 2(6,1)+(1,6)+(1,0)=(14,8)≡(0,1) remains false; the conditional CLM-0075 repair 2(6,1)+(2,4)+(0,1)=(14,7) is valid only in that explicitly available subcase.

## 3. Original Gao–Geroldinger1999 PRIMARY proof accessed

New lawful read-only FULL 33-page author-uploaded original article (PDF scanned publication, original printed pp179–211):
https://www.researchgate.net/profile/Weidong-Gao-5/publication/247011169_On_Long_Minimal_Zero_Sequences_in_Finite_Abelian_Groups/links/00b4953bdc82bc0399000000/On-Long-Minimal-Zero-Sequences-in-Finite-Abelian-Groups.pdf
DOI 10.1023/A:1004854508165, Gao–Geroldinger, Periodica Mathematica Hungarica 38 (1999). ORIGINAL Theorem10.7 **complete proof** and hypotheses viewed directly printed pp.206–208 (PDF zero-based pp27–29), with Lemma10.6 printed pp.204–206 (PDF pp25–27). This upgrades SRC-0026 from S009 METADATA_ONLY to **PROOF_INSPECTED**, not to programme proof. The theorem says every prime with Property B has Property C, assumes p odd in main argument (p=2 separated), and analyzes length3p−3 rank-two sequences with no short zero sum. It invokes Lemma4.3.2, Property B, extraction of minimal length2p−1 zero sum, Lemma10.6, further internal Lemma4.3.3/Cor10.5, changes of basis and final t-subset counting. Not all those imported premises or proof inferences were reconstructed independently in S010; CLM-0082 is SOURCE_STATED and full Property B=>C programme verification remains a gate. GG2006 SURVEY is NOT the 1999 original theorem. Reiher2010 Theorem10.2 and dependencies Lem7.2,9.2,9.6, Cor2.5, Props5.1,6.2,8.1,10.1 retain their scoped source inspection, not a claim of full independent derivation. BSP2012 p>=11 plane averaging m≤4 then m≤2 stays CONDITIONAL on the Property C/rank-two auxiliary proofs.

## 4. BSP coefficient and other restricted PRIMARY sources

BSP2012 printed Lemmas2.1/2.3 pp.22–23: splitting a zero 3p-block ensures at most R=(3p−1)/2, not printed 3(p−1)/2; stronger rank-three k-wise coefficient still unproved. CLM-0068 proves a complete upper-bound *deduction* only IF eta(Cp³)≤3p²−4p−3 and recorded classical Chevalley–Warning/p-group inputs, NOT eta7. BSP2007 original Prop1 printed p3 and Prop8 printed pp6–11 with diagrams: subscript multiwise D3(C3³)=15, D4=18 versus superscript at-most-3 zero-sum threshold 17. Printed 'at most k−2 triples' versus later k−3 remains a diagrammatic gap, not independently reconstructed proof.

Official Sheikh2017 137-page thesis Chapter4 URL https://pure.royalholloway.ac.uk/files/28262990/The_Davenport_Constant_of_Finite_Abelian_Groups.pdf S010 direct read-only retrieval produced **fresh HTTP403**; S009 had a separate internal fetch error, prior S007 an earlier 403. Full Chapter4/Remark4.3.11 unread. Its indexed exactly-three-free counterexample contains a zero-sum pair, so is NOT a counterexample to a no-AT-MOST-three-sum condition. GHST2007 Prop5.6 published pp16–17 original C53.html code AND output not retrieved, original historical URL currently inaccessible; NO code run. Yiu arXiv2609.04950v1 M1 repeated generation of 98,622 normal generators / 230,983 extensions does NOT independently replay the singly implemented FINAL three-disjoint-zero-sum predicate; M2 s≤6=24, M3 s≤7=19 are DIFFERENT tests. S010 obtained no authenticated complete original code/log/certificate bytes; none executed.

## 5. Exact thirty-row frontier mirrors: all n=1..30 checked

| n | D* | bound | n | D* | bound |
|---|---:|---:|---|---:|---:|
|1|1|1|16|46|46|
|2|4|4|17|49|49|
|3|7|7|18|52|52|
|4|10|10|19|55|55|
|5|13|13|20|58|58..59|
|6|16|16|21|61|61..63|
|7|19|19|22|64|64|
|8|22|22|23|67|67|
|9|25|25|24|70|70|
|10|28|28|25|73|73|
|11|31|31|26|76|76|
|12|34|34|27|79|79|
|13|37|37|28|82|82..83|
|14|40|40|29|85|85|
|15|43|43..45|30|88|88..90|

All 30 machine-readable and Markdown rows retain exactly the same source class and bounds: 25 source-stated exact/trivial, five conditional intervals n15 43..45,n20 58..59,n21 61..63,n28 82..83,n30 88..90. Fresh focused primary exact theorem checks authenticated no new exact result; failure to find a source is NOT a present-day openness claim. Schmid2011 published D(C6³)=16; original van Emde Boas II Cor4.3 exact rank-three n=2p^a and III Cor1.5 exact rank-three n=3·2^a retain SOURCE_STATED values even though full historical proofs are not fully independently reconstructed. Inherited multiwise 14/17, tripling +5 and orbit counts 43/699/5553 remain quarantined.

## 6. Phase gate

**Phase1 IN_PROGRESS/PASS withheld.** CLM-0081 closes ONE necessary published intermediate p7 inference; original GG1999 full Theorem10.7 proof text is NOW readable; major gaps remain in the later p7 doubled terms/t cases, eta7, exact stronger coefficient, full original B=>C and Reiher dependencies, BSP2007 diagrams, Sheikh full chapter, GHST original code/output, Yiu reproducibility, and historical long proofs. Phases2/3 NOT_STARTED, CAM-0001 PROPOSED/NOT RUNNING activation BLOCKED by source-stated n6=16, no replacement target/candidate/certificate. No exhaustive mathematical search, computations, author code, Lean or campaigns. Zero hosted CI checks at entry: ADMIN validation is NOT hosted CI PASS. STOP S010; S011 strictly future and unexecuted.
