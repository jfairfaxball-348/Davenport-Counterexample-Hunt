# S112 checkpoint — 18 October 2026

**Priority: SATURATION_FALLBACK.** The open targets are D(C20³) = 58 and D(C15³) = 43.

**Start here: the [consolidation review](research/S111_CONSOLIDATION_REVIEW.md).** It classifies every result as ALL-n, CONDITIONAL-on-family or n-SPECIFIC, with its dependencies.

**New in S112 (multi-route sieve):** using several block routes a | n at once.
- **n = 15:** every zero-sumfree sequence over C15³ with ≤ 5 distinct values has length ≤ 42, now by an **unconditional hand proof** (CLM-0376).
- **n = 20:** a counterexample needs **≥ 7 distinct values** (CLM-0377(i)).
- **n = 21:** the support-≤5 bound holds (CLM-0377(ii)).
- The remaining residue is explicit: 5 six-valued multiplicity patterns at n = 15, and 139 seven-valued ones at n = 20 (CLM-0378).

**New in S111 (generalisation, owner steering):**
- Even-n multiplicity caps for **all even n**: order n ≤ n−3, order n/2 ≤ n/2−2 (CLM-0368).
- **r+2-values bound at even n = 2b** whenever D(C_b^r) = D*, in any rank (CLM-0370). In rank 3 this proves the 5-value bound for n = 4p^k, including **n = 20** and 28 (CLM-0371). This is a proof route for the CLM-0367 bound independent of the S110 computation.
- **Parity structure at even n:** any counterexample has ≥ 6 values of odd multiplicity outside 2G. With exactly six, their mod-2 images form a Fano plane minus a point (CLM-0372).
- The counting block method provably cannot reach odd n such as 15 (CLM-0373).

**Earlier:** support-≤5 excluded at n15/n20 by exhaustive computation (CLM-0366/0367); multiplicity caps and transfer (CLM-0350/0355/0357); small-support bound (CLM-0359).

Claims 378, sources 34 (original 29 untouched), 30 frontier rows untouched, CI ABSENT_NOT_PASS. [S112 note](research/S112_MULTI_ROUTE_SIEVE.md) · [S111 note](research/S111_R_PLUS_TWO_AND_EVEN_CAPS.md) · [review](sessions/S112/REVIEW.md) · [S113 FUTURE](authoritative/NEXT_SESSION_PROMPT.md).
