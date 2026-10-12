# S023 — definitive BSP2012 splitting proof obstruction and bounded stop

Date: 2026-10-12. One bounded Phase-1 original-primary-source symbolic hand-proof and provenance session. Entry LIVE remote main `44d451ead8854a35419462cd0a69a35d847c12cc` with tree `b233c61e44ab1586b6c0a76bf54afb2f0706e7dc`. Historical-proof audit only; no rank-three Davenport counterexample, CAS, numerical mathematical search, programme or published-rank-three D theorem.

## Exact primary-source reading

The **definitive publisher offprint** Gautami Bhowmik and Jan-Christoph Schlage-Puchta, *Davenport’s constant for groups with large exponent*, Contemporary Mathematics 579 (2012), DOI 10.1090/conm/579/11515, original author-hosted https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf, printed pp.22–24 / PDF indices 1–3, was inspected both as original page images and as text, including Theorem 1.3, Lemmas 2.1–2.3. The annotated pre-publication draft SRC-0009 was NOT substituted for SRC-0021.

Lemma 2.1 **statement** says a 6p−3 term sequence over C_p³ has a nonempty zero-sum block of length ≤(3p−1)/2. Its proof first obtains a zero-sum Z of length p or 3p. In the 3p branch, it applies D(C_p³)=3p−2 to obtain a nonempty proper zero-sum Y⊊Z and complements it with Z\Y. It then asserts the stronger bound 3(p−1)/2. Lemma 2.3's rank-three bound is D_k(C_p³)≤max(5p−2, [3(p−1)/2]k+2p+5), with NO proof of the first inequality: it states only the d≥4 inequality is proved, and that proof invokes the same stronger short-block coefficient. Distinguish the validity of the claimed multiwise estimate from validity of the displayed derivation.

## CLM-0113 — what the splitting actually proves

For odd p, |Z|=3p. Since Y and Z\Y are disjoint nonempty zero sums, their shorter length satisfies

min(|Y|,3p−|Y|) ≤ floor(3p/2) = (3p−1)/2.

For a p-term Z this already exceeds the needed bound p≤(3p−1)/2 for p≥1 odd. The argument supplies **NO** implication that min≤3(p−1)/2: the integer pair ((3p−1)/2,(3p+1)/2) gives the missing balanced split. To exclude it requires an ADDITIONAL genuinely structural fact beyond existence of Y. At p=7 the only guaranteed length from the printed split is 10, not 9. At p=5 it is 7, not 6; at p=3 it is 4, not 3. For p=2, 6p−3=9 terms in a group of 8 elements have a singleton zero or a repeated pair, independently giving a zero sum of length≤2 (as the printed (3p−1)/2 statement requires); the split-only bound floor(3p/2)=3 is insufficient at p2. This lemma claims only what follows from this exact splitting argument, NOT optimality of a universal short-extraction theorem for p≥5 or p≥7.

## CLM-0114 — an explicit actual counterexample to the stronger universal short-extraction assertion at p=3

Let F=F₃ and q(x,y)=x²+y². Since nonzero squares in F are 1 and 1+1=2, q(v)≠0 for every nonzero v∈F² (anisotropy). Let

T = { (x,y,q(x,y)) : (x,y) ∈ F²\{(0,0)} } ⊂ F³.

There are exactly eight distinct nonzero points. No two T points are opposites: if (x,y,q(x,y)) and (−x,−y,−q(x,y)) both lay on the graph then q(x,y)=−q(x,y); since char F=3 this forces q(x,y)=0, contradiction.

No three *distinct* T points have zero sum: their distinct first-two-coordinate vectors u₁,u₂,u₃ with u₁+u₂+u₃=0 form a complete affine F₃-line {a−v,a,a+v} for some v≠0. The sum of the three third coordinates is q(a−v)+q(a)+q(a+v)=3q(a)+2q(v)=−q(v)≠0.

Form the indexed sequence T² (two copies of each point), of length 16. It has no nonempty zero sum of length≤3: singleton zero is absent; a repeated pair 2t≠0 and a distinct pair t+u=0 is impossible; a triple of equal terms is unavailable; 2t+u=0 forces u=t in characteristic 3, requiring three copies; and triples at three distinct points are excluded by the line argument. Deleting ANY one of its sixteen indexed positions leaves a 15-term short-free sequence S, with 15=6·3−3, having NO nonempty zero sum of length≤3=3(3−1)/2. This is a rigorous SYMBOLIC counterexample to the stronger uniform short-extraction assertion tacitly used in the printed proof. It is **NOT** a Davenport-conjecture candidate (indeed p3 D(C3³)=7 is source-stated) and does NOT refute the published weaker bound of four or the multiwise D_k estimate.

Consequently there is no universally valid missing lemma of the asserted short-extraction form **for all primes**. Whether the p≥7 version or the published D_k inequalities are correct via a different structural argument is OPEN IN THIS INTERNAL PROOF AUDIT; no global mathematical openness or falsity claim follows.

## Mandatory STOP on first unclosed prerequisite

The stronger block coefficient is false as a universal p3 statement and UNPROVED from the original printed argument for p≥7. The exact first essential missing premise for Lem2.3's original proof is a prime/range-specific valid theorem giving ≤3(p−1)/2 zeros in every required 6p−3 segment, OR a wholly different valid method deriving the multiwise D_k inequality. Because it is not supplied, the rank-three Lem2.3 induction is deliberately **NOT** reconstructed or assumed; its printed proof is omitted. No prior claim is promoted on its authority. The strongest proved weaker **split** bound for odd p remains (3p−1)/2 (at p7:10). Prior source-stated multiwise estimates remain source statements only.

## Read-only provenance and frontier integrity

Sheikh2017 original full 137-page thesis https://pure.royalholloway.ac.uk/files/28262990/The_Davenport_Constant_of_Finite_Abelian_Groups.pdf returned HTTP403 again; Chapter4/Remark4.3.11 NOT read. Original GHST2007 C53.html at https://www.combinatorics.net.cn/homepage/hou/C53.html inaccessible; historical complete code AND output not authenticated, NEVER executed. Yiu arXiv2609.04950v1 HTML https://arxiv.org/html/2609.04950v1 directly inspected: original author's M1 final three-disjoint test is stated as a single implementation despite independent candidate generation; no independent complete terminal M1 programme/log/certificates were authenticated here. Reported 98622/230983 generator counts are intermediate; M2/M3 different predicates. S013 archived 16680-byte SHA256 99dc658b3381038fe0c7b2f89145c52a9687e185883cf2a6fdcc0cb8860b1e21 covers TeX/README/bib, NOT M1. No absent-code, independent-certification or present-day-openness inference. BSP2007 full original diagrams and upper induction separate unproved gate.

The complete JSON n=1..30 mirror and Markdown n=1..30 table were individually reconciled. Preserve ALL 30 D numeric/status/source/evidence cells unaltered: 25 exact/trivial historical statuses and five conditional intervals n15=43..45, n20=58..59, n21=61..63, n28=82..83, n30=88..90. Schmid2011 n6=16 and van Emde Boas II/III rank-three 2p^a, 3·2^a source exact families remain SOURCE_STATED. Inherited D3/D4 ternary 14/17, +5 and 43/699/5553 orbit counts quarantined. Nondiscovery is NOT global absence or current openness. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED/NOT_RUNNING and BLOCKED by n6=16. No campaign, solver, candidate, new target, Lean, Palomar, outreach or publication.

Previous S012–S022 independently reconstructed historic proofs CLM-0087/0089–0112 remain in force. This p3 objection does not undermine S022 unconditional Property C or eta(C7³)≤116, neither of which depends on the disputed stronger splitting coefficient.
