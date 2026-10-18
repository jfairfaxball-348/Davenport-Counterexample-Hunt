# S113 hostile same-executor review — 18 October 2026

**ACCEPT, with the stated conditions:** CLM-0379, CLM-0380 and CLM-0383 as PROGRAMME_PROVED; CLM-0381 as PROGRAMME_PROVED (unconditional at n = 15; the n = 21 part and part (b) carry the cap / Olson premises); CLM-0382 as PROGRAMME_PROVED, conditional on CLM-0065, CLM-0039 and CLM-0350/0352.

**Attacks and resolutions:**
1. *Is t₀ ≥ 3b − (R+2)/a + U(a−1)/a valid when some o_i is strictly between 1 and a?* Yes: ⌊α/o⌋ = (α − r)/o ≥ (α − r)/a. Lemma 1 is only a necessary condition for failure; survivors are checked separately.
2. *Theorem A survivor direction.* An all-order-n pattern with R_a = 4a−2 has t₀ = 3b−4 and ν_lb = 1 at each route, because every D₂ bound used by CLM-0374 (5a−3 for primes, 2D₁ otherwise) exceeds 4a−2. Independently checked: for every pq ≤ 65 the survivors of a newly written closure test equal the (W)-solutions and the S112 route sieve counts (L3).
3. *Construction 1 edge cases.* a ≠ B because 5 ≤ 4 + c < A < B; b ≥ 1 because b ≤ 0 would force c ≥ A − 4; b ≤ A − 1 because bB < n. (bB mod A) = A − 4 − c and (aA mod B) = B − 4 − c follow from the congruence of m. Checked for all coprime odd pairs up to 401 (L1).
4. *Coverage of pairs.* A = 3 needs B coprime to 3, so B ∉ {9}; B ∈ {5, 7} are the exceptions and B ≥ 11 is Construction 3. A = 5: B ∈ {7, 9} witnesses, B ≥ 11 Construction 2. A ≥ 7: Construction 1. Even n are excluded from Theorem A by hypothesis.
5. *(3,5) and (3,7) impossibility.* The j-count Σj = 5 and the minimal-sum table were redone by brute force over all w-multisets (L2).
6. *Theorem B, route p forcing U = 0.* With six values and U ≥ 1, R ≤ 5(p−1) < 4p − 2 + (p − 1). Correct for all p ≥ 2.
7. *(B5) per-value inequalities.* Checked case by case for y ≤ 9; the y = 10 case (α = 19 = n − 1) is exactly what the CLM-0350 cap removes. Brute force over all odd α ≤ 18 confirms no solution (L4).
8. *Premise accounting.* (B5) uses only D₁ values: D(C₂³) and D(C₅³) (CLM-0142), D(C₄³) (CLM-0039), D(C₁₀³) (CLM-0065), plus the cap CLM-0350. CLM-0143, CLM-0368/0356 and CLM-0375 are not used.
9. *Is the "formula" a statement about D?* No. CLM-0383 is a statement about what the route method can force, proved in both directions. It says nothing about SAT15/SAT20.
10. *Steering compliance.* No sieve table, census or residue enumeration is a deliverable; the lemma tests are evidence only, run on integers. CLM-0378's residue was not enumerated further.

**Residual limitations:** all proofs internal and by the same executor; CLM-0381(b), CLM-0382 inherit source-stated premises; no Lean certificate (deferred); CI ABSENT_NOT_PASS. A process slip is recorded in the failure ledger (a pattern-based process kill).
