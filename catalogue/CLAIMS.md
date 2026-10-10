# Claims register

Authoritative machine-readable catalogue: [claims.json](claims.json). All owner-supplied seed facts were transcribed as **INHERITED_UNVERIFIED**, including the reported orbit counts and conditional implications. Stable IDs are never recycled.

Status enum: `SOURCE_STATED` is a literature statement, not verified proof; `PROGRAMME_PROVED` includes complete original mathematical argument; `COMPUTED_EXACT` requires a reproducible script/output hash; `HEURISTIC` reports only searched region; `FORMALLY_CERTIFIED` requires checked formal evidence; `INHERITED_UNVERIFIED` is not authority.

## Seed claim register
- **CLM-0001** [FOUNDATION] Definition of D(G), D*(G), and lower bound D>=D*; for C_n^3 lower 3n-2.
- **CLM-0002** [FOUNDATION] Rank-three conjecture D(C_n^3)=3n-2; target length 3n-2 zero-sumfree.
- **CLM-0003** [LITERATURE] Olson 1969 p-groups have D=D*; van Emde Boas–Kruyswijk independent pointer.
- **CLM-0004** [LITERATURE] Rank two C_m⊕C_n with m|n has D=m+n-1.
- **CLM-0005** [LITERATURE] Rank three remains generally unresolved, according to historical sources.
- **CLM-0006** [LITERATURE] Zakarczemny upper-bound coefficient a3<=20369.
- **CLM-0007** [LITERATURE] Girard–Schmid say rank-three wide open and cases first invariant 2 known.
- **CLM-0008** [LITERATURE] Wang AIMS 2020 calls rank-three open 50 years, cites Conjecture 3.5 in reference [11].
- **CLM-0009** [LITERATURE] Gao Discrete Math 222 (2000) rank-three paper and Gao-Geroldinger 2006 survey.
- **CLM-0010** [LITERATURE] No known rank-three or C_n^r example D>D* per HAL pointer.
- **CLM-0011** [LITERATURE] Infinitely many rank >=4 group examples D>D*, per Bhowmik–Schlage-Puchta 2012 pointer.
- **CLM-0012** [LITERATURE] Bhowmik–Schlage-Puchta 2007 claim D(C3⊕C3⊕C3d)=3d+4.
- **CLM-0013** [LITERATURE] Royal Holloway thesis reconstructs and challenges clarity of 2007 proof.
- **CLM-0014** [LITERATURE] 2025 Combinatorica k-th Davenport article says naive k-wise linear formula fails for elementary 2/3 rank>=3.
- **CLM-0015** [LITERATURE] Freeze–Schmid 2010 and Delorme–Ordaz–Quiroz 2001 multiwise literature pointers.
- **CLM-0016** [REDUCTION] Inductive bound D(G)<=D_{D(H)}(G/H) for subgroup H.
- **CLM-0017** [REDUCTION] Short-zero-sum removal if exists length <=e leaves bound e+g_{k-1}.
- **CLM-0018** [REDUCTION] Over C3^3 no short zero sum implies support A with A∪{0} affine cap, multiplicity <=2.
- **CLM-0019** [COMPUTATION] D_k(C2^3)=2k+3 for k>=2; k=2 witness six distinct nonzero elements.
- **CLM-0020** [COMPUTATION] D2(C3^3)=11 and GL(3,3) extremal length-10 orbit count 43.
- **CLM-0021** [COMPUTATION] D3(C3^3)=14 and GL(3,3) extremal length-13 orbit count 699.
- **CLM-0022** [COMPUTATION] D4(C3^3)=17 and GL(3,3) extremal length-16 orbit count 5553.
- **CLM-0023** [COMPUTATION] Prior sampled C3^3 cases independently crosschecked by another DP.
- **CLM-0024** [REDUCTION] D(C2m^3)<=2 D(Cm^3)+3.
- **CLM-0025** [REDUCTION] D(C3m^3)<=3 D(Cm^3)+5.
- **CLM-0026** [REDUCTION] Prime-power m yields D(C_2m^3), D(C_3m^3) in {3n-2,3n-1}.
- **CLM-0027** [REDUCTION] For n<=30 inherited sandwich examples n=6,10,12,14,15,18,21,22,24,26.
- **CLM-0028** [REDUCTION] For n=2m odd m: also D(C_n^3)<=D4(C_m^3).
- **CLM-0029** [REDUCTION] For n=2m odd m: mod-m skeleton has at most 3 pairwise disjoint zero sums.
- **CLM-0030** [REDUCTION] For n=2m odd m: valid mod-2 labels avoid zero on every mod-m zero-sum index subset.
- **CLM-0031** [CAMPAIGN] n=6 both bounds upper 17; search 5553 mod-3 orbits, lifts 48 Boolean variables.
- **CLM-0032** [CAMPAIGN] n=6 lifts possibly normalized by GL(3,2), reductions unproved.
- **CLM-0033** [CAMPAIGN] n=6 deciding all skeleton lifts would prove D=16 or exhibit length-16 counterexample, subject to certification.
- **CLM-0034** [CAMPAIGN] n=6 Bhowmik–Schlage-Puchta refinement should be studied, comparing C3⊕C3⊕C6 true D10 vs naive 11.
- **CLM-0035** [CAMPAIGN] n=10 would settle at D=28 if D4(C5^3)=28 (conditional only).
- **CLM-0036** [CAMPAIGN] n=10 length-28 counterexample needs C5^3 skeleton with at most 3 disjoint zero sums.
- **CLM-0037** [CAMPAIGN] n=10 D4(C5^3) >=29 would be necessary for such a skeleton.

## Fresh S001 claims
- **CLM-0038** **PROGRAMME_PROVED** — For all n>=2, D(C_n^3)>=3n-2, by three-coordinate basis sequence. Evidence: research/FOUNDATIONS.md.
- **CLM-0039** **SOURCE_STATED** — Olson p-group theorem: if G = ⊕ C_(p^a_i) then D(G)=1+Σ(p^a_i-1). Evidence: SRC-0001 (abstract), SRC-0003 (secondary exact formulation).
- **CLM-0040** **SOURCE_STATED** — Gao–Geroldinger Conjecture 3.5 includes D(C_n^3)=3n-2. Evidence: SRC-0018 secondary transcription; original SRC-0003 not yet inspected.
- **CLM-0041** **SOURCE_STATED** — Zakarczemny 2019 Lemma 3.3 states D(G)<=D_D(H)(G/H). Evidence: SRC-0006, HTML Lemma 3.3.
- **CLM-0042** **SOURCE_STATED** — Yiu 2026 preprint abstract reports D4(C5^3)=30. Evidence: SRC-0015 abstract; no independent computation or proof checked.
- **CLM-0043** **SOURCE_STATED** — AIMS Mathematics 2020 [11] identifies Gao–Geroldinger 2006 survey. Evidence: SRC-0007 publisher references; Conjecture 3.5 attribution through SRC-0018.
- **CLM-0044** **SOURCE_STATED** — Grinsztajn 2026 bound D(C_n^3)<=4n-P(n)-2 is reported by secondary page. Evidence: SRC-0018 only; inspect original proof in S002.
- **CLM-0045** **SOURCE_STATED** — Wang 2026 rank>=8 unbounded gap to D* is reported by abstract, not relevant to rank 3. Evidence: SRC-0017 abstract.
- **CLM-0046** **SOURCE_STATED** — Zakarczemny 2019 states bound with a3<=20369 for rank three. Evidence: SRC-0006 primary HTML abstract.

No S001 claim is COMPUTED_EXACT, HEURISTIC or FORMALLY_CERTIFIED. No counterexample is claimed.
