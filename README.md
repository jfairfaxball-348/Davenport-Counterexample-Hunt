# S105 checkpoint — 17 October 2026

**SEARCH_FIRST closed; priority is now SATURATION_FALLBACK.** The project hunted directly for a zero-sumfree sequence of length 43 in C15³ or length 58 in C20³ over two materially different, pre-registered HEURISTIC rounds:
- **Round 1 (S104, R1-ILS-1.0):** 12 workers × 200,000 iterations. Best lengths 42 / 57 = 3n−3, no hit.
- **Round 2 (S105, R2-LNS-1.0):** an exact remove-k/add-(k+1) repair search (CLM-0347), 12 workers × 1200 iterations. Best lengths 42 / 57 = 3n−3, no hit.
- All 24 workers exhausted their budgets, with no truncation or crash. Every best sequence was rechecked by two exact checkers. There is no candidate.

Under the owner's directive, two such rounds without a candidate, exclusion or structural theorem trigger the fallback. Budget exhaustion is **not** a negative result: the frontier is unchanged and nothing is excluded. The open fallback statement is that every zero-sumfree 57-term sequence in C20³ has subset sums equal to the whole group, equivalently D(C20³)=58.

Counters: setup 1, active search sessions 2, completed rounds 2. Claims 347, sources 32 (original 29 untouched), 30 frontier rows untouched, CI ABSENT_NOT_PASS. [Experimental closeout](research/S105_SEARCH_FIRST_EXPERIMENTAL_CLOSEOUT.md) · [round 1 and R2 design](research/S104_ROUND1_RESULTS_AND_ROUND2_PREREGISTRATION.md) · [review](sessions/S105/REVIEW.md) · [S106 FUTURE](authoritative/NEXT_SESSION_PROMPT.md).
