# S113 — Closed-form theorems for the multi-route block criterion (18 October 2026)

Priority: **SATURATION_FALLBACK** (fallback session 8). This session follows the owner steering of 18 October 2026: proof only, with closed-form hypotheses on n, and no new enumeration as a result. Targets, both OPEN: **SAT20** (D(C20³) = 58) and **SAT15** (D(C15³) = 43).

All proofs are elementary INTERNAL SAME_EXECUTOR hand proofs, and **no novelty is claimed**. Computation was used only to test the stated lemmas (`tools/zsf/test_s113.py`, §6). **No C15³ or C20³ sequence is computed.**

**Summary.**
- **(A) Two coprime routes, five values (CLM-0380/0381).** For odd n = AB with coprime A < B, the two routes A and B together exclude every 5-valued counterexample pattern **if and only if n ∈ {15, 21}**. The proof is by hand in both directions: an impossibility proof for 15 and 21, and explicit survivors for every other pair. Neither the D₂ lever (CLM-0143) nor any other D₂ bound can help: closing a survivor needs exactly D₂(C_a³) ≤ 4a−2.
- **(B) n = 4p (CLM-0382).** A hand proof that a counterexample at n = 20 has ≥ 7 distinct values, with fewer premises than S112 and without the computed certificate CLM-0375. For every prime p ≥ 7 an explicit 6-valued pattern survives all three routes. So the argument needs p = 5 at exactly one inequality, identified in §4.
- **(C) Formula (CLM-0383).** On these families the number of distinct values that the route method forces is k*(n) = 5 + [n even] + [n ∈ {15, 20, 21}]. Beyond the single-route bound, multi-route gains are confined to n = 15, 20, 21.

Nothing here proves or refutes SAT15/SAT20.

## 1. Set-up and the route-failure lemma

We use the notation of CLM-0374. S is a sequence over C_n³ of length 3n−2 with k distinct values g_i, of orders d_i and multiplicities α_i. A *route* is a prime power a | n, n = ab, with D(C_a³) = 3a−2 and D(C_b³) = 3b−2 recorded. o_i = a / gcd(a, n/d_i) is the order of the image of g_i in G/aG ≅ C_a³.
- t₀ = Σ_{o_i=1} α_i + Σ_{o_i>1} ⌊α_i/o_i⌋ and R = Σ_{o_i>1} (α_i mod o_i).
- Route a *closes* if t₀ + ν_lb(R) ≥ 3b−2, which gives a zero-sum (CLM-0374).
- *Failing* means not closing.
- U = Σ_{o_i=1} α_i.

**Lemma 1 (route-failure lemma; CLM-0379, PROGRAMME_PROVED).** Suppose route a fails, even when ν_lb uses only D₁ (ν_lb(R) ≥ 1 for R ≥ 3a−2). Then
- (i) R ≥ 4a − 2 + U(a−1);
- (ii) at least 4 + ⌈2/(a−1)⌉ values have o_i > 1, i.e. **≥ 6 values if a = 2 and ≥ 5 if a ≥ 3**;
- (iii) if every o_i = a, then R ≡ −2 (mod a) and t₀ = (3n−2−R)/a.

*Proof.* For o_i > 1, ⌊α_i/o_i⌋ = (α_i − r_i)/o_i ≥ (α_i − r_i)/a. Hence

  t₀ ≥ U + (3n−2−U−R)/a = 3b − (R+2)/a + U(a−1)/a.

- If R ≤ 3a−3, then (R+2)/a < 3, so t₀ > 3b−3 and t₀ ≥ 3b−2: the route closes.
- So R ≥ 3a−2 and ν_lb ≥ 1, and failure needs t₀ ≤ 3b−4. This gives R + 2 − U(a−1) ≥ 4a, which is (i).
- (ii) follows from R ≤ Σ_{o_i>1}(o_i − 1) ≤ (a−1)·#{i : o_i > 1}.
- (iii): when U = 0 and every o_i = a, t₀ is the integer (3n−2−R)/a. ∎

**Remark (where D₂ enters).** If D₂(C_a³) ≤ R as well, ν_lb ≥ 2 and failure needs R ≥ 5a−2 + U(a−1).

## 2. Theorem A — two coprime routes and five values

**Reduction.** Let A, B be coprime odd routes of n, with 3 ≤ A < B, and let S have five values.
- **Primes force full order.** Suppose A = p is prime and route p fails. By Lemma 1(i) with five values, U = 0: if U ≥ 1, at most four values have o > 1, so R ≤ 4(p−1) < 4p−2. Every o_i ∈ {1, p} is then p.
- **R is pinned.** R ≤ 5(p−1) and R ≡ −2 (mod p), so R = 4p−2.
- So for n = pq, a 5-valued pattern on which both routes fail has all values of order n, with R_p = 4p−2 and R_q = 4q−2.
- **The converse holds for any coprime routes A, B.** Take an all-order-n pattern with R_A = 4A−2 and R_B = 4B−2. Then t₀ = 3b−4 at each route. Also ν_lb(4a−2) = 1, because every D₂ bound the programme has exceeds 4a−2: 5a−3 for primes (CLM-0143) and 2D₁ = 6a−4 otherwise. So both routes fail.

**Integer form.** Put x_i = α_i + 1 and w_i = n − x_i. For an all-order-n pattern, a route a ∈ {A, B} has
- Σ_i (α_i mod a) = 5(a−1) − Σ_i ((−x_i) mod a), and
- (−x_i) mod a = w_i mod a.

The pattern therefore survives both routes if and only if w satisfies

  **(W)**  Σ w_i = 2n − 3,  Σ (w_i mod A) = A − 3,  Σ (w_i mod B) = B − 3.

The caps translate as follows:
- the trivial cap α ≤ n−1 is w_i ≥ 0;
- the CLM-0350 cap α ≤ n−2 (conditional on CLM-0352) is w_i ≥ 1.

**Theorem A (CLM-0380, PROGRAMME_PROVED; pure arithmetic).** Let 3 ≤ A < B be coprime odd integers, n = AB.
- (i) For (A, B) = (3, 5), (W) has no solution with w_i ≥ 0.
- (ii) For (A, B) = (3, 7), (W) has no solution with w_i ≥ 1. It does have solutions with some w_i = 0.
- (iii) For every other pair, (W) has a solution with every w_i ∈ [1, n−1], given explicitly below.

*Proof of (i)–(ii).* For A = 3, the condition Σ(w_i mod 3) = 0 forces w_i = 3a_i, with Σ a_i = 2B − 1. Let j_i = ⌊3a_i/B⌋ ∈ {0, 1, 2}; it is never an exact multiple, since B is coprime to 3 and 0 < a_i < B. Then

  Σ(w_i mod B) = 3Σa_i − BΣj_i = 6B − 3 − BΣj_i,

and this equals B − 3 iff **Σ j_i = 5**. The least a with ⌊3a/B⌋ = j is ⌈jB/3⌉.
- **B = 5**, so a_i ∈ [0, 4] and Σa = 9. The least a for j = 0, 1, 2 is 0, 2, 4. The (n₂, n₁, n₀) splits with n₁ + 2n₂ = 5 are (0,5,0), (1,3,1) and (2,1,2). Their minimal sums are 10, 10 and 10, all > 9. No solution.
- **B = 7**, so Σa = 13. The least a for j = 0, 1, 2 is 0 (or 1 when w ≥ 1), 3, 5.
  - With w ≥ 1, the minimal sums are 15, 1+9+5 = 15 and 2+3+10 = 15, all > 13. No solution.
  - With w ≥ 0, the split (2,1,2) reaches 0+0+3+5+5 = 13: w = (0, 0, 9, 15, 15), i.e. x = (21, 21, 12, 6, 6). Every such solution has a w_i = 0, i.e. α_i = n−1. ∎

*Proof of (iii).* Let α ∈ [1, B−1] be the inverse of A mod B and β ∈ [1, A−1] the inverse of B mod A. Then Aα + Bβ ≡ 1 mod n and A + B ≤ Aα + Bβ ≤ 2n − A − B, so **Aα + Bβ = n + 1**.

The residues are:
- w = Aα has residues (0 mod A, 1 mod B);
- w = Bβ has residues (1 mod A, 0 mod B).

- **Construction 1 (A ≥ 7).** Fix c ∈ [1, A−5] and put m = n − 4 − c.
  - Let a ∈ [1, B] satisfy aA ≡ m (mod B). Since B ∤ 4 + c (as 5 ≤ 4 + c < A < B), a ≠ B. Put b = (m − aA)/B.
  - If b ≤ 0, then aA ≥ m = n − 4 − c while aA ≤ n − A, which forces c ≥ A − 4. That is impossible, so b ≥ 1. Also bB < n, so b ≤ A−1.
  - Take **w = (Aα, Bβ, c, aA, bB)**.
  - The sum is (n+1) + (n−4) = 2n−3.
  - The residues mod A are 0, 1, c, 0 and (bB mod A) = A − 4 − c, totalling A − 3.
  - The residues mod B are 1, 0, c, (aA mod B) = B − 4 − c and 0, totalling B − 3.
- **Construction 2 (A ≥ 5, B ≥ A + 5).** Take **w = (Aα, Bβ, 1, A, n − 5 − A)**.
  - The sum is 2n − 3.
  - The residues mod A are 0+1+1+0+(A−5) = A−3.
  - The residues mod B are 1+0+1+A+(B−5−A) = B−3.
- **Construction 3 (A = 3, B ≥ 11).** Use w_i = 3a_i with every j_i = 1, i.e. B/3 < a_i < 2B/3, and Σa_i = 2B − 1.
  - For B = 3k+1 (k ≥ 4): a = (k+1, k+1, k+1, k+1, 2k−3).
  - For B = 3k+2 (k ≥ 3): a = (k+1, k+1, k+1, k+1, 2k−1).
  - Then Σ(w mod B) = 3(2B−1) − 5B = B − 3.
- **Witnesses for the two remaining pairs:**
  - (5, 7): w = (15, 15, 15, 15, 7), i.e. x = (20, 20, 20, 20, 28);
  - (5, 9): w = (1, 10, 10, 30, 36).

These cover every coprime odd pair with A ≥ 3, except (3,5) and (3,7):
- A ≥ 7 by Construction 1;
- A = 5 by Construction 2 when B ≥ 11, and by the witnesses when B = 7 or 9;
- A = 3 by Construction 3, since B ≥ 11 when B ∉ {5, 7}. ∎

**Corollary A (CLM-0381, PROGRAMME_PROVED).**
- (a) **n = pq, p < q odd primes.** Routes p and q (premises CLM-0142 and CLM-0369/0374) exclude every 5-valued (3n−2)-sequence **iff n ∈ {15, 21}**.
  - n = 15 is unconditional (this re-proves CLM-0376).
  - n = 21 additionally uses the CLM-0350 cap, conditional on CLM-0352. This is a hand proof of the content of CLM-0377(ii) that needs neither CLM-0143 nor the computed CLM-0375. CLM-0377 is not relabelled.
  - For every other pq (33, 35, 39, 55, …) explicit surviving patterns exist, namely α_i = n − 1 − w_i from Theorem A(iii).
- (b) **Odd n = p^a q^b.** The only routes are A = p^a and B = q^b, since n/p^j has two odd prime factors for j < a and its D is not recorded. Their D-values come from CLM-0039 (SOURCE_STATED) or CLM-0142. For every such n other than 15 and 21, the all-order-n survivors of Theorem A(iii) survive both routes, so **the route method gives only the CLM-0359 bound (≥ 5 values)**.
- (c) **Exact obstruction.** In every survivor of (W), each route has leftover R_a = 4a−2.
  - The pattern would close at route a if ν_lb(4a−2) ≥ 2, i.e. **D₂(C_a³) ≤ 4a−2**.
  - Conversely, if D₂(C_a³) ≤ 4a−2 for a single route a, that route alone excludes every 5-valued pattern. By the remark after Lemma 1, failure would need R ≥ 5a−2 > 5(a−1).
  - The lever CLM-0143 (D₂ ≤ 5p−3) can therefore never act at support 5, and the cap acts only at n = 21.
  - CLM-0373 shows that the unrestricted support-5 two-disjoint-zero-sum property TWO(a) fails for a = 3, 5. So closing the survivors needs the actual images of the values, not counting.

## 3. Theorem B — the family n = 4p

The routes of n = 4p (p ≥ 5 prime) are the following. The image group in every case is C_a³.

| route | b | D(C_b³) used | image orders o_i |
| --- | --- | --- | --- |
| a = 2 | 2p | CLM-0065, SOURCE_STATED | o = 2 iff 4 \| d_i |
| a = 4 | p | CLM-0142 | o = the 2-part of d_i |
| a = p | 4 | CLM-0039, SOURCE_STATED | o = p iff p \| d_i |

D(C₂³) = 4 and D(C_p³) = 3p−2 come from CLM-0142, and D(C₄³) = 10 from CLM-0039. Only D₁ values are used: no D₂ bound, no CLM-0143.

**Theorem B (CLM-0382, PROGRAMME_PROVED, conditional on CLM-0065, CLM-0039 and, for the cap, CLM-0350/0352).** Let S be a (12p−2)-term sequence over C_{4p}³ with k ≤ 6 distinct values, on which routes 2, 4 and p all fail. Then k = 6 and:
- **(B1)** every value has order 4p;
- **(B2)** every α_i is odd;
- **(B3)** #{i : α_i ≡ 3 mod 4} ∈ {4, 6};
- **(B4)** Σ_i ((−(α_i+1)) mod p) ∈ {p−4, 2p−4}.

In addition:
- **(B5) p = 5.** (B1)–(B4) together with α_i ≤ n−2 are contradictory. **Hence every zero-sumfree 58-term sequence over C20³ has at least 7 distinct values.**
- **(B6) p ≥ 7.** The pattern with all six values of order 4p and
  α = (2p−3, 2p−3, 2p−3, 2p−3, 2p+5, 2p+5)
  satisfies (B1)–(B4) and all caps (α ≤ n−3), and survives all three routes.

*Proof.*
- **Route 2.** By Lemma 1(ii), failure needs six values with o = 2, so k = 6. By Lemma 1(i), R ≥ 6 + U, and R ≤ 6, so U = 0 and R = 6. Every value therefore has 4 | d_i and odd α_i. This gives (B2) and the 2-part of (B1).
- **Route 4.** Every o_i = 4 and r_i = α_i mod 4 ∈ {1, 3}. So R₄ = 6 + 2m, where m = #{α_i ≡ 3 mod 4}.
  - Lemma 1(iii) gives R₄ ≡ −2 (mod 4), so m is even.
  - Lemma 1(i) gives R₄ ≥ 14, so m ≥ 4. This is (B3).
- **Route p.** Lemma 1(i) with six values gives U = 0: if U ≥ 1, then R ≤ 5(p−1) < 4p−2 + (p−1). Every value thus has p | d_i, which completes (B1).
  - Then R ≡ −2 (mod p) and 4p−2 ≤ R ≤ 6p−6, so R ∈ {4p−2, 5p−2}.
  - Since Σ_i(p−1−(α_i mod p)) = 6p−6−R and p−1−(α mod p) = (−(α+1)) mod p, this is (B4).
- **(B5).** Put y_i = (α_i+1)/2. Then y_i ∈ [1, 9] (α ≤ 18), Σy = 32, and y_i is even iff α_i ≡ 3 (mod 4).
  - Let u_i = ⌈2y_i/5⌉. Then Σ_i 5u_i = 64 + Σ s_i, where s_i = (−2y_i) mod 5. By (B4), Σ s_i ∈ {1, 6}, so Σu ≤ 14.
  - For y ≤ 9 one checks: **even y ≤ 2u** (y = 2, 4, 6, 8 give u = 1, 2, 3, 4) and **odd y ≤ 2u + 1** (y = 1, 3, 5, 7, 9 give u = 1, 2, 2, 3, 4).
  - Hence Σy ≤ 2Σu + #{odd y} ≤ 28 + 2 = 30 < 32, using (B3). Contradiction.
  - For k ≤ 5, route 2 already closes. ∎
- **(B6).** Here y = (p−1, p−1, p−1, p−1, p+3, p+3), all even, with Σy = 6p+2.
  - 2(p−1) ∈ (p, 2p] gives u = 2 and s = 2. 2(p+3) ∈ (2p, 3p] for p ≥ 6 gives u = 3 and s = p − 6.
  - So Σs = 2p−4, i.e. R_p = 4p−2 with t₀ = 8. Also ν_lb(4p−2) = 1, since 4p−2 < 5p−3. Route p fails: 8 + 1 < 10.
  - All α ≡ 3 (mod 4) gives R₄ = 18 and t₀ = 3p−5. With ν_lb(18) = 1 (D₂(C₄³) ≤ 20), 3p−4 < 3p−2, so route 4 fails.
  - R₂ = 6 gives t₀ = 6p−4. With ν_lb(6) = 1, 6p−3 < 6p−2, so route 2 fails. ∎

**Where p enters.** The single place is the inequality in (B5):
- the per-value bound y ≤ pu/2, sharpened by parity for even y, summed under Σu ≤ 14;
- its maximum is 30 < 6p+2 = 32 at p = 5, and it is ≥ 6p+2 for every p ≥ 7 (B6).

**Premises compared with S112:** CLM-0377(i) used CLM-0375 (computed), CLM-0143 and CLM-0368/0356. The hand proof (B5) uses none of them. CLM-0377 is not relabelled.

**Prime powers.** The same pattern (B6) survives at n = 4P for every odd prime power P ≥ 7, where the D₂ bound used is 2D₁. The route method therefore never gives 7 values on the family n = 4P with P ≥ 7.

## 4. Theorem C — the forced number of distinct values as a formula

Let k*(n) be the least k for which some k-valued (3n−2)-pattern survives every route of n under CLM-0374, using the programme's D-bounds and caps. The route method forces exactly "≥ k*(n) distinct values".

**Theorem C (CLM-0383, PROGRAMME_PROVED, premises as in A and B).**
- (i) **For every n** with at least one route: k*(n) ≥ max_a (4 + ⌈2/(a−1)⌉) over the routes a, which is 6 if 2 is a route and 5 otherwise (Lemma 1(ii)).
- (ii) For **odd n = p^a q^b** (exactly two prime factors): **k*(n) = 5 + [n ∈ {15, 21}]**.
- (iii) For **n = 4p**, p ≥ 5 prime: **k*(n) = 6 + [p = 5]**.

Together, on these families: **k*(n) = 5 + [n even] + [n ∈ {15, 20, 21}]**.

*Proof.*
- Lower bounds: (i), Theorem A(i)–(ii) and Theorem B(B5).
- Upper bounds: Theorem A(iii) and Theorem B(B6).
- At the three exceptional n, explicit survivors of size k* exist. Each can be checked by hand, all values of order n:

| n | α (multiplicities) | route checks |
| --- | --- | --- |
| 15 | (3, 8, 8, 8, 8, 8) | route 3: R = 10, t₀ = 11, 12 < 13; route 5: R = 18, t₀ = 5, 6 < 7 |
| 21 | (2, 5, 5, 11, 19, 19) | route 3: R = 10, t₀ = 17, 18 < 19; route 7: R = 26, t₀ = 5, 6 < 7 |
| 20 | (1, 3, 3, 3, 14, 17, 17) | each route of 2, 4, 5 fails; checked in L5 |

∎

**Reading of the formula.** Beyond the single-route bound, the averaging of several route deficits gains only on finitely many n in each family: 15, 21 and 20. The reason is structural. Every survivor sits at the minimal failing leftover R_a = 4a−2 (or 5a−2), and the CRT gives enough freedom to meet all routes' residue conditions at once as soon as A, B or p are not tiny. To improve on k*(n) one needs D₂-type information at the leftover level, or the actual images. Counting alone cannot do it.

## 5. Failed or limited directions (exact obstructions)

1. **The D₂ lever for n = pq.** It never acts at support 5, since R_a = 4a−2 < 5a−3 (Corollary A(c)). The needed inequality D₂(C_a³) ≤ 4a−2 is equivalent to closing every 5-valued pattern by one route. It is not available, and CLM-0373 (TWO(3), TWO(5) false) shows that it cannot be obtained by ignoring the images.
2. **n = 4p with p ≥ 7.** The 7-value bound is not provable by routes 2, 4 and p (B6). The obstruction is the slack 7p − O(1) ≥ 6p + 2 in the y-inequality.
3. **n = 2^e·m more widely.** For e ≥ 3, route 2 needs D(C_{n/2}³) with n/2 = 2^{e−1}m, which is not recorded. Only routes 2^{e−1} (b = 2m), 2^e and m remain, and Lemma 1(ii) then gives only 5. Not pursued.

## 6. Lemma tests (evidence only; `sessions/S113/S113_LEMMA_TESTS.json`)

`python -I tools/zsf/test_s113.py` runs in about 35 s and touches integers and multiplicity patterns only.
- **L1.** The constructions of Theorem A(iii) satisfy (W) for all coprime odd pairs with B ≤ 401.
- **L2.** Brute force over w-multisets confirms A(i) and A(ii).
- **L3.** For every pq ≤ 65, the 5-valued survivors of an independently written closure test equal the (W)-solutions, and agree with S112 `route_sieve.py` algorithm B. The counts are 0, 0, 2, 2, 3, 11, 42 at n = 15, 21, 33, 35, 39, 55, 65.
- **L4.** No solution of (B1)–(B4) at p = 5. The B6 pattern survives for all primes 7 ≤ p ≤ 199. At n = 20, 28, 44, 52 every 6-valued survivor satisfies (B1)–(B4); there are 0, 28, 330 and 794 survivors, with the cap n−2 only.
- **L5.** The Theorem C witnesses survive.

## 7. Status

- New claims: CLM-0379..0383. Claims go from 378 to 383.
- CLM-0366/0367/0375/0377 are not relabelled, and no source is promoted.
- Frontier unchanged. No SAT20/SAT15 or D-value statement.
- **Search-reopen condition: not met.**
