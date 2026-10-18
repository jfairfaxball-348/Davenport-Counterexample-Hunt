# S113 — PROOF-ONLY GENERALISATION: CLOSED-FORM RULES FROM THE BLOCK ROUTES (FUTURE / NOT EXECUTED)

**Owner steering (18 October 2026, after S112; installed by a non-session governance commit):** the owner wants a **non-brute-force, generalised rule or proof, not more enumeration**. This replaces the unexecuted S113 prompt, which planned sharper sieve constants, a re-sieve and image-level analysis of the residue.
- S113's deliverables are **theorems with closed-form hypotheses on n**, proved by hand.
- Computation is allowed **only** to test a stated lemma on small settled groups, or to search for a counterexample to a conjectured lemma. It is never the result itself.
- No new sieve tables, residue censuses or per-n case lists are deliverables.
- The CLM-0378 residue is **not** to be enumerated further.

The earlier 18 October steering (generalise to all n or to families of n; Lean deferred) stays in force.

**Active priority: SATURATION_FALLBACK** (since S105). General search stays closed, and any campaign needs a new owner decision.
- Run S113 only on a separate later owner instruction to run the next session, and run only ONE numbered session per invocation.
- Carry the priority, the frozen search counters, the search-reopen condition and both steerings into future prompts.

## 0. Entry and governance

Work in repository `jfairfaxball-348/Davenport-Counterexample-Hunt`.
- At entry, independently reread the LIVE main SHA and the actual Git root tree. Do not assume this governance merge is still the head.
- Read:
  - `AGENTS.md`;
  - `authoritative/STATE.json` (`counterexample_hunt_strategy` including `owner_steering`, `s111_result`, `s112_result`);
  - **`research/S111_CONSOLIDATION_REVIEW.md` (the entry point)**, `research/S112_MULTI_ROUTE_SIEVE.md` and `research/S111_R_PLUS_TWO_AND_EVEN_CAPS.md`;
  - `catalogue/CLAIMS.md` (CLM-0345..0378);
  - `docs/FAILURE_AND_LESSON_LEDGER.md` (S106–S112).
- Check hosted CI and branch protection. If CI is absent, record it as ABSENT_NOT_PASS.
- Archive the invocation in `sessions/S113/INPUT.md` and `INPUT_MANIFEST.json`. Paraphrase product or model names in owner text (AGENTS rule 10), and grep the staged diff for them before committing. The commit message must carry no model names or attribution trailers naming a model.
- **Git credentials:** the gh CLI keyring account (`jball348-svg`) has no write access. Push through Git Credential Manager as `jfairfaxball-348` with a one-command override (`git -c credential.https://github.com.helper= -c credential.https://github.com.helper=manager -c credential.https://github.com.username=jfairfaxball-348 push …`). Open and merge the PR with `GH_TOKEN` taken from that credential for that command only. Do not change the stored configuration.
- **Before committing,** verify that every intended file change is on disk. Re-run any test whose code changed after the run. Never kill processes by image name, and resolve the PID column explicitly before any kill.

**State at entry:**
- Claims 378. Sources 34 (original 29 untouched). Frontier 30 rows untouched.
- No campaign is active or pre-registered.
- Search counters frozen (setup 1, active 2, rounds 2). Fallback sessions 7.
- **Targets (OPEN):** SAT20, i.e. D(C20³) = 58, and SAT15, i.e. D(C15³) = 43.

**What is already a general rule:**
- CLM-0368: even-n caps.
- CLM-0370: the r+2-values bound at every n = 2b with D(C_b^r) known, in any rank.
- CLM-0372: even-n parity structure.
- CLM-0374: the multi-route block criterion, as a lemma.
- CLM-0376: the n = 15 hand proof.

**What is not:** CLM-0375/0377/0378 rest on per-n arithmetic enumeration. S113 should replace that dependence with proofs where it can.

## 1. S113 work (proof-only)

**(A) The two-prime theorem (n = pq, p < q distinct primes).**
- Premises are only CLM-0142 (D(C_p³), D(C_q³)) and CLM-0369/0374.
- The S112 hand proof shows that a 5-valued (3n−2)-sequence on which **both** routes fail must satisfy, with x_i = α_i + 1:
  - x_i = p·u_i − s_i = q·v_i − t_i, with s_i ∈ [0, p−1] and t_i ∈ [0, q−1];
  - Σs_i = p−3 and Σt_i = q−3;
  - Σu_i = 3q+1 and Σv_i = 3p+1;
  - 1 ≤ x_i ≤ n, or x_i ≤ n−1 with the CLM-0350 cap.
- **Goal:** a closed-form characterisation, by hand, of the pairs (p, q) for which this system is infeasible. That would give the 5-value bound by proof for every such n = pq, with n = 15 as the first case.
- Where it is feasible, determine symbolically whether the D₂ lever (CLM-0143: D₂(C_p³) ≤ 5p−3) or the CLM-0350 cap closes it. State the exact obstruction as a family.
- Then extend to n = p^a q^b using prime-power routes (CLM-0039 Olson, SOURCE_STATED).

**(B) A general theorem for n = 4p, and more widely n = 2^k·m.**
- Turn S112's "n = 20 needs ≥ 7 distinct values" into a hand proof valid for a whole family, for example every n = 4p with p an odd prime.
- Use routes 2, 4 and p, the even caps (CLM-0368) and the parity structure (CLM-0372).
- State the premises exactly: D(C_{2p}³) (CLM-0065), D(C₄³) (CLM-0039), D(C_p³) (CLM-0142).
- Identify precisely where the argument needs a specific p, if anywhere.

**(C) A formula, not a table.**
- Prove a lower bound on the number of distinct values that the multi-route argument forces, as an explicit function of the factorisation of n. For example, average the route deficits over all usable routes, or use the CRT on the residues α_i mod a.
- Compare it symbolically with the S112 numbers only as a sanity check.

**(D) Lean certification:** deferred by owner steering; do not start it.

**Honesty rules.**
- Failed attempts go in the failure ledger with their exact obstruction, stated symbolically.
- Do not upgrade inherited or source claims, and do not relabel CLM-0366/0367/0375/0377.
- Never state SAT20/SAT15 or a D value.
- No target-group computation, and no new enumeration as a result.

## 2. Deliverables and close

- Create S113 INPUT, INPUT_MANIFEST, PLAN, VALIDATION (`validation/validate_s113.py`), SOURCE_MANIFEST, a hostile REVIEW and a PRECOMMIT CLOSEOUT.
- Write a research note containing the theorems and full hand proofs. Small-group tests of the lemmas are optional and are evidence only.
- Update: claims, ledgers, STATE (`counterexample_hunt_strategy`: number_of_fallback_sessions 8), the consolidation review (in place, remaining the single entry point), README and START_HERE.
- Leave the frontier unchanged.
- Install a FULL S114 prompt that continues proof-only work.
- Close with one session branch, one atomic authored commit, an ordinary PR merge without force, and an independent reread of main afterwards.
- No model names in files or commits. CI absence is ABSENT_NOT_PASS.

**Non-negotiable intent:** find or rigorously exclude a real counterexample. Never present a heuristic budget as a proof, a literature statement as a programme proof, a single solver as a certification, or a family-restricted exclusion as SAT20/SAT15.
