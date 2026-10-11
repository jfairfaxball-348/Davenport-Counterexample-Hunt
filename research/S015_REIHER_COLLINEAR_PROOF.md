# S015 — Original Reiher Proposition 5.1 independently reconstructed

One bounded 2026-10-11 Phase-1 source-only hand-proof in Davenport-Counterexample-Hunt. LIVE entry main 2c1e0dac220467d5c3bab526ec56bca61308a2b8; original Christian Reiher, *A proof of the theorem according to which every prime number possesses property B*, SRC-0025, 29-page original Rostock PDF https://www.math.uni-rostock.de/math/pub/preprints/preprint/2010/pre10_01.pdf; inspected printed pp7–9 and 13–14. S013 historical PDF SHA256 7d94931bcbf8fb4ce77c0ed94206659df74e8cb5543e1615e7dde23e86b994d8, NOT freshly downloaded or rehashed. S014 independently proved Cor2.5, Obs2.6, Prop4.1 and the coefficient identities. No mathematical numerical search, CAS, SAT/ILP, orbit enumeration, historical program, Lean, campaign, candidate, manuscript or publication.

## Definitions, indexed positions and recursions

For vectors V_j=(a_j,b_j) define \(\mu_m(V_1,\ldots,V_N)=[x^my^{N-m}]\prod_j(a_jx+b_jy)\), and \(\mu=\mu_{p-1}\) for N=2p-2. Symmetric in positions and multilinear in each vector. If deleting indices I from 2p-1-term T, denote \(\mu_m^*(I)\). Recursion \(\mu_m(V,W)=a_V\mu_{m-1}(W)+b_V\mu_m(W)\). Deletes are indexed even when vectors repeat; all computations are symbolic over characteristic p.

## CLM-0098 — independent original Lemma 3.1, including replacement step

Given nonzero T_1,...,T_{2p-1} over characteristic-p field F, with \(\mu(T\setminus\{i\})=0\) for every index, at least p+1 T_i are linearly dependent (lie in a common one-dimensional F-subspace).

Assume no line has p+1 entries. Fix index 1 and permute indices so precisely i=1,...,r lie in FT_1, where 1≤r≤p. For i>r set \(u_i=\mu_{p-2}^*(1,i)\), \(v_i=\mu_{p-1}^*(1,i)\). Writing T_i=(a_i,b_i), the two given deletion equations, expanded at T_1 and T_i, are \(a_1u_i+b_1v_i=0\) and \(a_iu_i+b_iv_i=0\). Nonzero determinant \(a_1b_i-a_ib_1\) gives u_i=v_i=0. For 2≤i,j≤r, swap coordinate axes if needed to ensure a_1,...,a_r are nonzero. Dependence a_i b_j=a_j b_i and expansion at the other term yields
\[
a_i\mu_{p-2}^*(1,i)-a_j\mu_{p-2}^*(1,j)
=(a_ib_j-a_jb_i)\mu_{p-2}^*(1,i,j)=0,
\]
and identically with p-1 instead of p-2. Thus a_i u_i and a_i v_i each have a constant value (α and β) across indices 2,...,r. Count each coefficient occurrence:
\[
\sum_{i=2}^{2p-1} a_i\mu_{p-2}^*(1,i)=(p-1)\mu_{p-1}^*(1)=0,
\quad \sum_{i=2}^{2p-1} a_i\mu_{p-1}^*(1,i)=p\mu_p^*(1)=0.
\]
Since i>r summands are zero, (r-1)α=(r-1)β=0. If r≥2 then 1≤r-1≤p-1 is invertible, forcing α=β=0 and u_i=v_i=0 on 2,...,r. If r=1 all i>1 were already done. Therefore for any nonzero Q=(x,y), replacing T_1 by Q leaves deletion at index 1 unchanged and leaves all other deletion coefficients equal to xu_i+yv_i=0. This replacement property is invariant under reordering.

To justify repeated use without accidentally creating p+1 collinear points, extend scalars to the purely transcendental F(t). Choose U=(1,t), V=(1,t²). Their lines are distinct and neither meets a nonzero original F-vector line. Replace first p positions one by one by U, and remaining p-1 by V. Original-vector line multiplicities only decrease (initially at most p); the new lines never exceed p and p-1 respectively. Consequently each replacement satisfies its original hypothesis, and the final U^p V^(p-1) sequence still has all deletion coefficients zero. But an invertible linear transformation sending U to e1 and V to e2 (guaranteed since determinant t²-t is nonzero) preserves the zero-deletion property by S014 Obs2.2. The transformed e1^p e2^(p-1) sequence has deletion of one e1 equal to µ(e1^(p-1),e2^(p-1))=1, contradiction. This independently repairs the potentially implicit induction safety step in the printed 'applying (*) very often' argument. QED.

## CLM-0099 — independent original Proposition 3.3

Let P have 2p-1 nonzero positions, Q,R nonzero, disjoint exceptional sets A,B with |A∪B|<p, terms at A dependent on Q, terms at B dependent on R, and deletion µ(P minus i)=0 outside A∪B. If Q,R dependent, combine A and B and choose any independent replacement direction R. Otherwise one common GL2 transformation gives Q=e1,R=e2 and preserves the zero coefficient statements. For i in A, b_i=0,a_i≠0; for i in B, a_i=0,b_i≠0.

For i outside A, a_iµ*(i)=0 (either µ*=0 outside both sets or a_i=0 on B). For distinct i,j in A, expand at the other index to see
\[
a_i\mu^*(i)=a_ia_j\mu_{p-2}^*(i,j)=a_j\mu^*(j).
\]
The LHS is constant α on A. Summing over all i, \(|A|\alpha=\sum_i a_i\mu^*(i)=p\mu_p(P)=0\). Since |A|<p it is invertible when nonempty, hence α=0 and µ*(i)=0 on A. For B do the corresponding y-coordinate count: \(\sum_i b_i\mu^*(i)=p\mu_{p-1}(P)=0\), yielding µ*(i)=0 on B. The complete deletion condition of Lem3.1 holds, giving p+1 pairwise dependent P positions. No strengthened unconditional assumptions or hidden zero indices are used. QED.

## CLM-0100 — independent original Proposition 5.1, p=5 covered

For p=2 three distinct points cannot lie on an affine line of F2²; for p=3 every cloudy sequence is simple by S014 proof (five nonzero points distributed across four directions yield two dependent indices, and Obs2.6 applies). Assume p≥5. Take cloudy length-(2p-1) indexed S=(A,B,C,P1,...,P_(2p-4)) with A,B,C distinct and on one affine line. Cor2.5 forbids two distinct cloudy points dependent with the origin, so the line avoids 0. Choose independent X,Y and distinct a,b,c∈Fp such that A=X+aY, B=X+bY, C=X+cY.

Fix EACH original residual index i and delete exactly its occurrence P_i. The 2p-2 remaining terms form a suspicious sequence. Define trilinear symmetric \(T_i(U,V,W)=\mu(U,V,W,P_1,...,\widehat{P_i},...,P_{2p-4})\), with exactly 3+(2p-5)=2p-2 arguments. Apply S014 independently established exact strategic Proposition4.1. Let k=[XY]≠0. Compute
\[
[BC]=k(c-b),\qquad[CA]=k(a-c),\qquad[AB]=k(b-a),
\]
so their sum is 0. Thus the 3T_i(A,B,C) strategic cross term vanishes identically. The rest reads
\[
(c-b)T_i(A,A,A)+(a-c)T_i(B,B,B)+(b-a)T_i(C,C,C)=0.
\]
Multilinearity gives T_i(X+tY,X+tY,X+tY)=u0+3tu1+3t²u2+t³u3 with u2=T_i(X,Y,Y), u3=T_i(Y,Y,Y). For the three weights w=(c-b,a-c,b-a),
\[
\sum w=0,\quad \sum wt=0,\quad
\sum wt^2=\Delta=(a-b)(b-c)(c-a),\quad
\sum wt^3=(a+b+c)\Delta.
\]
These latter two are exact Vandermonde factorizations, obtained by expanding differences (not computationally). Since kΔ≠0, cancellation in Fp yields 3T_i(X,Y,Y)+(a+b+c)T_i(Y,Y,Y)=0. Set Z=3X+(a+b+c)Y=A+B+C. Trilinearity implies T_i(Y,Y,Z)=0 for ALL i. Z≠0, because A+B+C=0 would be a nonempty proper zero-sum subsequence (3<2p-1). Furthermore [Y,Z]=-3[XY]≠0 for p≥5, so Y and Z are *independent*, including p=5; no division by 3 or factorial required.

Apply independent Prop3.3 to indexed auxiliary \(P'=(Y,Y,Z,P_1,...,P_{2p-4})\) of length 2p-1. Its 3 exceptional indexed positions are A'={1,2} dependent on Q=Y and B'={3} dependent on R=Z, with |A'∪B'|=3<p; deleting ANY other position gives exactly T_i(Y,Y,Z)=0. Lem3.1/Prop3.3 yields p+1 auxiliary terms on a common one-dimensional line. Because the two Y's form one line while Z is on a *different* line, AT MOST TWO of the auxiliary first three terms lie on the common line. Therefore at least p-1 ORIGINAL residual positions P_i lie on that line, counted with exact original multiplicities and positions. By independently proved S014 Obs2.6, the original cloudy S is simple. This establishes all p≥5 and hence all primes. QED.

**Dependency precision:** Proposition5.1 uses S014 Prop4.1, Cor2.5, Obs2.6 and independently closed new Lem3.1/Prop3.3. Obs7.1's factorial identity is not used in this proposition; previously established factorial identities retain their separate scope. Divisions in Section3 are only by nonzero determinants and positive counts strictly less than p. No unfinished imported lemma.

## Read-only provenance and numerical frontier

Official Royal Holloway Sheikh2017 137-page original thesis PDF https://pure.royalholloway.ac.uk/files/28262990/The_Davenport_Constant_of_Finite_Abelian_Groups.pdf: S015 direct HTTP403 (separate S014/S013403). Full Chapter4 and Remark4.3.11 unavailable, no upgrade. GHST2007 historical C53.html code AND detailed output http://www.combinatorics.net.cn/homepage/hou/C53.html: original web access route inaccessible, neither code nor output authenticated or executed (separate S013 timeout). Yiu arXiv2609.04950v1 original abstract and HTML read-only: independent final M1 three-disjoint predicate code/log/certificate unverified. S013 16680-byte source archive SHA256 99dc658b3381038fe0c7b2f89145c52a9687e185883cf2a6fdcc0cb8860b1e21 was five repeated TeX/README/bibliography items, not an independently verified final M1 predicate implementation. M1 repeated 98622 generators/230983 extensions differ from final three-disjoint test; M2s≤6=24 and M3s≤7=19 distinct. No non-discovery⇒nonexistence.

GG1999 SRC-0026 B⇒C remains PROGRAMME_PROVED only CONDITIONAL on prime Property B (older CLM-0082 remains historical SOURCE_STATED). BSP2012 SRC-0021 gives only coefficient R=(3p-1)/2, not 3(p-1)/2. BSP2007 SRC-0008/0019 original diagrams/upper induction not reconstructed; restricted k-3 count insufficient. Multiwise SUBSCRIPT D3(C3³)=15,D4=18 differs from superscript at-most-three threshold17.

Thirty-row frontier (n1..30) read and mirrored without numerical/status/evidence change; 25 exact/trivial historical/trivial rows and five conditional intervals: n15 43..45, n20 58..59, n21 61..63, n28 82..83, n30 88..90. No new authenticated exact primary claim in bounded targeted searches; this is not evidence of present-day openness. Schmid2011 n6=16 and original van Emde Boas II/III rank-three 2p^a/3·2^a exact families remain SOURCE_STATED without whole historic proofs. Inherited14/17, +5 and orbit43/699/5553 remain quarantined. No Phase2/3, tooling, activation, candidate or numerical campaign.

STOP: exact single active Proposition5.1 closed; no attempt on Proposition6.2,8.1, Section9, Proposition10.1 or full Property B in S015.
