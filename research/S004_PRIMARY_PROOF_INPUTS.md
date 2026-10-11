# S004 — Primary proof inputs and corrected frontier

Date: 2026-10-11. One bounded Phase-1 source-verification session. **Phase 1 IN_PROGRESS; Phases 2 and 3 NOT_STARTED.** No mathematical search, solver, enumeration, candidate, formalisation or campaign was executed. `PROOF_INSPECTED` below means the specified written proof was read; it does not mean every dependency was independently proved.

## 1. Material frontier correction

**The published literature already gives D(C6³)=16.** Schmid, *The inverse problem associated to the Davenport constant for C2 ⊕ C2 ⊕ C2n, and applications to the arithmetical characterization of class groups*, E-JC 18 (2011), P33, Theorem 4.1(2), printed/PDF p.27, states D(C6² ⊕ C6t)=D* for every positive integer t. Set t=1. The calculation D*=1+3(6−1)=16 has no extra hypothesis. This is SRC-0022 / CLM-0064, a **SOURCE_STATED exact value**, not programme certification of a sequence. Section 4.2's exclusion of t=1, on p.29, does not apply to Section 4.1 or its theorem.

The proof on pp.27–29 uses Proposition 4.2 (doubling via ν; tripling via Property Q), Lemma 4.3, and the structural Theorem 3.13. Lemma 4.3 explicitly omits long subsum case checks on p.29. Those cases were not independently reconstructed here. For t=1 an older route is available: the original 1969 reports already treat the required prime-power lifting families. Neither route is a claim of a new theorem.

Original CWI report II, van Emde Boas, ZW007 (1969), SRC-0023: Theorem (4.2), printed pp.33–35 / PDF pp.35–37, doubles a rank-three group satisfying the ν condition; Corollary (4.3), printed p.35 / PDF p.37, applies to C(2p^a1) ⊕ C(2p^a2) ⊕ C(2p^a3), with ordered positive exponents. Its cited p-group input is Theorem (2.8). In particular D(C(2p^a)³)=6p^a−2. This settles n=6,10,14,18,22,26 in our range. The report's μ is modern D, λ is D−1, M is D*, and Λ is D*−1; confusing λ with D creates a one-unit error.

Original report III, van Emde Boas–Kruyswijk, ZW008 (1969), SRC-0002 (corrected URL): Lemma (1.3)(b), printed p.4 / PDF p.6, and Theorem (1.4), printed p.5 / PDF p.7, imply Corollary (1.5), family VIII, printed p.13 / PDF p.15: equality for C(3·2^a1) ⊕ C(3·2^a2) ⊕ C(3·2^a3). Its deduction ends on printed p.14 / PDF p.16. Theorem (1.4)'s proof is on printed pp.12–13. Thus n=6,12,24 are exact here. Lemma (1.2)'s computational structural argument is referred elsewhere and Lemma (1.3) is only sketched; no independent exhaustive proof is asserted. Schmid's introduction independently identifies these two classical homocyclic families.

Consequently the inherited n=6 tooling recommendation is withdrawn. CAM-0001 stays **PROPOSED / NOT RUNNING**, with activation blocked because its counterexample premise is obsolete on the source record. No replacement campaign or Phase-2 target is selected. n=15 is merely the first remaining *interval entry requiring literature review*, not a certified open problem.

## 2. Grinsztajn written proof: identity, all inputs and deductions

SRC-0016's actual four-page `davenport_cn3_bound.pdf` was downloaded and read in full. Author-repository main was independently read as commit `848b081e40ecd769017a6199ebcb4e31fe125483` (this is a commit, not a tree; its tree is `89da712d9e2cf9067a49790fecfa13c76b88e8bb`). PDF blob `5a698f1edee8cf0b1fabcb8b865f0fd04617ab0d`; SHA-256 and byte length are in the source manifest. The written PDF, not its README or conditional formalisation, is now the principal object of audit. The conditional file was read only to inventory the ten external axioms; it was not executed.

Here Dk means k disjoint nonempty zero sums; η means a nonempty zero sum of length **at most** the exponent. These are different from exactly-p-term constants.

| Imported axiom | Exact range / written location | Primary match and audit outcome |
|---|---|---|
| `D_prime_power` | q≥2 a prime power; D(Cq³)=3q−2; PDF p.2 | Classical Olson theorem, SRC-0001 / survey SRC-0003. Source theorem retained; original full Olson proof was not reconstructed. |
| `D_lower_bound` | m≥1; D(Cm³)≥3m−2; p.2 | Complete basis-sequence proof in FOUNDATIONS, CLM-0038; m=1 follows from D({0})=1. |
| `inductive_inequality` | p,m≥1; D(Cpm³)≤D(D(Cm³))(Cp³); p.2 Lemma 2.1 | Freeze–Schmid Thm 3.6, p.9, positive multiwise index and arbitrary subgroup; complete k=1 proof in S002, including H=pG. No coprimality needed. |
| `Dk_eq_two` | k≥2; Dk(C2³)=2k+3; p.2 | Freeze–Schmid Remark 5.3(3), pp.11–12, D0=3 and kD=2. Complete independent upper/lower proof in S002, CLM-0048. k=1 is separately D=4. |
| `D3_le_three` | every length≥15 sequence over C3³ has three disjoint zeros; p.2 | BSP 2007 Prop.1, p.3; Prop.8, pp.10–11. Source statement matched; diagrammatic auxiliary cases not all independently reconstructed. |
| `eta_three` | length≥17 yields a zero sum of length≤3; p.2 | BSP 2007 superscript D³=17 in Prop.1. Also follows from GHST Thm1.7 at n=3. Not multiwise D3. |
| `eta_five` | length≥33 yields a zero sum of length≤5; p.3 | Published BSP 2012 p.28; definitive GHST 2007 Thm1.7 p.4 at n=5, proof p.17 via Prop.5.6 pp.16–17. GHST computational premise not reproduced. |
| `D3_le_five` | length≥33 yields three disjoint zeros; p.3 | Published BSP p.28. Complete extraction deduction from η5≤33 and p-group input is supplied below; no assertion of the exact D3 value. |
| `eta_large` | prime p≥7, η(Cp³)≤M=3p²−4p−3; p.3 (2) | Published BSP Thm1.2(3), printed p.22, includes p=7; proof pp.28–30. Separate p=7 Lemma5.2 case proof remains incompletely checked. |
| `Dk_small_large` | prime p≥7, j≥1; Dj(Cp³)≤max(5p−2,3(p−1)j/2+2p+5); p.3 (3) | Exact statement matches published BSP Lemma2.3, printed p.23. Its coefficient does not follow from the preceding displayed short-block bound; proof gap remains, detailed below. |

Freeze–Schmid SRC-0010 was read at Proposition 3.1(3), pp.6–7; Proposition 3.2 / Remark 3.3, pp.7–8; Lemma 3.4, p.8; Proposition 3.5 / Theorem 3.6, p.9; and Remark 5.3, pp.11–12. Theorem 3.6's proof refers the general inequality to an earlier source; S002 supplies the independently checked k=1 argument actually used here. Its more general statement also follows by taking Dk(H) disjoint quotient blocks and then k disjoint subgroup zero sums. None of this requires H to be a direct summand.

**Extraction, p.2 Lemma 2.2.** If η(G)≤M and Dj(G)≤M, j≥1, removing k−j blocks each of length≤e from a sequence of length M+e(k−j) leaves at least M terms. At every extraction the remaining length is at least M, so the η hypothesis is available. The j final blocks are disjoint from those removed. This checks the boundary k=j and proves Dk≤M+e(k−j).

**Local p=2,3,5 deductions, pp.2–3.** At p=2, 2k+3≤2k+4 for k≥3p−2=4. At p=3 use j=3, M=17: D3≤15≤17 and η≤17 imply Dk≤3k+8≤3k+9 for k≥3, hence for k≥7. At p=5 use j=3, M=33: Dk≤5k+18≤5k+25 for k≥3, hence for k≥13. These are complete conditional deductions, not independent proofs of all small-prime inputs.

**D3(C5³)≤33 deduction.** More generally for odd p≥3, a sequence of length 4p−3 over Cp³, embedded as (g,1) in Cp⁴, has by the p-group theorem a zero sum whose size is p,2p or 3p. A 3p-term zero sum splits into two nonempty zero sums: apply D(Cp³)=3p−2 to any 3p−2 of its terms, then take the complementary block. One block has length≤(3p−1)/2≤2p. Thus s≤2p(Cp³)≤4p−3. At p=5 remove ≤5 terms from 33 using η5, then ≤10 from the remaining at least 28≥17, then one more zero sum from the remaining at least 18≥13. This supplies every threshold in BSP's brief p.28 deduction (CLM-0067, conditional on the stated source inputs).

**Large-prime rounding, p.3.** Put a=3(p−1)/2, b=2p+5 and x=(M−b)/a=2(3p²−6p−8)/(3(p−1)); j0=floor(x). For p≥7, x≥10 because 3p²−21p+7≥0; thus j0≥1. Also x<2p, since subtracting the numerators gives −6p−16<0. Hence j0<2p<3p−2. Further M−(5p−2)=3p²−9p−1>0, and aj0+b≤M. The axiom would give Dj0≤M. Since j0≥x−1,

    pj0+p²−M ≥ p(x−1)+p²−M = (3p²−16p−9)/(3(p−1)) ≥ 0.

The last numerator equals 26 at p=7 and increases thereafter. At p=7 explicitly M=116, a=9, b=19, x=97/9, j0=10, and pj0+p²=119≥116. Extraction now gives Dk≤pk+p² for k≥3p−2. The rounding and inequalities are sound **conditional on** the two displayed imported estimates; checking them does not resolve Lemma2.3's proof discrepancy.

The read-only axiom inventory uses natural-number subtraction and division. In its stated ranges m≥1, q≥2 and p≥7 all the displayed differences are nonnegative; since p≥7 is prime, p−1 is even and `3*(p−1)/2` is exactly the displayed integer coefficient. Thus natural-number truncation does not change these imported formulas. This is a paper check of the input expressions, not execution or verification of the formalisation.

**Global induction, pp.3–4.** Q=P(n) is the largest full primary component p^a dividing n, not the largest prime divisor. Write n=Qp1…ps with primes repeated according to multiplicity. Every pi≤Q and each intermediate m≥Q. At the base, D(CQ³)=3Q−2=4Q−Q−2. At a step k=D(Cm³)≥3m−2≥3p−2, so the local estimate applies. The subgroup deduction gives D(Cpm³)≤pD(Cm³)+p². The required comparison to 4pm−Q−2 is p²−2p+2≤(p−1)Q, which follows from Q≥p and p≥2. Prime-power n has s=0 and is covered. n=1 is outside the theorem and treated separately. Finally Q≥2 gives D≤4(n−1); consequently (D−1)/(n−1)≤4−1/(n−1), and the supremum is at most 4. This last claim is an upper bound, not a claim the supremum equals 4. CLM-0071 records only the conditional implication.

## 3. Definitive published large-exponent version and remaining gap

SRC-0021 is the author-hosted **publisher offprint**, Contemporary Mathematics 579 (2012), pp.21–31, DOI 10.1090/conm/579/11515. The printed imprint, page numbers and DOI were checked. It differs materially from the annotated nine-page draft SRC-0009: the draft's Lemma4.2 is published Lemma2.1, the draft note “Forgot the second claim” is absent, and the published proof adds a sentence about the second claim. The published Theorem1.2(3) says **p≥7**, not the draft's p>7. Thus the publication/version uncertainty is resolved; completeness of each argument is a separate question. The later arXiv copy is not substituted for the publisher offprint.

Published Lemma2.1's *statement*, p.22, bounds a short block in Cp³ by R=(3p−1)/2 at length 6p−3. Its p.23 proof splits a 3p-term zero sum but writes 3(p−1)/2 instead. For odd p the split guarantees floor(3p/2)=(3p−1)/2, which is **one larger**. Published Lemma2.3 uses the smaller coefficient 3(p−1)/2; the rank-three proof is omitted as easier, and the supplied higher-rank proof repeats the smaller coefficient. The printed statement therefore matches Grinsztajn's axiom, but the displayed argument does not discharge it. We have not disproved Lemma2.3. An additional sharper argument or corrected estimate is needed before declaring that exact imported axiom proof-verified.

The Chevalley–Warning equations on p.23 print all plus signs. The usual equations have alternating signs for odd multiples of p. Under the assumed absence of p- and 3p-term zero sums those terms vanish, and the 5p term is separately excluded; the specialized proof still works. Section 4 below gives the coefficients and contradiction explicitly, without adopting the stronger short-block conclusion.

For η in rank three, p.30's plane averaging gives, with m maximal line occupancy,

    |A∩U| ≥ 3p−7 + m + (4−m)/(p+1).

No short zero sum implies |A∩U|≤3p−3 because η(Cp²)=3p−2. This forces m≤4. If m=4, |A∩U|≥3p−3 and published Lemma5.1 (rank-two Property C) gives a point of multiplicity p−1>4, impossible for p≥7. If m=3, integrality gives |A∩U|≥3p−3 and the same contradiction. Thus m≤2. Now integrality gives |A∩U|≥3p−6 while line occupancy gives |A∩U|≤2(p+1), so p≤8. This closes the **p≥11 reduction conditional on the cited rank-two facts**, including the integer ceilings missing from the terse text. Lemma5.1 itself cites the Property B and Property C results; those original proofs were not fully reconstructed.

At **p=7** the surviving plane has at least 15 terms and at most two per line. Lemma5.2, printed pp.29–30, is needed. Its case discussion is explicitly brief; exclusions of permitted points and several symmetry reductions are not completely justified in the printed text. One subcase says (1,6) does not occur, then includes (1,6) in its proposed zero sum. A valid correction and complete case exhaustion were not established in this session. **η(C7³)≤116 remains SOURCE_STATED, not independently closed.** No enumeration was used to fill the gap.

For p=5, the definitive source of η5=33 is GHST, *On Short Zero-Sum Subsequences II*, Integers 7 (2007), A21, SRC-0024. Theorem1.7 p.4 says s(Cn³)=η(Cn³)+n−1=9n−8 for n=3^a5^b. At n=5, η=37−4=33. Its proof p.17 uses Proposition5.6 pp.16–17, a computational classification giving s(C5³)=37 and Property D. The structural starting reduction Proposition5.5 p.16 and the program description were read. No code or output was executed or certified; this is a remaining primary computational dependency, not a programme exact computation. At n=3 the same theorem gives η3=19−2=17, consistent with BSP2007.

## 4. A weaker estimate suffices for the local deduction

This is a **complete conditional paper deduction** (CLM-0068) that avoids assuming the unverified coefficient in Lemma2.3. Assumptions are the classical Chevalley–Warning theorem, the p-group Davenport theorem (rank three and four), and the *source-stated* η(Cp³)≤M for prime p≥7. It does not repair the exact stronger axiom or the p=7 η proof.

First prove the correctly rounded short bound R=(3p−1)/2 at length 6p−3. For a sequence S with no p- or 3p-term zero sum, let Nr count zero-sum index subsets of size r. Chevalley–Warning applied to the three coordinate equations and the length equation, all using variables to the power p−1, gives alternating sums 1−Np+N2p−N3p+…≡0 for any sequence of length at least 4p−3. The total degree is 4(p−1)<4p−3. Each selected index contributes p−1≡−1 choices, explaining the signs.

There can be no 5p-term zero sum Z in S: take T⊂Z of length 4p−3. The congruence for T reduces to 1+N2p(T)≡0, so a 2p-term zero sum exists; its complement in Z would have length 3p. For A=N2p(S) and B=N4p(S), sum the T congruences over all (4p−3)-subsets of S, and the analogous U congruences over all (5p−3)-subsets. The resulting congruences are

    10+3A ≡ 0,    5+3A+B ≡ 0,    1+A+B ≡ 0 (mod p).

The coefficients follow from binomial counting and Lucas reduction: the constants are binom(5,3)=10 and binom(5,4)=5; the A coefficients are binom(3,1)=3 and binom(3,2)=3; the B coefficient is 1. Here p≥7 ensures the displayed base-p digits are valid. Subtract the last two equations to get 4+2A≡0; combine with the first to obtain 4≡0, impossible. Therefore S has a p- or 3p-term zero sum. In the latter case the splitting argument from Section 2 gives a block of length at most R. All index blocks used in this argument are nonempty; the complement in a 3p block is nonempty because the selected sub-block has length at most 3p−2.

Next D2(Cp³)≤5p−2: use s≤2p≤4p−3 proved in Section 2 to extract ≤2p terms, leaving ≥3p−2 for another zero sum. Inductively, for every integer j≥2,

    Dj(Cp³) ≤ 5p−2 + (j−2)R.

For j≥3 the proposed starting length is at least 5p−2+R≥6p−3, so one R-short block can be removed and the induction hypothesis applied to the remainder. Now choose the **integer j=2p−4**, which is at least 2 and at most 3p−2. Its bound is

    5p−2+(2p−6)(3p−1)/2 = 3p²−5p+1 ≤ M,

with slack p−4. With η≤M the extraction lemma yields, for k≥3p−2≥j,

    Dk(Cp³) ≤ M+p(k−j) = pk+p²−3 ≤ pk+p².

This supplies an alternative sufficient local bound using the weaker, justified short-block estimate. It establishes a conditional mathematical route, not unconditional source certification, and does not upgrade the exact imported `Dk_small_large` axiom.

## 5. BSP2007 and Sheikh: which assertion is affected?

BSP2007 SRC-0008 / SRC-0019 Proposition1 p.3 and Proposition8 pp.10–11 distinguish the **subscript** D2=11, Dk=3k+6 (k≥3), from **superscript** D³=17, the at-most-three threshold. Proposition8 relies on short-zero-sum classifications in the earlier diagrammatic lemmata. Its lower-bound description distributes k−3 extra triples, so the maximum number of monochromatic zero-sum triples is k−3; the nearby k−2 phrase on p.10 is inconsistent with that count. Its later counting uses k−3. This observation alone does not verify all classification cases or establish a new proof of Proposition8. The S002 prose that called superscript D³ an exactly-three invariant is corrected to at most three; its displayed multiwise formulas stay unchanged.

The full Aleen Sheikh thesis (2017, Royal Holloway, 137 pages) remains inaccessible through the university PDF and tested public file variants (HTTP403). **Full Chapter4 was not read.** Primary indexed Chapter4 opening and Remark4.3.11, printed p.41, were accessible. The latter points to a statement on BSP p.19: a length-16 sequence with no **exactly three-term** zero sum need not have total sum zero. Its doubled eight-point example has total (1,2,2). Among its listed support points are (1,0,0) and (2,0,0), whose sum is zero. Thus it fails the **no zero sum of length at most three** hypothesis of earlier Lemma1 and of the corresponding Proposition8 classification step. This particular remark therefore does **not** refute the distinct multiwise Proposition1/8. It also does not rehabilitate every argument in that proposition; the full thesis and the earlier auxiliary cases still need inspection. The later family C3⊕C3⊕C3d is different from C6³.

## 6. Yiu main proof and actual ancillary access

SRC-0015 arXiv:2609.04950v1 (4 September 2026), all 13 written PDF pages, was read. It claims D4(C5³)=30 and Dk(C5³)=5k+10 for k≥2. Evidence status stays **SOURCE_STATED**, with written proof access upgraded to `PROOF_INSPECTED` of the stated scope. It is not `COMPUTED_EXACT` or `FORMALLY_CERTIFIED` for this programme.

The factorisation characterization in Lemma2.1 and the Freeze–Schmid recurrence in Lemma2.2 were checked at the level of their stated deductions. The latter uses extremal *zero-sum* sequences, so its threshold is max(Dk+ℓ,s≤ℓ−1), not a mistaken arbitrary-sequence extraction at s≤ℓ−1. The D2=20 input is attributed either to Zhao's analytic preprint or to the paper's separate short-block route; neither is independently proved here. The subsequent recurrence deductions are conditional on those base values.

The upper D4 argument reduces a hypothetical extremal length-31 zero-sum sequence to a restricted search. Its reductions use η5=33, Property C/saturation, GL normalisation, multiplicity constraints, rank/plane coverings and earlier computations for small supports. The paper reports 60 multiplicity patterns and 78 normalised branches; these are **author-reported counts**, not counts computed here. The main obstruction is the computational premises: M1 (D3=25) has a single final implementation; independently repeated candidate-generation totals are not an independent repeat of the final three-disjoint-zero-sum predicate. M2 (s≤6=24) is described as independently repeated; M3 (s≤7=19) supports an alternative D2 route. For the ensuing deductions only the upper inputs D3≤25 and s≤6≤25 are needed, a distinction from proving those exact constants. Theorem1.1(a)'s length-31 exclusion does not use M1–M3; part (b)'s passage to D4 and the full multiwise formula does. The paper's audit discussion on p.12 explicitly describes the absence of external review/certificates and the scope of the repeats. No premise is promoted on the strength of that description alone.

Both the unversioned and v1 arXiv source downloads were inspected as archives, **without running code**. Each was 16,680 bytes with the same SHA-256. Their complete member list is `00README.json` (300 bytes), `bibliography.bib` (3559), `body.tex` (43822), `main.tex` (634), and `preamble.tex` (1028). There is no code, log or ancillary folder in either downloaded archive. The versioned `/anc` source route returned HTTP404; the retrieved abstract HTML's comment refers to ancillary files but exposed no such download links. This establishes a discrepancy for the actual retrieved bundles, **not** that the advertised records cannot exist elsewhere. Exact original code/log/certificate URLs and predicate coverage remain missing. No new algorithm was written or executed to substitute for them.

## 7. Every n≤30 row and source hierarchy

All lower endpoints are 3n−2, with n=1 separately D=1. The table below is the paper audit; its numbers are not results of a group-element search. The complete 30-row machine-readable and Markdown frontier is synchronized separately.

| Inputs | n in 1..30 | Result / deduction |
|---|---|---|
| Definition | 1 | 1 |
| Source-stated p-group theorem | 2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29 | Exact 3n−2: 4,7,10,13,19,22,25,31,37,46,49,55,67,73,79,85 respectively |
| Original II Cor.(4.3), plus Schmid Thm4.1 for n=6 | 6,10,14,18,22,26 | Exact 16,28,40,52,64,76 respectively |
| Original III Cor.(1.5), VIII | 12,24 | Exact 34,70 (also covers n=6) |
| S002 tripling and D(C5³)=13 | 15 | 43..45 because 3·13+6=45 |
| S002 doubling and source-stated D(C10³)=28 | 20 | 58..59 because 2·28+3=59 |
| S002 tripling and D(C7³)=19 | 21 | 61..63 because 3·19+6=63 |
| S002 doubling and source-stated D(C14³)=40 | 28 | 82..83 because 2·40+3=83 |
| S002 tripling and source-stated D(C10³)=28 | 30 | 88..90 because 3·28+6=90; doubling via n15 would give 93 |

There are 25 literature-exact/trivial rows and five interval rows. Exact historical values are source statements, while interval arithmetic is a programme deduction conditional on its recorded source inputs. No frontier endpoint needs Yiu's new computational theorem or the Grinsztajn universal bound. The older 16..17 interval remains a valid but nonsharp inequality; its use to recommend n=6 was a literature-coverage failure.

Fresh targeted searches included `"Davenport" "C_6" "2026"`, `"Davenport constant" "C6" exact` with a one-year recency filter and an unfiltered Schmid/Theorem4.1 query. Recent search-result dates often belonged to crawls or reference lists for old work, not new exact theorems. The authenticated exact C6³ result is the published 2011 theorem, with the 1969 routes above. No separate newer exact determination was authenticated in this bounded pass; **non-discovery is not evidence of openness**. The other five interval entries likewise carry no present-day openness assertion.

## 8. Gate and exact remaining obligations

**PASS withheld.** The actual Grinsztajn PDF, publication version, axiom statement matching and algebra are substantially resolved, and the frontier omission is corrected. Remaining obligations are:

1. Published BSP Lemma2.3 p.23: supply a proof for its exact 3(p−1)/2 coefficient or retain that exact axiom as unverified. Section4 supplies a sufficient weaker route but does not prove the axiom.
2. Published BSP Lemma5.2 pp.29–30: fully justify the p=7 cases and repair the inconsistent (1,6) subcase. For p≥11, identify/inspect the original rank-two Property B/C dependencies sufficiently; the conditional plane deduction is checked.
3. BSP2007 auxiliary diagrammatic classifications before Proposition8, and the full Sheikh Chapter4 / p.41 context, are not completely checked. The specific remark's hypothesis mismatch is resolved only to the extent described above.
4. GHST2007 Prop.5.6 pp.16–17: published computational input to η5; independent evidence review remains, with no execution authorized in this session.
5. Yiu's advertised computational records are absent from the downloaded source bundles. Locate and inspect the actual records and their independent-check scope before promoting computational claims.
6. The corrected historical frontier needs proof-dependency review (II Theorem2.8/4.2; III Lemma1.2/1.3 and Theorem1.4) and targeted literature review of the five remaining intervals. Full original Olson proof was not rechecked.

These are unresolved research obligations for a future separately invoked Phase-1 session. No owner decision, credential, third-party contact or external write is required to close S004. No campaign started; no negative exhaustive result, orbit count, counterexample or candidate was certified. Inherited 14/17, +5 and 43/699/5553 remain quarantined; the first two numerical formulas conflict with the correctly read cited multiwise theorem, and the orbit counts lack provenance.
