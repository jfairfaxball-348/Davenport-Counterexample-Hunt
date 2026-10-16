# S103: search-first tooling, scoped gates and campaign pre-registration (16 October 2026)

S103 is the first session under the owner's SEARCH_FIRST directive. It is a **setup session**. It built and tested exact tooling, recorded scoped Phase-1 and Phase-2 gate decisions, and pre-registered round-1 campaigns CAM-0002 (n=15) and CAM-0003 (n=20).

**No n=15 or n=20 search was executed.** `docs/SESSION_PROTOCOL.md` allows advancing to the next phase "only after explicit committed PASS review", so activation is deferred to S104. All engine pre-flight runs used settled groups (n=4,5,6) only.

## 1. Target and evidence matrix

| n | target zero-sumfree length | consequence if found | recorded frontier | lower-bound evidence | upper-bound evidence | S103 status |
|---|---|---|---|---|---|---|
| 15 | 43 (then 44) | D(C15³) ≥ 44 > 3n−2 = 43, refuting rank-three equality at n=15 | 43..45 | CLM-0038 PROGRAMME_PROVED; CLM-0346 COMPUTED_EXACT (standard 42-term sequence zero-sumfree, two checkers) | 45 = 3·13+6, PROGRAMME_DERIVED via CLM-0051 / SRC-0008 and source D(C5³)=13 | CAM-0002 PREREGISTERED, not run |
| 20 | 58 | D(C20³) = 59 given the recorded upper bound 59 | 58..59 | CLM-0038; CLM-0346 (standard 57-term sequence, two checkers) | 59 = 2·28+3, PROGRAMME_DERIVED via CLM-0049 / SRC-0023 historical D(C10³)=28 | CAM-0003 PREREGISTERED, not run |

**Search definitions.** A *target hit* is an indexed sequence over (Z/n)³ (repetition allowed) of the stated length with no nonempty index subset summing to 0. The definition needs neither upper bound: a valid 43-term sequence at n=15 proves D(C15³) ≥ 44 on its own. Upper-bound provenance affects only the interpretation "forces D=59" at n=20, and that interpretation stays INHERITED from the source-dependent interval.

### Literature context, checked in S103

- The public optimisation-problems page for D(C_n³) (SRC-0030, SECONDARY_ONLY) records 3(n−1)+1 ≤ D(C_n³) ≤ 4n − P(n) − 2. Here P(n) is the largest primary component, and the bound is attributed to a 2026 proof PDF (SRC-0031, METADATA_ONLY, not inspected). This gives D(C15³) ≤ 53 and D(C20³) ≤ 73, both weaker than the recorded 45 and 59.
- Han–Zhang, arXiv 2610.15102, submitted 10 October 2026 (SRC-0032, ABSTRACT_INSPECTED), proves the general bound D(G) < 4.86·exp(G)·log|G|/log exp(G) and an almost-all asymptotic. The abstract claims no exact value for C15³ or C20³.
- Not finding an exact value is **not** a claim that the problem is open, and nothing here asserts priority.

## 2. CLM-0345: prefix criterion and saturation equivalence (PROGRAMME_PROVED)

Let G be a finite abelian group and S = (g_1, …, g_L) an indexed sequence. Write Σ(S) = {Σ_{i∈I} g_i : I ⊆ [L]}, where **the empty I is included**, so 0 ∈ Σ(S).

**(a) Prefix criterion.** S is zero-sumfree (no nonempty I with Σ_I = 0) iff for every k, −g_k ∉ Σ(g_1, …, g_{k−1}).

*Proof.* Suppose a nonempty zero-sum subset I exists, and let k = max I. Then I∖{k} ⊆ [k−1], and its sum is −g_k, which therefore lies in the prefix Σ. This includes the case I = {k}, where g_k = 0 and the empty subset sum is 0 = −g_k. Conversely, if −g_k = Σ_J with J ⊆ [k−1], then J ∪ {k} is a nonempty zero-sum subset. ∎

**(b) Exact update.** Σ(S·g) = Σ(S) ∪ (g + Σ(S)), by splitting subsets according to whether they contain the new index.

**(c) Saturation equivalence.** For L ≥ 0 the following are equivalent:
- (i) some zero-sumfree sequence of length L+1 exists;
- (ii) some zero-sumfree sequence S of length L has Σ(S) ≠ G.

*Proof.* (i)⇒(ii): delete the last term g of a zero-sumfree T. The remainder S is zero-sumfree, and by (a), −g ∉ Σ(S). (ii)⇒(i): if h ∉ Σ(S), append −h. The new last term passes the criterion in (a) because −(−h) = h ∉ Σ(S), and the earlier terms are unchanged. ∎

So with L = 57 and G = C20³, "every zero-sumfree 57-term sequence has Σ = G" is equivalent to "no zero-sumfree 58-term sequence exists". This is the fallback statement, and it remains OPEN.

**(d) Invariances used by search, and only these.** Zero-sumfreeness is preserved by permuting indices, by passing to subsequences, and by applying any automorphism φ ∈ GL₃(Z/n), since φ maps zero-sum subsets to zero-sum subsets and back. No orbit normalisation is used by CAM-0002/0003 round 1, and no completeness claim relies on these invariances.

## 3. Exact tooling (`tools/zsf/`)

| file | role | algorithm |
|---|---|---|
| `checker_a.py` | Checker A and incremental Oracle | numpy boolean (n,n,n) array; exact cyclic translation with `np.roll` on all axes; prefix criterion (a); rollback stack of stored arrays |
| `checker_b.py` | Checker B | pure Python; exact arbitrary-precision **count** of index subsets per group element, with hand-written mixed-radix index arithmetic; zero-sumfree iff count[0] == 1; explicit zero-sum witness extraction and direct re-summation |
| `brute.py` | reference C (tests only) | all 2^L − 1 nonempty index subsets via `itertools.combinations` |
| `test_zsf.py` | unit tests | see §4 |
| `bench.py` | throughput benchmark | fixed inputs; not a search |
| `ils_engine.py` | CAM-0002/0003 round-1 engine R1-ILS-1.0 | softmin-coverage greedy growth with ruin-and-regrow local search; HEURISTIC |
| `preflight_engine.py` | engine pre-flight | settled n=4,5,6 only; FFT coverage formula checked against the exact oracle |

**Independence.** A and B use different data structures (numpy boolean set vs Python integer count list), different criteria (prefix −g membership vs final count of zero-sum subsets), different translation code (`np.roll` vs explicit index decode/encode) and no shared module. They are **algorithmically distinct but written by the same executor**: this is not independent authorship. The certification rule in `candidates/README.md` additionally requires a Lean 4 kernel proof and a cold re-check in a later session.

## 4. Tests actually run (S103, same machine)

Command: `python -I tools/zsf/test_zsf.py` → `sessions/S103/TEST_OUTPUT.json`, overall PASS, about 127 s wall.
- **Empty sequence and zero element:** an element congruent to 0 modulo n, e.g. (n,0,2n), is rejected.
- **Duplicates and inverses:** g^(n−1) is zero-sumfree; g^n and (g, −g) are not.
- **Modular wraparound:** (n−1,0,0)+(1,0,0), (n−1,n−1,n−1)+(1,1,1), and negative inputs.
- **Standard sequences** e1^(n−1) e2^(n−1) e3^(n−1) at n=15 (42 terms) and n=20 (57 terms): zero-sumfree under both A and B. Both give |Σ| = n³ (3375 and 8000), i.e. saturating, and every tested one-term extension fails. Recorded as CLM-0346.
- **Seeded random cross-validation** of A vs B vs brute force: groups 2³, 3³, 4³, 5³, 6³, 15³, 20³ and 2×4×8, with seeds 1–8, 2300 sequences in total of length ≤ 12. All three agree. Every non-zero-sumfree case gives a B witness that passes direct re-summation.
- **Oracle rollback:** 4000 random push/pop steps at n=15 and n=20 (seed 11). After every push Σ equals an independent recomputation; after every pop Σ equals the stored snapshot; `legal_mask` agrees with `legal`.
- **Exhaustive small-group maximum length** by nondecreasing multiset DFS: C2³ → D=4, C3² → 5, C2×C4 → 5, C4² → 7, C2×C2×C4 → 6, C3³ → 7. All equal D*, matching the source-stated p-group and rank-≤2 theorems. This is tooling validation only, not a new claim.

`python -I tools/zsf/bench.py` → `sessions/S103/BENCHMARK.json`, on an i7-11800H with 16 logical CPUs and 16.9 GB RAM:
- about 56k (n=15) and 54k (n=20) exact push/pop cycles per second per process;
- about 40k / 37k legal-mask evaluations per second;
- Checker A on the standard sequence: 0.4 ms / 0.6 ms;
- Checker B on the standard sequence: 0.21 s / 0.67 s.

`python -I tools/zsf/preflight_engine.py` → `sessions/S103/ENGINE_PREFLIGHT.json`:
- 800 FFT-coverage values equal direct exact updates;
- with 150 iterations each at n=4,5,6 (seeds 1,2,3), the engine reaches exactly 3n−3 = 9, 12, 15 and never more, consistent with D = 3n−2 for these settled groups.

## 5. Gate decisions (recorded in `docs/PHASE_GATE_LEDGER.md`)

- **Phase 1: SCOPED PASS, search targets n15/n20 only.** The target definitions are exact, the lower bounds are programme-proved and computationally rechecked, the upper-bound provenance is identified (PROGRAMME_DERIVED, source-conditional), and the 2026 literature context has been checked. A hit's validity does not depend on any open Phase-1 obligation.
  - The general frontier map stays IN_PROGRESS. The BSP/Reiher/GHST/Sheikh/Yiu provenance obligations remain open but do not block searching.
- **Phase 2: SCOPED PASS, exact zero-sumfree checking tooling and the R1 heuristic engine.** This covers two algorithmically distinct checkers, a brute-force reference, the test suite above, and engine pre-flight on settled groups.
  - It does **not** cover symmetry-reduced exhaustive enumeration, SAT/DRAT/LRAT tooling, or Lean certification. Those must pass their own gates before any EXHAUSTIVE or negative claim.
- **Phase 3: CAM-0002 and CAM-0003 PREREGISTERED**, activation permitted from S104 after this PASS is committed on main. Nothing was activated in S103.

## 6. What S103 does not establish

- No candidate, no new bound, no exclusion, and no rate of any kind on the target groups.
- No campaign round has been completed, so the search-first counters stay at 0 active search sessions and 0 completed rounds; S103 counts as setup session 1.
- Hosted CI is absent (ABSENT_NOT_PASS).
- The review is INTERNAL_SAME_EXECUTOR.
