# S103 PRECOMMIT CLOSEOUT — 16 October 2026

The owner's "run next session" authorises S103 only.
- Entry was live main `13ce00e0f04715418f99687a858892f02f3457b4` (tree `e63f39d5…`), the merge of the owner's SEARCH_FIRST directive #106 on top of S102 #105.
- Planned: ONE branch `session/S103-search-tooling-preregistration`, ONE atomic authored commit, an ordinary PR merge, and an independent reread of main afterwards.
- **PRECOMMIT:** this file does not cite a future PR number, authored SHA or merge result.

**Outcome: setup session.** The priority remains SEARCH_FIRST.
- **Exact tooling** in `tools/zsf/`: checker A (numpy, prefix criterion) and checker B (pure-Python exact subset counting, a different algorithm), a brute-force reference, and the R1-ILS-1.0 heuristic engine.
- **Tests run:** all PASS (`sessions/S103/TEST_OUTPUT.json`). This includes 2300 seeded A/B/brute agreements, standard-sequence saturation at n15/n20, oracle rollback, and exhaustive reproduction of D for six small settled groups.
- **Benchmark:** about 55k exact push/pop per second per process. Engine pre-flight on settled n=4,5,6 reaches exactly 3n−3.
- **Claims:** CLM-0345 PROGRAMME_PROVED (prefix criterion and the 57↔58 saturation equivalence) and CLM-0346 COMPUTED_EXACT (standard sequences, two checkers).
- **Sources:** SRC-0030..0032 record 2026 literature context, which leaves both targets live.
- **Gates:** scoped Phase-1 PASS (search targets) and scoped Phase-2 PASS (checkers and engine). CAM-0002 (n15 L43) and CAM-0003 (n20 L58) are PREREGISTERED with SHA-256-pinned code.

**Not done, honestly stated:**
- No n15/n20 search ran, under the committed-PASS protocol. There is no maximum length, rate or candidate for the targets.
- No Lean, SAT or exhaustive tooling was built.
- Review is INTERNAL_SAME_EXECUTOR, and CI is ABSENT_NOT_PASS.
- Counters: setup 1, active 0, rounds 0.
- The original 29 sources and 30 frontier rows are untouched.

No owner or external blocker remains. The full S104 prompt is installed in `authoritative/NEXT_SESSION_PROMPT.md`: activate round 1 on both targets, then pre-register a materially different round 2.
