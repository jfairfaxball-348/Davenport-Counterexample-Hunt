# S112 — Multi-route block sieve: n = 15 support-5 by proof, n = 20 support ≥ 7 (18 October 2026)

Priority: **SATURATION_FALLBACK** (fallback session 7). Owner steering of 18 October 2026 is still in force: generalise. Targets, both OPEN: **SAT20** (D(C20³) = 58) and **SAT15** (D(C15³) = 43).

All proofs are elementary INTERNAL SAME_EXECUTOR hand proofs, and **no novelty is claimed**. The only computation is arithmetic over multiplicity patterns, plus tests on settled small groups. **No C15³ or C20³ sequence is computed.**

## 1. Idea

S111 used one factorization n = ab at a time (CLM-0369). Each "route" a fails only on a narrow arithmetic set of multiplicity vectors. Different routes fail on different sets. **Requiring every route to fail at once** is often arithmetically impossible.

## 2. Routes and the sieve criterion

**CLM-0374 (PROGRAMME_PROVED, FOUNDATION).** Let S be a sequence over G = C_n³ with |S| = 3n−2, distinct values g_i of orders d_i and multiplicities α_i. Call a prime power a | n a *route* if D(C_a³) = 3a−2 and D(C_b³) = 3b−2 for b = n/a. Let o_i = a / gcd(a, n/d_i), the order of g_i + aG. Define

  t₀ = Σ_{o_i=1} α_i + Σ_{o_i>1} ⌊α_i/o_i⌋,  R = Σ_{o_i>1} (α_i mod o_i).

If t₀ + ν_lb(R) ≥ 3b−2, then S has a nonempty zero-sum. Here ν_lb(R) = max{j : D_j(C_a³) ≤ R}, computed with:
- D₁ = 3a−2;
- D₂(C₂³) = 7 (lemma below);
- D₂(C_p³) ≤ 5p−3 for odd primes p (CLM-0143);
- D₂ ≤ 2D₁ in general;
- D_j ≤ D₂ + (j−2)D₁.

*Proof.*
- **Order of the image.** g_i = (n/d_i)u with ord u = n (CLM-0354). The image of u in G/aG ≅ C_a³ has order a, so the image of g_i has order o_i.
- **Blocks.** g_i^{o_i} blocks give t₀ disjoint subsequences with sums in aG; when o_i = 1, each copy is its own block. The leftover has R terms.
- **Leftover zero-sums.** By the definition of D_j, the leftover image contains ν_lb(R) disjoint zero-sums, i.e. subsequences with sums in aG.
- **Conclusion.** Apply CLM-0369(i): D(C_b³) block sums in aG ≅ C_b³ contain a zero-sum.

The bound D_j ≤ D₂ + (j−2)D₁ holds greedily. Any D₁ terms contain a zero-sum of length ≤ D₁. Removing j−2 of them leaves ≥ D₂ terms, which hold two more.

**Lemma (D₂(C₂³) = 7).** Six distinct nonzero vectors of F₂³ have no two disjoint zero-sums (S111, CLM-0372). Any 7 terms do:
- a zero term, plus a zero-sum among the other 6 ≥ 4 terms;
- or a repeated pair, plus the remaining 5 ≥ 4 terms;
- or all 7 nonzero vectors, which split as a Fano line and its complement.

T1 checks all 3,432 multisets of size 7.

**Multiplicity caps used:**
- α_i ≤ d_i − 1;
- order n: α ≤ n−2 (CLM-0350, conditional on CLM-0352);
- even n: order n ≤ n−3 and order n/2 ≤ n/2−2 (CLM-0368, conditional on CLM-0356).

A multiplicity pattern is a multiset of pairs (d_i, α_i) with Σα_i = 3n−2. It **survives** if no route closes it. By CLM-0374, a counterexample with k distinct values needs a surviving pattern with k entries.

## 3. Results of the sieve

**CLM-0375 (COMPUTED_EXACT).** `tools/zsf/route_sieve.py` uses two independent algorithms: a counting knapsack DP over additive route statistics, and recursive multiset enumeration with a separately written closure test. They agree on every count (`sessions/S112/ROUTE_SIEVE.json`). The table lists the number of surviving patterns by k; it is arithmetic only.

| n | routes | k ≤ 4 | k = 5 | k = 6 | k = 7 |
| --- | --- | --- | --- | --- | --- |
| 12 | 2, 3, 4 | 0 | 0 | 0 | 2 |
| **15** | 3, 5 | 0 | **0** | 5 | 85 |
| 18 | 2, 3, 9 | 0 | 0 | 0 | 48 |
| **20** | 2, 4, 5 | 0 | **0** | **0** | 139 |
| **21** | 3, 7 | 0 | **0** | 31 | — |
| 28 | 2, 4, 7 | 0 | 0 | 28 | — |
| 30 | 3, 5 | 0 | 1 | — | — |
| 33 | 3, 11 | 0 | 2 | — | — |
| 35 | 5, 7 | 0 | 2 | — | — |

(For n = 12 and 18, D(C_n³) is already settled, so their rows only test the method.)

**Consequences: CLM-0376 and CLM-0377 (PROGRAMME_PROVED).**
- **n = 15 (CLM-0376, unconditional).** Every zero-sumfree sequence over C15³ with ≤ 5 distinct values has length ≤ 42. The hand proof below uses only CLM-0142 and CLM-0369. This turns the content of CLM-0366 (computation) into a theorem. CLM-0366 itself is **not relabelled**.
- **n = 20 (CLM-0377(i)).** Every zero-sumfree 58-term sequence over C20³ has **at least 7 distinct values**. This is conditional on CLM-0375 and on the cited D-values:
  - CLM-0065: D(C10³) = 28 (SOURCE_STATED);
  - CLM-0039: D(C4³) = 10 (SOURCE_STATED);
  - CLM-0142: D(C5³) = 13;
  - CLM-0143, CLM-0350/0352 and CLM-0368/0356.
- **n = 21 (CLM-0377(ii)).** Every zero-sumfree sequence over C21³ with ≤ 5 distinct values has length ≤ 60. This is conditional on CLM-0375, CLM-0142, CLM-0143 and CLM-0350/0352.

**Hand proof of the n = 15 case (two routes, D₁ only).** Let S have ≤ 5 values and |S| = 43.
- **When a route fails.** For a prime p | 15, route p has deficit δ ≤ ⌊(R+2)/p⌋ − 2. It closes when R ≤ 4p−3: for δ = 1, the leftover has ≥ 3p−2 = D(C_p³) terms.
- So a failing route needs R ≥ 4p−2 > 4(p−1). This forces five values, all with o_i = p.
- Then R ≡ Σα_i = 43 ≡ −2 (mod p). Hence B := Σ_i(p−1−(α_i mod p)) ∈ [0, p−3] satisfies B ≡ −3, so **B = p−3**.
- **Route 3 fails** ⇒ B = 0 ⇒ every α_i ≡ 2 (mod 3).
- **Route 5 fails** ⇒ Σ_i(4 − (α_i mod 5)) = 2.
- **Contradiction.** Put x_i = α_i + 1 ∈ [1, 15]. Then 3 | x_i, so x_i ∈ {3, 6, 9, 12, 15}, and Σx_i = 48. The route-5 condition reads Σ_i((−x_i) mod 5) = 2, which allows only x_i ∈ {3, 9, 15}, with weights 2, 1, 0.
  - Weight 2 forces one 3 and four 15s, a sum of 63.
  - Otherwise it forces two 9s and three 15s, also a sum of 63.
  - Either way the sum is 63 ≠ 48.
- The premises are D(C3³) = 7 and D(C5³) = 13, both CLM-0142. ∎

## 4. The precise residue

**CLM-0378 (COMPUTED_EXACT, part of the sieve output).**
- **n = 15, k = 6:** exactly **5** surviving patterns, and all values have order 15: (2,4,8,8,8,13), (2,8,8,8,8,9), (3,8,8,8,8,8), (4,4,8,8,8,11), (4,7,8,8,8,8).
- **n = 20, k = 7:** 139 surviving patterns.
- These are arithmetic survivors, not candidates. A finer, image-level analysis in C3³ / C5³ (or C2³ / C4³ / C5³, plus the CLM-0372 parity constraint) may close them.

## 5. Exact tests (settled groups only; `sessions/S112/S112_TESTS.json`)

- **T1:** D₂(C₂³) = 7, exhaustive.
- **T2:** constructive soundness. Random 5–7-valued sequences of length 3n−2 over C_n³, n ∈ {6, 10, 12} (301 sequences). For each route the sieve declares closing (651 route runs), the proof's procedure was run. It uses blocks, an exact maximum disjoint packing of the leftover image, and a zero-sum among the block sums in aG.
  - It produced a nonempty zero-sum every time, verified by checkers A and B.

## 6. Status

- New claims CLM-0374..0378. Claims 373 → 378.
- At n = 15 the support-≤5 bound is now a theorem. At n = 20 a counterexample needs ≥ 7 distinct values. At n = 21 it needs ≥ 6.
- **Open:** n = 30, 33, 35 at support 5 (1, 2 and 2 arithmetic survivors), and the residues of §4.
- No SAT20/SAT15 or D-value statement; frontier unchanged.
- **Search-reopen condition: not met.** The residues are explicit finite multiplicity families, but any computation on target groups needs an owner decision.
