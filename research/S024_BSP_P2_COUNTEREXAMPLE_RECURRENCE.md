# S024 — BSP2012 all-prime Lemma 2.3 counterexamples and a safe weaker multiwise recurrence

Date 2026-10-12. Exactly one bounded Phase-1 primary-source symbolic proof/provenance session. Entry remote main `a57c7aaa264951ad2570459c319fcee36509feb6`; S023 atomic commit `d59503a362226d735bf8d6aab60d793edf4434e4`, parent `44d451ead8854a35419462cd0a69a35d847c12cc`, tree `2588637b673715f6809d3740502ccd8e584c60c8`; original two-parent merge/main `a57c7aaa264951ad2570459c319fcee36509feb6` with parents [`44d451ead8854a35419462cd0a69a35d847c12cc`, `d59503a362226d735bf8d6aab60d793edf4434e4`], PR23 MERGED. These refs were re-read from LIVE GitHub API, not inferred from the S023 precommit closeout. No mathematical computation/search/candidate/Lean/Palomar/author code. Source verification and symbolic proofs are separate from hosted CI.

## Source: the definitive printed claim

Bhowmik and Schlage-Puchta, *Davenport's constant for groups with large exponent*, Contemporary Mathematics 579 (2012), DOI 10.1090/conm/579/11515, definitive publisher-provided offprint https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf, printed pp22–24 / PDF indices 1–3. THEOREM 1.3 has short-extraction threshold `(6p−4)p^(d−3)+1` and length cap `(3p−1)/2`; Lemma 2.1 statement repeats cap `(3p−1)/2` for length `6p−3`; its split proof instead asserts an unexplained shorter `3(p−1)/2`. Lemma 2.3 PRINTS for rank 3, without proof, `D_k(C_p^3) ≤ max{5p−2, 3(p−1)k/2 +2p+5}`, and for `d≥4`, `D_k(C_p^d) ≤ max{(6p−4)p^(d−3)+1, 3(p−1)k/2 +1+(6p−4)p^(d−3)(1/4+3/(2p)−3/(4p²)−1/(dp))}`. The text does not restrict the prime p; p=2 is therefore inside its printed quantifier. No erratum/prior-art novelty claim is made.

## CLM-0115: the printed rank-three inequality is actually FALSE at (p,k)=(2,19)

Let `g≠0` in `C_2^3`; it has order 2. For every k, a sequence of `2k−1` indexed copies of g contains at most `floor((2k−1)/2)=k−1` disjoint nonempty zero-sum subsequences (each has even positive cardinality). Hence `D_k(C_2^3)≥2k`. At `k=19`, this yields `D_19(C_2^3)≥38`. But the printed upper bound is `max{8,(3/2)·19+9}=max{8,75/2}=75/2=37.5`. An integer `D_19` cannot be at once at least 38 and at most 37.5. **The ALL-PRIME printed rank-three Lemma2.3 statement is false**. This is not a rank-three Davenport conjecture counterexample (which concerns `D_1(C_n^3)`), nor a proof of any odd-prime failure, nor a claim about the original authors' intentions.

## CLM-0116: the printed d≥4 inequality is also FALSE at (p,d,k)=(2,4,25)

Let `g≠0` in `C_2^4`. The same repeated-order-two argument proves `D_25(C_2^4)≥50`. In the second printed bound, `(6p−4)p^(d−3)=8·2=16`; the parenthesized fraction at `p=2,d=4` is `1/4+3/4−3/16−1/8=11/16`. Thus the claimed RHS is `max{17,(3/2)·25+1+16(11/16)}=max{17,99/2}=49.5`, contradicting `D_25≥50`. In fact for every group containing an element of order p, the elementary repeated-element construction yields `D_k≥pk`, so any proposed global affine upper bound valid for arbitrarily large k must have slope at least p. The BSP displayed slope `3(p−1)/2` is below p only at p=2. It is NOT ruled out by this argument for odd primes.

## CLM-0117: an independently proved safe short-extraction recurrence

Fix finite abelian G. Assume EVERY sequence of length `A` has a nonempty zero-sum subsequence of length at most the positive integer `L`. For every integer `k≥1`,
`D_{k+1}(G) ≤ max{D_k(G)+L, A−1}`.

**Complete indexed proof.** Take `S` of length `N≥max{D_k+L,A−1}`, append a distinct indexed term `g=−σ(S)`, so `B=S·g` is zero-sum, length `N+1≥A`. Obtain a nonempty zero-sum `T⊆B`, `|T|≤L`. If `g∉T`, remove T from S; its complement has `N−|T|≥D_k` indexed terms and therefore k disjoint nonempty zero sums, disjoint from T. If `g∈T`, let `U=T\{g}`. As `σ(T)=0`, `σ(U)=−g=σ(S)`; hence `V=S\U` is zero-sum. Moreover `|V|=N−|U|≥N−L+1≥D_k+1`. Remove ANY one indexed term x from V, leaving ≥D_k terms; find k disjoint nonempty zero sums therein. Their indexed complement INSIDE V includes x, is nonempty, and has zero sum because V and all extracted blocks sum to zero. Thus V contains k+1 disjoint nonempty zero sums, as does S. This proves the recurrence with integer threshold `A−1` exactly (no rounding mistake). It is independent of any stronger BSP coefficient, and it parallels known Freeze–Schmid/Yiu completion arguments; NO originality claim.

For `u_1=D_1(G)`, `u_2=max{D_1+L,A−1}`, induction yields the explicit upper bound for all `k≥2`:
`D_k(G) ≤ max{D_1+(k−1)L, A−1+(k−2)L}`.
This is a FULL symbolic inductive replacement bound, not the printed Lemma2.3 assertion.

## CLM-0118/0119: exact scope of replacement in elementary p-groups

For odd primes `p≥3`, set `L=(3p−1)/2`, integral; set `A_d=(6p−4)p^(d−3)+1` for `d≥3`. CONDITIONAL on the short-extraction conclusion in the printed BSP2012 Theorem1.3/Lemma2.1 being true (not on the INVALID stronger length `3(p−1)/2`), using the classical source-stated Olson p-group `D_1(C_p^d)=d(p−1)+1`, the recurrence proves for `k≥2`:
`D_k(C_p^d) ≤ max{d(p−1)+1+(k−1)L, (6p−4)p^(d−3)+(k−2)L}`.
For rank 3, `6p−4≥3p−2+L` since difference is `3(p−1)/2≥0`; therefore
`D_k(C_p^3) ≤ 6p−4+(k−2)(3p−1)/2` for `k≥2`. `D_1=3p−2`. The odd-prime SHORT-EXTRACTION claim used as input is SOURCE_STATED and remains to be rebuilt at exact original proof level, so the conditional inference is PROGRAMME_PROVED, not an unconditional independently established odd-prime short-sum theorem and not the published strong multiwise inequality.

For `p=2`, `A_d=2^d+1` by direct algebra, and any such length in `C_2^d` has a zero entry or two identical entries by pigeonhole, hence a zero sum of size ≤2. Here `L=2` is PROGRAMME_PROVED unconditionally; Olson's source-stated p-group D1 is `d+1`. Thus the recurrence gives the **unconditional** (given classical p-group D1) replacement `D_k(C_2^d) ≤max{d+1+2(k−1),2^d+2(k−2)}` for k≥2. At d=3, `D_1=4,D_2≤8`, and `D_k≤2k+4` for k≥2. In fact the original Yiu2026 v1 primary text SOURCE-STATES the stronger exact `D_k(C_2^3)=2k+3` for k≥2; no independent reconstruction of that external result is claimed.

**Precise prime/range separation.** (a) ALL primes: the strong printed inequalities are REFUTED by p2. (b) Odd p≥5: order-p lower bounds do not refute the printed slope; the stronger bound is UNPROVED in this session. (c) p≥7: same UNPROVED; S023 3p split cannot supply its missing unit. (d) Fixed k: p2 refutations use k19 (rank3) and k25 (d4); this does not establish failure at smaller k or for odd p. The S023 p3 short-extraction counterexample concerns an auxiliary claim, not the Lem2.3 multiwise inequality; the p3 D_k formula remains a separate SOURCE_STATED result. Because the necessary odd-prime STRONG structural extraction is unproved, DO NOT reconstruct or certify the omitted original rank3 Lem2.3 induction. The completed safe RECURRENCE is a different, weaker theorem. STOP there.

## Read-only external provenance, frontier and certification limits

Official Royal Holloway Sheikh2017 thesis metadata page is reachable, official full PDF click/direct fetch gives internal error/inaccessible; no Chapter4 or full Remark4.3.11 authenticated, no exactly-three/at-most-three conflation. GHST2007 original C53.html complete historical author code/output still inaccessible, NEVER RUN. Yiu arXiv2609.04950v1 original HTML Section2.3 M1 itself says 98,622 normalized seeds and 230,983 extensions, but a second generator did NOT rerun final independent M1 three-disjoint predicate; M2/M3 verify different thresholds. No independent final M1 programme/log/certificate accessed; prior S013 16680-byte TeX/bib SHA is NOT M1. These are access constraints, not proofs of absent artifacts. Bounded exact-source queries for n15,20,21,28,30 did not authenticate new theorems; not an openness inference.

Full JSON/Markdown thirty-row admin comparison was exact: 25 exact/trivial source status rows and five intervals 15=43..45,20=58..59,21=61..63,28=82..83,30=88..90; all D endpoints, evidence and statuses UNCHANGED. Schmid2011 n6=16 and rank3 van Emde Boas 2p^a/3·2^a remain SOURCE_STATED. Inherited14/17,+5,43/699/5553 quarantined. CAM-0001 PROPOSED/NOT_RUNNING BLOCKED n6=16, Phase1 IN_PROGRESS, Phase2/3 NOT_STARTED. Original BSP2007 diagrams/upper induction unrelated/unclosed. No rank-three Davenport exact bound altered; no novelty, computational enumeration, hosted CI PASS, formal certification or owner-gated external action.
