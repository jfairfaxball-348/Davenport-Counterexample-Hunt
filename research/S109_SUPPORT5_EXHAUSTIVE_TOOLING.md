# S109 — Support-5 exhaustive tooling, gate and pre-registration (17 October 2026)

Priority: **SATURATION_FALLBACK**, with the **owner-authorised** support-5 exhaustive track (authorisation 2026-10-17, PR #114: "Yes allow it").

**Family.** Zero-sumfree sequences over C_n³ with **at most five distinct values**, n ∈ {15, 20}.

**Question.** Does such a sequence of length ≥ 3n−2 exist?
- By CLM-0359, such a sequence would have exactly 5 distinct values.
- A negative answer would exclude **only this family**. It would never settle SAT20/SAT15.

All proofs are elementary INTERNAL SAME_EXECUTOR hand proofs; no novelty is claimed. Notation follows S108: values a_1..a_5, multiplicities α_i, relation module K = {ρ ∈ (Z/n)^5 : Σ ρ_i a_i = 0}, and ⟨x⟩ ∈ [0, n−1]. By CLM-0358, S is zero-sumfree iff every nonzero ρ ∈ K has some ⟨ρ_i⟩ > α_i. Write ESC(K, α) for this condition, and OPT(K) for the maximum of Σα over α ∈ [0, n−1]^5 with ESC(K, α).

## 1. Proved reductions

**CLM-0361 (PROGRAMME_PROVED) — reduction to generating labelled values.**
- **Statement.** For every labelled list (a_1..a_5) over C_n³ there is a labelled list (b_1..b_5) generating C_n³ whose relation module K′ satisfies K′ ⊆ K. Consequently:
  - the maximum length of a zero-sumfree sequence over C_n³ with at most 5 distinct values equals max OPT(K) over relation modules K of *generating* labelled 5-lists;
  - these K are exactly the **free rank-2 direct summands** of (Z/n)^5.

*Proof.*
- **Setting up.** Let φ: (Z/n)^5 → (Z/n)^3 be φ(x) = Σ x_i a_i, with K = ker φ.
- **Localising.** By CRT it suffices to work over Z/q for each prime power q ∥ n. Z/q is a local principal ideal ring, so φ has a Smith normal form φ = U·[D | 0]·W with U ∈ GL₃, W ∈ GL₅ and D = diag(d_1,d_2,d_3).
- **The refinement.** Put ψ = [I₃ | 0]·W. Then ψ is surjective, and φ = U·D·ψ, so ker ψ ⊆ ker φ. Glue the local ψ's by CRT, and let b_i = ψ(e_i).
- **Monotonicity.** ESC is monotone: if K′ ⊆ K, then ESC(K, α) ⇒ ESC(K′, α). So OPT can only grow.
- **Labelled lists versus multisets.** A labelled list with multiplicities α is zero-sumfree iff the multiset it defines is zero-sumfree: both have the same family of subsequences. So merged or zero values cause no issue, and the maximum over labelled 5-lists equals the maximum over sequences with ≤ 5 distinct values.
- **Which K occur.** The kernel of a surjection (Z/n)^5 → (Z/n)^3 is a free rank-2 summand, because the sequence splits. Conversely, every free rank-2 summand K has (Z/n)^5/K ≅ (Z/n)^3 and so is such a kernel. ∎

**CLM-0362 (PROGRAMME_PROVED) — CRT decomposition.**
- A subgroup K ⊆ (Z/n)^5 is a free rank-2 summand iff K = ∏_q K_q, with each K_q ⊆ (Z/q)^5 a free rank-2 summand.
- The residue ⟨ρ_i⟩ mod n of ρ ∈ K is the CRT combination of its components.
- So K is enumerated as the product of component enumerations. ∎ (Standard: (Z/n)^5 ≅ ∏ (Z/q)^5, and freeness and summand-ness are componentwise.)

**CLM-0363 (PROGRAMME_PROVED) — local graph form and count.** Let q = p^k.
- **Graph form.** A subgroup K_q ⊆ (Z/q)^5 is a free rank-2 summand iff it has a 2×5 generator matrix B such that some 2×2 minor B_{(i,j)} is a unit mod p. Then K_q is the graph {ρ : ρ_{others} = L·(ρ_i, ρ_j)} of a unique L ∈ M_{3×2}(Z/q) over the pair (i, j).
- **Count.** The number of such K_q is p^{6(k−1)}·[5 choose 2]_p, the Gaussian binomial.

*Proof.*
- **Graph form.** B extends to a basis of (Z/q)^5 iff B mod p has rank 2 (Nakayama over the local ring), iff some 2×2 minor is a unit mod p. Multiplying B on the left by the inverse of that minor gives the graph form over (i, j), and L is unique for a fixed pair.
- **Count.** Reduction mod p maps the free rank-2 summands onto the 2-dimensional subspaces of F_p^5. The fibre over each subspace consists of the graphs of the lifts of a fixed 3×2 matrix, so it has size (p^{k−1})^6.
- **Tool check.** Both tools reproduce the count exactly: 155 (q=2), 1210 (q=3), 9920 (q=4), 20306 (q=5), 140050 (q=7). ∎

**CLM-0364 (PROGRAMME_PROVED) — S₅ symmetry and representative enumeration.**
- **Invariance.** For σ ∈ S₅, ESC(σK, σα) ⟺ ESC(K, α), so OPT(σK) = OPT(K).
- **Representatives.** If R is a set of S₅-orbit representatives of free rank-2 summands of (Z/q₀)^5, then every free rank-2 summand of (Z/n)^5 is S₅-equivalent to one whose q₀-component lies in R.
- **Consequence.** Enumerating R × ∏_{q≠q₀}{all K_q} visits at least one member of every S₅-orbit. Algorithm A takes q₀ = the smallest prime power and algorithm B the largest.

*Proof.* Permuting coordinates permutes the box constraints and preserves Σα. Given K, choose σ with σ(K_{q₀}) ∈ R; the other components of σK are free rank-2 summands, which are all enumerated. ∎

**Optimisation exactness.**
- **Algorithm A** uses branch and bound on upper bounds u, starting from u = (n−1,…).
  - If no nonzero ρ has v(ρ) ≤ u, then α = u is feasible and optimal below u.
  - Otherwise, take a violated ρ. Every feasible α ≤ u has some i with α_i ≤ v_i(ρ) − 1 and v_i(ρ) ≥ 1, so the branches over such i cover the feasible set.
  - Pruning at Σu ≤ best is safe.
- **Algorithm B** uses the identity: α is feasible iff α_5 ≤ F(α_1..α_4) − 1, where F(a) = min{v_5(ρ) : ρ ≠ 0, v_{1..4}(ρ) ≤ a}.
  - F is computed exactly by scattering v_5 at index v_{1..4} and taking prefix minima along the four axes.
  - It then maximises a_1+…+a_4 + min(n−1, F(a)−1) over the n⁴ grid, excluding points with F(a) = 0.

**Completeness class: EXHAUSTIVE for the support-≤5 family.** If both algorithms report max OPT < 3n−2 over their complete enumerations, no zero-sumfree sequence over C_n³ with ≤ 5 distinct values has length ≥ 3n−2.

## 2. Two independent implementations

They share no code; they import only numpy and the standard library.

| | Algorithm A (`tools/zsf/support5_a.py`) | Algorithm B (`tools/zsf/support5_b.py`) |
|---|---|---|
| components | graph over the lexicographically first unit-minor pair (no deduplication needed) | kernels of [I₃ \| X] with any pivot 3-set, deduplicated by element-set dictionary |
| S₅ representatives | of the FIRST prime-power component | of the LAST prime-power component |
| CRT | accumulate coefficients Q·Q⁻¹ mod q | same formula, separate code |
| optimum | branch and bound on upper bounds | dense prefix-minimum DP over the n⁴ grid |

Both use the same canonical-key *definition* (the minimum over S₅ of the sorted base-n encodings of the elements), each with its own code, so that orbit sets can be compared by hash. Both support `--shard k --nshards N` (index mod N) and a JSONL checkpoint that logs every K with OPT ≥ the report threshold, progress every 20,000 evaluations, and an end record.

## 3. Pre-flight on settled groups (results in `sessions/S109/PREFLIGHT_SUMMARY.json`)

The pre-flight runs only on n with known D(C_n³) = 3n−2:
- n = 2, 3, 5, 7: primes, CLM-0142, PROGRAMME_PROVED;
- n = 4: a 2-group, SOURCE_STATED;
- n = 6, 10, 12: SOURCE_STATED (CLM-0064/0065/0066).

The expected max OPT is ≤ 3n−3. Every value in the result file was produced by the committed code.

**Results (both algorithms, final code; SHA-256 A `41d37aa63767`, B `f2d06fe1db89`):**

| n | components | A reps / B reps | A pairs / B pairs | max length A / B | orbit sets |
|---|---|---|---|---|---|
| 2 | 155 | 10 / 10 | 10 / 10 | 3 / 3 | 10 orbits, hashes equal |
| 3 | 1210 | 39 / 39 | 39 / 39 | 6 / 6 | 39, equal |
| 4 | 9920 | 205 / 205 | 205 / 205 | 9 / 9 | 205, equal |
| 5 | 20306 | 289 / 289 | 289 / 289 | 12 / 12 | 289, equal |
| 6 | 155 × 1210 | 10 / 39 | 12100 / 6045 | 15 / 15 | 2368, equal |
| 7 | 140050 | 1538 / 1538 | 1538 / 1538 | 18 / 18 | 1538, equal |
| 10 | 155 × 20306 | 10 / 289 | 203060 / 44795 | 27 / 27 | threshold 28: 0 / 0; optimum-value sets {19, 23, 27} agree |
| 12 | 9920 × 1210 | 205 / 39 | 248050 / 386880 | 33 / 33 | threshold 34: 0 / 0; optimum-value sets {21, 22, 23, 27, 28, 33} agree |

**What this shows:**
- At every settled n tested, the maximum length of a zero-sumfree sequence with at most 5 distinct values is exactly 3n−3, consistent with D(C_n³) = 3n−2. This is recorded as CLM-0365, COMPUTED_EXACT, with two algorithms.
- The full orbit sets agree for n ≤ 7, including the two-prime CRT path at n = 6.
- The n = 10, 12 runs use the campaign mode: sharded, with a threshold and checkpoints.

## 4. Cost estimate for n = 15, 20 (from settled timings only; no n = 15/20 enumeration was run)

The orbit-representative counts come from the settled runs: q=3: 39, q=4: 205, q=5: 289.

**Exact pair counts** (pinned in the pre-registrations):
- **n = 15:** A 39 × 20306 = 791,934; B 1210 × 289 = 349,690.
- **n = 20:** A 205 × 20306 = 4,162,730; B 9920 × 289 = 2,866,880.

**Measured per-pair cost:**
- A: 12.4 ms (n=10) and 7.7 ms (n=12).
- B: 1.1 ms (n=12). B's cost is dominated by its n⁴ grid.

**Extrapolation.** A is scaled by |K| from the worse n=10 rate; B is scaled by n⁴ from n=12.
- **A:** about 28 ms per pair at n=15 and about 50 ms at n=20.
- **B:** about 2.7 ms at n=15 and about 8.5 ms at n=20.
- **CPU time:** n15 A ≈ 6 CPU-h, n15 B ≈ 0.3 CPU-h, n20 A ≈ 58 CPU-h (worst case), n20 B ≈ 7 CPU-h. In total ≈ 72 CPU-h, or about 5–6 hours of wall time on 14 processes.

These are estimates, not rates, so the budget carries a ×2 margin through the per-shard walltime cap.

## 5. Phase-2 gate extension and pre-registration

**Phase-2 SCOPED PASS extension.** It covers support-≤5 exhaustive tooling A/B: proved reductions CLM-0361..0364, the settled-group pre-flight CLM-0365, and two independent implementations.

**CAM-0006 (n = 15, L = 43) and CAM-0007 (n = 20, L = 58)** are PREREGISTERED, not run. Details are in `campaigns/CAM-000{6,7}/PREREGISTRATION.json`.
- **Completeness:** EXHAUSTIVE, for the support-≤5 family only.
- **Activation:** S110 at the earliest.
- **Negative outcome** (both algorithms complete, max OPT ≤ 3n−3): "no zero-sumfree sequence over C_n³ with at most five distinct values has length 3n−2". This is not SAT20/SAT15.
- **Positive outcome:** a CANDIDATE only.
