# S104 checkpoint — 17 October 2026

**SEARCH_FIRST, active search session 1.** The project hunts directly for a zero-sumfree sequence of length 43 in C15³ or length 58 in C20³. S104 delivered:
- **Round 1 executed** exactly as pre-registered: CAM-0002 (n15) and CAM-0003 (n20), R1-ILS-1.0, 6 workers each × 200,000 iterations. All 12 workers BUDGET_EXHAUSTED, no truncation, no crash. **Best lengths 42 and 57 (= 3n−3); no hit, no candidate.** Both checkers confirm every best sequence standalone.
- **Round 2 pre-registered** (not run): CAM-0004 (n15) and CAM-0005 (n20), R2-LNS-1.0, an exact remove-k/add-(k+1) deficiency-repair search with structured seeds, pre-flighted on settled groups only. Phase-2 scoped PASS extended to this engine.
- **Claim:** CLM-0347 (two-term extension criterion, elementary corollary of CLM-0345).

Budget exhaustion is **not** a negative result. Counters: setup 1, active search sessions 1, completed rounds 1. Claims 347, sources 32 (original 29 untouched), 30 frontier rows untouched, CI ABSENT_NOT_PASS. [Results and round-2 pre-registration](research/S104_ROUND1_RESULTS_AND_ROUND2_PREREGISTRATION.md) · [review](sessions/S104/REVIEW.md) · [S105 FUTURE](authoritative/NEXT_SESSION_PROMPT.md). Previous: [S103 tooling](research/S103_SEARCH_TOOLING_AND_PREREGISTRATION.md).
