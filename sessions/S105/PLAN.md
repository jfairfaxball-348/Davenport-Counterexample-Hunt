# S105 PLAN — 17 October 2026

One bounded numbered session: SEARCH_FIRST round 2 execution and the mandatory fallback decision.

1. Entry: reread live main SHA/tree, governance files, CI (ABSENT_NOT_PASS) and branch protection; archive INPUT/INPUT_MANIFEST.
2. Re-verify before activation: SHA-256 (LF/blob bytes) of `lns_engine.py`, `checker_a.py`, `checker_b.py` against CAM-0004/0005; rerun `test_zsf.py` and `preflight_lns.py` (overall PASS); record Python/numpy.
3. Activate CAM-0004 (n15, L43, seeds 104001–104006) and CAM-0005 (n20, L58, seeds 104101–104106) exactly as pre-registered (`--iterations 1200 --walltime 7200`, init uniform for the first three seeds and standard for the last three), 12 concurrent background processes.
4. Report actual per-worker results with standalone two-checker verdicts, move statistics and full-log hashes (as-written and LF-normalised). Quarantine any hit.
5. Fallback decision per the S105 prompt §2: if round 2 completes on both targets with no surviving candidate, write the experimental closeout and switch priority to SATURATION_FALLBACK; otherwise follow §1.4 / partial-round rules.
6. Sync ledgers, STATE, README/START_HERE; VALIDATION (validate_s105.py), SOURCE_MANIFEST, hostile REVIEW, PRECOMMIT CLOSEOUT; install the full S106 prompt.
7. One session branch, one atomic commit, ordinary PR merge without force, independent reread of main.
