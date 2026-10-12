# S001 elementary foundation (programme proof)

**Lemma.** For every integer $n\ge 2$, $D(C_n^3)\ge3n-2$.

**Proof.** Let $e_1,e_2,e_3$ be the three standard basis elements of $(\mathbb Z/n\mathbb Z)^3$. Form a sequence $S$ with exactly $n-1$ copies of each $e_i$. A subsequence chooses integers $0\le a_i\le n-1$. Its sum is $(a_1,a_2,a_3)$ modulo $n$. If this sum vanishes, $n\mid a_i$ for each $i$, so every $a_i=0$; hence the subsequence is empty. Thus $S$ is zero-sumfree of length $3(n-1)$, so the shortest universal zero-sum length is at least $3(n-1)+1=3n-2$. QED.

**Counterexample equivalence (from definitions).** If a zero-sumfree sequence of length $3n-2$ exists, then $D(C_n^3)\ge3n-1$. Conversely, if $D(C_n^3)>3n-2$, by the definition of the least universal length there is a zero-sumfree sequence of length $3n-2$. This equivalence needs no computation; it does not assert existence.

**Prime powers (source stated, not programme proved).** Olson's p-group theorem gives $D(C_{p^a}^3)=3p^a-2$. Direct full primary proof not inspected in S001; catalogued as a classical literature result, not a new theorem.

**Inductive upper bound (primary source stated, not yet programme proved).** Zakarczemny 2019 Lemma 3.3 (SRC-0006) states $D(G)\le D_{D(H)}(G/H)$. Derivation and exploitation scheduled S002.

**Important:** The inherited no-short-zero-sum cap reduction, the D_k values, the off-by-one sandwiches and 5553 orbits remain INHERITED_UNVERIFIED. They must not be promoted by this document.

## S012 scoped proof addition

S012 complete hand proof CLM-0084–0087 closes BSP2012 Lem5.2, including actual doubled alternatives and t=1,2,4. eta7 and rank-three plane deductions remain CONDITIONAL on original rank-two eta/Property C; stronger coefficient unproved. CLM-0088 proves only the actual GG1999 terminal trichotomy implication; full B=>C/Reiher inputs remain unproved. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; CAM-0001 PROPOSED / NOT RUNNING, activation BLOCKED by published n6=16. All 30 numerical rows unchanged; no openness inference. Hosted CI absent, NOT PASS. Full proof and explicit availability are in research/S012_SOURCE_PROOF_VERIFICATION.md; no replacement of the source-stated historical exact family inputs.

## S013 — 2026-10-11

S013 CLM-0089–0093 hand-prove rank-two p/2p extraction, D(Cp²)=2p−1, eta<=3p−2/long-zero short block, original Lem10.6 and the full B=>C implication CONDITIONAL on Property B. Complete S012 p7 Lem5.2 preserved. FIRST unconditional prerequisite is Reiher Property B through unrebuilt strategic-equation/geometric chain; stronger coefficient unproved. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; CAM-0001 PROPOSED / NOT RUNNING activation BLOCKED by published n6=16. All 30 numeric rows unchanged; no openness inference. Zero hosted CI, NOT PASS. No owner-action blocker identified; source-access limitations remain research obligations. S014 strictly FUTURE UNEXECUTED.

## S017 — 2026-10-12

S017 independently reconstructs ONLY original Reiher Proposition8.1, CLM-0103: both η²=1 configurations, four genuine indexed conditional µ=1 identities, exact strategic equation and printed multipliers giving 2(1−x−y)=0; three DISTINCT ORIGINAL collinear A,B,C permit proved Prop5.1, including p5. STOP before Section9. Universal Property B, unconditional Property C, eta(C7³)≤116 and rank-three conjecture NOT proved. All 30 numeric/evidence rows unchanged; Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED / NOT RUNNING activation BLOCKED by published n6=16. Zero hosted checks NOT CI PASS.

See research/S017_REIHER_PROPOSITION_8_1.md. Next S018 original Obs9.1/Lem9.2 is strictly FUTURE UNEXECUTED; no owner-action blocker prevents closeout.

## S018 — 2026-10-12

S018 independently reconstructs ONLY original Reiher Observation9.1 and Lemma9.2 over arbitrary K, char(K) != 2 (CLM-0104/0105), with dependent-X,Y basis case, exact conic equations, fourteen-sum collisions, all 4-of-7 pair line subcases, all 6-of-7 proper conic relabellings and verified printed typo Observation10.1 -> Observation9.1. STOP at Lem9.2: Section9 quartic/Obs9.4/9.5/Lem9.6 and Prop10.1 remain unproved; no universal Property B, unconditional Property C, eta(C7^3)<=116 or rank-three theorem. Thirty frontier values/evidence classes unchanged; Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED / NOT RUNNING, activation BLOCKED by published n6=16. Zero hosted CI is NOT PASS.

See research/S018_REIHER_SECTION9_CONIC_LEMMA.md; original quartic/Prop10.1 proof still unbuilt. S019 only on separate future owner invocation.

## S022 new historic proof dependencies

CLM-0111 every-prime Property C (S013 conditional B⇒C plus S021 universal B) and CLM-0112 eta(C7³)≤116 (CLM-0091 rank-two eta, CLM-0087 p7 lemma, eight-plane CEIL m cases) independently reconstructed in research/S022_PROPERTY_C_ETA7.md. Not rank-three Davenport exactness nor a new publication. BSP stronger coefficient/general omitted Lem2.3 still unproved.

## S025 scoped original-primary-source proof addition

CLM-0120 reconstructs the definitive original BSP2012 odd-prime C_p³ length 6p−3 Chevalley–Warning p-or-3p existence, including the complete 5p exclusion and mod-p factor identities. With CLASSICAL Olson D(C_p³)=3p−2 imported SOURCE_STATED, <=(3p−1)/2 short extraction is independently proved for odd primes, thereby discharging S024's rank3 conditional antecedent. S023 p3 stronger <=3(p−1)/2 obstruction still holds, p>=7 stronger case UNPROVED. CLM-0121 yields exact S024 recurrence D_k<=6p−4+(k−2)(3p−1)/2 for k>=2 (relative to Olson) and a two-position M+2 shortfall at downstream k=2p−4. Neither is a novel exact D(C_n³) theorem or a candidate. Source and detailed calculations research/S025_BSP_ODD_PRIME_EXTRACTION.md. All original n1..30 endpoints/evidence unchanged, Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 BLOCKED.

## S026 symbolic incidence extension

CLM-0122 derives, from S025 p-or-3p existence and **SOURCE_STATED classical Olson rank3 D1=3p−2**, the exact balanced-pair-cover and three-cut obstruction: a hypothetical p>=7 no-<=3(p−1)/2 sequence forces >=4 indexed b=(3p−1)/2 zero-sum blocks in each 3p zero-sum Z. It does not eliminate >=4 blocks or prove stronger extraction / original BSP rank3 multiwise bound. The safe downstream M+2 deficit and every n1..30 D1 historical frontier cell remain unchanged. Full argument in research/S026_BALANCED_ONLY_INCIDENCE.md; S027 future only.

## S027 exact-four-block four-cube forest obstruction

CLM-0123 proves (relative to SOURCE_STATED Olson rank3 D1 and previous CLM-0120/0122) that exactly FOUR balanced b-index zero-sum blocks in a hypothetical no-short p>=7 zero-sum 3p block entail at least SIX distinct 4-bit index-signature classes. Four coordinate-labelled distance-three edges are linearly independent mod2 and acyclic; five classes force affine determinant +/-1 or +/-3 and a forbidden short zero-sum class. SIX OR MORE remain unresolved, and family with five or more blocks is unaddressed. No p>=7 strong extraction, D2<=6p−6, D1 case, campaign or hosted CI claim. Read full research/S027_FOUR_BLOCK_CUBE_FOREST.md; S028 is future-only.
