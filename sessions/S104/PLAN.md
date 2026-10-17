# S104 PLAN — 17 October 2026

One bounded numbered session: SEARCH_FIRST round 1 execution plus round-2 pre-registration.

1. Entry: reread live main SHA/tree, governance files, CI (ABSENT_NOT_PASS) and branch protection; archive INPUT/INPUT_MANIFEST.
2. Re-verify before activation: SHA-256 of `tools/zsf/ils_engine.py`, `checker_a.py`, `checker_b.py` against both pre-registrations; rerun `python -I tools/zsf/test_zsf.py` (overall PASS required); record Python/numpy versions.
3. Activate CAM-0002 (n15, L43, seeds 103001–103006) and CAM-0003 (n20, L58, seeds 103101–103106) exactly as pre-registered: `--iterations 200000 --walltime 7200`, 12 concurrent background processes, checkpoints in `campaigns/CAM-000x/checkpoints/`. No mid-run parameter change.
4. Report actual per-worker results (status, iterations, elapsed, best length, histogram, best SHA-256, both checker verdicts). Quarantine any hit under `candidates/`.
5. Round 2 (NOT run in S104): implement R2-LNS-1.0 (method (c) exact remove-k/add-(k+1) deficiency repair with structured standard-sequence seeds for half the workers), pre-flight on settled groups n=3..6 only, record a Phase-2 gate extension, and pre-register CAM-0004 (n15) / CAM-0005 (n20) with pinned code hashes.
6. Update counters, STATE, ledgers, registry, README/START_HERE, tools README; write VALIDATION, SOURCE_MANIFEST, hostile REVIEW, PRECOMMIT CLOSEOUT; install the full S105 prompt.
7. One session branch, one atomic commit, ordinary PR merge without force, independent reread of main.
