# S107 PRECOMMIT CLOSEOUT — 17 October 2026

The owner's instruction ("Did you close out this session? If so, start next") authorises S107 only. S106 closeout was confirmed first: main `8788f57` was reread and the S106 validator passed.
- Entry was live main `8788f57ff9ce9c3b4c9447df98550cb9e9bc26cd` (tree `8f20b23b…`), the S106 merge #110.
- Planned: ONE branch `session/S107-multiplicity-defect-reduction`, ONE atomic authored commit, an ordinary PR merge, and an independent reread of main afterwards.
- **PRECOMMIT:** this file does not cite a future PR number, authored SHA or merge result.

**Outcome: SATURATION_FALLBACK session 2.**
- **Claims (352→357):**
  - CLM-0353: general multiplicity criterion.
  - CLM-0354: pure elements.
  - CLM-0355: multiplicity-defect transfer to C_{nd/m} ⊕ C_n ⊕ C_n.
  - CLM-0356: SOURCE_STATED D(C2⊕C2m⊕C2mn) = 2m+2mn.
  - CLM-0357: at n=20, order-20 multiplicities ≤ 17 and order-10 multiplicities ≤ 8 (conditional on CLM-0352/0356). This closes the S106 open case at n=20.
- **Tests:** independent exact tests on small groups PASS.
- The frontier is unchanged, and the original 29 sources and 30 rows are untouched.

**Honestly stated:**
- At n=15 nothing beyond CLM-0350 is unconditional. The next step needs D(C3⊕C15⊕C15) or D(C5⊕C15⊕C15), both unknown.
- The caps do not reduce SAT20 to a small family, so the search-reopen condition is not met.
- Review is INTERNAL_SAME_EXECUTOR, and CI is ABSENT_NOT_PASS.
- Counters: search frozen (setup 1, active 2, rounds 2); fallback sessions 2.

No owner or external blocker remains. The full S108 prompt is installed in `authoritative/NEXT_SESSION_PROMPT.md`.
