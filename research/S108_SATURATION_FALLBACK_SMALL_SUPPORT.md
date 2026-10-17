# S108 — Saturation fallback session 3: small-support bound (17 October 2026)

Priority: **SATURATION_FALLBACK**. Targets, both OPEN:
- **SAT20:** D(C20³) = 58.
- **SAT15:** D(C15³) = 43.

All proofs are elementary INTERNAL SAME_EXECUTOR hand proofs. Lattice and counting arguments of this kind are standard, and **no novelty is claimed**.

## 1. Source frontier for the S107 lever groups

A literature search on 2026-10-17 looked for exact Davenport constants of C4⊕C20⊕C20, C5⊕C20⊕C20, C10⊕C20⊕C20, C3⊕C15⊕C15 and C5⊕C15⊕C15, and of the general families C_m⊕C_n⊕C_n with m > 2.
- **Result:** no exact value was found.
- **Context only:** the SRC-0005 introduction calls rank three "wide open" beyond special families. SRC-0022 (Schmid 2011) gives D(C4²⊕C4n) and D(C6²⊕C6n), which have a different shape. The Zakarczemny bound (SRC-0006) is far from D*.
- **No new records** were created, because nothing was used as a premise.
- Not finding a value is **not** a claim that these groups are open.
- The S107 levers therefore stay conditional.

## 2. Lemmas

Setting: S is a sequence over C_n^r with distinct values a_1,…,a_k and multiplicities α_1,…,α_k. If S is zero-sumfree, then α_i ≤ ord(a_i) − 1 ≤ n − 1. Write ⟨x⟩ ∈ [0, n−1] for the least nonnegative residue of x mod n. Define the **relation module** K = {ρ ∈ (Z/n)^k : Σ ρ_i a_i = 0}.

**CLM-0358 (PROGRAMME_PROVED) — box/kernel criterion.** If all α_i ≤ n−1, then S is zero-sumfree iff no nonzero ρ ∈ K satisfies ⟨ρ_i⟩ ≤ α_i for every i.

*Proof.* A nonempty zero-sum subsequence is a vector x ∈ Z^k, x ≠ 0, with 0 ≤ x_i ≤ α_i and Σ x_i a_i = 0. Then ρ = x mod n lies in K, with ⟨ρ_i⟩ = x_i ≤ α_i, and ρ ≠ 0 because 0 ≤ x_i ≤ n−1. Conversely, such a ρ gives x_i = ⟨ρ_i⟩. ∎

**CLM-0359 (PROGRAMME_PROVED) — counting bound.** If S is zero-sumfree, then

  |S| ≤ k(n−1) − n + n/|K|.

Since K is the kernel of (Z/n)^k → ⟨a_1,…,a_k⟩ ≤ C_n^r, we have |K| ≥ n^{k−r}. **Hence if |supp(S)| ≤ r+1, then |S| ≤ r(n−1).** In particular, every zero-sumfree sequence over C_n³ with at most 4 distinct values has length ≤ 3n−3.

*Proof.*
- **Every nonzero ρ escapes the box.** By CLM-0358, every nonzero ρ ∈ K has some coordinate i with ⟨ρ_i⟩ > α_i.
- **Counting escapes in one coordinate.** Fix i. The projection K → Z/n, ρ ↦ ρ_i, has image d_iZ/nZ for some d_i | n, with fibres of size |K|d_i/n. The multiples of d_i in [0, n−1] that exceed α_i number n/d_i − 1 − ⌊α_i/d_i⌋. So the number of ρ ∈ K with ⟨ρ_i⟩ > α_i is (|K|/n)(n − d_i − d_i⌊α_i/d_i⌋). Since d_i⌊α_i/d_i⌋ ≥ α_i − d_i + 1, this is at most (|K|/n)(n − 1 − α_i).
- **Summing.** Over i: |K| − 1 ≤ (|K|/n)(k(n−1) − |S|), which rearranges to the bound.
- **The support case.** For k = r+1, |K| ≥ n, so |S| ≤ (r+1)(n−1) − n + 1 = r(n−1). For k ≤ r the bound α_i ≤ n−1 already gives it. ∎

**CLM-0360 (PROGRAMME_PROVED) — relation bound.** If S is zero-sumfree and ρ ∈ K has order n, then

  Σ_{i : ρ_i ≠ 0} (n − 1 − α_i) ≥ n − 1.

*Proof.* Apply the counting of CLM-0359 to the cyclic subgroup ⟨ρ⟩ ⊆ K, which has order n. Each tρ with 1 ≤ t ≤ n−1 is nonzero, so it escapes in some coordinate. Coordinates with ρ_i = 0 never escape. Each coordinate i with ρ_i ≠ 0 escapes for at most n−1−α_i values of t. ∎

**Example.** If b ∈ ⟨a⟩ with a of order n, then b = ca and ρ = (c, −1) has order n, so α_a + α_b ≤ n−1. This is the familiar cyclic-subgroup bound.

## 3. Consequences at the targets

**Corollary (part of CLM-0359).** A zero-sumfree (3n−2)-term sequence over C_n³ has at least **5 distinct values**. This holds for every n, and in particular at n = 15 and n = 20.
- This generalises CLM-0153 (basis plus one extra value).
- It strengthens the S107 count at n = 20 (≥ 4 distinct values from the multiplicity caps).
- It is unconditional: no literature premise is used.

**Support exactly 5 becomes a finite lattice problem.**
- A (3n−2)-term counterexample with 5 distinct values that generate C_n³ has K ≅ (Z/n)², since the kernel of a surjection (Z/n)^5 → (Z/n)^3 is free of rank 2. If the values generate a proper subgroup, K is larger.
- By CLM-0358, such a counterexample exists iff there is a rank-2 free summand K ⊂ (Z/n)^5 that is the relation module of five distinct values, together with multiplicities α ∈ [0, n−1]^5 summing to 3n−2, such that every nonzero ρ ∈ K escapes the box.
- The counting in CLM-0359 gives only |S| ≤ 4n − 5 here (|K| = n²), so it does not exclude this case. CLM-0360 applies to every order-n ρ ∈ K.
- This is an exactly specified finite family. Deciding it would need either a further proof or a gated, pre-registered EXHAUSTIVE computation with certificates (§5).

## 4. Exact tests (`tools/zsf/test_small_support.py`, output `sessions/S108/SMALL_SUPPORT_TESTS.json`; n ≤ 10 only)

These are independent of the proofs.
- **Random supports:** 1,040 random supports in C_n² (n = 2..10) and C_n³ (n = 2..6), mostly of size r+1. For each, the maximum zero-sumfree length was found by brute force over all multiplicity vectors.
  - CLM-0359 held in every case: the maximum is ≤ r(n−1), and ≤ k(n−1) − n + n/|K|.
  - Every maximiser was re-checked by checkers A and B.
- **CLM-0358:** 5,200 random multiplicity vectors agree with checkers A/B.
- **CLM-0360:** 7,288 relation checks hold on zero-sumfree instances.
- **Exhaustive:** over every 4-value support in C2³ and C3³, the maximum length is exactly 3 = 3·1 and 6 = 3·2 respectively.

There was no n = 15/20 computation.

## 5. Status and search-reopen assessment

- New PROGRAMME_PROVED: CLM-0358, CLM-0359, CLM-0360. They are unconditional.
- Any counterexample at n = 15 or 20 has ≥ 5 distinct values.
- The fallback targets remain OPEN.

**Search-reopen assessment: not met by S108 alone.**
- The support-5 case is now a precisely specified finite structured family, which is the kind of reduction the reopen condition contemplates.
- But it covers only one support size, not SAT20.
- Running it on n = 20 would also be a target-group computation, and a negative outcome would need certificate-grade completeness (AGENTS rule 6).
- Whether to pre-register a support-5 EXHAUSTIVE campaign is an **owner decision**. S108 neither pre-registers nor runs it. S109 may design the tooling and pre-flight it on settled groups only.

Fallback sessions completed: 3.
