# S042 — Sharp symbolic C5^3 core countermodels and maximal CRT decorations

13 October 2026. Internal symbolic mathematics; NO numerical/computational mathematical search, CAS, SAT/ILP, orbit generation, historical code, Lean or Palomar. The upper D_j(C5^3)<=5j+10 remains SOURCE_STATED/Yiu, with independently unauthenticated finite predicates. Our lower construction is independent of that source.

## CLM-0160: an explicit sharp lower multiwise family with no <=4 zero sum

For every k>=2 let
 A_k = e1^(5k-6) e2^4 e3^4 (e1+e2)^3 (e1+e3)^2 (e2+e3)^2
in C5^3, indexed even when values repeat.

Length is (5k-6)+4+4+3+2+2 = 5k+9.
The three coordinate totals when lifted to ordinary nonnegative integers are
 (5k-1, 9, 8).
Every term has coordinates 0 or1 and is nonzero, so a nonempty zero-sum subset with at most four terms is impossible: all its coordinate totals would be between0 and4 and hence zero as integers, impossible.

Suppose k pairwise index-disjoint nonempty zero-sum blocks exist. Since total second coordinate is9 and total third is8, at most one zero block uses coordinate2 and at most one uses coordinate3 (each nonzero coordinate total of a zero block is >=5, divisible by5).

If at most one block meets {coordinate2,coordinate3}, at least k-1 blocks consist only of pure e1 indices. They need 5(k-1)=5k-5 distinct e1 copies, but only 5k-6 are present.

Otherwise exactly two separate blocks are exceptional: one has coordinate2>0, coordinate3=0, and the other coordinate3>0, coordinate2=0; all other k-2 blocks are pure e1. The first exceptional block requires at least one e1+e2 (only four e2 terms have coordinate2 without coordinate3), so its first-coordinate total is positive and divisible by5, hence >=5. Likewise the second requires e1+e3 and first total >=5. Therefore their first-coordinate demand together with k-2 pure-e1 blocks is at least 5(k-2)+5+5=5k, exceeding the full available first total 5k-1. Contradiction.

Thus A_k has fewer than k disjoint zero sums, showing D_k(C5^3)>=5k+10 by a standalone hand proof. This verifies only the LOWER side of the source-stated Yiu exact formula; the finite/computational UPPER input has not been authenticated.

At k=4, A_4 has 29 terms and no zero subset of size <=4, <4 disjoint zero sums, and total (4,4,3) modulo5. Delete ONE pure e1 position to obtain A'_4 of length28, with the same local zero-subset exclusions and <4 disjoint zero sums, total (3,4,3). Therefore BOTH the 28 and 29 critical-core numerical/short-zero profiles occurring in S041 CLM-0156 really exist in C5^3. A universal '28/29 core cannot exist' assertion is FALSE; the kernel decorations and preceding zero blocks are indispensable.

Hostile checks: distinct indexed e1 copies are counted, not collapsed. A zero block involving BOTH coordinates2/3 does not violate the proof, because then too few pure e1 copies remain for k-1 other blocks. The incorrect variant e1^(5k-5)e2^4e3^4(u12)^2(u13)^2(u23)^2 fails: it has k-1 pure e1^5 blocks PLUS e2^4e3^4u23, a full k-block packing. That invalid variant was rejected before registering the proved construction. This matters: merely checking the two-separate-exceptional case is insufficient.

## CLM-0161: exact maximal-decorations partition from a 28/29 core

Retain EXACTLY the S041 SOURCE_STATED-conditional hypotheses for n=5m with m in {3,4,6}, k=3m-2, N=5k+8. They give k-4 disjoint quotient-C5 zero blocks B_i of length4 or5 and a residual R of 28 or29 positions having fewer than four further disjoint quotient zero sums; R29 has no size4 zero.

Additionally use the SOURCE_STATED p5 D_3(C5^3)=25. Since |R|>=28, there are THREE disjoint nonempty quotient-zero blocks C1,C2,C3 in R. Together with the preceding B_i, there are exactly k-1 quotient-zero blocks. Let H=C_m^3 be the CRT kernel, with D(H)=k (at m=3,4 p-group; at m=6 retain its historical SOURCE_STATED status). Write v_i for their H-valued decorated sums. The sequence V of k-1 decorations is zero-sumfree: any nonempty sum of selected v_i vanishing in H corresponds to a nonempty zero sum of the original S. By D(H)=k it has maximum possible zero-sumfree length.

**Full subset-sum saturation:** Sigma(V)=H including the empty subset. Indeed if h were not a subset sum, appending -h to V would give a zero-sumfree sequence of length k=D(H), impossible. h=0 is already covered by the empty subset. This coverage is of unions of COMPLETE selected quotient-zero blocks; it does NOT imply arbitrary unused singletons can be absorbed.

Let L be the positions of R left after C1,C2,C3. Since any nonempty quotient-zero subset of L would supply a k-th block, L is quotient-zero-sumfree. The internally proved prime rank-three D(C5^3)=13 (S039 CLM-0142) yields |L|<=12. Thus the three C blocks consume >=16 positions of R28 and >=17 of R29. In R28 at least one of the three has size >=6; in R29, whose 4-zeros are globally forbidden, their sizes must be >=5 and either one is >=7 or at least two are >=6. No all-length-five triple packing is possible, since it would leave >=13 and force another quotient zero.

This theorem synchronizes the two sides of the CRT problem: one may always reach a MAXIMAL zero-sumfree decorated H-sequence of length k-1, whose subset sums cover H, paired with a genuinely Q-zero-sumfree residual of at most12 positions. What remains is an **exchange premise**: a quotient-zero subcollection overlapping the chosen blocks must permit a new index-disjoint selection whose H decoration cancels a subset of V. Subset-sum saturation alone does not provide such an exchange, and the explicit A4/A4' cores prevent pretending the C5-only residual is impossible.

For n15/n20/n30 the initial extracted block numbers remain 3/6/12; H dimensions are C3^3/C4^3/C6^3, and the maximal decoration lengths are 6/9/15. No composite D1 equality or zero-sumfree candidate is obtained.
