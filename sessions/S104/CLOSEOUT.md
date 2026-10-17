# S104 PRECOMMIT CLOSEOUT — 17 October 2026

The owner's "run next session" authorises S104 only.
- Entry was live main `eec2f529c3c5fe5cb71a27eb83d52c7696c8569a` (tree `c06780ea…`), the S103 merge #107.
- Planned: ONE branch `session/S104-search-round1-execution`, ONE atomic authored commit, an ordinary PR merge, and an independent reread of main afterwards.
- **PRECOMMIT:** this file does not cite a future PR number, authored SHA or merge result.

**Outcome: active search session 1. Round 1 is COMPLETE, with no hit.**
- **Re-verification:** pinned code SHA-256s match, `test_zsf.py` PASS, and Python 3.12.10 / numpy 1.26.4 match the registration.
- **CAM-0002 (n15, target 43):** 6/6 workers BUDGET_EXHAUSTED at 200,000 iterations in 918–963 s. Best length 42 for every worker.
- **CAM-0003 (n20, target 58):** 6/6 workers BUDGET_EXHAUSTED at 200,000 iterations in 1306–1313 s. Best length 57 for every worker.
- No truncation, no crash and no candidate. All best sequences are zero-sumfree by checkers A and B standalone. Results are in `campaigns/CAM-000{2,3}/RESULT.json` and the full logs are committed.
- **Round 2 (not run):** R2-LNS-1.0 implemented (`tools/zsf/lns_engine.py`) and pre-flighted on settled n=3..6. Phase-2 scoped PASS extended. CAM-0004 (n15) and CAM-0005 (n20) PREREGISTERED with pinned code and parameter hashes.
- **Claims:** CLM-0347 PROGRAMME_PROVED (two-term extension criterion), 346→347.
- Sources stay at 32, with the original 29 untouched. All 30 frontier rows are untouched.

**Not done, honestly stated:**
- Budget exhaustion is not a negative result.
- No exhaustive, SAT or Lean tooling exists yet.
- Review is INTERNAL_SAME_EXECUTOR, and CI is ABSENT_NOT_PASS.
- Counters: setup 1, active 1, completed rounds 1. The fallback trigger is not met.

No owner or external blocker remains. The full S105 prompt is installed in `authoritative/NEXT_SESSION_PROMPT.md`: activate round 2 on both targets, then apply the two-round fallback test.
