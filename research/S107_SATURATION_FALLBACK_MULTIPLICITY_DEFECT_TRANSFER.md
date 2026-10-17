# S107 — Saturation fallback session 2: multiplicity-defect transfer (17 October 2026)

Priority: **SATURATION_FALLBACK**. Targets, both OPEN:
- **SAT20:** D(C20³) = 58.
- **SAT15:** D(C15³) = 43.

S106 left the multiplicity-(n−2) case open (failure ledger: counting disjoint zero-sums cannot close it). S107 closes it at n = 20, and more generally transfers every multiplicity-defect case to a Davenport question in a *smaller* rank-three group C_e ⊕ C_n ⊕ C_n with e | n.

All proofs are elementary INTERNAL SAME_EXECUTOR hand proofs. Quotient/inductive arguments of this kind are classical in spirit (cf. SRC-0004, METADATA_ONLY), and **no novelty is claimed**.

Notation: G = C_n³, v_h(S) is the multiplicity of h in S, and σ is the sum.

## 1. Source used

**CLM-0356 (SOURCE_STATED, SRC-0005).** Girard–Schmid (arXiv:1806.07636v2, inspected 2026-10-17), recalled Theorem 2.7: "Let m, n ≥ 1 be two integers. Then D(C2 ⊕ C2m ⊕ C2mn) = 2m + 2mn." With m = 10 and n = 1 this gives D(C2 ⊕ C20 ⊕ C20) = 40 = D*. The paper's introduction also says that for groups C2 ⊕ C_{n2} ⊕ C_{n3} "the Davenport constant is known".
- Only the statement was inspected, consistent with SRC-0005's recorded STATEMENT_INSPECTED level. The original proof the paper recalls was not inspected.
- The SRC-0005 record itself is one of the original 29 and is left byte-unchanged. This inspection is logged in the `s107_audit` block of `catalogue/sources.json`.

## 2. Lemmas

**CLM-0353 (PROGRAMME_PROVED) — general multiplicity criterion.** Let h ∈ G (any finite abelian G) have order m, let 1 ≤ j ≤ m, and let T be any sequence. Then h^{m−j}T is zero-sumfree iff every nonempty subsequence T′ of T with σ(T′) ∈ ⟨h⟩ has σ(T′) ∈ {h, 2h, …, (j−1)h}.

*Proof.* Write σ(T′) = kh with 0 ≤ k ≤ m−1.
- (⇒) If k = 0, T′ is a zero-sum. If j ≤ k ≤ m−1, adding m−k ∈ [1, m−j] block copies of h gives a zero-sum. So 1 ≤ k ≤ j−1.
- (⇐) Let U = h^i T′ be a nonempty zero-sum, 0 ≤ i ≤ m−j.
  - If T′ is empty, then ih = 0 with 1 ≤ i ≤ m−1, which is impossible.
  - Otherwise σ(T′) = −ih ∈ ⟨h⟩, so σ(T′) = kh with 1 ≤ k ≤ j−1, and (i+k)h = 0 with 1 ≤ i+k ≤ m−1, which is impossible. ∎

The cases j = 1 and j = 2 are CLM-0349 and CLM-0351.

**CLM-0354 (PROGRAMME_PROVED) — pure elements of C_n^r.** Every h ∈ C_n^r of order m equals (n/m)·u for some u of order n. Hence G/⟨h⟩ ≅ C_{n/m} ⊕ C_n^{r−1}, and for every d | m, G/⟨dh⟩ ≅ C_{nd/m} ⊕ C_n^{r−1}. Under that isomorphism the image of h has order d.

*Proof.* Let q = n/m.
- **Finding w.** Since mh = 0, every coordinate h_i satisfies (n/gcd(h_i,n)) | m, so q | h_i. Put w = h/q coordinatewise, so qw = h.
- **Freedom to adjust.** For any t, u = w + m t also satisfies qu = h, because qm = n.
- **Making u of order n.** Fix a prime p | n. We need some coordinate of u to be a unit mod p.
  - If p ∤ m, choose t_1 mod p so that w_1 + m t_1 ≢ 0 mod p; this works because m is invertible mod p.
  - If p | m, then u ≡ w mod p, since mt ∈ pG. If all w_i ≡ 0 mod p, then h = qw ∈ qpG and the order of h divides m/p, a contradiction.
  - Glue the per-prime choices of t by the CRT. Then gcd(u_1,…,u_r,n) = 1, so u has order n.
- **Quotients.** By CLM-0348, G = ⟨u⟩ ⊕ K with K ≅ C_n^{r−1}, and ⟨dh⟩ = ⟨(nd/m)u⟩ ⊆ ⟨u⟩. Hence G/⟨dh⟩ ≅ ⟨u⟩/⟨(nd/m)u⟩ ⊕ K ≅ C_{nd/m} ⊕ K. The image of h = (n/m)u has order (nd/m)/(n/m) = d. ∎

**CLM-0355 (PROGRAMME_PROVED) — multiplicity-defect transfer.** Let S be zero-sumfree over G = C_n³, h of order m, v_h(S) = m − j with 1 ≤ j ≤ m, and S = h^{m−j}T. Let d | m with d ≥ j, Q = G/⟨dh⟩ ≅ C_{nd/m} ⊕ C_n ⊕ C_n (CLM-0354), and π: G → Q. Then h̄^{d−j}·π(T) is zero-sumfree over Q, of length |S| − m + d. Consequently

  |S| ≤ m − d + d(Q), where d(Q) = D(Q) − 1.

*Proof.* In Q, h̄ = π(h) has order d.
- A subsequence T′ of T has π-sum in ⟨h̄⟩ iff σ(T′) ∈ ⟨h⟩ + ⟨dh⟩ = ⟨h⟩.
- By CLM-0353 (⇒) in G, σ(T′) = kh with 1 ≤ k ≤ j−1, so π(σ(T′)) = k h̄.
- Since 1 ≤ k ≤ j−1 ≤ d−1, this lies in {h̄, …, (j−1)h̄}.
- By CLM-0353 (⇐) in Q (order d, parameter j), h̄^{d−j}π(T) is zero-sumfree. ∎

**Corollary (part of CLM-0355).** Suppose |S| = 3n−2 and D(Q) = D*(Q), so that d(Q) = nd/m + 2n − 3. Then the case v_h(S) = m − j is impossible whenever

  n + 1 + d > m + nd/m.

- For m = n this always holds: n + 1 + d > n + d.
- **For m = n**, d = 1 recovers CLM-0350 (Q = C_n², rank two).
- **For m = n** and any 1 < d | n, the case v_h = n − j with j ≤ d reduces to D(C_d ⊕ C_n ⊕ C_n) = D*.

## 3. Consequences at the targets

**CLM-0357 (PROGRAMME_PROVED, conditional on SOURCE_STATED CLM-0352 and CLM-0356).** Every zero-sumfree 58-term sequence S over C20³ satisfies the following.
- **Order 20:** v_h(S) ≤ 17.
  - Multiplicity 19 is excluded by CLM-0350.
  - Multiplicity 18 (j = 2) is excluded by CLM-0355 with d = 2: Q ≅ C2 ⊕ C20 ⊕ C20 and D(Q) = 40 = D*, so |S| ≤ 20 − 2 + 39 = 57.
- **Order 10:** v_h(S) ≤ 8. Multiplicity 9 (j = 1, d = 1) gives Q ≅ C2 ⊕ C20 ⊕ C20 by CLM-0354, so |S| ≤ 10 − 1 + 39 = 48.
- **Orders 5, 4, 2:** the trivial caps 4, 3, 1.
- **Support:** S has at least ⌈58/17⌉ = 4 distinct values.

**n = 15 (conditional only, no claim of the premise).** No group C_e ⊕ C15 ⊕ C15 with 1 < e | 15 has a known Davenport constant in the repository's sources, so only CLM-0350 applies unconditionally: order-15 multiplicities are ≤ 13. CLM-0355 gives the following.
- If D(C3 ⊕ C15 ⊕ C15) = D* = 31: order-15 cap 11 (d = 3 excludes j ≤ 3) and order-5 cap 3.
- If D(C5 ⊕ C15 ⊕ C15) = D* = 33: order-15 cap 9 (d = 5) and order-3 cap 1.

**Further levers at n = 20, all conditional and unproved:**
- If D(C4 ⊕ C20 ⊕ C20) = D*: order-20 cap 15 (d = 4), order-10 cap 7, order-5 cap 3.
- If D(C5 ⊕ C20 ⊕ C20) = D*: order-20 cap 14 (d = 5), order-4 cap 2.
- If D(C10 ⊕ C20 ⊕ C20) = D*: order-20 cap 9, order-10 cap 4, order-4 cap 1, and no elements of order 2.

Each conditional cap was recomputed mechanically from the corollary's inequality: for a given e, the case is excluded for every j ≤ d over all (m, d) with nd/m = e.

These are exactly the D*-questions for the groups C_e ⊕ C_n ⊕ C_n. The transfer makes them sufficient, not necessary, for structure in C_n³.

## 4. Exact tests (`tools/zsf/test_transfer_lemmas.py`, output `sessions/S107/TRANSFER_LEMMA_TESTS.json`; small groups only)

These are independent of the proofs.
- **CLM-0354:** the proof's construction of u succeeds for all 44,080 nonzero elements of (Z/n)³, n = 2..20.
- **CLM-0353:** 1,587 random instances (n ∈ {3,4,5,6,8,9,10,12}, random j) agree with checkers A and B.
- **CLM-0355:** 897 random constructed zero-sumfree S = h^{m−j}T (n ∈ {4,6,8,9,10,12}, random d | m with d ≥ j). Each was projected through explicit basis coordinates (inverse matrix over Z/n). The image of h has order d, and h̄^{d−j}π(T) is zero-sumfree by both checkers.

There was no search on n = 15/20 sequences.

## 5. Status

- New PROGRAMME_PROVED: CLM-0353, CLM-0354, CLM-0355. CLM-0357 is PROGRAMME_PROVED conditional on CLM-0352 and CLM-0356.
- New SOURCE_STATED: CLM-0356.
- The S106 open case (multiplicity n−2) is **closed at n = 20**, conditional on SOURCE_STATED values. At n = 15 it is open and reduced to D*(C3 ⊕ C15 ⊕ C15) or D*(C5 ⊕ C15 ⊕ C15).
- **The search-reopen condition is not met.** Multiplicity caps of 17/8 do not reduce SAT20 to a small family.
- Fallback sessions completed: 2.
