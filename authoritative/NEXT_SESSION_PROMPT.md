# S114 — PROOF-ONLY: BEYOND ROUTE COUNTING (FUTURE / NOT EXECUTED)

**Owner steering in force:**
- 18 October 2026, after S110: generalise to all n or to families of n; Lean deferred.
- 18 October 2026, after S112: a **non-brute-force, generalised rule or proof, not more enumeration**.

Deliverables are **theorems with closed-form hypotheses on n, proved by hand**. Computation is allowed **only** to test a stated lemma on small settled groups, or to search for a counterexample to a conjectured lemma. It is never the result itself. No sieve tables, residue censuses or per-n case lists are deliverables. The CLM-0378 residue is **not** to be enumerated further.

**Active priority: SATURATION_FALLBACK** (since S105). General search stays closed, and any campaign needs a new owner decision.
- Run S114 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters, the search-reopen condition and both steerings into future prompts.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume the S113 merge is still the head.
- Read:
  - `AGENTS.md`;
  - `authoritative/STATE.json` (`counterexample_hunt_strategy` including `owner_steering`, `s112_result`, `s113_result`);
  - **`research/S111_CONSOLIDATION_REVIEW.md` (the entry point)**, `research/S113_CLOSED_FORM_ROUTE_THEOREMS.md`, `research/S112_MULTI_ROUTE_SIEVE.md`, `research/S108_SATURATION_FALLBACK_SMALL_SUPPORT.md` and `research/S109_SUPPORT5_EXHAUSTIVE_TOOLING.md`;
  - `catalogue/CLAIMS.md` (CLM-0345..0383);
  - `docs/FAILURE_AND_LESSON_LEDGER.md` (S106–S113).
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S114/INPUT.md` and `INPUT_MANIFEST.json`. Paraphrase product or model names in owner text (AGENTS rule 10), and grep the staged diff for them before committing. The commit message must carry no model names.
- **Git:**
  - On the owner's local machine, push through Git Credential Manager as `jfairfaxball-348` with the one-command override recorded in the S113 prompt (blob `c8837d56032f02313054da55faad17d450f1aa26`). Do not change the stored configuration.
  - In a hosted container, use the assigned session branch and the hosted git proxy.
  - Either way: one atomic commit, an ordinary PR merge without force, and an independent reread of main.
- **Before committing,** verify that every intended file change is on disk. Re-run any test whose code changed after the run. **Never kill processes by image name or command-line pattern** (S113 lesson); stop background jobs through the harness or by an explicit PID.

**State at entry:**
- Claims 383. Sources 34 (original 29 untouched). Frontier 30 rows untouched.
- No campaign is active or pre-registered.
- Search counters frozen (setup 1, active 2, rounds 2). Fallback sessions 8.
- **Targets (OPEN):** SAT20, i.e. D(C20³) = 58, and SAT15, i.e. D(C15³) = 43.

**What S113 established:**
- Route counting is **sharp and exhausted** on odd n = p^a q^b and on n = 4p (CLM-0383).
- Every surviving 5-valued pattern at odd n = AB has all values of order n, and at each route a the leftover is exactly 4a−2 terms, with multiplicities r_i = a−1−s_i and Σs_i = a−3 (CLM-0381).
- A bound D₂(C_a³) ≤ 4a−2 would close everything at support 5, but the unrestricted version fails for a = 3, 5 (CLM-0373).

## 1. S114 work (proof-only)

**(A) Restricted two-disjoint lemma at the leftover level.**
- Formulate TWO*(a): every sequence over C_a³ with five distinct values whose multiplicities are a−1−s_i, with Σs_i = a−3, has two disjoint nonempty zero-sums, **or** the block decomposition can be re-chosen to gain one block.
- The re-choice may mix values whose combined sum lies in aG; this is where the actual images enter.
- Prove it by hand for a family of primes, or find the exact obstruction. Small-group tests on C₃³, C₅³ and C₇³ are allowed as evidence only.
- A proof for prime a would give the support-5 bound for every n = pq (with a cap where needed).

**(B) The relation-module route for support 5 at n = pq.**
- Combine CLM-0358 (box/kernel criterion) and CLM-0362 (CRT: K = K_p ⊕ K_q) with the S113 structure: all values of order n, and α_i ≡ −1−s_i (mod p) with Σs_i = p−3, likewise mod q.
- Goal: a hand proof that no rank-2 free summand K ⊂ (Z/n)⁵ avoids every box ∏[0, α_i] for such α, for a closed-form family of (p, q).
- Identify exactly which K-shapes are not excluded.

**(C) Even n beyond 4p.**
- For n = 8p and n = 2^e·m, determine the forced number of values from the routes that remain (route 2 is absent when D(C_{n/2}³) is unknown).
- State it as a formula with exact survivors, as in CLM-0382/0383.

**(D) Lean certification:** deferred by owner steering; do not start it.

**Honesty rules.**
- Failed attempts go in the failure ledger with their exact obstruction, stated symbolically.
- Do not upgrade inherited or source claims, and do not relabel CLM-0366/0367/0375/0377.
- Never state SAT20/SAT15 or a D value.
- No target-group computation, and no new enumeration as a result.

## 2. Deliverables and close

- Create S114 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (`validation/validate_s114.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note containing the theorems and full hand proofs. Lemma tests are optional and are evidence only.
- Update: claims, ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 9), the consolidation review (in place, remaining the single entry point), README and START_HERE.
- Leave the frontier unchanged.
- Install a FULL S115 prompt.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, a single solver as a certification, or a family-restricted exclusion as SAT20/SAT15.
