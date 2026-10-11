# Tools policy

No search scripts, solver tests, Lean runs or sample reproductions were executed in S001. Future exact scripts must record versions/parameters/input, output SHA-256, implementation independence, full enumeration coverage and symmetry proofs. Tooling gate Phase-2 NOT_STARTED. Prefer deterministic no-network verification for claims and explicit failure on missing data.

S004 adds `validation/validate_s004.py` solely for repository consistency: JSON, IDs, references, fixed paper-derived intervals, handoff equality and gate checks. It performs no group-element enumeration, candidate search, solver work or mathematical certification and does not start Phase 2.
