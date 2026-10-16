# Tools policy

No search scripts, solver tests, Lean runs or sample reproductions were executed in S001. Future exact scripts must record versions/parameters/input, output SHA-256, implementation independence, full enumeration coverage and symmetry proofs. Tooling gate Phase-2 NOT_STARTED. Prefer deterministic no-network verification for claims and explicit failure on missing data.

S004 adds `validation/validate_s004.py` solely for repository consistency: JSON, IDs, references, fixed paper-derived intervals, handoff equality and gate checks. It performs no group-element enumeration, candidate search, solver work or mathematical certification and does not start Phase 2.

## S103 — exact zero-sumfree tooling (`tools/zsf/`), Phase-2 SCOPED PASS

- `checker_a.py`: numpy boolean subset-sum DP using the prefix criterion (CLM-0345). Also provides the incremental `Oracle` with exact rollback.
- `checker_b.py`: pure-Python exact subset-count DP. A sequence is zero-sumfree iff count[0]==1. Includes zero-sum witness extraction. It shares no code with A.
- `brute.py`: explicit subset enumeration, used for tests only.
- `test_zsf.py`: deterministic tests. Run with `python -I tools/zsf/test_zsf.py`; S103 output is in `sessions/S103/TEST_OUTPUT.json`.
- `bench.py`: primitive throughput on fixed inputs. It is not a search.
- `ils_engine.py`: the R1-ILS-1.0 HEURISTIC engine for CAM-0002/0003. Its SHA-256 is pinned in their pre-registrations.
- `preflight_engine.py`: runs the engine on settled n=4,5,6 only.

Environment: Python 3.12.10, numpy 1.26.4, Windows 11, i7-11800H (16 logical CPUs). Not built: SAT/DRAT/LRAT tooling, symmetry-reduced exhaustive enumeration, and a Lean 4 certificate pipeline. elan/lean are installed locally, but no Lean run was performed.
