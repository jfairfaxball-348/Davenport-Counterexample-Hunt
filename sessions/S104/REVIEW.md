# S104 hostile same-executor review — 17 October 2026

**ACCEPT, narrowly:** round-1 execution and reporting, CLM-0347, the R2-LNS-1.0 Phase-2 extension and the CAM-0004/0005 pre-registrations. This is NOT an independent or kernel validation.

**Attacks and resolutions:**
1. *Was round 1 run exactly as pre-registered?* The code SHA-256s were rechecked against both pre-registrations before launch. Every worker's logged `param_hash` equals its pre-registered value. The commands match the registered command line, with no mid-run change. Python and numpy versions match.
2. *Could the round be overstated as complete?* All 12 end records show BUDGET_EXHAUSTED at 200,000 iterations. None reports WALLTIME_CAP_TRUNCATED, and all exit codes were 0. The round is complete on both targets in the pre-registered sense only.
3. *Is "no hit" being sold as a negative result?* No. Everywhere it is labelled HEURISTIC budget exhaustion, and the frontier is unchanged. The plateau at 3n−3 is described as a property of the R1 method, not of the groups.
4. *Were the best sequences really checked by two checkers?* The engine's in-process verdicts were not relied on. The validator reloads each logged best sequence, recomputes its canonical SHA-256, and reruns checkers A and B standalone. All 12 are zero-sumfree with |Σ| = n³.
5. *Are the committed logs the logs that ran?* The full-log SHA-256s were recorded in RESULT.json directly after the run. The engine wrote them in Windows text mode (CRLF); an initial check that they were LF was wrong (Git Bash grep hid the CRs) and was caught when the staged blob hash differed. RESULT.json now records both the as-written CRLF hash and the LF-normalised hash, which equals the committed blob because `.gitattributes` pins `campaigns/**/*.jsonl` to eol=lf. The validator checks the LF-normalised hash.
6. *Is R2 materially different from R1, or a parameter tweak?* It uses a different move structure: exact neighbourhood decision via CLM-0347 rather than random ruin. It has a different acceptance and plateau mechanism (tabu), a different growth rule (uniform rather than softmin) and a different seed family (structured standard start). It shares only the exact oracle and checkers.
7. *Did the round-2 budget sizing secretly search the targets?* No. It only timed `rebuild` of the fixed standard prefix and one FFT at n15/n20. No R2 iteration ran on the target groups, and the CAM-0004/0005 checkpoint directories do not exist.
8. *Is CLM-0347 correct?* Prefix criterion: Tab is zero-sumfree iff a is legal for T and b is legal for Ta. A legal b exists iff Σ(Ta) ≠ G. Since Σ(Ta) = Σ(T) ∪ (a+Σ(T)), |Σ(Ta)| = |Σ(T)| + |(a+Σ)∖Σ|. The FFT evaluation is rounded exact-integer arithmetic. It was cross-checked 120 times against exhaustive oracle enumeration, and an error could only miss moves, never accept a non-zero-sumfree sequence, because every push is exact.
9. *Is the R2 pre-flight meaningful?* It only shows the engine reaches, and never exceeds, the known maxima on settled groups, and that its moves fire. It says nothing about target performance.

**Residual limitations:**
- Hosted CI is ABSENT_NOT_PASS (0 runs, 0 check-runs).
- The review is internal, by the same executor.
- No Lean pipeline exists yet.
- Both round methods are HEURISTIC.
- The fallback trigger is likely to be met after round 2 unless R2 finds something.
