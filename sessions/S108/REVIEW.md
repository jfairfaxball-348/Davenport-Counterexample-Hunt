# S108 hostile same-executor review — 17 October 2026

**ACCEPT, narrowly:** CLM-0358/0359/0360 as elementary, unconditional programme proofs. This is NOT an independent or kernel validation.

**Attacks and resolutions:**
1. *CLM-0358: is reducing mod n safe?* A zero-sum vector has 0 ≤ x_i ≤ α_i ≤ n−1. So x ↦ x mod n is injective on the box, and x ≠ 0 implies ρ ≠ 0. The criterion only needs α_i ≤ n−1, which zero-sumfreeness guarantees, since ord(a_i) ≤ n. It agreed with checkers A/B on 5,200 random vectors.
2. *CLM-0359: are the projection fibres uniform?* K → Z/n is a homomorphism, so all fibres over its image have the same size. The escape count over the image d_iZ/n is n/d_i − 1 − ⌊α_i/d_i⌋, and the bound d⌊α/d⌋ ≥ α − d + 1 is elementary. For |K| ≥ n^{k−r}: K is the kernel of (Z/n)^k → H with |H| ≤ n^r.
3. *Is "at least 5 distinct values" really unconditional?* Yes. It uses no literature value: only k = 4 ≤ r+1 with r = 3. Values of small order are covered, because the bound uses α_i ≤ n−1 and never needs ord(a_i) = n.
4. *Sharpness and consistency:* the bound is attained by the standard sequence (support 3, length 3n−3). The exhaustive 4-value checks in C2³ and C3³ attain exactly 3n−3.
5. *CLM-0360 scope:* it is stated only for ρ of order n. Elements of smaller order are not claimed.
6. *Overreach check:* the support-5 case is reduced, not decided. The search-reopen condition is assessed as not met, and the exhaustive campaign is flagged as an owner decision with no pre-registration.
7. *Literature check honesty:* the search found no lever-group values. No source records were added and no premise was used.
8. *Search discipline:* tests are on n ≤ 10 only (C_n³ for n ≤ 6).

**Residual limitations:**
- CI is ABSENT_NOT_PASS.
- The review is internal, by the same executor.
- No Lean formalisation exists.
- SAT20/SAT15 remain OPEN.
