# S105 hostile same-executor review — 17 October 2026

**ACCEPT, narrowly:** round-2 execution and reporting, the experimental closeout, and the switch to SATURATION_FALLBACK. This is NOT an independent or kernel validation.

**Attacks and resolutions:**
1. *The logged parameter hashes do not match the pre-registration. Was the registered experiment actually run?* Yes. For all 12 workers the logged `params` record equals the registered values field by field. The registered hash is reproduced from those values with walltime serialised as int `7200`, and the logged hash with float `7200.0`, which is how the engine's argparse stores it. The defect is in the S104 pre-registration's hashing, and it is disclosed in RESULT.json, the registry, the failure ledger and STATE. It could have been hidden by "fixing" the pre-registration; that was not done, and the pre-registration files are byte-unchanged (checked by the validator).
2. *Was the code that ran the code that was registered?* SHA-256 values were computed from the git blob and the working tree before launch, and both matched. The validator rechecks them on the session branch.
3. *Is the round complete?* 12/12 end records show BUDGET_EXHAUSTED at 1200 iterations, with no truncation (all under 450 s against a 7200 s cap) and every exit code 0.
4. *Is round 2 really materially different from round 1, so that the trigger counts?* Yes, as argued in S104 §4. It uses an exact neighbourhood decision (CLM-0347) instead of random ruin, tabu plateau moves, uniform growth and structured seeds. The move statistics show the exact repair moves firing hundreds of times per target, so it was not a renamed R1.
5. *Is the fallback switch premature?* The directive's trigger is mechanical: two completed, materially different, bounded and documented rounds, with no candidate, no certified exclusion and no substantive theorem. All of these hold. Switching is required, not optional.
6. *Is anything being presented as a negative result?* No. The closeout, README, STATE, registry and frontier note all state that HEURISTIC exhaustion proves nothing. The frontier is unchanged.
7. *Are the observations overstated?* "k=1-closed" is stated only for visited states. The S104 multiplicity-(n−1) lead is explicitly weakened by the round-2 best sequences.
8. *Log integrity:* full-log hashes are recorded both as written (CRLF) and LF-normalised (git blob). The validator checks the LF-normalised hash.

**Residual limitations:**
- CI is ABSENT_NOT_PASS (0 runs, 0 check-runs).
- The review is internal, by the same executor.
- No Lean, exhaustive or SAT tooling exists.
- The fallback statement remains OPEN.
