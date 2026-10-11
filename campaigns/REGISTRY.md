# Campaign registry

Every campaign **before activation** must state: exact target, search space, method, proved symmetry reductions, completeness class EXHAUSTIVE / PARTIAL / HEURISTIC, bounded budget, persisted checkpoint format and stopping rule. A PROPOSED record never authorizes execution.

## CAM-0001 — n=6 skeleton–lift, PROPOSED / NOT STARTED
- Target: decide whether $C_6^3$ has a zero-sumfree sequence of length 16; a certified example would imply $D(C_6^3)>16$.
- Search space (conditional): all length-16 multisequences over $C_3^3$ admitting <=3 disjoint nonempty zero-sum subsequences, then all $C_2^3$ labels satisfying nonzero projected lifts; inherited 5553 GL(3,3) skeleton orbits are **unverified AND affected by S002 corrected D4(C3^3)=18, not 17**. Neither this count nor the old threshold establishes completeness.
- Proposed method: independently verify skeleton enumeration and GL(3,3) orbit completeness; encode each mod-2 zero-sum avoidance condition into SAT or exact enumeration; cross-check with independent lifting algorithm.
- Symmetry: GL(3,3) on skeletons and GL(3,2) on labels are candidate reductions **not yet proved nor implemented**; retain all branches until proof.
- Completeness class: **PARTIAL (PROPOSED)**; exhaustive designation blocked on proofs of enumeration, orbit reductions and SAT correctness.
- Resource budget: maximum 1 bounded campaign session after separate Phase-2 PASS; per-branch CPU/time and instance limits to be fixed at start of an owner-authorized Phase-3 step.
- Checkpoint format: `campaigns/CAM-0001/checkpoints/*.jsonl` with canonical orbit representatives, SHA-256, covered indices, algorithm version, instance ID, solver result, certificate path/hash and deterministic resume offset.
- Stopping rule: stop when allocated session budget exhausted, a candidate is quarantined, or all pre-registered instances independently certified; never infer global UNSAT from a timeout.
- Precondition: Phase-1 and Phase-2 PASS with executable independent verification, not met in S001.
- S001 work: **none**. No SAT, no search, no solver run.

### S002 gate annotation (2026-10-10)
- **PROPOSED / NOT RUNNING.** n=6 target interval 16..17 independently derived; no candidate evaluated.
- The original source states D4(C3^3)=18, not inherited 17; any 5553-orbit list must be revalidated from first principles. 48 Boolean variables are simply 16×3 CRT labels, not an activated SAT instance.
- Prerequisites remain Phase-1 PASS, then Phase-2 certified tooling and independent symmetry/exhaustiveness proof. S003 is a Phase-1 source-proof session only.

### S003 — PROPOSED / NOT RUNNING (2026-10-11)
Phase 1 IN_PROGRESS, Phases 2 and 3 NOT_STARTED. No SAT/ILP, candidates, orbitting, solver, enumeration, certification or computed count. The inherited 5553 orbit claim has no completeness provenance and used the wrong D4=17. n=6 16..17 remains future tooling target only.
