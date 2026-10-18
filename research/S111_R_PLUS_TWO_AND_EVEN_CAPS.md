# S111 — Generalisation: even-n caps and the "r+2 values" bound (18 October 2026)

Priority: **SATURATION_FALLBACK** (fallback session 6). Owner steering (18 October 2026): generalise to all n or to families of n. Targets, both OPEN: **SAT20** (D(C20³) = 58) and **SAT15** (D(C15³) = 43).

All proofs are elementary INTERNAL SAME_EXECUTOR hand proofs. Block/subgroup arguments of this kind are classical in spirit (cf. CLM-0150, SRC-0003), and **no novelty is claimed**. Exact tests use settled or small groups only; there is no C15³ or C20³ sequence computation.

Notation: G = C_n^r. For a | n write n = ab. Then G/aG ≅ C_a^r, and aG ≅ C_b^r via ax ↦ x mod b. D* (C_b^r) = r(b−1)+1. ν(T) is the maximum number of pairwise disjoint nonempty zero-sum subsequences of T.

## 1. Even-n multiplicity caps (part (b))

**CLM-0368 (PROGRAMME_PROVED, conditional on SOURCE_STATED CLM-0352 and CLM-0356).** Let n ≥ 4 be even and S zero-sumfree over C_n³.
1. If some h of order n has v_h(S) = n−2, then |S| ≤ 3n−3.
2. If some h of order n/2 has v_h(S) = n/2 − 1, then |S| ≤ 5n/2 − 2.

Hence every zero-sumfree (3n−2)-term sequence over C_n³ has **order-n multiplicities ≤ n−3** and **order-(n/2) multiplicities ≤ n/2 − 2**.

*Proof.* CLM-0356 is SRC-0005 Theorem 2.7, D(C2⊕C2m⊕C2mn) = 2m+2mn. With m = n/2 and the theorem's n equal to 1 it gives D(C2⊕C_n⊕C_n) = 2n, so d(Q) = 2n−1 for Q = C2⊕C_n⊕C_n. Apply the CLM-0355 bound |S| ≤ m − d + d(Q), where Q = G/⟨dh⟩ ≅ C_{nd/m}⊕C_n⊕C_n.
- (1) Take (m, d, j) = (n, 2, 2). Then d | m, d ≥ j and nd/m = 2, so |S| ≤ n − 2 + 2n − 1 = 3n−3.
- (2) Take (m, d, j) = (n/2, 1, 1). Then nd/m = 2, so |S| ≤ n/2 − 1 + 2n − 1 = 5n/2 − 2 < 3n−2.
- Multiplicity n−1 for order n is CLM-0350. ∎

**Mechanical check (T1).** For every even n ≤ 400, the script enumerates all (m, d, j) with m | n, d | m and 1 ≤ j ≤ d. It applies the bound for the levers with nd/m ∈ {1, 2}, the only ones whose D is source-stated for every even n. Results:
- The pairs giving nd/m = 2 are exactly (n, 2) and (n/2, 1). The reason: m = nd/2 must divide n, so d ∈ {1, 2}.
- The resulting caps are n−3 for order n and n/2 − 2 for order n/2. Every other order keeps its trivial cap m−1.
- At n = 20 this reproduces CLM-0357 (17 and 8), which CLM-0368 generalises.

**Exact random tests (T2), n = 4, 6, …, 14.** Maximal zero-sumfree sequences were built greedily with a fixed h-multiplicity and checked by both checkers. All respect the bounds.
- At n = 4 both bounds are attained (9 and 8).
- At larger n, greedy extension stays below them. This says nothing about sharpness.

## 2. The block-packing lemma

**CLM-0369 (PROGRAMME_PROVED, FOUNDATION).** Let n = ab, G = C_n^r, and S a sequence over G.
- (i) If S contains D(C_b^r) pairwise disjoint nonempty subsequences, each with sum in aG, then S has a nonempty zero-sum subsequence.
- (ii) Let S have distinct values g_i with multiplicities α_i. Let o_i | a be the order of g_i + aG, and write α_i = q_i o_i + ρ_i with 0 ≤ ρ_i < o_i. The blocks g_i^{o_i} give t₀ = Σq_i ≥ (|S| − R)/a disjoint subsequences with sums in aG, where R = Σρ_i. Let L̄ be the image of the leftover ∏g_i^{ρ_i} in G/aG. If t₀ + ν(L̄) ≥ D(C_b^r), then S has a nonempty zero-sum.
- (iii) If |S| = r(n−1)+1 and D(C_b^r) = D*, the deficit δ = D* − t₀ satisfies δ ≤ ⌊(R − (a−1)(r−1))/a⌋.

*Proof.*
- (i) The sums σ(B_j) form a sequence in aG ≅ C_b^r of length ≥ D(C_b^r). So some nonempty J has Σ_{j∈J} σ(B_j) = 0, and ∏_{j∈J} B_j is a nonempty zero-sum.
- (ii) Each block g_i^{o_i} has sum o_i g_i ∈ aG. Disjoint zero-sum subsequences of L̄ are disjoint subsequences of the leftover with sums in aG. Since o_i ≤ a, t₀ = Σ(α_i − ρ_i)/o_i ≥ (|S| − R)/a. Apply (i).
- (iii) δ ≤ rb − r + 1 − (rab − r + 1 − R)/a = (R − (a−1)(r−1))/a, and δ is an integer. ∎

Part (i) is the classical subgroup inequality (compare CLM-0150, which measures its unrestricted gaps). The point of (ii)–(iii) is that **few distinct values force a small leftover**: R ≤ k(a−1) for k distinct values.

## 3. The r+2 values bound at even n (part (c))

**CLM-0370 (PROGRAMME_PROVED, conditional on D(C_b^r) = r(b−1)+1).** Let n = 2b and r ≥ 1. Every zero-sumfree sequence over C_n^r with at most r+2 distinct values has length ≤ r(n−1).

*Proof.* Let |S| = r(n−1)+1, with k ≤ r+2 distinct values, and take a = 2 in CLM-0369.
- Every o_i ∈ {1, 2}, so ρ_i ≤ 1 and R ≤ r+2.
- By (iii), δ ≤ ⌊(R − r + 1)/2⌋ ≤ 1, and δ = 1 only if R ≥ r+1.
- In that case L̄ is a sequence of R ≥ r+1 vectors in F₂^r. It has a nonempty zero-sum: a repeated vector gives a pair, and otherwise r+1 distinct vectors are linearly dependent over F₂. So ν(L̄) ≥ δ.
- CLM-0369(ii) then gives a nonempty zero-sum. ∎

**CLM-0371 (PROGRAMME_PROVED, conditional on the cited D-values).** Every zero-sumfree sequence over C_n³ with at most 5 distinct values has length ≤ 3n−3 when n = 2b and D(C_b³) = 3b−2. That premise is available in the following cases.
- b prime: CLM-0142, programme-proved.
- b a prime power: CLM-0039, SOURCE_STATED.
- b = 2p^k: CLM-0065, SOURCE_STATED.
- b = 6: CLM-0064, SOURCE_STATED.
- b = 3·2^k: CLM-0066, SOURCE_STATED.

**Consequences.**
- The bound holds for n = 4p^k with p odd (in particular **n = 20**, via D(C10³) = 28, and n = 28, via D(C14³) = 40). These are the substantive new cases.
- For n = 2p^k, n = 12 and n = 3·2^k it is implied by the known D(C_n³) anyway (CLM-0065/0066).
- For general rank r it holds for n = 2p^k (CLM-0039).
- **Relation to CLM-0367.** At n = 20, CLM-0371 re-proves the support-≤5 bound by a route that shares no premise with CAM-0007:
  - CLM-0371 uses CLM-0065 (SOURCE_STATED) and the hand proof above.
  - CAM-0007 uses CLM-0358/0361..0364 and two exhaustive codes.
  - CLM-0367 keeps its COMPUTED_EXACT label. It is not retroactively relabelled.

**Exact constructive tests (T3).** The proof is an algorithm. It was run on random sequences of length r(n−1)+1 with r+2 values: r = 2 (n = 4..10), r = 3 (n = 4..14) and r = 4 (n = 4, 6), 2,600 instances in all.
- Every run produced a nonempty zero-sum, verified by checkers A and B.
- The extra-block branch (δ = 1) occurred 459 times.

## 4. Even-n parity structure for all supports

**CLM-0372 (PROGRAMME_PROVED, conditional on D(C_b³) = 3b−2).** Let n = 2b and S zero-sumfree over C_n³ with |S| = 3n−2, of any support. Let O be the set of distinct values g ∉ 2G whose multiplicity is odd. Then:
- (a) |O| ≥ 6;
- (b) |O| ≠ 7;
- (c) if |O| = 6, the images of O in G/2G ≅ F₂³ are six distinct nonzero vectors, i.e. F₂³ ∖ {0, P} for some P ≠ 0;
- (d) in general, ν(Ō) ≤ ⌊(|O| − 2)/2⌋ − 1.

*Proof.* With a = 2, the leftover is exactly one copy of each value in O, so R = |O|, and CLM-0369(iii) gives δ ≤ ⌊(|O| − 2)/2⌋. Zero-sumfreeness forces ν(Ō) < δ, which is (d).
- |O| ≤ 3: δ ≤ 0, which is impossible.
- |O| ∈ {4, 5}: Ō has ≥ 4 = D(C2³) terms, so ν(Ō) ≥ 1 ≥ δ.
- |O| ∈ {6, 7}: we need ν(Ō) ≤ 1.
  - If two images coincide, they form a zero-sum pair, and the other ≥ 4 terms contain another zero-sum. So the images are distinct and nonzero.
  - For |O| = 7 they are all of F₂³∖0. A Fano line and its complementary four vectors are disjoint zero-sums, because the seven nonzero vectors sum to 0. So |O| ≠ 7.
  - For |O| = 6 the images are F₂³∖{0, P}. ∎

**The residual configuration is genuinely tight for the method.**
- Six distinct nonzero vectors of F₂³ never contain two disjoint zero-sums. Any two Fano lines meet, a 4-set and a line inside six points meet, and the 5- and 6-subsets have nonzero sums. The test checks this exhaustively.
- For a 6-valued S in the residual pattern, no re-partition into mod-2 blocks reaches 3b−2 blocks either. Each value has odd multiplicity and pairs preserve parity, so every value needs odd coverage by non-pair blocks or unused terms. But the excess-length budget Σ(ℓ_j − 2) + (unused) is at most 2, and two lines meet in a point. So the a = 2 method cannot exclude this pattern.

**Corollary at n = 20 (and n = 28; conditional on CLM-0065).**
- Every zero-sumfree 58-term sequence over C20³ has at least six distinct values of odd multiplicity outside 2G, i.e. with an odd coordinate.
- A **6-valued** counterexample must have all six multiplicities odd, all values outside 2G, and mod-2 images forming a Fano plane minus one point.
- A 7-valued counterexample has exactly six such values, with that same image pattern.
- This strengthens the support-≥6 statement (CLM-0359 + CLM-0367) with parity structure, and it holds for all n = 2b with D(C_b³) known.

**Exact tests (T5).** 900 random 6- and 7-valued sequences of length 3n−2 (n = 4..14) were generated, one fifth of them forced into the residual pattern.
- Outside the residual case, the procedure always produced a zero-sum, verified by both checkers. The 34 residual instances were reported as residual, as expected.
- The Fano-complement fact was checked exhaustively.

## 5. Odd n: where the proof fails

For a ≥ 3 the leftover can be large. With five values, R ≤ 5(a−1), so δ ≤ ⌊(R+2)/a⌋ − 2 ≤ 2.
- δ = 1 is closed by the 5-valued bound in C_a³: CLM-0142/0365 for a = 3, 4, 5.
- δ = 2 (R ≥ 4a−2) needs the finite lemma **TWO(a)**: every sequence over C_a³ with ≤ 5 distinct values and length ≥ 4a−2 has two disjoint nonempty zero-sums.
  - Hand reductions (a coincident image gives a length-≤a zero-sum; fewer than five values cannot reach length 4a−2; monotonicity in r) reduce it to five distinct nonzero values with multiplicities r_i ≤ ord−1 and Σ(a−1−r_i) ≤ a−3.
  - For a = 3 all five 5-subsets were enumerated. For a = 4, 5 the GL₃-normalised families were enumerated: three values forming a basis mapped to e₁, e₂, e₃, plus the non-generating cases.

**CLM-0373 (COMPUTED_EXACT).** TWO(a) is **false** for a = 3, 4, 5. Two independently implemented algorithms (relation-box enumeration; pair dynamic programme) agree instance by instance, with identical decision-stream SHA-256:

| a | instances | failures |
| --- | --- | --- |
| 3 | 65,780 | 5,616 |
| 4 | 271,560 | 432 |
| 5 | 337,260 | 7,188 |

An example for a = 3 is e₃, e₂, e₂+e₃, e₁, e₁+e₂+2e₃, each twice.

**Borrowing does not rescue the method at n = 15.** Re-partitioning all blocks optimally still falls short (T4: exact maximum packing, cross-checked by a second recursion):
- a = 3, b = 5: images (e₃, e₂, e₂+e₃, e₁, e₁+e₂+2e₃), α = (2, 2, 11, 14, 14), |S| = 43. The maximum number of disjoint mod-3 blocks is 12, and D(C5³) = 13 are needed.
- a = 5, b = 3: images (e₁, e₂, e₃, e₂+e₃, e₁+e₂+2e₃), α = (4, 3, 9, 14, 13). The maximum is 6, and D(C3³) = 7 are needed.

So **no argument of the form "pack blocks with sums in aG, then apply D(C_b³)" proves the 5-value bound at n = 15**. The same value pattern obstructs both factorizations. These are images only; CLM-0366 (computation) independently says no zero-sumfree 43-term 5-valued S exists over C15³.
- **Exact location of the gap:** an odd-n proof must use how the block sums in aG are distributed. Here these are the values o_i·g_i together with ≤ 2 extra sums, a ≤ 7-valued sequence in C_b³. It cannot rest on their number alone.
- A natural next lemma is a **"7-values" bound in C_b³ for prime b**, or a direct polynomial argument.

## 6. Guidance from the computed data

- CLM-0365..0367 found the support-≤5 maximum 3n−3 at every computed n. CLM-0370/0371 now explain this for n ∈ {4, 6, 10, 12, 20} by proof. The other computed n are 2, 3, 5, 7, which are primes with D known (CLM-0142), and 15. So **n = 15 is the single computed case not explained by a proof**.
- The S110 optimum-value sets ({26, 34, 42} at n = 15; {33, 36, 39, 45, 48, 57} at n = 20) are recorded but not explained. No lemma is claimed from them.

## 7. Status

| r+2 bound for r = 3 | status |
| --- | --- |
| n prime power, 2p^k, 6, 3·2^k (D known) | implied by the source-stated D |
| n = 4p^k, p odd (20, 28, 44, 52, …) | **CLM-0371** (proof, conditional on source-stated D(C_b³)) |
| n = 15 | CLM-0366 only (computation) |
| odd composite n (21, 33, 35, …), n = 30 | **OPEN**; the block method provably cannot close n = 15 (CLM-0373) |

- New claims: CLM-0368..0373. Claims 367 → 373.
- There is no SAT20/SAT15 or D-value statement, and the frontier is unchanged.
- The search-reopen condition is **not met**. CLM-0372 is a structural reason for a possible support-6 parity-restricted family at n = 20, but any campaign needs an explicit owner decision and full pre-registration.
