# S103 hostile same-executor review — 16 October 2026

**ACCEPT, narrowly:** scoped gates, tooling, CLM-0345/0346 and two pre-registrations. This is NOT an independent or kernel validation.

**Attacks and resolutions:**
1. *Is a scoped Phase-1 PASS a silent upgrade?* No. The general frontier stays IN_PROGRESS, and every historical obligation is still listed as open. The scope is search-target validity, and a found sequence is checkable without any literature input. The upper-bound interpretation (D=59 at n20) stays source-conditional and is labelled that way.
2. *Are A and B really independent?* They share no code. They use different data structures (numpy boolean set vs Python integer counts), different criteria (prefix −g membership vs count[0]==1) and different translation code. They were written by the same author in the same session, so they are **not** independently authored. Certification additionally requires Lean 4 and a cold re-check.
3. *Is the empty-sum convention handled?* Σ includes 0 in both. A rejects g ≡ 0 because 0=−0 ∈ Σ(∅). In B, a zero element doubles count[0] from 1 to 2. Tests cover (0,0,0) and (n,0,2n).
4. *Could the FFT coverage introduce error into correctness?* No. FFT values only bias move selection, and every push is decided by the exact boolean oracle. They were also checked equal to direct updates 800 times. An error there could only hurt search quality, never validity.
5. *Did a benchmark or pre-flight secretly search the targets?* The benchmark times push/pop of random single elements from the empty state, legal masks at a 14- or 19-term prefix, and full checks of the standard sequence. The pre-flight runs only n=4,5,6. No sequence longer than 3n−3 at n15/n20 was sought or recorded.
6. *Is the exhaustive small-group DFS complete?* It enumerates multisets in nondecreasing element order with exact pruning; a prefix that is not zero-sumfree has no zero-sumfree extension (CLM-0345(a)). Its results equal source-stated D. It is used only as validation, not as a new claim.
7. *Witness extraction in B:* it is verified by direct re-summation on every non-zero-sumfree case in the tests.
8. *Hash fragility:* with `core.autocrlf=true`, line endings could change the SHA-256. Fixed by `.gitattributes` eol=lf; the pre-registration notes that hashes are over LF bytes.
9. *Is the budget realistic?* It is bounded by iteration count plus a walltime cap with an explicit truncated status. It is set from measured primitive throughput (about 55k push/pop per second, 16 logical CPUs). Per-iteration cost on the target groups was deliberately not measured, so S104 must report the actual elapsed time.

**Residual limitations:**
- Hosted CI is ABSENT_NOT_PASS (0 runs, 0 check-runs).
- The review is internal, by the same executor.
- No Lean pipeline exists yet.
- The R1 domain is heuristic, and exhausting its budget proves nothing.
