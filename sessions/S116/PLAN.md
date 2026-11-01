# S116 bounded tooling preregistration

Entry main e541e5982fa972857f359838e25110db16e217b9, tree 6cd646efb1e7897e521b113a529c55c2d0ad1b39. Clean checkout, ls-remote agreement, PR125 merged, no open PR, zero Actions workflows/runs (ABSENT_NOT_PASS). One session, one authored commit and ordinary PR merge. No target CRT pair evaluation in S116. Review INTERNAL_SAME_EXECUTOR.

## P1 complete predicates and settled tests

Implement independent A actual-image meet-in-the-middle and B finite-field kernel-vector CRT intersection. Each has its own key decoder, column admissibility test, zero predicate and ordinal traversal. Same profile labels across factors. Bounds are strictly below pq, so every coefficient has one CRT residue. Provide literal witnesses, checking bounds and modular sums. Any support-only pruning must be proved; two-label checks may reject but never certify zero-sumfreeness.

Preflight: all rank-three RREF pairs over p2/q3 with k4 (15*40=600), at each of four profiles (1,1,1,1), (2,2,2,2), (4,4,4,4), (1,2,3,4). Compare A and B on every pair including inadmissible inputs; direct bounded coefficient oracle on every pair, and legacy Boolean/counting checkers on every admissible pair. Positive bases and negative controls, zeros contained entirely in either half, pair-pass/triple-zero, repeated projected columns, distinctness/full-order failures, differing pivot triples, and malformed inputs. Independently enumerate the local spaces for test coverage. Cap 10 minutes; stop on mismatch. Freeze code before execution; repairs require a recorded new version and complete rerun.

## P2 durable harness and coverage

Pin the two S115 arrays by byte hashes without evaluating their product. Validate sorted uniqueness, expected lengths and independent key round trips. A enumerates row-major ordinals by divmod; B visits nested rows/columns independently and assigns the same ID. Test all endpoints, disjoint shard partition and hash/count reconciliation. Exact target ID is i*40110+j, total 5815950. No unsupported independent component relabeling.

Implement hash-bound job identity (inputs/code/environment/profile/shard), deterministic chunks, output-first atomic commit markers, chain hashes and exact ordinal checks. On incomplete orphan output safely recompute; committed malformed/missing/hash-mismatched records fail closed. Test stop before output, after output, after marker, chunk duplicates/gaps/corruption, code/input/environment mismatch, budget exhaustion, candidate-stop and failed checker. Settled resumed/uninterrupted records must be identical. Fault fixtures at most 1000 records per scenario, cap 5 minutes, temporary evidence retained in a compact test receipt. Production inputs and code must be pinned before any future activation.

## P3 operation-cost gate (no target samples)

At most 31 repetitions of each synthetic full-work primitive: A coefficient grids with 324 and 729 rows and all sorting/matching work; B 27*125 CRT vector combinations with six coordinates. No target matrix pair or candidate tested. Time separate actual key decoding/kernel preparation on at most 3 keys per component, never joining them. Record distributions, full operation dimensions, setup costs, environment, input hashes; bound operation counts independently. Synthetic rates are not target rates or guaranteed walltime. Include conservative 10x margin and complete two-engine cost. If budget is not defensible, do not register a campaign; identify exact bottleneck and bounded next task.

Only complete correctness/coverage/recovery PASS plus defensible finite cost may support a future CAM registration. Registration must pin full runtime entrypoint, input arrays, exact shards, both engines, stop semantics, budgets (suggest 6 hours per run, absolute 12), and verification. Never activate that campaign in S116. Otherwise record precise NO-GO, even if predicates pass. No new target exclusions, candidates, formal proofs or source promotions. Preserve historical records; synchronize ledgers, closeout and full next prompt absent owner/external blocker.
