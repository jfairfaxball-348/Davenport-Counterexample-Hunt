# S103 checkpoint — 16 October 2026

**SEARCH_FIRST setup session.** The project now hunts directly for a zero-sumfree sequence of length 43 in C15³ or length 58 in C20³. S103 delivered:
- **Exact tooling** (`tools/zsf/`): checker A (numpy prefix DP, CLM-0345) and checker B (pure-Python exact subset counts), which are algorithmically distinct; a brute-force reference; and the R1 heuristic engine. All tests PASS.
- **Claims:** CLM-0345 (prefix criterion and the 57↔58 saturation equivalence) and CLM-0346 (standard n15/n20 sequences zero-sumfree and saturating, two checkers).
- **Gates:** a scoped Phase-1 PASS (search targets) and a scoped Phase-2 PASS (checkers and engine).
- **Campaigns:** CAM-0002 (n15) and CAM-0003 (n20) PREREGISTERED; activation is in S104.

**No target-group search has run yet**, and there is no candidate, bound or exclusion. Claims 346, sources 32 (original 29 untouched), 30 frontier rows untouched, CI ABSENT_NOT_PASS. [Tooling and pre-registration](research/S103_SEARCH_TOOLING_AND_PREREGISTRATION.md) · [review](sessions/S103/REVIEW.md) · [S104 FUTURE](authoritative/NEXT_SESSION_PROMPT.md). Previous S102 axial work (CLM-0344) is archived secondary context.
