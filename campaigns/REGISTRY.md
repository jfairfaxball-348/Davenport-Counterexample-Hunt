# Campaign registry

Every campaign **before activation** must state: exact target, search space, method, proved symmetry reductions, completeness class EXHAUSTIVE / PARTIAL / HEURISTIC, bounded budget, persisted checkpoint format and stopping rule. A PROPOSED record never authorizes execution.

## CAM-0001 — n=6 skeleton–lift, PROPOSED / NOT STARTED
- Target: decide whether $C_6^3$ has a zero-sumfree sequence of length 16; a certified example would imply $D(C_6^3)>16$.
- Search space (conditional): all length-16 multisequences over $C_3^3$ admitting <=3 disjoint nonempty zero-sum subsequences, then all $C_2^3$ labels satisfying nonzero projected lifts; inherited 5553 GL(3,3) skeleton orbits are **unverified**.
- Proposed method: independently verify skeleton enumeration and GL(3,3) orbit completeness; encode each mod-2 zero-sum avoidance condition into SAT or exact enumeration; cross-check with independent lifting algorithm.
- Symmetry: GL(3,3) on skeletons and GL(3,2) on labels are candidate reductions **not yet proved nor implemented**; retain all branches until proof.
- Completeness class: **PARTIAL (PROPOSED)**; exhaustive designation blocked on proofs of enumeration, orbit reductions and SAT correctness.
- Resource budget: maximum 1 bounded campaign session after separate Phase-2 PASS; per-branch CPU/time and instance limits to be fixed at start of an owner-authorized Phase-3 step.
- Checkpoint format: `campaigns/CAM-0001/checkpoints/*.jsonl` with canonical orbit representatives, SHA-256, covered indices, algorithm version, instance ID, solver result, certificate path/hash and deterministic resume offset.
- Stopping rule: stop when allocated session budget exhausted, a candidate is quarantined, or all pre-registered instances independently certified; never infer global UNSAT from a timeout.
- Precondition: Phase-1 and Phase-2 PASS with executable independent verification, not met in S001.
- S001 work: **none**. No SAT, no search, no solver run.
