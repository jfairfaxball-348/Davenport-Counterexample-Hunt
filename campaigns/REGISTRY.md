# Campaign registry

Every campaign **before activation** must state: exact target, search space, method, proved symmetry reductions, completeness class EXHAUSTIVE / PARTIAL / HEURISTIC, bounded budget, persisted checkpoint format and stopping rule. A PROPOSED record never authorizes execution.

## CAM-0001 — n=6 skeleton–lift, PROPOSED / NOT RUNNING

**Current S004 disposition (2026-10-11): activation blocked; premise obsolete.** Published Schmid2011 Theorem4.1(2) gives D(C6³)=16 (SRC-0022 / CLM-0064), corroborated by original 1969 exact families. Thus a length-16 zero-sumfree target is excluded by the source-stated theorem. Preserve this campaign as PROPOSED / NOT RUNNING by owner instruction; withdraw its target recommendation. No replacement campaign, solver, orbit enumeration or tooling is authorized. Phase 1 IN_PROGRESS, Phases 2/3 NOT_STARTED. The proposal and annotations below are historical provenance, not current activation instructions.

### Historical proposal
- Target: decide whether $C_6^3$ has a zero-sumfree sequence of length 16; a certified example would imply $D(C_6^3)>16$.
- Search space (conditional): all length-16 multisequences over $C_3^3$ admitting <=3 disjoint nonempty zero-sum subsequences, then all $C_2^3$ labels satisfying nonzero projected lifts; inherited 5553 GL(3,3) skeleton orbits are **unverified AND affected by S002 corrected D4(C3^3)=18, not 17**. Neither this count nor the old threshold establishes completeness.
- Proposed method: independently verify skeleton enumeration and GL(3,3) orbit completeness; encode each mod-2 zero-sum avoidance condition into SAT or exact enumeration; cross-check with independent lifting algorithm.
- Symmetry: GL(3,3) on skeletons and GL(3,2) on labels are candidate reductions **not yet proved nor implemented**; retain all branches until proof.
- Completeness class: **PARTIAL (PROPOSED)**; exhaustive designation blocked on proofs of enumeration, orbit reductions and SAT correctness.
- Resource budget: maximum 1 bounded campaign session after separate Phase-2 PASS; per-branch CPU/time and instance limits to be fixed at start of an owner-authorized Phase-3 step.
- Checkpoint format: `campaigns/CAM-0001/checkpoints/*.jsonl` with canonical orbit representatives, SHA-256, covered indices, algorithm version, instance ID, solver result, certificate path/hash and deterministic resume offset.
- Stopping rule: stop when allocated session budget exhausted, a candidate is quarantined, or all pre-registered instances independently certified; never infer global UNSAT from a timeout.
- Precondition: Phase-1 and Phase-2 PASS with executable independent verification, not met in S001.
- S001 work: **none**. No SAT, no search, no solver run.

### S002 gate annotation (2026-10-10)
- **PROPOSED / NOT RUNNING.** n=6 target interval 16..17 independently derived; no candidate evaluated.
- The original source states D4(C3^3)=18, not inherited 17; any 5553-orbit list must be revalidated from first principles. 48 Boolean variables are simply 16×3 CRT labels, not an activated SAT instance.
- Prerequisites remain Phase-1 PASS, then Phase-2 certified tooling and independent symmetry/exhaustiveness proof. S003 is a Phase-1 source-proof session only.

### S003 — PROPOSED / NOT RUNNING (2026-10-11)
Phase 1 IN_PROGRESS, Phases 2 and 3 NOT_STARTED. No SAT/ILP, candidates, orbitting, solver, enumeration, certification or computed count. The inherited 5553 orbit claim has no completeness provenance and used the wrong D4=17. S003 recommended n=6 at 16..17; **S004 withdraws that recommendation** on the published exact theorem above.

### S005 disposition — 2026-10-11

CAM-0001 **PROPOSED / NOT RUNNING**, activation BLOCKED: Schmid2011 source-stated exact D(C6³)=16 rules out its zero-sumfree length-16 premise. S005 performed source-proof and provenance review only, no activation, solver, enumeration, candidate or new campaign. Phase1 IN_PROGRESS; Phases 2/3 NOT_STARTED; no replacement target selected.

### S006 disposition — 2026-10-11

CAM-0001 stays **PROPOSED / NOT RUNNING**, activation **BLOCKED** by published D(C6³)=16. S006 p7 source-audit repair has no bearing on target activation. No replacement campaign or Phase-2 tooling. Phases2/3 NOT_STARTED; no numerical search, solver, candidate, orbit or certified negative.

### S007 status — 2026-10-11

CAM-0001 remains **PROPOSED / NOT RUNNING**, activation **BLOCKED** by source-stated exact D(C6³)=16; S007 mathematical source audit changes no premise. No replacement campaign/tooling, SAT/ILP, numerical search, orbit count, candidate or exhaustive negative. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED.

### S008 disposition — 2026-10-11

CAM-0001 **PROPOSED / NOT RUNNING**, activation **BLOCKED**: original Schmid2011 exact D(C6³)=16 invalidates the length-16 zero-sumfree premise. S008 only checked sources and symbolic conditional sublemmas CLM-0077/0078; no replacement, tooling, numerical search, solver, campaign, candidate or exhaustive negative. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED.

### S009 disposition — 2026-10-11

CAM-0001 remains **PROPOSED / NOT RUNNING**, activation **BLOCKED** by source-stated published Schmid2011 D(C6³)=16 and corroborating original 1969 exact families. Conditional p7 CLM-0079 and original-paper SRC-0026 bibliographical finding do not affect or activate this campaign. **Phase1 IN_PROGRESS; Phase2/3 NOT_STARTED.** No target replacement, solver, mathematical enumeration, candidate or certification.

### S010 disposition — 2026-10-11

CAM-0001 still **PROPOSED / NOT RUNNING** with activation BLOCKED by source-stated published Schmid2011 exact D(C6³)=16. CLM-0081 is a rank-two p7 intermediate source hand proof; SRC-0026 a 1999 proof access update. Neither authorises n6 search, replacement target, Phase2/3, SAT/ILP, candidate or verification campaign.

### S011 disposition — 2026-10-11

CAM-0001 **PROPOSED / NOT RUNNING**, activation **BLOCKED** by published Schmid2011 `D(C6³)=16`; its length-16 zero-sumfree target is obsolete on the source record. CLM-0083 is only p7 paper projective geometry and cannot reactivate it. NO Phase2/3, replacement campaign/tool target, mathematical numerical search, solver, orbit enumeration, candidate or certificate. Phase1 IN_PROGRESS.

### S012 disposition — 2026-10-11

CAM-0001 **PROPOSED / NOT RUNNING**, activation **BLOCKED** by published D(C6³)=16. Complete p7 rank-two Lem5.2 changes no campaign premise. No replacement campaign, target, candidate, certificate or source-code run. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED.

## S013 — 2026-10-11

S013 CLM-0089–0093 hand-prove rank-two p/2p extraction, D(Cp²)=2p−1, eta<=3p−2/long-zero short block, original Lem10.6 and the full B=>C implication CONDITIONAL on Property B. Complete S012 p7 Lem5.2 preserved. FIRST unconditional prerequisite is Reiher Property B through unrebuilt strategic-equation/geometric chain; stronger coefficient unproved. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; CAM-0001 PROPOSED / NOT RUNNING activation BLOCKED by published n6=16. All 30 numeric rows unchanged; no openness inference. Zero hosted CI, NOT PASS. No owner-action blocker identified; source-access limitations remain research obligations. S014 strictly FUTURE UNEXECUTED.

### S014 — PROPOSED / NOT RUNNING, ACTIVATION BLOCKED

No replacement search/tool/campaign. Published n6=16 blocks inherited CAM-0001; first Reiher proof package does not change its premise.

### S015 — PROPOSED / NOT RUNNING, ACTIVATION BLOCKED

Original rank-two Reiher CLM-0098–0100 does not change published Schmid2011 n6=16; CAM-0001 length-16 zero-sumfree premise remains obsolete. No activation, replacement campaign, target, mathematical computation, tooling, candidate or certificate; Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED.

### S016 — CAM-0001 remains PROPOSED / NOT RUNNING, ACTIVATION BLOCKED

Independent rank-two Reiher Section6 CLM-0101/0102 do not change published source-stated Schmid2011 D(C6³)=16. Historical length-16 zero-sumfree CAM-0001 premise remains obsolete. No replacement campaign/target, Phase2/3, mathematical numerical computation/search, candidate, solver, code, Lean or certificate. Phase1 IN_PROGRESS.

### S017 — CAM-0001 PROPOSED / NOT RUNNING, ACTIVATION BLOCKED

S017 independently reconstructs ONLY original Reiher Proposition8.1, CLM-0103: both η²=1 configurations, four genuine indexed conditional µ=1 identities, exact strategic equation and printed multipliers giving 2(1−x−y)=0; three DISTINCT ORIGINAL collinear A,B,C permit proved Prop5.1, including p5. STOP before Section9. Universal Property B, unconditional Property C, eta(C7³)≤116 and rank-three conjecture NOT proved. All 30 numeric/evidence rows unchanged; Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED / NOT RUNNING activation BLOCKED by published n6=16. Zero hosted checks NOT CI PASS. No replacement campaign, target, tooling, candidate or certificate.

### S018 — CAM-0001 remains PROPOSED / NOT RUNNING, ACTIVATION BLOCKED

S018 independently reconstructs ONLY original Reiher Observation9.1 and Lemma9.2 over arbitrary K, char(K) != 2 (CLM-0104/0105), with dependent-X,Y basis case, exact conic equations, fourteen-sum collisions, all 4-of-7 pair line subcases, all 6-of-7 proper conic relabellings and verified printed typo Observation10.1 -> Observation9.1. STOP at Lem9.2: Section9 quartic/Obs9.4/9.5/Lem9.6 and Prop10.1 remain unproved; no universal Property B, unconditional Property C, eta(C7^3)<=116 or rank-three theorem. Thirty frontier values/evidence classes unchanged; Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED / NOT RUNNING, activation BLOCKED by published n6=16. Zero hosted CI is NOT PASS.

No replacement campaign, target, solver, candidate, source-code execution or certificate.

### S019 — CAM-0001 remains PROPOSED / NOT RUNNING, activation BLOCKED

Published Schmid2011 source-stated D(C6³)=16 makes its inherited length16 zero-sumfree campaign obsolete. Original Reiher rank-two geometry CLM-0106–0108 cannot reactivate it. No Phase2/3, replacement campaign, new target, search, candidate, certificate or numerical mathematical computation.

### S020 — CAM-0001 remains PROPOSED / NOT RUNNING, activation BLOCKED

Published Schmid2011 source-stated n6=16 makes the inherited length16 zero-sumfree premise obsolete. S020 rank-two Proposition10.1 cannot reactivate this rank-three campaign. No Phase2/3, replacement target/campaign, code, candidate, solver, Lean, certificate or numerical mathematical search.

### S021 — CAM-0001 PROPOSED / NOT RUNNING / ACTIVATION BLOCKED

Source-stated published D(C6³)=16 still invalidates the inherited length16 zero-sumfree premise. Universal prime Property B is rank TWO and does not change this fact. No Phase2/3, replacement campaign/target, mathematical search, solver, code, candidate, Lean or certificate.

### S022 — 2026-10-12

CAM-0001 stays PROPOSED / NOT RUNNING, activation BLOCKED by published historical exact D(C6³)=16. S022 rank-two Property C and rank-three eta upper bound do NOT change that campaign or select a new D target. No Phase2/3, candidate, mathematical search, solver or certificate; Phase1 IN_PROGRESS.

### S023 — 2026-10-12

CAM-0001 remains PROPOSED / NOT RUNNING; activation BLOCKED because published Schmid2011 D(C6³)=16 disqualifies inherited length16 counterexample premise. S023 p3 symbolic SHORT-EXTRACTION obstruction is not a rank-three Davenport zero-sumfree candidate and does NOT activate or replace any campaign. No campaign, solver, mathematical computational search, tooling or new target; Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED.

### S024 — 2026-10-12: CAM-0001 NOT RUNNING, BLOCKED

Printed BSP2012 **generalized D_k** all-prime inequalities are refuted at p2 by CLM-0115/0116; this neither changes source-stated Schmid2011 D(C6³)=16 nor licenses inherited length16 zero-sumfree search. CAM-0001 still PROPOSED / NOT RUNNING, activation BLOCKED by n6=16; no replacement target/campaign, no Phase2/3, solver, code, candidate or certificate. Phase1 IN_PROGRESS.

## S025 administrative non-activation confirmation

CAM-0001 retains original PROPOSED / NOT RUNNING status; activation BLOCKED by SOURCE_STATED exact D(C6³)=16, with obsolete n6 premise. NO Phase2 tooling, Phase3 campaign, solver, orbit count, candidate, certification, target selection or numerical search. New CLM-0120/0121 are symbolic source audits unrelated to campaign activation. All thirty rank-three D1 original source/evidence classes and endpoints preserved.

## S026 administrative non-activation confirmation

CLM-0122 is a bounded symbolic obstruction, NOT a counterexample or search authorization. CAM-0001 remains PROPOSED / NOT RUNNING, activation BLOCKED by SOURCE_STATED Schmid D(C6³)=16, and premise remains obsolete. No replacement target, campaign activation, solver, code execution, enumeration, Phase2/3, Lean or Palomar. Full original n1..30 D1 table rows untouched, Phase1 IN_PROGRESS; missing hosted checks NOT CI PASS.

## S027 administrative non-activation confirmation

CLM-0123 is a symbolic four-cut necessity only, NOT a new target, computed candidate or zero-sumfree D1 construction. CAM-0001 remains PROPOSED/NOT_RUNNING with activation BLOCKED by SOURCE_STATED published Schmid D(C6³)=16; no replacement target/campaign, mathematical search, solver, orbit, Phase2/3, Lean, Palomar or certificate. Preserve all 30 original rank3 D1 frontier rows/source categories; missing hosted CI is NOT PASS.

## S028 — no campaign activated; aggregate model NOT a candidate

CLM-0124 assigns only six formal cell cardinalities and six AGGREGATE group sums, not any individual indexed group-element sequence. It is not a mathematical candidate for zero-sumfreeness or a new campaign authorisation. CAM-0001 remains PROPOSED / NOT RUNNING with activation BLOCKED by historical SOURCE_STATED Schmid D(C6³)=16. No replacement target, mathematical computational search, solver/orbits, candidate, tooling, Lean or Palomar. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; full original 30 D1 rows preserved.

## S029 — no campaign or candidate

The indexed m>=2p necessary-condition theorem does not construct or certify a sequence. CAM-0001 retains PROPOSED / NOT RUNNING with activation BLOCKED by SOURCE_STATED Schmid D(C6³)=16. No replacement target/campaign, mathematical computation/search, solver, author code, tooling, Lean or Palomar; Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED.

## S030 — no campaign/candidate

CLM-0127/0128 give local symbolic necessary identities, not an actual indexed zero-sumfree sequence, exhaustive search, generalized D2 saving or classic D1 advance. CAM-0001 stays PROPOSED / NOT RUNNING / BLOCKED by SOURCE_STATED Schmid n6=16. No replacement target, numerical mathematical search, tooling, solver, Lean or Palomar. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; all thirty original D1 rows conserved.

## S031 — no search, no campaign, no candidate

CLM-0129/0130/0131 are internal symbolic necessary conditions on a hypothetical prime Z. They do NOT construct a zero-sumfree sequence, give a rank3 classic D1 candidate, prove D2, or license searching. CAM-0001 remains PROPOSED/NOT_RUNNING with activation BLOCKED by SOURCE_STATED published Schmid n6=16. No replacement target/campaign, mathematical numerical or computational search, solver, orbit enumeration, Lean/Palomar or Phase2/3. Full30 frontier rows preserved; hosted CI absent NOT PASS.

## S032 — no campaign or candidate

CLM-0132/0133/0134 are conditional symbolic necessary conditions and coarse counting NO-GO, not a zero-sumfree vector assignment or a new rank3 D1 theorem. CAM-0001 remains PROPOSED / NOT RUNNING, activation BLOCKED by historical SOURCE_STATED Schmid n6=16; no replacement campaign, numerical mathematical search, SAT/ILP, orbit enumeration, author code execution, Lean or Palomar. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED; all original30 frontier row objects and Markdown rows unchanged; no hosted CI PASS.

## S033 — no campaign activation

Conditional CLM-0135 requires unproved pair-positivity; unconditional CLM-0136 is an exact Psi star identity, not a zero-sumfree sequence or D1/Dk advance. CAM-0001 stays PROPOSED / NOT RUNNING / BLOCKED by original SOURCE_STATED Schmid n6=16. No new target, tooling, author code, search, candidate, Phase2/3, Lean, Palomar or certificate. Original 30 frontier rows preserved; no hosted CI PASS.

## S034 — no campaign/candidate

CLM-0137 proves only an internal symbolic necessary Psi-support condition on a hypothetical indexed p>=7 Z, not a vector sequence or rank-three D1/Dk theorem/candidate. CAM-0001 stays PROPOSED/NOT_RUNNING with activation BLOCKED by historical SOURCE_STATED Schmid D(C6^3)=16. No new mathematical numerical search, tooling, solver, author code execution, Phase2/3, Lean or Palomar. Original 30 frontier rows preserved; hosted CI absent NOT PASS.

### S035 disposition — 2026-10-12

CAM-0001 stays **PROPOSED / NOT RUNNING / activation BLOCKED** by published source-stated Schmid2011 D(C6³)=16; Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED. New S035 CLM-0138 is a hypothetical indexed Psi support lower bound, NOT a search target, solver result, counterexample, new D1/Dk theorem or authorization for the obsolete n6 campaign. No replacement activation.

### S036 disposition — 2026-10-12

CAM-0001 **PROPOSED / NOT RUNNING / activation BLOCKED** by historical SOURCE_STATED Schmid D(C6³)=16. S036 CLM-0139 is conditional symbolic vector-weighted coefficient support (m2p p7 W>=58, p13 W>=256), not a vector sequence, new D1/Dk value, counterexample, search/candidate or alternative campaign. No numerical mathematical/computational search, solver, author code, Lean, Palomar, publication or Phase2/3. Phase1 IN_PROGRESS, original30 frontier entries and 28 sources unchanged; absent hosted checks NOT PASS.

## S037 nonactivation — 2026-10-13

CAM-0001 still PROPOSED/NOT_RUNNING/BLOCKED by SOURCE_STATED n6=16. CLM-0140 is a hypothetical-Z symbolic necessary Psi support bound (m2p p7 W>=87, p13 W>=383), not a candidate, rank3 Davenport D1/Dk value, search permission or replacement campaign. Phase1 IN_PROGRESS, Phase2/3 NOT_STARTED; no numerical mathematical/computational search, original author code, solver, Lean/Palomar or hosted CI PASS.

## S038 nonactivation — 2026-10-13

CAM-0001 remains PROPOSED / NOT RUNNING / activation BLOCKED by historical SOURCE_STATED n6=16. CLM-0141 is a hypothetical indexed m=2p critical Psi witness necessary lower bound, p7 W>=156,p13 W>=570, NOT a zero-sumfree assignment, new rank3 D1/Dk theorem, candidate, solver result, campaign target or search permission. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED; original30 frontier rows and 28 source records unchanged. No numerical mathematical/computational search, author code, Lean/Palomar, publication, or hosted CI PASS.

## S039 — 2026-10-13

S039 CLM-0142–0144 directly reconstruct prime D1 and prove D2(Cp^3)<=5p-3 for odd primes, then D_k<=5p-3+(k-2)(3p-1)/2. At k0=2p-4, D_k0<=M-(p-3), p7 112<=116 and p13 442<=452: the prior M+2 comparison obstacle is CLOSED independently of strong extraction/Psi. S004/S005 already contained a weaker conditional bypass; this restores that dependency and improves its base one position, with no novelty claim. CLM-0145–0147 add six/seven containment witnesses, matching actual mixed upper capacities, boundary-adjacent all-layer cuts and >=5 vector VALUES. No incompatible upper, m2p/higher exclusion, strong extraction, composite Davenport resolution or candidate. General eta/global induction remain separate. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED / NOT RUNNING / BLOCKED n6=16; original30 frontier/28 source records preserved; hosted CI ABSENT_NOT_PASS. S040 STRICTLY FUTURE.

## S042 — 2026-10-13

S042 CLM-0158–0163 internal symbolic proofs: corrected NON-SPLIT n20 twisted Fano six-edge compatibility and full affine-span necessary for eligible E(P), explicitly RETRACT naive split-derived seven-class parity-fullness; independent C5³ generalized Davenport LOWER and actual local 28/29 critical core countermodels, showing pure core exclusion FALSE; conditional maximal kernel-decoration zero-sumfree saturation with quotient leftover≤12, but missing an indispensable overlap-exchange lemma; exact 17-plane rectangle extension character; conditional n15 ternary antipodal support≤14. No D(C15³)=43 or D(C20³)=58 theorem, no counterexample, novelty or Phase1 gate PASS. Original frontier 30 row objects/table rows and source 28 records unchanged; original published finite p5 UPPER and eta and ternary inverse remain SOURCE_STATED. Phase1 IN_PROGRESS, CAM-0001 PROPOSED NOT_RUNNING BLOCKED n6=16, hosted checks absent ABSENT_NOT_PASS, same-executor review INTERNAL, no numerical mathematical search/CAS/SAT/Lean/Palomar. S043 strictly FUTURE.

## S043 audit — 2026-10-13

S043 CLM-0164–0167 internally narrow eligible n20 Fano P26 quotient mod2 profiles to (z,r)=(0,4),(0,6),(1,7); exactly realise four-class twisted K4 with six original C20 singleton edges but no P26; establish conditional local indexed p5 CRT replacement restriction |B_i|+|L|≤19; obtain n15 every-y anchored 13-block ternary partition of augmented minimal zero T44 using SOURCE_STATED D12(C3³)=42, without BSP2007 diagrams just for existence. No exact D(C15³) or D(C20³), candidate, new numeric frontier or source promotion. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED; CAM-0001 BLOCKED by source-stated n6=16, hosted checks ABSENT_NOT_PASS. S044 future.

CAM-0001 remains PROPOSED / NOT RUNNING / BLOCKED by published source-stated n6=16; no replacement target activated, no computational mathematical campaign or phase promotion.


## S044 audit — 2026-10-13

No numerical/computational mathematical search/candidate/campaign launched. Four internal symbolic CLM-0168..0171 constrain hypothetical n20/n15 quotient partitions and prove p5 local19 sharp. Original n1..30 frontier row records and28 source objects unchanged, no new bound. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED; CAM-0001 PROPOSED / NOT RUNNING / BLOCKED published SOURCE_STATED n6=16, no replacement target. Hosted CI ABSENT_NOT_PASS; S045 future only.

## S045 — 13 October 2026

One explicitly owner-invoked symbolic Phase1 session against live merge-main 96f731120ac1a61892104604c1280cb99fdd3c0c. CLM-0172 all 26 indexed parity-pair hubs × six non-split pencil assignments (plus complement-symmetry hostile correction); CLM-0173 n15 quotient support>=6 and six-class residual short-free cap (no historical D11/D12 required); CLM-0174 canonical 11 mono-triples plus two 4+7/5+6 mixed quotient circuits (H minimal but not cancelled); CLM-0175 A_k exact all t local packing saturation. No D(C15³) or D(C20³) equality, candidate, source promotion, hosted CI PASS, novelty or Phase1 PASS. Original 30 frontier row objects/table and 28 source objects unchanged. CAM-0001 PROPOSED/NOT_RUNNING/BLOCKED n6=16. Same-executor mathematical review INTERNAL. S046 strictly FUTURE, UNEXECUTED.
