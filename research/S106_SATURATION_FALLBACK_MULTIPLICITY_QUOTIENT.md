# S106 — Saturation fallback session 1: multiplicity–quotient lemmas (17 October 2026)

Priority: **SATURATION_FALLBACK** (switched in S105). Targets, both OPEN:
- **SAT20:** every zero-sumfree 57-term sequence in C20³ has Σ = G, equivalently D(C20³) = 58.
- **SAT15:** the analogue with 42 terms in C15³, equivalently D(C15³) = 43.

Both are instances of the rank-three conjecture CLM-0002 (INHERITED_UNVERIFIED), via CLM-0345(c) and CLM-0038. No separate claim ID is created for them, to avoid duplicating CLM-0002.

All proofs below are elementary, INTERNAL SAME_EXECUTOR hand proofs. The quotient technique is classical in spirit; Gao 2000 (SRC-0004, METADATA_ONLY) studies "zerofree sequences in groups with rank two" to settle special rank-three groups. **No novelty is claimed.**

Notation:
- G is a finite abelian group, and S is an indexed sequence over G.
- v_g(S) is the multiplicity of g in S, and σ(T) is the sum of T.
- Sequences of the form g^j T are multisets with j extra copies of g.

## 1. Source frontier (S106 check)

- **SRC-0030** (constants table entry 53a, page dated 2026-09-26) was re-inspected. Rank three is still recorded as open, with 3n−2 ≤ D(C_n³) ≤ 4n−P(n)−2. No exact value is recorded for n = 15 or 20, so the frontier is unchanged.
- **SRC-0033 (new, STATEMENT_INSPECTED).** D. J. Grynkiewicz, *A Multiplicative Property for Zero-Sums II*, Electron. J. Combin. 29(3) (2022) P3.12, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i3p12/pdf. The inspected text states that D(C_n ⊕ C_mn) = mn + n − 1 and η(C_n ⊕ C_mn) = mn + 2n − 2, citing Olson, van Emde Boas–Kruyswijk and Geroldinger–Halter-Koch Theorem 5.8.3.
- **SRC-0034 (new, STATEMENT_INSPECTED).** A. Geroldinger, W. Yang, *On a classical zero-sum invariant*, arXiv:2608.19090, https://arxiv.org/pdf/2608.19090. The inspected text states that d*(G) ≤ d(G) with "Equality holds for p-groups and for groups with rank r ≤ 2."
- **CLM-0352 (SOURCE_STATED; SRC-0033, SRC-0034; original pointer SRC-0027).** D(C_n ⊕ C_n) = 2n − 1, so every zero-sumfree sequence over C_n² has length at most 2n − 2. Neither the original Olson nor the van Emde Boas–Kruyswijk rank-two proof was re-inspected in S106.

## 2. Lemmas

**CLM-0348 (PROGRAMME_PROVED) — basis completion.** Let G = (Z/n)^r with r ≥ 1 and n ≥ 2. Every g ∈ G of order n is the first column of a matrix in GL_r(Z/n). Hence G = ⟨g⟩ ⊕ K with K ≅ (Z/n)^{r−1}, and G/⟨g⟩ ≅ (Z/n)^{r−1}.

*Proof.* Write g = (a_1,…,a_r). Then g has order n iff gcd(a_1,…,a_r,n) = 1, i.e. for every prime p | n some a_i is a unit mod p.
- Let n = ∏ q_p with q_p = p^{k_p}. For each p, fix such an index i(p). Let M_p be the matrix over Z/q_p whose first column is g and whose remaining columns are the standard basis vectors e_j, j ≠ i(p).
- Expanding along the rows j ≠ i(p) gives det M_p = ±a_{i(p)}. This is a unit in the local ring Z/q_p.
- By the CRT, Z/n ≅ ∏ Z/q_p, so there is a unique M over Z/n reducing to every M_p. Its determinant is a unit modulo every q_p, hence modulo n, so M ∈ GL_r(Z/n).
- Then G = M(⟨e_1⟩ ⊕ ⟨e_2,…,e_r⟩) = ⟨g⟩ ⊕ K. ∎

**CLM-0349 (PROGRAMME_PROVED) — quotient equivalence.** Let g ∈ G have order m ≥ 1, let T be any sequence over G, and let π: G → G/⟨g⟩. Then g^{m−1}T is zero-sumfree iff π(T) is zero-sumfree, i.e. iff no nonempty subsequence of T has sum in ⟨g⟩.

*Proof.*
- (⇐) Let U = g^j T′ be a nonempty zero-sum subsequence, with 0 ≤ j ≤ m−1 copies from the g^{m−1} block. Then σ(T′) = −jg ∈ ⟨g⟩, so T′ is empty by hypothesis. Then jg = 0 with 1 ≤ j ≤ m−1, which contradicts ord g = m.
- (⇒) Let T′ be nonempty with σ(T′) = kg, 0 ≤ k ≤ m−1. If k = 0, T′ is a zero-sum. If k ≥ 1, then T′ together with m−k ∈ [1, m−1] copies of g from the block has sum mg = 0. ∎

**CLM-0350 (PROGRAMME_PROVED, conditional on SOURCE_STATED CLM-0352) — multiplicity cap for long sequences.** Let n ≥ 2 and let S be zero-sumfree over C_n³.
- If v_g(S) = n − 1 for some g of order n, then |S| ≤ 3n − 3.
- Consequently, every zero-sumfree sequence of length 3n − 2 over C_n³ has v_g(S) ≤ n − 2 for every g of order n. Elements of order m < n trivially have v_g(S) ≤ m − 1.
- In particular, a hypothetical zero-sumfree 58-term sequence in C20³ (resp. 43-term sequence in C15³) has every multiplicity at most 18 (resp. 13).

*Proof.* Write S = g^{n−1}T. By CLM-0349, π(T) is zero-sumfree over G/⟨g⟩, which is ≅ C_n² by CLM-0348. CLM-0352 then gives |T| ≤ 2n − 2. ∎

*Equality.* |S| = 3n − 3 with v_g(S) = n − 1 holds iff π(T) is a zero-sumfree sequence of maximal length 2n − 2 in C_n². The structure of those sequences is described in the rank-two inverse literature (Property B and its multiplicative extension). That is not inspected here and is not used.

**CLM-0351 (PROGRAMME_PROVED) — multiplicity m−2 criterion.** Let g have order m ≥ 3 and let T be any sequence over G. Then g^{m−2}T is zero-sumfree iff every nonempty subsequence T′ of T with σ(T′) ∈ ⟨g⟩ has σ(T′) = g exactly.

*Proof.*
- (⇐) Let U = g^j T′ be a nonempty zero-sum, 0 ≤ j ≤ m−2.
  - If T′ is empty, then jg = 0 with 1 ≤ j ≤ m−2, which is impossible.
  - Otherwise σ(T′) = −jg ∈ ⟨g⟩, so σ(T′) = g by hypothesis. Then (j+1)g = 0 with 1 ≤ j+1 ≤ m−1, which is also impossible.
- (⇒) Let σ(T′) = kg with 0 ≤ k ≤ m−1. If k = 0, T′ is a zero-sum. If 2 ≤ k ≤ m−1, adding m−k ∈ [1, m−2] copies of g gives a zero-sum. So k = 1. ∎

**Corollary (part of CLM-0351).** In that situation, no two disjoint nonempty subsequences of T have sums in ⟨g⟩, i.e. π(T) has no two disjoint nonempty zero-sum subsequences. Otherwise their union is nonempty with sum 2g ∈ ⟨g⟩, so 2g = g, i.e. g = 0.

## 3. Consequence for the fallback targets, and the honest limit

Let S be a hypothetical zero-sumfree (3n−2)-term sequence over C_n³ (n = 15 or 20).
- By CLM-0350, every value has multiplicity ≤ n−2.
- If some g of order n has v_g(S) = n−2, then T = S·g^{−(n−2)} has 2n terms. Its image π(T) in C_n² (CLM-0348) has length 2n ≥ D(C_n²) = 2n−1, so it contains zero-sum subsequences. By CLM-0351:
  - every such subsequence lifts to sum exactly g;
  - any two of them intersect;
  - every one has complement zero-sumfree in C_n², hence of length ≤ 2n−2, so every zero-sum subsequence of π(T) has length ≥ 2.

**Obstruction (recorded, not overcome).** Disjointness alone gives no contradiction. The 2-wise rank-two constant (smallest ℓ forcing two disjoint nonempty zero-sums in C_n²) is 3n − 1 by the rank-two k-th Davenport results. Those are only cited in the repository, under SRC-0014 METADATA_ONLY and SRC-0010, and are not re-inspected here. Since 3n − 1 > 2n, the multiplicity-(n−2) case is not excluded by this count. Excluding it needs the finer lifting condition (all zero-sum subsequences lift to the *same* element g), which is the natural next step.

**Relation to the search data (descriptive).** The logged S104/S105 best sequences of length 3n−3 with a value of multiplicity n−1 are exactly the equality case of CLM-0350. CLM-0350 shows this structure can never extend to 3n−2, which explains why R1 (which often reached such states) could not leave the plateau there. It is not evidence for SAT20.

## 4. Exact tests (settled groups only; `tools/zsf/test_quotient_lemmas.py`, output `sessions/S106/QUOTIENT_LEMMA_TESTS.json`)

These are independent of the proofs: direct exact subset-sum computation with checkers A and B.
- **CLM-0348:** the explicit CRT construction gives a matrix with unit determinant for all 40,567 elements of order n in (Z/n)³, for every n = 2..20.
- **CLM-0349:** 1,981 random instances in (Z/n)³ for n ∈ {3,4,5,6,8,9,10,12} agree (checkers A and B on g^{m−1}T vs. the nonempty-sum criterion).
- **CLM-0351:** 1,892 random instances agree.
- **CLM-0350 instance:** an exhaustive DFS over T in (Z/n)³, n = 3, 4, for g = e1 and a non-axis g of order n, finds a maximum |T| of exactly 2n − 2. This is complete because the criterion is order-independent and subsequence-closed.

These are tests in settled groups. They are not a search of n15/n20 and not a certification.

## 5. Status after S106

- New PROGRAMME_PROVED: CLM-0348, CLM-0349, CLM-0351. CLM-0350 is PROGRAMME_PROVED conditional on CLM-0352.
- New SOURCE_STATED: CLM-0352.
- These are genuine but elementary structural constraints, not a substantive reduction of SAT20.
- **The search-reopen condition is NOT met.** A multiplicity cap of n−2 does not reduce the search to a small family.
- Fallback sessions completed: 1.
