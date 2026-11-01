# S115 bounded preregistration — 1 November 2026

Entry main3039bcaa52238bb21c2127ddb1c66c54f153c89b, clean, independently ls-remote verified; tree b05cee15128d0ca95472f74acab62e99dfaea34e. PR124 merged, no active target campaign, hosted workflows0/runs0: ABSENT_NOT_PASS. One numbered session and one atomic authored commit/ordinary merge. Review INTERNAL_SAME_EXECUTOR; no delegated review.

## S115-L1: complete local spaces, not a target sequence search

For p=3,5 and each of the five S114 n15 profiles, enumerate all rank-three image maps F_p^6 -> F_p^3 modulo left GL. Counts33880 and2558556. Reject zero columns (full global order15 requires nonzero columns in both factors) and reject a nonempty projected zero with coefficient bounds floor(alpha/(15/p)). Scaling each image by the other prime is invertible and therefore leaves these zero predicates unchanged. Local equal columns are allowed. No pair of components will be searched as a full length43 target sequence.

Two independent implementations: A enumerates image RREF matrices and checks bounded free-variable solutions; B enumerates relation kernels in RREF, checks their vector boxes independently, and emits the unique annihilator-image RREF key. Independent enumeration and predicates, no shared mathematical helper code. The common format is a canonical row-major base-p encoding of the image RREF matrix. Full sorted survivor key sets must agree, with per-profile and image-pivot-stratum counts/hashes.

Bound: two complete enumerations each at p3/p5, processing five profiles together; cap six hours total, two hours per engine/component, at most one component job per engine at a time, no more than two concurrent jobs, memory target <2GB. Deterministic pivot/free-digit order; chunk checkpoints with last completed interval and code/profile/environment hash; atomic outputs and no counting of partial chunks. Stop on mismatch/error/candidate/time cap; mark PARTIAL if incomplete. No negative target claim. Freeze code and parameters in RUN_MANIFEST.json before enumeration; changes require a logged version/reset. Progress at every pivot stratum, finer chunks within large strata. Survivor sets retained (compressed lossless integer arrays if useful).

Preflight: all image/kernel representatives at p2,k4,r3 and p3,k4,r3 (15/40); representative count agreement; all boxes with coordinates in0..p-1 and sum<=3(p-1), including zeros; compare exact direct coefficient enumeration to both predicates. Additional fixed six-column small-field controls, A/B legacy sequence checker samples, and kernel-to-image uniqueness/count agreement. Budget ten minutes. Only then run L1.

## S115-T1: precise lemma and n20 parity count

Prove the annihilator correspondence, necessary-filter soundness, and a label-coupled two-column compatibility filter (zero coefficients x,y within their profile bounds must vanish in both projections at once). Test this filter against direct coefficient enumeration for every ordered nonzero pair in C6^3 with bounds1..2, capped five minutes; report disagreements, not a target theorem. Local tests alone remain insufficient.

Independently count parity image orbits for six specified odd slots forming F2^3 minus{0,P}, seventh nonzero (all order20), by direct labelled vector assignments and RREF canonicalization. Prove the GL action free and count mod4 lifts; no mod4 target enumeration. Budget one minute.

## Benchmarks, review and gate

Record per-nonempty profile/image-pivot stratum local-filter sample timings (deterministic early/middle/late surviving keys, at least three where available) with min/median/max and input hashes. Compute exact remaining Cartesian-product sizes, not actual compatible counts. No target pair-rate claim from local timing. Evaluate whether a stronger provable join reduction is needed. A future campaign may be registered only if independent complete coverage, realistic target rates and a tested restart harness actually pass; otherwise NO-GO with a specific next task. Test interruption/resume and tampered-code rejection on settled local work. All code, input, environment, output hashes must be recorded.

Preserve source objects, all390 old claims, thirty frontier rows and historical target-search counters. Add only supported claims with stable IDs. Sync JSON/Markdown ledgers; closeout, hostile review, full S116 prompt if no owner/external blocker; one authored commit and ordinary PR/merge, verify remote main and stop. No S116 execution.
