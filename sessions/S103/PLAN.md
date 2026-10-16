# S103 PLAN — executed 16 October 2026

1. Authenticate live main, tree and parents; read the governance documents, the directive, the registry, the gates and the n15/n20 frontier provenance; check hosted CI.
2. Check the 2026 literature context for n15/n20 so that no obsolete target is chased (as happened with n6). Record the sources at their honest access levels.
3. Prove the prefix criterion and saturation equivalence (CLM-0345). Implement checker A, an algorithmically distinct checker B, and a brute-force reference.
4. Test: edge cases, wraparound, standard sequences, seeded A/B/brute cross-validation, oracle rollback, and exhaustive D reproduction on small settled groups. Benchmark the primitives on fixed inputs only.
5. Build the R1 heuristic engine and pre-flight it on settled n=4,5,6 only.
6. Record the scoped Phase-1 and Phase-2 gate decisions. Pre-register CAM-0002 and CAM-0003 with SHA-256-pinned code.
7. **Stopping rule:** do NOT run any n15/n20 search in S103. The protocol requires a committed PASS before advancing to Phase 3.
8. Sync the ledgers, write the full S104 prompt, then make one atomic commit, an ordinary PR merge, and an independent reread of main.
