# S055 — complete Fano parity saturation of the 28-block method (CLM-0208)

14 October 2026. Phase1, original-index symbolic proof. Conditional setting ONLY: S054's specified hypothetical minimally zero-sum 59-term T in G=C20³, consisting of 22 original equal-quotient pairs, eight common-quotient outsider positions and seven singleton outsider positions of the seven distinct nonzero quotient parities. By S054's source-dependent CLM-0206 every one of the original 59 terms has NONZERO image in Q=G/2G=F2³. The seven quotient-class multiplicities are ALL ODD, because the 22 paired terms and eight common-q outsiders contribute even counts and the seven singleton positions contribute once each. This section uses ONLY the quotient data: no D(C10³)=28 is needed for the classification.

## Theorem — exact structure at 28 blocks

Suppose all 59 original positions are partitioned into 28 nonempty disjoint index blocks, each with quotient sum zero. Every block has size at least two (there are no parity-zero original singletons). Relative to 28 pairs, the 59 positions contain exactly three excess positions. Thus the only possible size patterns are:

(A) 27 two-blocks and one five-block;
(B) 26 two-blocks, one three-block and one four-block;
(C) 25 two-blocks and three three-blocks.

Two-blocks must consist of original terms of the SAME nonzero quotient parity. Removing any number of two-blocks leaves each of the seven parity-class multiplicities odd. Case (A) is impossible: the one five-block cannot contain an odd number of positions in all seven parity classes. In case (B), the three- and four-blocks together contain exactly seven positions, therefore they contain precisely ONE representative of EACH of the seven nonzero quotient classes. A zero-sum nonzero triple in F2³ is exactly a Fano line; the remaining four classes are its complementary cap, automatically summing to zero. In case (C), the nine positions in three nonzero zero-sum triples must contain odd numbers of occurrences of EACH of seven classes. Hence one class occurs three times and all six other classes once. Each triple is a Fano line. The three lines therefore meet at the triply occurring hub class; they are the THREE lines of its Fano pencil (each of the other six points occurs once). All positions, values and multiplicities here are ORIGINAL INDEXED, not orbit classes.

These patterns are NECESSARY, not claimed always realisable for arbitrary fine labelled multiplicities. In particular the S054 735 partitions are of type (B), but type (C) must not be ignored, and arbitrary replacements of original pairings within equal parity classes must be considered. This classification does not supply a new H-valued maximal-atom inverse theorem.

## Saturation theorem — no over-budget partition is possible from this parity profile

**(i)** No partition of ALL 59 positions into 29 quotient-zero nonempty blocks exists. A 29-block partition would have 28 two-blocks and one triple (59=58+1); its non-pair positions could occupy at most three of the seven odd parity classes, contradiction.

**(ii)** No PROPER original-index subset of T can be partitioned into 28 or more quotient-zero nonempty blocks. At least 56 positions are needed for 28 blocks. Let d be the number of deleted original positions, so d∈{1,2,3} (for d≥4 there are at most55 positions and the bound follows just from sizes).

* d=1: 58 positions, six quotient classes retain odd multiplicity. A 28-block size profile is either 27 pairs plus one four-block, which cannot absorb six odd classes, or 26 pairs plus two triples. In the latter case the triples must be two disjoint Fano lines, since they must account for six *different* odd parity classes exactly once. TWO DISTINCT FANO LINES IN F2³ ALWAYS INTERSECT (they are two-dimensional subspaces with a common nonzero vector), contradiction.
* d=2: 57 positions, at least five quotient classes have odd multiplicity. A 28-block partition would be 27 pairs plus one triple, which can account for only three odd classes. Contradiction.
* d=3: 56 positions, at least four quotient classes retain odd multiplicity. A 28-block partition would consist entirely of 28 same-parity pairs, which requires all class multiplicities even. Contradiction.

Larger block counts are also impossible for a proper subset, since for 58 positions 29 blocks would all be pairs yet six classes have odd multiplicity, and 30 blocks would require at least60 positions. This covers ALL original subsets, irrespective of which a_i or b_i, g_j or s_r positions are removed. The zero-sum condition on the ORIGINAL T is not used, so this is an exact quotient-combinatorial NO-GO, not a counterexample to its existence.

## Mathematical consequence, strictly bounded

The sharp SOURCE_STATED bound D(H)=28 can create an immediate contradiction via **29 disjoint quotient-zero blocks** on all originals or **28 such blocks on a proper original subset**. The preceding theorem says NEITHER can occur at all in the surviving all-nonzero-parity seven-odd-classes quotient profile. Therefore a proof restricted to this **disjoint-block cardinality mechanism** is exhausted: one must use an inverse theorem on the H VALUES of 28-block atoms, finer original subset sums involving overlapping blocks, a different starting 59-term decomposition, or a new argument. This does NOT establish that a minimal T59 exists, that its 735 extremal atoms are simultaneously realisable in H, or that all possible arguments using D(H)=28 have been ruled out. Only this specific disjoint-block count mechanism has been proved unable to force a contradiction.

## Hostile audit

- Do not count one common hub index three times: the pencil uses THREE DIFFERENT ORIGINAL INDICES of the hub parity class. Thus the hub class must have multiplicity at least three.
- The 5-block pattern fails by seven odd-class counts, even though five nonzero binary vectors may sum to zero in other class profiles.
- A two-triple deletion partition is impossible specifically because six distinct Fano points cannot be partitioned into TWO DISJOINT LINES. It is invalid to argue merely from sizes.
- A minimal 28-term H atom is perfectly consistent with SOURCE_STATED D(H)=28. The result is a negative proof-method theorem, NOT D(C20³)=58.
- This all-nonzero profile is inherited CONDITIONALLY from CLM-0206 and SOURCE_STATED C10³ D=28; the classification itself is elementary and independent of that source bound.
