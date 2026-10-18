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

## S104 — R2-LNS-1.0 engine, Phase-2 SCOPED PASS extension

- `lns_engine.py`: R2-LNS-1.0 HEURISTIC engine for CAM-0004/0005 (round 2, pre-registered, not run in S104). Exact remove-k/add-(k+1) deficiency repair: the k=1 neighbourhood of each visited state is decided exhaustively with one exact FFT new-coverage evaluation per removed value (T extends by two terms iff some legal a has |Σ(T)|+newcov_T(a)<|G|); k=2 is sampled; plateau swaps use a tabu list; half the workers start from the structured standard sequence. Its SHA-256 is pinned in CAM-0004/0005.
- `preflight_lns.py`: settled groups n=3,4,5,6 only. 120 FFT two-addition decisions agree with exhaustive oracle enumeration; best length exactly 3n−3 for both seed families; determinism. Output: `sessions/S104/LNS_PREFLIGHT.json`.

## S106 — lemma tests

- `test_quotient_lemmas.py`: exact tests of CLM-0348..0351 on settled groups only. It checks the basis-completion construction for all order-n elements of (Z/n)³ (n ≤ 20), random A/B agreements for the quotient and multiplicity-(m−2) criteria, and an exhaustive n=3,4 instance of the multiplicity cap. Output: `sessions/S106/QUOTIENT_LEMMA_TESTS.json` (about 9 minutes, dominated by the exhaustive n=4 DFS).

## S107 — transfer lemma tests

- `test_transfer_lemmas.py`: exact tests of CLM-0353..0355 on small groups only.
  - It runs the proof's pure-element construction for all nonzero elements of (Z/n)³, n ≤ 20.
  - It checks random A/B agreements for the general multiplicity criterion.
  - It checks random constructed transfers through explicit quotient coordinates.
  - It is self-contained (the helpers are copied from `test_quotient_lemmas.py`), runs in about 20 s, and writes `sessions/S107/TRANSFER_LEMMA_TESTS.json`.

## S108 — small-support tests

- `test_small_support.py`: exact tests of CLM-0358..0360 on small groups only (C_n² for n ≤ 10, C_n³ for n ≤ 6).
  - For each tested support it computes the maximum zero-sumfree length by brute force over multiplicity vectors, using the kernel criterion, and cross-checks with checkers A/B.
  - It also checks every 4-value support in C2³ and C3³ exhaustively.
  - It takes about 15 s and writes `sessions/S108/SMALL_SUPPORT_TESTS.json`.

## S109 — support-≤5 exhaustive tools (Phase-2 extension)

- `support5_a.py` (algorithm A) and `support5_b.py` (algorithm B): two independent exhaustive tools. Each computes the exact maximum zero-sumfree length over C_n³ for sequences with at most 5 distinct values, over all free rank-2 relation modules up to S₅. See CLM-0361..0364.
- **Options:** `--shard k --nshards N`, `--threshold`, `--report-keys-at`, and `--checkpoint` (JSONL).
- **Pre-flight:** `sessions/S109/PREFLIGHT_SUMMARY.json`. The hashes are pinned in CAM-0006/0007.

## S113 — lemma tests (evidence only)

- `test_s113.py`: arithmetic tests of the S113 hand-proved lemmas (CLM-0380..0383) over integers and multiplicity patterns only. It checks the Theorem A constructions for all coprime odd pairs up to 401, brute-forces the (3,5)/(3,7) exceptions and the n = 20 system, compares five-valued survivors with `route_sieve.py` for pq ≤ 65, and checks the Theorem B/C witnesses. It takes about 35 s and writes `sessions/S113/S113_LEMMA_TESTS.json`.
