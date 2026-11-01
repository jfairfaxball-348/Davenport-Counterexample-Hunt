# S114 — fixed-profile image reductions and feasibility, 1 November 2026

**Outcome: NO-GO for direct unfiltered target enumeration.** No target sequence search, candidate, new support exclusion or D-value. A complete fixed-profile generating reduction is proved below; an exact prototype passes settled-group checks. The next task is local-kernel pruning and independently implemented enumeration, not an overnight launch. Review is INTERNAL_SAME_EXECUTOR, not formal certification.

## 1. Prior-art gate

See [inspection matrix](../sessions/S114/LITERATURE.md) and [machine-readable observations](../sessions/S114/SOURCE_INSPECTIONS.json). The version check matters: Wang's current v4 improves the v1 rank threshold from eight to five; Geroldinger–Wang–Yang has a 27 October v2. Neither is a homocyclic rank-three counterexample. Yiu concerns generalized constants of C5^3. Grinsztajn's primary PDF was read in memory, not retained. Source statements stay SOURCE_STATED. No exhaustive literature coverage, priority, or universal novelty is asserted. The historical 30 frontier rows remain unchanged; n15 43..45 and n20 58..59 retain their recorded premises. C10^3=28 is re-observed in the original 1969 report II Corollary 4.3, not reproved.

## 2. Regenerated arithmetic residue

`sessions/S114/validate.py` does not use the old sieve to generate profiles. It generates integer partitions of 3n-2, assigns admissible orders, and computes route block counts and a list of multiwise thresholds independently. Equal multiplicities have nondecreasing assigned orders, preventing duplicate multisets. Every positive multiplicity partition and every permitted order assignment is visited. Only afterwards it compares with the committed output and a fresh run of S112 algorithm B (with sufficient list capacity).

- n15 support six: exactly (2,4,8,8,8,13), (2,8,8,8,8,9), (3,8,8,8,8,8), (4,4,8,8,8,11), (4,7,8,8,8,8).
- n20 support seven: exactly 139; the full lists match the fresh S112 list, not only its 40 saved examples. Every value has order 20, and every profile has exactly six odd multiplicities.

These recheck CLM-0378, retaining its status and source-dependent sieve assumptions. They are not sequences or evidence that a profile can be realised zero-sumfree.

## 3. Fixed-profile generating refinement — CLM-0384 (PROGRAMME_PROVED)

Let n>=2, k>=r, and let g_1,...,g_k be distinct elements of (Z/n)^r with fixed positive multiplicities alpha_i. There exists a generating labelled list h_1,...,h_k such that ker(h) is contained in ker(g). Consequently, zero-sumfreeness for exactly the same alpha is preserved, the h_i remain distinct, and ord(g_i) divides ord(h_i). In particular, if every g_i has order n, each h_i has order n. Thus existence of a zero-sumfree sequence with a fixed positive profile, k distinct full-order values, is equivalent to existence of one whose values also generate.

Proof. For each prime-power component R=Z/p^e, diagonalise the r-by-k matrix of g by invertible row/column operations: g=U[D|0]W, with W invertible and D diagonal (zeros allowed). Such diagonalisation follows by choosing an entry of least p-adic valuation, moving it to the first position, multiplying by a unit to make it a power of p, and subtracting multiples to clear its row and column; all remaining entries are divisible by that pivot. Recurse on the remaining rectangle. Define h=[I_r|0]W locally. It is surjective and g=UDh, so ker(h) is contained in ker(g). CRT glues these maps and the factorisation across all components, giving a global surjection.

Any bounded nonzero coefficient vector x with h(x)=0 would also give g(x)=0. This preserves zero-sumfreeness with unchanged multiplicities. If h_i=h_j, then e_i-e_j belongs to ker(h), hence g_i=g_j, a contradiction. If t h_i=0 then t g_i=0; therefore ord(g_i) divides ord(h_i), and both divide n. This proves the full-order assertion. The reverse existential direction is immediate since generating lists are a subclass. No claim says the original support generates or is GL-equivalent to its refinement. Lower exact orders need not be preserved. This extends the mechanism of CLM-0361 to arbitrary k>=r while proving the fixed-profile obligations explicitly.

Application: both independently regenerated target profile lists have all orders n, so the reduction applies to them. It does not resolve higher support or certify a negative search.

## 4. Canonical images and exact counts — CLM-0385 (PROGRAMME_PROVED)

For squarefree n, a generating r-by-k matrix is equivalent under independent left GL_r(F_p) actions to one and only one tuple of rank-r reduced-row-echelon matrices, one for each p|n. Left actions are automorphisms of the ambient CRT group and preserve all coefficient-box zero relations, distinctness and element orders. Hence enumerate each RREF component, combine corresponding columns by CRT, and discard only actual repeated columns or columns of wrong order. Together with CLM-0384 this covers every fixed-profile full-order counterexample. It is an existence-covering reduction, not a classification of original non-generating orbits.

Proof of enumeration/count. For pivots j_1<...<j_r, pivot columns are the identity; entries before each row's pivot are zero; each nonpivot entry to its right is freely chosen. These are precisely all RREF matrices, uniquely. Equivalently count ordered independent rows in F_p^k and divide by the number of ordered bases in F_p^r:

    [k choose r]_p = product_{i=0}^{r-1}(p^k-p^i)/(p^r-p^i).

At k=6,r=3: 33,880 components at p=3 and 2,558,556 at p=5. Their product is **86,683,877,280** per labelled profile, **433,419,386,400** for five. These are exact unfiltered enumeration counts, not surviving-support counts.

For a prime-power q=p^e the analogous number of free rank-r row summands is p^((e-1)r(k-r))[k choose r]_p. Each mod-p subspace has that many lifts: choose a fixed pivot minor, normalize it to I, and freely lift its r(k-r) other entries. Each subspace has a unique first admissible pivot minor after reduction, avoiding multiple counting. At n20,k7,r3 the component counts are 48,377,856 (mod4) and 320,327,931 (mod5), product **15,496,778,518,695,936 per profile**. A correct mod4 enumerator is NOT implemented in S114.

No permutation quotient is implemented. For a fixed sorted profile only permutations preserving its multiplicities may be used without carrying the profile along. For the five n15 profiles their stabilizer sizes are 6,24,120,12,24. Orbit sizes need not equal these sizes, so dividing by them is not an exact orbit count. Independently permuting CRT components is unsound: labels must be aligned. In particular normalizing the same first three columns to a basis in both components can omit cases with different pivot sets.

## 5. Exact checker and a false shortcut — CLM-0386 (PROGRAMME_PROVED)

For any actual values g_i, zero-sumfreeness is equivalent to the absence of a nonzero integer vector 0<=x_i<=alpha_i with sum x_i g_i=0. `box_zero` splits the support, enumerates all coefficient tuples on both halves, and matches opposite group sums. It keeps a nonzero representative in preference to the empty one when sums collide; this prevents losing a zero wholly inside one half. Every returned tuple is directly checked against the bounds and group sum. This algorithm differs from both indexed Boolean prefix propagation (A) and indexed subset-count DP (B).

For n=pq with distinct primes, a necessary condition is that the projected sequence (qg_i mod p) with multiplicities floor(alpha_i/q) be zero-sumfree; analogously exchange p,q. Indeed, a zero with coefficients y lifts to x=qy, lying within alpha and vanishing also mod q. More generally a compatible pair of local kernel vectors whose coordinatewise CRT residues fit alpha is exactly a global box zero. Both local relations must refer to the SAME coordinate labels.

The two pure-component tests are not sufficient. In C6^3 take g=(0,0,1), h=(0,0,5), alpha=(1,1). Each pure test has all multiplicities zero, yet g+h=0. This is minimum possible sequence length for a zero using nonzero terms, and n=6 is the smallest product of two distinct primes. S114-V2 found this first pair and all three checkers verified it. This refutes only this precisely stated shortcut, not stronger restricted image lemmas.

## 6. Settled-group preflight and cost

S114-V1 was registered in PLAN.md before execution, with a ten-minute cap. Final exact output is RESULTS.json, with environment/code hashes; SHA256SUMS.json hashes that output.

| n | profile | complete RREF/CRT pairs | distinct full-order cases checked by all three algorithms |
|---|---|---:|---:|
| 2 | (1,1,1,1,1,1) | 1,395 | 30 |
| 3 | (2,2,2,1) | 40 | 30 |
| 6 | (4,4,4,4) | 600 | 390 |

All 450 valid cases have literal zero witnesses and all three checkers agree. Positive basis sequences at n=2,3,4,5,6 and negative basis controls also agree. These tests exercise actual CRT images, coefficient checking, duplicate/full-order filtering and both positive/negative verdicts. They are tooling tests, not new certified exclusions: only one image enumerator exists, and all share the internal completeness proof. A/B independently check each emitted sequence; they do not independently verify the enumeration coverage.

The 256-case settled n6 six-column benchmark is a deterministic prefix (includes invalid supports) and takes about 0.03 seconds. Its timing is a sample, not a target throughput estimate. Even assumed costs of 1, 10, 100 microseconds per raw pair give respectively **120.4, 1,203.9, 12,039.4 aggregate CPU-hours** for five n15 profiles. At hypothetical ideal eight-worker scaling, these mean 15.0,150.5,1504.9 hours; contention and memory only worsen ideal scaling. There is no measured target rate and no lower bound on the running time of a different/pruned algorithm. For n20 even one raw profile at 1 microsecond is about 4.3 million CPU-hours. Moving directly to n20 is not a sensible fallback.

## 7. Changed plan and future harness

**Readiness gate NO-GO for a target campaign.** Missing: strong measured rejection before forming the product, independent complete image enumeration, and tested resumable coverage. The prototype is not campaign software. No CAM identifier is allocated or activated; original search counters remain unchanged.

Next bounded task: enumerate/filter local n15 RREF kernels against the two pure-component boxes, retaining exact profile-specific survivor IDs and hashes; independently reproduce survivor sets and pivot strata. Then exploit the full compatible relation-box condition to reject joins before the expensive checker. Local filters are sound by CLM-0386 but cannot certify a surviving pair zero-sumfree. Establish exact remaining pair counts and benchmark every pivot/profile stratum before registering a target campaign. Prefer a bounded local classification with a proof-relevant residue over arbitrary random walks or another support-five run.

Proposed future deterministic harness (design only): stable IDs (profile,pivot3,digits3,pivot5,digits5), index by mixed radix and pair ordinal; disjoint contiguous shards partition the exact retained product. Persist the first unprocessed ordinal atomically with profile/code/environment hashes, cumulative counts, rejection-reason counts and chained log digest. On restart reject mismatched hashes, replay the boundary record and resume; an interrupted record is recomputed without counting twice. Per-run wall budget 6 hours, absolute cap 12; finish current item then checkpoint. Resume until every registered shard is complete, or stop on candidate/disagreement. Do not infer exclusion from any elapsed budget. Candidate goes to candidates/ with canonical sequence/hash, A/B checking, later Lean kernel verification and a later cold session. Before a negative result, two independently implemented exhaustive engines and proved reductions must establish full coverage; reject partial/truncated logs. HEURISTIC samplers would need separate registration and could never give exclusions.

For n20, the 139 profiles have six odd multiplicities. CLM-0372 requires those six actual mod2 images to be F2^3 minus {0,P}, hence distinct and nonzero. This offers a strong filter before lifting to mod4 and pairing mod5. Completeness still requires all P and all compatible lifts or a proved GL normalization; actual order20 and pairwise distinct C20^3 columns must be checked. No mod4 implementation or cost after this filter is claimed.

Even a successful n15 support-six exclusion yields only support>=7; an n20 support-seven exclusion yields only support>=8. General SAT15/SAT20 still requires all higher supports, a theorem forcing small support, or the saturation statement CLM-0345 for every length42/57 zero-sumfree sequence. None is supplied here. A precise subsequent theory goal is: prove every compatible local-kernel pair for one of the five specified boxes contains a nonzero CRT vector inside that box; an exhaustive local filter may identify the right restricted hypothesis. It is a proposed obligation, not an additional claim.
