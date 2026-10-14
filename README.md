# Rank-three Davenport counterexample hunt

Goal: test the conjecture $D(C_n^3)=3n-2$ by source-first reduction theory and eventually certified computation. An explicit zero-sumfree sequence of length $3n-2$ would refute equality. **No counterexample is claimed.**

Current completed session: **S029**. Indexed deletion counts now eliminate every exactly-four balanced family and force at least 2p blocks; arbitrary larger families remain unresolved. [Full proof](research/S029_INDEXED_CW_BLOCK_MULTIPLICITY.md). Older numbered summaries below are historical at their session cutoffs.

S004 corrected the frontier: **D(C6³)=16 is already a published exact result**, and classical 1969 families settle several other inherited interval entries. CAM-0001 remains **PROPOSED / NOT RUNNING**, with its premise obsolete and activation blocked. Phase 1 is **IN_PROGRESS**; Phases 2 and 3 have not started. No replacement tooling target is selected.

Read [authoritative/START_HERE.md](authoritative/START_HERE.md), [AGENTS.md](AGENTS.md), the [frontier](frontier/FRONTIER.md), and [claims](catalogue/CLAIMS.md) before doing any work. Current [next-session handoff](authoritative/NEXT_SESSION_PROMPT.md) must be invoked separately. Source facts, mathematical proofs, computations, heuristics and formal certificates are different evidence classes.

The [S004 primary-proof audit](research/S004_PRIMARY_PROOF_INPUTS.md) records the actual Grinsztajn written proof, definitive BSP offprint, remaining proof gaps, limited Sheikh thesis access, and Yiu's written proof and missing records in the downloaded source bundles. Literature exact values are source statements, not programme certificates. Remaining frontier intervals are n=15: 43..45, n=20: 58..59, n=21: 61..63, n=28: 82..83, and n=30: 88..90; none is asserted open merely because no exact source was found.

## S012 current record

S012 complete hand proof CLM-0084–0087 closes BSP2012 Lem5.2, including actual doubled alternatives and t=1,2,4. eta7 and rank-three plane deductions remain CONDITIONAL on original rank-two eta/Property C; stronger coefficient unproved. CLM-0088 proves only the actual GG1999 terminal trichotomy implication; full B=>C/Reiher inputs remain unproved. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; CAM-0001 PROPOSED / NOT RUNNING, activation BLOCKED by published n6=16. All 30 numerical rows unchanged; no openness inference. Hosted CI absent, NOT PASS. See authoritative/START_HERE.md and sessions/S012/CLOSEOUT.md. S013 is FUTURE UNEXECUTED and requires a new owner invocation.

## S029 current result

S029 CLM-0125/0126: elementary indexed Chevalley–Warning deletion counts force the complete number m of balanced b-zero-sum blocks to be a positive multiple of p and m>=2p, with 2r_i=m+(-1)^b mod p. At m=2p there is an exact two-degree census. Therefore EVERY exactly-four indexed family is impossible, independently of signature count. An arbitrary S028 no-short six-cell lift is NOT ruled out: it must create at least 2p-4 additional partial-cell b-blocks. First essential gap is m>=2p indexed families. Strong extraction and D2<=6p-6 remain UNPROVED; no rank-three D1/Dk numerical update, no novelty claim. See [indexed deletion proof](research/S029_INDEXED_CW_BLOCK_MULTIPLICITY.md). Phase1 remains IN_PROGRESS and the [S030 handoff](authoritative/NEXT_SESSION_PROMPT.md) is strictly future, unexecuted.


S057 (14 October 2026): exact FULL original seven-Fano-line lift iff inherited binary tensor; conditional 3-deletion kernel-basis/residual≤13 theorem for maximal C10³ atoms; four-block shadow packing dichotomy. D(C15³)=43 and D(C20³)=58 remain open; Phase1 active, S058 future. See authoritative/START_HERE.md and research/S057_*.

S058 (14 October 2026): a source-conditional common three-block C2³ kernel basis is now available across ALL THREE original quartet-switched maximal C10³ atoms simultaneously, leaving one C5³ projected zero-free residue of length≤11 with three atom completions. An actual P11 inverse and full original-index mixed-primary contradiction remain missing; C15 B-only first-character restriction is exact but does not reject S052 fixed decoration. No 43/58 equality, original G witness, certification or mathematical search. Phase1 IN_PROGRESS; S059 FUTURE. See [S058 results](research/S058_CROSS_FRONT_SYNTHESIS.md).
