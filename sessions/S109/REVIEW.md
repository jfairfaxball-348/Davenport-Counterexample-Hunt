# S109 hostile same-executor review — 17 October 2026

**ACCEPT, narrowly:** CLM-0361..0364 (hand proofs), CLM-0365 (settled computation, two algorithms), the Phase-2 extension, and the CAM-0006/0007 pre-registrations. This is NOT an independent or kernel validation.

**Attacks and resolutions:**
1. *Is the reduction to generating lists sound?* The Smith normal form exists over each local ring Z/q, and φ = U·D·ψ gives ker ψ ⊆ ker φ, so the box constraints only weaken. Zero or repeated values in either list are harmless, because the labelled list and the multiset share the same subsequences.
2. *Is every relation module enumerated?* The kernels of surjections are exactly the free rank-2 summands (split exact sequence). Both tools reproduce the exact Gaussian counts (155, 1210, 9920, 20306, 140050), which independently confirms that the component enumeration is complete.
3. *S₅ coverage:* A takes representatives of the first component and B of the last, and both enumerate the other components fully. Their orbit sets agree exactly for n ≤ 7, including composite n=6. The n=10, 12 runs agree on max, threshold and the set of optimum values.
4. *Optimiser exactness:* the branch-and-bound branching covers the feasible set, and the DP identity is exact. The two optimisers are different, and they agree on every settled orbit (n ≤ 7) and on the value sets (n = 10, 12).
5. *Same-author risk:* the two tools were written by the same executor in one session. They share no code, but they share the mathematical reduction (CLM-0361). An error in CLM-0361 would affect both. That is why the reduction is a separate hand-proved claim, and the certificate is explicitly not Lean/DRAT.
6. *Did a target computation happen?* No. Cost was estimated from settled timings, and orbit-representative counts came from the q = 3, 4, 5 settled runs. No n = 15/20 relation module was evaluated.
7. *Is the budget honest?* It is an estimate with a stated basis, a ×2 margin through walltime caps, explicit truncation semantics, and coverage checks against exact expected pair counts.
8. *Scope:* a negative result covers only sequences with at most 5 distinct values. This is stated in the pre-registrations, the registry, README and STATE.

**Residual limitations:**
- CI is ABSENT_NOT_PASS.
- The review is internal, by the same executor.
- No Lean certification exists.
- The A-cost at n = 20 is uncertain (branch-and-bound size).
