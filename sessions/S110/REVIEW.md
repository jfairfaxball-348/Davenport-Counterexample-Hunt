# S110 hostile same-executor review — 18 October 2026

**ACCEPT, narrowly:** CLM-0366/0367 as COMPUTED_EXACT exclusions of the support-≤5 family at n=15 and n=20. This is NOT a formal certification.

**Attacks and resolutions:**
1. *Was the registered code run?* The hashes were re-verified against both pre-registrations before activation, and the validator confirms the tools are byte-unchanged from entry. The n=6 re-check reproduced the S109 orbit hash.
2. *Is coverage complete?* For each algorithm, the sum of `pairs_evaluated` over the 14 shards equals the pre-registered expected total exactly (791,934 / 349,690 / 4,162,730 / 2,866,880). Every shard log ends with an `end` record, and every exit code is 0, so nothing was truncated.
3. *Two-algorithm agreement:* the maxima are equal (42, 57), there are zero threshold records in each, and the sets of attained optimum values are identical. Agreement of the full value sets is a non-trivial cross-check, because the two algorithms enumerate different representative systems with different optimisers.
4. *Shared-premise risk:* both algorithms depend on the same reduction (CLM-0358, CLM-0361..0364: hand proofs, same executor). A flaw there would be common-mode. This is why the claims are labelled conditional and are not FORMALLY_CERTIFIED. The settled-group pre-flight (CLM-0365), which matched the known D at eight values of n, is evidence against such a flaw but not proof.
5. *Scope:* family exclusion only. The text never states SAT15/SAT20 or a D value, and the frontier is unchanged.
6. *Honest cost reporting:* ≈ 146 CPU-h actual against 72 estimated, recorded in the failure ledger.
7. *Log integrity:* the SHA-256 of every shard log (LF) is recorded in RESULT.json and re-verified by the validator. The logs are committed (≈ 240 KB).

**Residual limitations:**
- CI is ABSENT_NOT_PASS.
- The review is internal, by the same executor.
- No Lean/DRAT certificate exists.
- Support ≥ 6 remains open.
