# S108 checkpoint — 17 October 2026

**Priority: SATURATION_FALLBACK** (since S105). The search phase closed after two complete heuristic rounds reached only 3n−3; that is not a negative result. The open targets are D(C20³) = 58 (SAT20) and D(C15³) = 43 (SAT15).

**Fallback progress.** All results are elementary INTERNAL proofs, tested exactly on small groups, with no novelty claimed.
- **S106:** order-n multiplicities ≤ n−2 in any counterexample (CLM-0350).
- **S107:** the multiplicity-defect transfer (CLM-0355). At n=20, order-20 multiplicities ≤ 17 and order-10 multiplicities ≤ 8 (CLM-0357, conditional on two SOURCE_STATED values).
- **S108:** an unconditional small-support bound (CLM-0359). A zero-sumfree sequence over C_n^r with at most r+1 distinct values has length ≤ r(n−1), so **any counterexample needs at least 5 distinct values**. The 5-value case is a finite rank-2 lattice problem. Whether to attack it by a pre-registered exhaustive computation is an owner decision.

Claims 360, sources 34 (original 29 untouched), 30 frontier rows untouched, CI ABSENT_NOT_PASS. [S108 note](research/S108_SATURATION_FALLBACK_SMALL_SUPPORT.md) · [S107 note](research/S107_SATURATION_FALLBACK_MULTIPLICITY_DEFECT_TRANSFER.md) · [S106 note](research/S106_SATURATION_FALLBACK_MULTIPLICITY_QUOTIENT.md) · [search closeout](research/S105_SEARCH_FIRST_EXPERIMENTAL_CLOSEOUT.md) · [review](sessions/S108/REVIEW.md) · [S109 FUTURE](authoritative/NEXT_SESSION_PROMPT.md).
