# S111 hostile same-executor review — 18 October 2026

**ACCEPT, with the stated conditions:**
- CLM-0368..0372 as PROGRAMME_PROVED. Each is conditional on the source-stated or programme-proved D-values it names.
- CLM-0373 as COMPUTED_EXACT.
- The consolidation review as a classification only; it upgrades nothing.

**Attacks and resolutions:**
1. *CLM-0368 instantiation.* SRC-0005 Thm 2.7 (via CLM-0356) allows "m, n ≥ 1". Taking m = n/2 and the theorem's n = 1 gives D(C2⊕C_n⊕C_n) = 2n. The CLM-0355 hypotheses d | m and d ≥ j hold for (n, 2, 2) and (n/2, 1, 1). The mechanical script recomputes the bounds from |S| ≤ m − d + d(Q) and cross-checks the corollary inequality for even n ≤ 400.
2. *CLM-0370: are the block sums in the right group?* Blocks g^{o} with o the order of g mod 2G have sums in 2G, and 2G ≅ C_b^r via 2x ↦ x mod b, which is well defined and bijective for n = 2b. The deficit bound uses t₀ ≥ (|S| − R)/2, with values in 2G counted with full multiplicity. δ = 1 needs R ≥ r+1 leftover vectors in F₂^r, which are dependent. The 2,600 constructive runs (r = 2, 3, 4) exercised both branches, and every output zero-sum was verified by both checkers.
3. *CLM-0371 at n = 20: overclaim risk.* It rests on CLM-0065 (SOURCE_STATED; D(C10³) = 28 is in its recorded exact rows). It is stated as conditional. CLM-0367 is explicitly **not** relabelled; the review records two independent routes instead.
4. *CLM-0372 logic.* The leftover is exactly one copy of each value in O, so R = |O|. The deficit is ≤ ⌊(|O|−2)/2⌋, and zero-sumfreeness forces ν(Ō) < δ. The cases |O| ≤ 5, |O| = 7 and coincident images each produce the needed disjoint zero-sums. The Fano-complement fact was verified exhaustively. The "re-partition cannot help" remark is restricted to 6-valued residual S and argued by parity and length budget; it is not a claim.
5. *CLM-0373 is a falsity claim.* Its truth needs only one verified witness per a, and the two algorithms agree on every instance, with identical decision-stream SHA-256. Enumeration completeness (GL normalisation) affects only the reported counts. The packing maxima use the minimal-block DP and are exact. The brute cross-check's length cut ≤ D(C_a³) is exact, because packings refine into minimal zero-sums. These are statements about images and proof methods, not about C15³ sequences.
6. *Code/result consistency.* After a docstring-only edit to `two_disjoint.py`, all six TWO runs were repeated with the final code, and the decision-stream hashes were unchanged. The tool hashes are recorded by the validator. Exploratory checks with a MILP solver are not committed and support no claim.
7. *Scope.* No C15³/C20³ sequence was computed. The frontier is unchanged, and the text never states SAT15/SAT20 or a D value.

**Residual limitations:**
- Every proof is internal and by the same executor.
- CLM-0368/0370..0372 inherit source-stated premises.
- No Lean certificate exists (deferred by the owner).
- CI is ABSENT_NOT_PASS.
- Odd n remains open beyond the n = 15 computation.
