# S105 PRECOMMIT CLOSEOUT — 17 October 2026

The owner's "Run next stage/session" authorises S105 only.
- Entry was live main `35ee471d8f48d6e183c10916ab8b2fd006148497` (tree `b3f30c6b…`), the S104 merge #108.
- Planned: ONE branch `session/S105-search-round2-execution`, ONE atomic authored commit, an ordinary PR merge, and an independent reread of main afterwards.
- **PRECOMMIT:** this file does not cite a future PR number, authored SHA or merge result.

**Outcome: active search session 2. Round 2 is COMPLETE with no hit. The fallback trigger is MET, and the priority is now SATURATION_FALLBACK.**
- **Re-verification:** pinned code SHA-256s match; `test_zsf.py` and `preflight_lns.py` PASS; Python/numpy are the registered versions.
- **CAM-0004 (n15, target 43):** 6/6 workers BUDGET_EXHAUSTED at 1200 iterations in 202–277 s. Best length 42 for every worker.
- **CAM-0005 (n20, target 58):** 6/6 workers BUDGET_EXHAUSTED at 1200 iterations in 276–446 s. Best length 57 for every worker.
- No truncation, no crash and no candidate. Every best sequence is two-checker zero-sumfree. Results are in `campaigns/CAM-000{4,5}/RESULT.json`, with the full logs committed.
- **Disclosed defect:** the S104 parameter hashes were computed with an int walltime. The logged parameters equal the registered values exactly.
- **Experimental closeout:** `research/S105_SEARCH_FIRST_EXPERIMENTAL_CLOSEOUT.md`.
- **Claims:** none new; the total stays at 347. Sources stay at 32 (original 29 untouched), and all 30 frontier rows are untouched.

**Not done, honestly stated:**
- Budget exhaustion is not a negative result.
- No exhaustive, SAT or Lean tooling exists.
- Review is INTERNAL_SAME_EXECUTOR, and CI is ABSENT_NOT_PASS.
- Final counters: setup 1, active 2, completed rounds 2.

No owner or external blocker remains. The full S106 saturation-fallback prompt is installed in `authoritative/NEXT_SESSION_PROMPT.md`.
