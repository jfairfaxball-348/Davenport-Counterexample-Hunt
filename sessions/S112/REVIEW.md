# S112 hostile same-executor review — 18 October 2026

**ACCEPT, with the stated conditions:**
- CLM-0374 and CLM-0376 as PROGRAMME_PROVED. CLM-0376 uses programme-proved inputs only.
- CLM-0377 as PROGRAMME_PROVED, conditional on the arithmetic certificate CLM-0375 and the cited D-values.
- CLM-0375 and CLM-0378 as COMPUTED_EXACT.

**Attacks and resolutions:**
1. *Image orders.* For g = (n/d)u with ord u = n (CLM-0354), the image in G/aG ≅ C_a³ has order a / gcd(a, n/d). The constructive tests compute the actual orders of the actual elements and agree with the sieve's closure verdicts: every closing route produced a verified zero-sum (651 runs).
2. *ν_lb inputs.*
   - D₂(C₂³) = 7 is a hand lemma, checked exhaustively.
   - D₂(C_p³) ≤ 5p−3 is CLM-0143 (PROGRAMME_PROVED, odd primes).
   - D₂ ≤ 2D₁ and D_j ≤ D₂ + (j−2)D₁ are greedy bounds; minimal zero-sums have length ≤ D₁.
   - D₁(C₄³) = 10 is CLM-0039 (SOURCE_STATED); this is why CLM-0377(i) is conditional.
3. *Caps.* α ≤ d−1 is trivial. The order-n cap n−2 is CLM-0350, conditional on rank-two D. The even caps are CLM-0368. The n = 15 hand proof uses only α ≤ 14.
4. *n = 15 hand proof.* The failure condition B = p−3 follows from R ≥ 4p−2 (which forces all five o_i = p) and the congruence Σα ≡ −2. The x-substitution leaves only x ∈ {3, 9, 15} with weights 2, 1, 0, and both weight-2 completions sum to 63 ≠ 48. This was checked independently by brute force over all α (zero solutions).
5. *Two algorithms for CLM-0375.* The counting knapsack DP and the recursive multiset enumeration have separately written closure tests, and the counts agree for every n and k. Both share the route list and caps (same premises). A shared-premise error would be common-mode, which is why the conclusions are labelled conditional.
6. *Is the sieve a target-group computation?* No. It enumerates multisets of (order, multiplicity) pairs with Σα = 3n−2; no group element of C15³ or C20³ is formed. The constructive tests use n ∈ {6, 10, 12} only.
7. *Scope.*
   - CLM-0366/0367 are not relabelled. CLM-0376 proves the same statement as CLM-0366 by an independent route.
   - The text never states SAT15/SAT20 or a D value, and the frontier is unchanged.
   - The residue (CLM-0378) is reported as arithmetic survivors, not candidates.

**Residual limitations:**
- Every proof is internal and by the same executor.
- CLM-0377 inherits source-stated premises.
- No Lean certificate exists (deferred).
- CI is ABSENT_NOT_PASS.
- n = 30, 33, 35 gain nothing at support 5.
