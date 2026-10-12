# S016 — Reiher Section 6, original Lemma 6.1 and Proposition 6.2

2026-10-12, ONE bounded Phase-1 original-primary-source symbolic hand-proof. SRC-0025: Christian Reiher, original 29-page PDF https://www.math.uni-rostock.de/math/pub/preprints/preprint/2010/pre10_01.pdf, printed pp14–15, PDF zero-based pp13–14, directly inspected as original page images and text. S013 historical SHA256 7d94931bcbf8fb4ce77c0ed94206659df74e8cb5543e1615e7dde23e86b994d8 NOT rehashed here. All computations below are symbolic hand calculations, not CAS/numerical search. No author code, enumeration, SAT/ILP, Lean, campaign, candidate or manuscript.

## Inputs and small primes

A cloudy sequence over Fp² has length 2p−1, sum zero and no nonempty proper zero-sum index-subsequence; deleting ANY original indexed term gives suspicious length 2p−2. By S014 independently proved Lemma2.3 every such deletion has µ=1, where µ(V1,...,V_(2p−2)) is the coefficient of x^(p−1)y^(p−1) in the product of coordinate linear forms. µ is symmetric and multilinear. By S014 Cor2.5 distinct cloudy points are pairwise linearly independent with the origin; no term is zero. By Obs2.6 p−1 original positions dependent on one line imply the cloudy sequence is simple.

For p≥5 the S014 independently proved strategic Proposition4.1 for suspicious (X,Y,Z,P1,...,P_(2p−5)) states
 [YZ]T(X,X,X)+[ZX]T(Y,Y,Y)+[XY]T(Z,Z,Z)+3([YZ]+[ZX]+[XY])T(X,Y,Z)=0,
where T(U,V,W)=µ(U,V,W,P1,...,P_(2p−5)) and [XY]=det(X,Y). S015 Prop3.3 permits up to two exceptional prescribed nonzero vector directions of total *indexed cardinality strictly less than p* in a nonzero auxiliary 2p−1-term sequence, provided µ vanishes on deletion of every other indexed term; its conclusion is at least p+1 auxiliary terms on one line. S015 Prop5.1: any cloudy sequence with three DISTINCT collinear points on an affine line is simple. For p=2 Obs2.6 finishes since p−1=1. For p=3 five nonzero cloudy terms occupy only four one-dimensional lines, hence two share a direction; Cor2.5 makes them equal and p−1=2, so Obs2.6 finishes. Therefore it suffices for both Section6 assertions to prove p≥5, INCLUDING p=5.

## CLM-0101 — Lemma 6.1, non-parallelogram trapezoid

Let S=(A,B,C,P1,...,P_(2p−4)) be cloudy with 0,A,B,C the vertices of a trapezoid but NOT a parallelogram. Relabel A,B,C to ensure [AB]=k≠0 and C=B+rA: the parallel pair can be chosen to be 0A and BC. r≠0 by distinctness; r=1 gives C=A+B (a parallelogram), while r=−1 gives A+C=B (also a parallelogram, under another vertex ordering). Thus r∉{−1,0,1}, so k(r³−r)=k r(r−1)(r+1) ≠0 in Fp.

For EACH original residual occurrence Pi, delete just its index. The remaining suspicious sequence defines symmetric trilinear Ti(U,V,W)=µ(U,V,W,P1,...,omit Pi,...,P_(2p−4)), with exactly 3+(2p−5)=2p−2 positions. The strategic equation with A,B,C singled out has
 [BC]=−rk, [CA]=−k, [AB]=k, [BC]+[CA]+[AB]=−rk.
Since C=rA+B,
 Ti(C,C,C)=r³Ti(A,A,A)+3r²Ti(A,A,B)+3rTi(A,B,B)+Ti(B,B,B)
 and Ti(A,B,C)=rTi(A,A,B)+Ti(A,B,B).
Substituting all terms into the exact strategic identity cancels Ti(A,A,B), Ti(A,B,B), Ti(B,B,B) coefficient-by-coefficient, leaving
 k(r³−r)Ti(A,A,A)=0.
The coefficient is nonzero, giving Ti(A,A,A)=0 for EVERY residual index i, not merely their sum.

Introduce an auxiliary 2p−1-position nonzero sequence H=(A,A,A,P1,...,P_(2p−4)). Apply S015 Proposition3.3: exceptional positions E={1,2,3}, all aligned with Q=A, second exceptional set empty and any nonzero R; |E|=3<p even for p=5. Every NON-exceptional indexed deletion has µ exactly Ti(A,A,A)=0. Hence ≥p+1 auxiliary positions occupy one line L. If L=Fp A, at most 3 of those are the inserted A positions, leaving at least p−2 ORIGINAL residual Pi positions, and the single ORIGINAL A in S brings the original count to at least p−1. If L≠Fp A, all ≥p+1 line positions already belong to the original residual positions. In both cases S has ≥p−1 original indexed terms in a line; S014 Obs2.6 proves it simple. All divisors and multiplicity counts explicit. QED (all primes including p=5).

## CLM-0102 — Proposition 6.2, including parallelogram configuration

By CLM-0101 it suffices to treat a trapezoid that IS a parallelogram. Relabel the three present nonzero vertices as A,B,A+B, where k=[AB]≠0 (Cor2.5), and each is nonzero and distinct. If the entire cloudy sequence uses only these three values, S014 CLM-0097 already proves simplicity. Alternatively, with multiplicities α,β,γ≤p−1, total length α+β+γ=2p−1 and zero total gives α+γ≡β+γ≡0 (mod p); because each lies between 2 and 2p−2, both equal p. Thus α=β=p−γ, so 2p−γ=2p−1 implies γ=1 and α=β=p−1; Obs2.6 applies. This checks the original printed argument independently.

Otherwise choose a fourth DISTINCT nonzero original C and write S=(A,B,A+B,C,P1,...,P_(2p−5)), C=rA+sB uniquely. Put T(U,V,W)=µ(U,V,W,P1,...,P_(2p−5)), symmetric trilinear with exactly 2p−2 indexed positions, and X=T(A,A,A), Y=T(A,A,B), Z=T(A,B,B), W=T(B,B,B). The FOUR genuine cloudy-deletion µ=1 equations, omitting original A,B,A+B,C respectively, are:
 E1: rY+(r+s)Z+sW=1, since T(B,A+B,C)=1;
 E2: rX+(r+s)Y+sZ=1, since T(A,A+B,C)=1;
 E3: rY+sZ=1, since T(A,B,C)=1;
 E4: Y+Z=1, since T(A,B,A+B)=1.
No µ=0 blanket condition is assumed.

Omit indexed A+B; suspicious (A,B,C,P1,...). In its strategic equation [BC]=−rk, [CA]=−sk, [AB]=k, their sum =k(1−r−s); moreover
 T(C,C,C)=r³X+3r²sY+3rs²Z+s³W, T(A,B,C)=rY+sZ.
Dividing solely by k≠0, the FIFTH equation is:
 E5: (r³−r)X+3r(r−1)(s−1)Y+3(r−1)s(s−1)Z+(s³−s)W=0.
Indeed the cross Y coefficient =3r²s+3r(1−r−s)=3r(r−1)(s−1); the Z coefficient =3rs²+3s(1−r−s)=3s(r−1)(s−1).

Use the exact printed multipliers for (E1,E2,E3,E4,E5), in that ORDER:
 1−s², 1−r², (r−s)²+3(r+s)−4, −(r+s), 1.
The X coefficient in the sum equals r(1−r²)+(r³−r)=0, the W coefficient equals s(1−s²)+(s³−s)=0. The Y coefficient expands to
 (r−rs²)+(r+s−r³−r²s)+(r³−2r²s+rs²+3r²+3rs−4r)−(r+s)+(3r²s−3r²−3rs+3r)=0;
the Z coefficient is its r↔s symmetric counterpart and also zero. So weighted LHS=0. Weighted RHS equals
 (1−s²)+(1−r²)+(r−s)²+3(r+s)−4−(r+s)
 =−2+2(r+s)−2rs=−2(r−1)(s−1).
Thus the entire cancellation forces −2(r−1)(s−1)=0. p≥5 guarantees 2≠0, hence r=1 or s=1 (NO division by r,s,r−1,s−1).

If r=1, original A,A+B,C=A+sB are THREE DISTINCT points (C chosen distinct) on the affine line A+Fp B, which does not contain 0 because [AB]≠0. Exact S015 Prop5.1 applies. If s=1, original B,A+B,C=rA+B are three distinct points on B+Fp A, likewise not through origin; apply exact Prop5.1. This proves every parallelogram case, hence together with Lem6.1 every trapezoid case. p=5 works with 3<p and 2≠0; p2/3 were independently settled. QED.

## Scope, original provenance and frontier audit

STOP after Section6 Proposition6.2: no original Prop8.1, Section9 Lem9.2/9.6, conics/quartics, Prop10.1 or full Property B proved. New CLM-0101/0102 are rank-two geometry only. S012 p7 corrected doubled triple 2(6,1)+(2,4)+(0,1)=0 versus printed false 2(6,1)+(1,6)+(1,0), CLM-0084–0088, S013 exact rank-two CLM-0089–0093 including original GG1999 B=>C CONDITIONAL on Property B (historical CLM-0082 SOURCE_STATED), S014 CLM-0094–0097 and S015 CLM-0098–0100 unchanged. No universal Property B, unconditional C, eta(C7³)≤116 or rank-three conjecture theorem. BSP2012 SRC-0021 coefficient ONLY R=(3p−1)/2, NOT 3(p−1)/2. BSP2007 full diagrams/induction not reconstructed; restricted k−3 count insufficient. Subscript multiwise D3(C3³)=15,D4=18 is not superscript at-most-three threshold17.

S016 fresh read-only provenance: SRC-0013/SRC-0020 official Sheikh2017 137-page thesis PDF Chapter4/Remark4.3.11 HTTP403, separately logged from S013–S015 HTTP403. SRC-0024 original GHST2007 C53.html full code/output URL inaccessible; nothing executed/authenticated. SRC-0015 original arxiv2609.04950v1 Yiu abstract and HTML read; no independent final M1 three-disjoint test program/log/certificate authenticated. S013 original source archive 16680 bytes SHA256 99dc658b3381038fe0c7b2f89145c52a9687e185883cf2a6fdcc0cb8860b1e21 was only repeated TeX/README/bibliography entries; old archive bytes/hash NOT freshly acquired. Repeated 98622 generators/230983 extensions are not the final test, M2s≤6=24/M3s≤7=19 distinct. No non-discovery means nonexistence.

Full n=1..30 in two 30-row mirrors: retain 25 historically exact/trivial source claims and five conditional intervals n15 43..45, n20 58..59, n21 61..63, n28 82..83, n30 88..90. Bounded literature query found no newly authenticated exact primary update; no CURRENT openness assertion. Schmid2011 D(C6³)=16 and van Emde Boas II/III 2p^a / 3·2^a exact rank-three families SOURCE_STATED, no fresh entire historical proofs; inherited14/17, +5, orbit43/699/5553 quarantined. Phase1 IN_PROGRESS, Phase2/3 NOT_STARTED, CAM-0001 PROPOSED/NOT RUNNING, activation BLOCKED by n6=16. No replacement, mathematical search, campaign, candidate, Lean or outreach.