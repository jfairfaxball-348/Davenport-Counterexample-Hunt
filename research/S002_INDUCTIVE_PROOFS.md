# S002 — Inductive bounds, exact binary multiwise lemma, and corrected ternary route

**S004 correction:** the inequalities in this historical proof remain valid, but the n=6 target recommendation below is superseded: published Schmid2011 Theorem4.1 gives D(C6³)=16, and original 1969 exact families improve several other rows. See [the current audit](S004_PRIMARY_PROOF_INPUTS.md) and frontier. No Phase-2 target is currently selected.

## Definitions and inputs

A sequence is a finite multiset; nonempty zero-sum subsequences may repeat group elements at distinct positions. \(D_k(Q)\) is the smallest \(L\) for which every length-\(L\) sequence over \(Q\) contains \(k\) pairwise disjoint nonempty zero-sum subsequences. The classical Olson p-group identity \(D(C_{p^a}^3)=3p^a-2\) is **SOURCE_STATED**, not independently reproved. No inherited orbit count, software or numerical campaign is used.

## Lemma 1: subgroup induction (PROGRAMME_PROVED; CLM-0047)

Let \(H\le G\) be finite abelian, let \(k=D(H)\), and let \(L=D_k(G/H)\). Every length-\(L\) sequence \(S\) over \(G\) projects to a sequence with \(k\) pairwise disjoint nonempty zero-sum blocks \(B_1,\ldots,B_k\) in \(G/H\). The sums \(b_i=\sum B_i\), now taken in \(G\), lie in \(H\). Since \(k=D(H)\), a nonempty subcollection of the \(b_i\) sums to zero. The union of the corresponding (disjoint) original blocks is a nonempty zero-sum subsequence of \(S\). Hence
\[
D(G)\le D_{D(H)}(G/H).
\]
This establishes the inequality without borrowing the proof in SRC-0006.

For \(G=C_{am}^3\) and \(H=aG\cong C_m^3\), \(G/H\cong C_a^3\), for all positive integers \(a,m\). Thus \(D(C_{am}^3)\le D_{D(C_m^3)}(C_a^3)\).

## Lemma 2: exact \(D_k(C_2^3)=2k+3\) for every \(k\ge2\) (PROGRAMME_PROVED; CLM-0048)

Write \(V=\mathbb F_2^3\). Every four vectors in \(V\) are linearly dependent, so any four terms contain a nonempty zero sum and \(D(V)=4\).

**Upper bound, base \(k=2\).** For seven terms, if one is zero, remove it and use \(D(V)=4\) on the remaining six. If two terms coincide, remove their zero-sum pair and use \(D(V)=4\) on the remaining five. Otherwise the terms are precisely the seven distinct nonzero vectors. Pick independent \(x,y\); their third companion \(x+y\) is present and gives a zero-sum triple. The four remaining terms contain a zero sum, independent of the triple. Thus \(D_2(V)\le7\).

**Upper induction.** At length \(2k+3\ge9\), \(k\ge3\), among the terms there is either a zero term or a repeated pair (only seven distinct nonzero elements exist). Remove that zero sum of length at most two. At least \(2k+1=2(k-1)+3\) terms remain, and by induction they contain \(k-1\) disjoint zero sums. Hence \(D_k(V)\le2k+3\).

**Sharpness.** Choose six distinct nonzero vectors \(A\) among the seven; their total sum is the seventh omitted nonzero vector \(b\), as the sum of all seven nonzero vectors is zero. Choose \(a\in A\), and append \(2(k-2)\) copies of \(a\). The resulting \(2k+2\)-term sequence still has nonzero total sum \(b\), and it has \(2k-3\) occurrences of \(a\) and five other distinct nonzero values. Every zero-sum block has length at least two, and every block of length two is an \(a,a\) pair, of which at most \(k-2\) are disjoint. If there were \(k\) disjoint zero-sum blocks, at least two would have length at least three, so their combined length would be at least \(2(k-2)+3+3=2k+2\): they would exhaust the sequence. But then its total sum would be zero, contradiction. Therefore \(D_k(V)>2k+2\), proving equality.

## Corollary 3: doubling (PROGRAMME_PROVED; CLM-0049)

For \(m\ge2\), \(D(C_m^3)\ge3m-2\ge4\). Apply Lemmas 1 and 2 with quotient \(C_2^3\):
\[
D(C_{2m}^3)\le D_{D(C_m^3)}(C_2^3)=2D(C_m^3)+3.
\]
If \(m\) is a prime power, SRC-0003 gives \(D(C_m^3)=3m-2\), whence \(6m-2\le D(C_{2m}^3)\le6m-1\). In particular \(16\le D(C_6^3)\le17\).

## Corrected Lemma 4: tripling (complete deduction from SOURCE_STATED multiwise theorem)

Original Bhowmik–Schlage-Puchta SRC-0008/SRC-0019, Proposition 1, explicitly states
\[
D_2(C_3^3)=11,\qquad D_k(C_3^3)=3k+6\ (k\ge3).
\]
The same page also uses \(D^3\) for a *different* invariant (a zero sum of length **at most three**; wording corrected in S004), which must not be confused with subscript \(D_3\). Thus \(D_3=15\), \(D_4=18\), **not** 14/17 (S001 inherited). Combining Lemma 1 and this **SOURCE_STATED** theorem, since \(D(C_m^3)\ge4\), proves the conditional-on-published-theorem deduction
\[
D(C_{3m}^3)\le3D(C_m^3)+6\quad(m\ge2).
\]
For prime-power \(m\), this gives \(9m-2\le D(C_{3m}^3)\le9m\), a *two-step*, not off-by-one, interval. Therefore the S001 seed inequality \(3D(C_m^3)+5\) and implied 3m sandwiches may **not** be used. We do not assert the +5 inequality is mathematically false for every \(m\), only that it is not established by the cited multiwise theorem.

## Lemma 5: necessary skeleton and exact CRT characterization (PROGRAMME_PROVED)

Suppose a length-16 sequence \(S\in C_6^3\) is zero-sumfree. If its reduction to \(C_3^3\) contained four disjoint nonempty projected zero-sum blocks, their sums in \(C_6^3\) would lie in the kernel \(C_2^3\). Since \(D(C_2^3)=4\), a nonempty subcollection of those four block sums would sum to zero, contradicting zero-sumfreeness. Thus at most three such blocks exist. Since 2 and 3 are coprime, CRT identifies \(C_6^3\cong C_2^3\oplus C_3^3\). Under this identification a nonempty index subset has zero total in \(C_6^3\) iff its mod-3 sum **and** mod-2 label sum are both zero. Equivalently, to lift a chosen mod-3 skeleton zero-sumfreely, **every nonempty mod-3-zero-sum index subset** must have nonzero mod-2 label sum. No orbit count, label equivalence or solver correctness is presumed.

## Explicit n≤30 bounds from these rules

For prime-power n, the source-stated Olson equality applies. For composite n≤30, repeatedly use doubling and tripling as above, always with the minimum available upper bound; the resulting intervals are listed in frontier/FRONTIER.md. These are deductions, not new exact evaluations or evidence that any composite n is currently an open problem in the external literature.

**Historical S002 n=6 entry decision (withdrawn in S004):** The 16..17 deduction led to a proposed first Phase-2 tooling target after Phase-1 PASS. S004 located exact historical D(C6³)=16 and withdrew that recommendation while retaining CAM-0001 PROPOSED / NOT RUNNING. The primary 2007 C3⊕C3⊕C3d result is for a different invariant-factor family. The inherited '5553' GL(3,3) skeleton-orbit claim has no reproduced evidence and must never be treated as a complete count.
