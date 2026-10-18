# Consolidation review: what we know (S111, updated S112; 18 October 2026)

This is the **single entry point** to the programme's results. It classifies every result from S103–S112 (CLM-0345..0378), plus the earlier results worth carrying forward, into three groups: **ALL-n**, **CONDITIONAL-on-family** and **n-SPECIFIC**. For each result it states what the result depends on and its scope. Statuses are those of `catalogue/claims.json`; this review upgrades nothing.

**Targets (OPEN):** SAT20 (D(C20³) = 58) and SAT15 (D(C15³) = 43). The open rows of the frontier at n ≤ 30 are n = 15, 20, 21, 28, 30.

## 0. One-paragraph summary

A zero-sumfree sequence of length 3n−2 over C_n³ (a counterexample) is constrained as follows.
- **Every n:** it needs ≥ 5 distinct values (proof), and order-n multiplicities ≤ n−2 (proof plus the source-stated rank-two D).
- **Even n:** order-n multiplicities ≤ n−3 and order-n/2 multiplicities ≤ n/2−2 (proof plus a source-stated D(C2⊕C_n⊕C_n)).
- **n = 2b with D(C_b³) known** (this includes n = 20, 28 and 4p^k):
  - ≥ 6 distinct values, by proof;
  - indeed ≥ 6 distinct values of odd multiplicity outside 2G;
  - with exactly six such values, their mod-2 images form a Fano plane minus a point.
- **n = 20 (S112):** ≥ **7** distinct values, by proof from the multi-route sieve (CLM-0377(i)).
- **n = 15:** ≥ 6 distinct values, now **by an unconditional hand proof** (CLM-0376, two block routes 3 and 5), as well as by computation (CLM-0366). A single block route cannot give this (CLM-0373); two routes together do.
- **n = 21:** ≥ 6 distinct values (CLM-0377(ii)).

Nothing proves or refutes SAT15/SAT20.

## 1. ALL-n results

These hold for every n, and where stated for any rank r or any finite abelian group. All are PROGRAMME_PROVED unless marked otherwise.

| claim | statement (short) | scope | depends on |
| --- | --- | --- | --- |
| CLM-0038 | D(C_n³) ≥ 3n−2 (basis sequence) | all n | hand proof |
| CLM-0345 | prefix criterion; Σ update; saturation equivalence; GL-invariance | any finite abelian G | hand proof |
| CLM-0347 | two-term extension criterion | any G | CLM-0345 |
| CLM-0348 | order-n elements of C_n^r complete to a basis | C_n^r | hand proof (CRT) |
| CLM-0349 | g^{m−1}T zero-sumfree ⇔ image of T in G/⟨g⟩ zero-sumfree | any G | hand proof |
| CLM-0351 | g^{m−2}T criterion (sums in ⟨g⟩ equal g) | any G, ord ≥ 3 | hand proof |
| CLM-0353 | g^{m−j}T criterion (general j) | any G | hand proof |
| CLM-0354 | h of order m is (n/m)u, ord u = n; G/⟨dh⟩ ≅ C_{nd/m}⊕C_n^{r−1} | C_n^r | CLM-0348 |
| CLM-0355 | multiplicity-defect transfer \|S\| ≤ m − d + d(C_{nd/m}⊕C_n⊕C_n) | C_n³, all n | CLM-0353/0354 (to *use* it, a D-value of the smaller group is needed) |
| CLM-0358 | box/kernel criterion over the relation module K | C_n^r | hand proof |
| CLM-0359 | \|S\| ≤ k(n−1) − n + n/\|K\|; **≤ r+1 values ⇒ \|S\| ≤ r(n−1)**; a counterexample needs ≥ 5 values | C_n^r, all n, r | CLM-0358 |
| CLM-0360 | per-relation bound Σ_{ρ_i≠0}(n−1−α_i) ≥ n−1 | C_n^r | CLM-0358 |
| CLM-0361..0364 | support-5 reduction to rank-2 free summands K ⊂ (Z/n)^5; CRT; local counts; S₅ symmetry | all n | hand proofs |
| CLM-0369 | **block-packing lemma** (pack disjoint blocks with sums in aG, apply D(C_b^r)); deficit ≤ ⌊(R − (a−1)(r−1))/a⌋ | C_n^r, n = ab | hand proof |
| CLM-0153 | basis plus one extra value excluded | all n | hand proof; subsumed by CLM-0359 |
| CLM-0374 | **multi-route block criterion** (all prime-power routes a \| n at once; D₂(C₂³) = 7; D_j ≤ D₂ + (j−2)D₁) | C_n³, all n (each route needs its two D-values) | CLM-0354, CLM-0369, CLM-0143 |

## 2. CONDITIONAL-on-family results

These hold for every n in a family, given a smaller or different group's Davenport constant (source-stated or programme-proved).

| claim | statement (short) | family | depends on |
| --- | --- | --- | --- |
| CLM-0350 | order-n multiplicity n−1 ⇒ \|S\| ≤ 3n−3; so caps ≤ n−2 | all n | CLM-0352 (SOURCE_STATED rank-two D, known for all n) |
| CLM-0368 | **even-n caps:** order n ≤ n−3, order n/2 ≤ n/2−2; bounds 3n−3 and 5n/2−2 | all even n ≥ 4 | CLM-0355 + CLM-0356 (SOURCE_STATED, SRC-0005 Thm 2.7) + CLM-0352 |
| CLM-0370 | **r+2 values at even n:** zero-sumfree with ≤ r+2 values over C_{2b}^r has length ≤ r(2b−1) | n = 2b, any r, with D(C_b^r) = D* | CLM-0369 + that D-value |
| CLM-0371 | r = 3 case of CLM-0370: 5-valued bound 3n−3 | n = 2b with D(C_b³) known: **n = 4p^k (20, 28, 44, …)**, plus already-settled n | CLM-0370 + CLM-0142 / 0039 / 0064 / 0065 / 0066 |
| CLM-0372 | **even-n parity structure:** ≥ 6 values of odd multiplicity outside 2G; exactly six ⇒ images F₂³∖{0,P}; never seven | n = 2b with D(C_b³) known (20, 28, …) | CLM-0369 + that D-value |
| CLM-0142 | D(C_p³) = 3p−2 | primes p (unconditional) | Chevalley–Warning, hand proof |
| CLM-0143, 0148, 0149 | D₂(C_p³) ≤ 5p−3; η and D_k bounds for p ≥ 7 | primes | hand proofs, some with source inputs (see claims) |
| CLM-0150 | the bare subgroup inequality overshoots 3pm−2 by 1–2 at n = 15, 20, 21, 28, 30 | composite n | source-stated D_k values |
| SOURCE_STATED inputs | CLM-0039 (Olson, p-groups), CLM-0352 (rank two), CLM-0356 (C2⊕C2m⊕C2mn), CLM-0064 (C6³), CLM-0065 (C_{2p^a}³), CLM-0066 (C_{3·2^a}³) | as stated | literature statements, not programme proofs |

## 3. n-SPECIFIC results

| claim / block | content | n | depends on |
| --- | --- | --- | --- |
| CLM-0346 | standard sequences zero-sumfree and saturating (tooling validation) | 15, 20 | two checkers |
| CLM-0357 | caps 17 / 8 at n = 20 | 20 | now the n = 20 case of CLM-0368 |
| CLM-0365 | support-≤5 maximum 3n−3 (COMPUTED_EXACT) | 2–7, 10, 12 | two exhaustive codes + CLM-0358/0361..0364 |
| CLM-0366 | support-≤5 maximum 42 (COMPUTED_EXACT) | 15 | CAM-0006 + same reductions |
| CLM-0367 | support-≤5 maximum 57 (COMPUTED_EXACT) | 20 | CAM-0007 + same reductions; **also implied by CLM-0371**, an independent proof route via CLM-0065 |
| CLM-0373 | TWO(a) false for a = 3, 4, 5; a *single* route falls short at n = 15 for a = 3 and a = 5 (COMPUTED_EXACT) | finite C_a³; 15 | two algorithms; exact packing DP |
| CLM-0375 | route-sieve outcomes (COMPUTED_EXACT, arithmetic only) | 12, 15, 18, 20, 21, 28, 30, 33, 35 | two algorithms |
| CLM-0376 | **support-≤5 bound at n = 15 (hand proof, unconditional)** | 15 | CLM-0142, CLM-0369/0374 |
| CLM-0377 | **n = 20: ≥ 7 distinct values**; n = 21: support-≤5 bound | 20, 21 | CLM-0375 + CLM-0065/0039/0142/0143/0350/0368 |
| CLM-0378 | residue: 5 six-valued patterns at n = 15 (all order 15); 139 seven-valued patterns at n = 20 (COMPUTED_EXACT) | 15, 20 | two algorithms |
| S104/S105 rounds (CAM-0002..0005) | heuristic search, best 42 / 57; **no proof content** | 15, 20 | HEURISTIC budgets |
| S060–S102 axial programme | conditional local structure of hypothetical extremal C20³ configurations (axial q-groups, Fano/colour collisions, five-flat sub-cases) | 20 (with C10³/C5³ quotients) | source-conditional hand proofs; **not re-audited in S111**; none excludes a counterexample; not carried forward as a lever |
| S025–S043 indexed/extraction programme | odd-prime indexed block structure; n15/n20 quotient profiles | primes ≥ 7; 15, 20 | partly source-conditional; local necessary conditions only |

**Not used anywhere:** the 37 INHERITED_UNVERIFIED claims (CLM-0001..0037) stay quarantined.

## 4. What is known about the "r+2 values" conjecture

**Conjecture:** every zero-sumfree sequence over C_n^r with ≤ r+2 distinct values has length ≤ r(n−1).
- **r = 1, 2:** true (D(C_n), D(C_n²)).
- **r = 3:**
  - Proved for n = 2b with D(C_b³) known (CLM-0371); this includes n = 20 and 28.
  - Implied by the known D for prime powers, 2p^k, 6 and 3·2^k.
  - Proved at n = 15 (CLM-0376, unconditional) and n = 21 (CLM-0377(ii)) by the multi-route sieve; also computed at n = 15 (CLM-0366).
  - **Open** for n = 30, 33, 35 (1, 2 and 2 arithmetic survivors) and for other odd composite n not yet sieved.
- **General r:** proved for n = 2p^k (CLM-0370 + CLM-0039).

## 5. Where the frontier of ideas is

1. **n = 20:** the 6-valued case is closed (CLM-0377). The 7-valued residue is 139 multiplicity patterns (CLM-0378). The next step is image-level analysis in C₂³ / C₄³ / C₅³, combined with the parity structure CLM-0372, and sharper small-group constants D₂, D₃.
2. **n = 15:** the 6-valued residue is five patterns, all values of order 15 (CLM-0378). These can be attacked by exact image analysis in C₃³ and C₅³, which are small groups.
3. Any computation on target groups needs an owner decision and pre-registration.
4. **Lean certification:** deferred by owner steering.

Detailed proofs: [S112 note](S112_MULTI_ROUTE_SIEVE.md), [S111 note](S111_R_PLUS_TWO_AND_EVEN_CAPS.md). Earlier notes: S106–S110 in this directory.
