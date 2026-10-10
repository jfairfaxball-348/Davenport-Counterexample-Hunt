# Repository rules

1. The committed main branch is the only authority. Check remote SHA and all relevant governance documents before writes. Only one bounded numbered session per invocation.
2. Rank-three target: a zero-sumfree length $3n-2$ sequence in $C_n^3$. A candidate is **never** certified by one solver, a plausible construction, or a copied transcript.
3. Every nontrivial source has stable SRC-#### identifier and access level: METADATA_ONLY, ABSTRACT_INSPECTED, STATEMENT_INSPECTED, PROOF_INSPECTED or SECONDARY_ONLY. Record direct observations and links; no copyrighted PDF copies.
4. Every claim has stable CLM-#### identifier and one status: SOURCE_STATED, PROGRAMME_PROVED, COMPUTED_EXACT, HEURISTIC, FORMALLY_CERTIFIED, INHERITED_UNVERIFIED. A statement in the literature is not a programme proof.
5. A certified counterexample needs canonical sequence + SHA-256, two independent algorithmically distinct zero-sum-freeness checks, Lean 4 kernel verification, and a cold re-check in a later session. Candidates stay in candidates/.
6. Negative results: proved complete symmetry reductions AND checked DRAT/LRAT UNSAT certificate or two independently implemented exhaustive algorithms; code, versions, parameters and hashes.
7. Searches require a pre-registered campaign with explicit bounded search space, reductions, completeness class, budget, checkpoint/stopping rule. No searches in S001.
8. Sequential phases 0 governance, 1 frontier, 2 reductions/tooling, 3 campaigns, 4 owner-gated certification/writeup; record a PASS gate before advancing.
9. One atomic session-branch commit and PR/merge without force; independently verify remote main SHA. Never silently upgrade evidence or fabricate priority.
10. No named results after owner/programme; no third-party contact, public submission, Palomar, publication, or new project without explicit owner authorization. No model names in files or commits.
11. On close, sync all JSON and Markdown ledgers, write closeout and full next prompt. If owner/external blocker, describe precise action and do not write a next-session prompt.
