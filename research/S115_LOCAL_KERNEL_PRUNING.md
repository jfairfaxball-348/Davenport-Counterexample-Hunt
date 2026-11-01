# S115 — independently checked local pruning and symmetry

1 November 2026. **Result:** complete local enumeration and a proven representative-system reduction shrink the five-profile n15 space from433,419,386,400 raw pairs to718,716,282. The smallest profile now has5,815,950 pairs. This is a concrete computational reduction, **not an exclusion of any target sequence**. No full CRT pair was checked and no target campaign was registered. The new local-tooling gate is SCOPED_PASS; the full target campaign gate is NO-GO pending pair engines and measured throughput.

## 1. Scope, registration and evidence

Entry main3039bcaa52238bb21c2127ddb1c66c54f153c89b, clean and independently remote-verified. S115-L1 was registered in PLAN.md and RUN_MANIFEST.json before local enumeration. S115-L2 was registered after L1 exposed the remaining product, before orbit enumeration, with an immutable final ORBIT_PLAN.md/ORBIT_RUN_MANIFEST.json. No new external sources were used; S114 source statements retain their statuses.

Inputs are the five fixed profiles of CLM-0378, all values of order15. By CLM-0384, an existential counterexample with such a profile can be taken generating, preserving distinctness, order and multiplicities. By CLM-0385, its two images have unique rank3 RREF matrices over F3/F5 up to independent ambient automorphisms. Local columns may repeat; zero local columns are disallowed since each original value has full order15.

The filters use beta_p=floor(alpha/(15/p)). Scalar multiplication by15/p is invertible mod p, so its omission in zero testing is exact. A surviving local matrix has no nonzero kernel vector in the integer box[0,beta_p]. This condition is necessary, not sufficient, for global zero-sumfreeness (CLM-0386).

Evidence: RESULTS.json (complete local sets/counts and84 nonempty profile/image-pivot-stratum timing records), ORBIT_RESULTS.json (independent orbit agreement), PREFLIGHT.json (settled checks and restart faults), THEORY_TESTS.json, and LOCAL_EVIDENCE.zip. The archive preserves every chunk, checkpoint and sorted survivor array from both engines; ARCHIVE_MANIFEST.json verifies every archived byte against the original before duplicate removal. Restore with `python -m zipfile -e sessions/S115/LOCAL_EVIDENCE.zip sessions/S115`. No evidence was discarded.

## 2. Complete local enumeration and symmetry proof — CLM-0391 (PROGRAMME_PROVED)

Engine A (`local_images_a.py`) enumerates image RREF matrices M directly, through every pivot triple and all allowed free entries. For pivot columns P and complement F, any kernel coefficient vector satisfies x_P=-M_F x_F. For each profile it visits all bounded x_F in[0,beta_F], skips the all-zero tuple and rejects precisely when the resulting x_P lies in[0,beta_P]. The zero free tuple yields only x_P=0, so skipping it cannot discard a nonempty zero. Both enumeration and rejection are complete for the stated local predicate.

Engine B (`local_kernels_b.py`) instead enumerates all rank3 relation subspaces K in F_p^6 by their unique kernel RREF generators B, with a different digit order. It enumerates every nonzero coefficient t in F_p^3 and checks tB against all five boxes. A unit-support kernel vector exists exactly when an image column is zero; that is its independent full-order filter. To compare objects, it constructs a basis of K-perp and independently row-reduces it to an image RREF matrix. Orthogonal complementation is a bijection between dimension3 subspaces of F_p^6. For M with row space K-perp, ker M=K, so its bounded-vector test is the same mathematical predicate, implemented differently.

The full sets contain33,880 keys at p3 and2,558,556 at p5 with no duplicates, and the A/B sets agree exactly. The common key definition is sum M_ij*p^(6i+j), not a shared implementation. Independent candidate checkers alone would not establish coverage; here the entire independently generated local image sets and all survivor sets are compared.

For a fixed alpha let H_alpha be the permutations of labels within equal-multiplicity blocks. If sigma lies in H_alpha, it preserves each beta box, nonzero columns and every coefficient-zero predicate. Apply the SAME sigma to both CRT components. After applying independent ambient row operations to each component, zero relations are unchanged. Therefore every surviving pair is equivalent to one whose p3 component is an H_alpha orbit representative, while its p5 component remains in the fully enumerated p5 survivor set. Enumerating p3 representatives times ALL p5 survivors covers all possible counterexamples in that profile. It may contain several representatives of the same joint orbit; its product count is not a joint-orbit count.

L2 computes p3 orbit representatives twice: (A) minimum key over every group permutation, with vectorized row reduction; (B) union-find components under adjacent transpositions within equal blocks, with separately written scalar Gaussian elimination. Adjacent transpositions generate each symmetric block, so the connected components are precisely the H_alpha orbits. Both minimum representative sets and all orbit sizes agree. Membership of every transformed key in the complete survivor set is verified. This proves the reduction without dividing a count by the group order.

## 3. Exact local counts — CLM-0392 (COMPUTED_EXACT)

All counts below come from full, independently agreeing local computations under CLM-0391. Profiles are numbered0..4 in code; human numbering below is1..5.

| Profile alpha | p3 survivors | p5 survivors | Cartesian pairs | p3 profile-stabilizer orbits | Covering pairs after symmetry |
|---|---:|---:|---:|---:|---:|
| (2,4,8,8,8,13) | 12,168 | 223,200 | 2,715,897,600 | 2,462 | 549,518,400 |
| (2,8,8,8,8,9) | 8,970 | 147,684 | 1,324,725,480 | 542 | 80,044,728 |
| (3,8,8,8,8,8) | 8,970 | 40,110 | 359,786,700 | 145 | **5,815,950** |
| (4,4,8,8,8,11) | 12,168 | 47,529 | 578,332,872 | 1,296 | 61,597,584 |
| (4,7,8,8,8,8) | 8,970 | 40,110 | 359,786,700 | 542 | 21,739,620 |
| Total | — | — | **5,338,529,352** | — | **718,716,282** |

The first reduction is81.19-fold from433,419,386,400, and both reductions together are about603-fold. The groups have sizes6,24,120,12,24; orbit sizes vary. For the smallest profile, orbit-size histogram is15:8,30:33,60:77,120:27, accounting for all8,970 local images. There are145 actual orbits, not8,970/120. Profiles3 and5 have the same pure local survivor sets but different exact profiles/stabilizers; one cannot interchange their final searches.

These products precede actual CRT-column distinctness and mixed zero rejection. No pair in the table is asserted feasible or zero-sumfree. No support-six exclusion, improved D-value, or candidate results.

## 4. A coupled pair lemma and its exact limit — CLM-0393 (PROGRAMME_PROVED)

Fix two labelled values g_i,g_j over C_pq^r, p,q coprime, and multiplicity limits a,b. Define R_p(i,j) as the set of integer pairs(x,y),0<=x<=a,0<=y<=b,(x,y)!=(0,0), such that xg_i+yg_j vanishes mod p. Define R_q analogously, using the SAME integer coefficient labels. Then a nonempty zero supported in these two labels exists iff R_p(i,j) intersects R_q(i,j).

Proof: each bounded pair is a selectable subsequence; CRT makes its global sum zero iff both local sums vanish. A common element of the sets is the same bounded pair in both components. This can be encoded as a bitset at position x(b+1)+y. Intersect the bitsets to reject a join without constructing a length43 sequence. Rows/columns can be normalized by local ambient GL without changing the sets. The bitset must retain the integer coefficient pair, not just an unlabelled residue or a yes/no local zero flag.

Pair testing is not sufficient for global zero-sumfreeness: over C6^3 take e1,e2,-e1-e2 with multiplicities1. No nonempty subsequence of size<=2 sums to zero, while all three do. This is minimum length for a zero evading all two-label tests. S115-T1 checks184,900 decisions (all ordered nonzero pairs in C6^3, bounds in{1,2}^2), comparing local bitset intersection with direct integer-coordinate summation. These checks support the implementation; the equivalence is proved above.

The next precise computational/theory obligation is whether every pair in the5,815,950-case profile3 covering system has a compatible bounded relation on ANY support. A proof would exclude that one multiplicity profile only. A counterexample to a proposed stronger restricted pair lemma must be separated from a genuine global zero-sumfree candidate. No negative finite test here proves that obligation.

## 5. n20 parity-first count — CLM-0394 (PROGRAMME_PROVED)

For any fixed one of the139 n20 profiles, six labelled slots have odd multiplicity and all seven values have order20. Conditional on the established parity constraint CLM-0372, the six odd slots project to the six distinct nonzero vectors of F2^3 other than one missing P. The seventh slot must also be nonzero mod2: a mod4 vector reducing to zero mod2 has order at most2, and its mod5 component cannot raise the full order to20.

There are7*6!*7=35,280 labelled parity assignments. The six odd vectors span F2^3, since a proper subspace has at most3 nonzero points. Thus GL3(F2) acts freely on each labelled assignment: fixing spanning columns fixes the automorphism. Its order is(8-1)(8-2)(8-4)=168. The exact number of labelled parity orbits is therefore210:30 where the seventh value is the missing P,180 where it repeats one of the six. Independent binary Gaussian elimination of all35,280 assignments yields exactly210 keys in PARITY_ORBITS.txt.

Each parity row subspace has exactly2^(3*(7-3))=4096 rank3 free row-subspace lifts to(Z/4)^7. Choose its canonical mod2 pivot minor, normalize the corresponding mod4 minor to I, and freely lift the remaining12 entries from their mod2 residues (two choices each). Every matrix lifting that parity row space has this pivot minor invertible, and its normalization is unique, so no lift is omitted or duplicated. Hence **860,160 mod4 image classes per fixed profile** before further local/mixed tests. Equal parity columns need not coincide mod4 or in C20; do not discard them. Pairwise actual C20 distinctness is still required later.

This reduces the prior mod4 count48,377,856, but still leaves860,160*320,327,931 possible pairs before mod5 pruning, for EACH profile. No mod4 image search was run. The counting theorem is elementary; applying its six-odd-column premise to target counterexamples inherits CLM-0372 and its recorded source-stated D(C10^3)=28 dependency.

## 6. Validation, checkpointing, budgets and process limitations

- Preflight exhausts15 rank3 images at(p,k)=(2,4) against15 boxes and40 at(3,4) against76 boxes; direct coefficient enumeration agrees with both engines. Legacy A/B sequence checkers verify sampled boxes, including positive and negative decisions.
- Full local coverage: each engine completes34 chunks at p3 and1,263 at p5. Exact interval sets are checked; duplicate/missing chunks fail validation. Full sorted all-image and profile-survivor arrays agree. Chunk hashes and final array hashes are retained.
- Measured sum of chunk runtimes: A3 about0.35s, B3 about0.52s, A5 about22.1s, B5 about76.5s. These exclude some checkpoint/consolidation overhead and are NOT target pair rates. The two p5 jobs ran concurrently, within the registered limits.
- Every one of84 nonempty profile/image-pivot strata is benchmarked on first/middle/last survivor keys where available, seven timing repetitions, with min/median/max and sample hashes. Empty strata remain explicit in the200-row table. Local timings do not predict full mixed CRT checking cost.
- Settled checkpoint tests stop after two chunks, emulate an orphan data file, resume to the same full result as uninterrupted execution and reject a modified code hash. This certifies these local-runner tests only, not an unimplemented target-pair runner.
- L1 plan was initially extended in place for L2, which would invalidate its pinned hash. The original PLAN.md was restored byte-for-byte; the expanded content is preserved as ORBIT_PLAN.md. L2 was rerun under the final manifest. The initial T1 diagnostic run preceded its code-hash freeze; final identical-code T1 evidence was rerun after THEORY_RUN_MANIFEST.json. Neither event is hidden as retrospective preregistration. Mathematical outputs were unchanged.

## 7. Decision and next bounded session

**PASS extension: independently exhaustive local component filters, local profile-stabilizer orbits and tested local checkpointing. NO-GO: target pair campaign.** No target engine exists yet; target pair throughput, early-exit distribution, mixed pruning effectiveness and complete pair restart/certification have not been tested. No new target campaign is registered or active, and historical target-search counters are unchanged.

Use profile(3,8,8,8,8,8) as the first prospective target scope:145 p3 representatives times40,110 p5 survivors. It is an exact covering system with5,815,950 pairs. Hypothetical costs1/10/100 microseconds per pair mean5.8/58.2/581.6 seconds of CPU work; at1 millisecond, about1.62 CPU-hours. These are scenarios, not forecasts. All five profiles at1 millisecond would take about199.6 CPU-hours. The single-profile pilot is the justified next focus, not the earlier 433-billion raw enumeration or n20.

S116 should build two genuinely different complete pair engines, exercise the coupled coefficient relation filter, verify exact CRT distinctness and full box predicates on settled groups, and test pair shard/restart semantics. Then preregister a named future bounded profile3 campaign only after passing that gate. Target-length samples require an explicit registered scope and may not become an undeclared exhaustive run. No S116 or target search is executed here.

Even exclusion of profile3 alone leaves four support-six profiles, every higher support at n15, all n20 support-seven profiles and higher supports, and the global saturation theorem unresolved. Internal proofs and finite computations are not Lean certification or a new Davenport equality. Review is INTERNAL_SAME_EXECUTOR, no novelty claim; hosted CI ABSENT_NOT_PASS.
