# S018 — Reiher original Section 9 Observation 9.1 and Lemma 9.2

2026-10-12. One owner-invoked bounded Phase-1 original-primary-source **symbolic hand-proof** session. SRC-0025 original Christian Reiher 29-page 2010 Rostock PDF, https://www.math.uni-rostock.de/math/pub/preprints/preprint/2010/pre10_01.pdf, printed pp. 18–20 (PDF pages 17–19, indexed from zero); original image of printed pp19–20 and source text of printed p18 inspected. Web PDF rendering is fresh S018 access, but no fresh binary download/hash: historical S017 289379-byte SHA256 `7d94931bcbf8fb4ce77c0ed94206659df74e8cb5543e1615e7dde23e86b994d8` is **historical only**. No author code, mathematical computation, CAS, enumeration, SAT, Lean, candidate, campaign, manuscript, outreach or publication. This independent proof stops exactly at Lemma9.2.

## CLM-0104: Observation 9.1 — complete proof

Work in any field K with char K != 2. An affine conic is the zero set of `a x^2+b xy+c y^2+d x+e y+f`. It is **proper** precisely if at least one of a,b,c is nonzero; even all K^2 is a conic by the source definition. The hypothesis explicitly requires the SEVEN **distinct** points `0,X,Y,Z,X+Y,Y+Z,Z+X` (order immaterial) to lie on one proper conic. The claim is that some line through 0 contains at least two members of X,Y,Z.

The printed normalization `X=(1,0),Y=(0,1)` needs a case split. If X,Y are linearly dependent, their line through 0 already proves the claim (the seven-point distinctness ensures X and Y are nonzero). Otherwise X,Y are a basis; an invertible linear coordinate change sends them to standard basis vectors and preserves lines, distinctness and properness of the conic (the nonzero degree-two homogeneous leading form remains nonzero under an invertible substitution).

Now write `Z=(r,s)`. Passing through `0,(1,0),(0,1),(1,1)` respectively forces `f=0,d=-a,e=-c,b=0`. Hence the **proper** conic has equation `a(x^2-x)+c(y^2-y)=0`, with `(a,c)!=(0,0)`. Substitution at `Z=(r,s)`, `X+Z=(r+1,s)`, and `Y+Z=(r,s+1)` yields exactly
```
a(r^2-r)+c(s^2-s)=0,
a(r^2+r)+c(s^2-s)=0,
a(r^2-r)+c(s^2+s)=0.
```
Subtract the first equation from the second and third: `2ar=0` and `2cs=0`. Because 2 is invertible, if `a!=0` then `r=0` so Z,Y lie on the y-axis through 0. Otherwise a=0 entails c!=0, hence s=0 and Z,X lie on the x-axis through 0. No division by r or s is used. This closes Obs9.1 for arbitrary K char!=2.

## CLM-0105: Lemma 9.2 — complete seven-alternative proof

Let A,B,C,D be FOUR **distinct** points of K^2. The seven conclusions are exactly the original alternatives: (a) a nonempty indexed submultiset has zero sum; (b) two original points linearly dependent; (c) three original points collinear; (d) three original points together with 0 are the vertices of a trapezoid; (e) one original point equals the sum of the three others; (f) original quadruple forms a parallelogram; or (g) all 14 sums of nonempty subsets of sizes 1,2,3 are distinct, and no 4 of the 7 complementary pairs contribute 8 collinear points, and no 6 pairs contribute 12 points lying on a **proper** conic. The seven complementary pairs, all with common sum T=A+B+C+D, are:
```
(A, B+C+D), (B,A+C+D), (C,A+B+D), (D,A+B+C),
(A+B,C+D), (A+C,B+D), (A+D,B+C).
```
We prove failure of (g) forces one of (a)–(f), in exactly three cases. No uniqueness/classification stronger than (g) is assumed.

**I. Collision of two of the 14 indexed sums.** For distinct nonempty proper subsets I,J of {A,B,C,D} of cardinalities 1–3 satisfying sum(I)=sum(J), cancel the common indexed members, yielding sum(U)=sum(V) for disjoint U=I\\J, V=J\\I. If either is empty, the other is a nonempty zero-sum set, (a). If both nonempty, |U|+|V|<=4. (1,1) contradicts the four original point values being distinct. Up to swapping sides the remaining partitions are (2,1): `A+B=C`, then 0,A,B,C are the vertices of a parallelogram (and hence trapezoid), giving (d); (3,1): `A+B+C=D` gives (e); (2,2): `A+B=C+D` gives (f). These are exhaustive by disjointness and total four indices. This does NOT require a stronger zero-sum assumption.

**II. Eight collinear points from four complementary pairs, assuming all fourteen sums distinct.** Let ell be the common affine line. Each selected pair contributes two distinct points; there are only THREE 2+2 partition-type pairs, so at least ONE of the FOUR singleton/complement pairs was selected. Accordingly ell contains m of the original A,B,C,D with 1<=m<=4 (precisely the number of singleton pairs among the four selected). If m>=3, three originals lie on ell: (c).

If m=2, relabel the two originals on ell A,B. At least TWO 2+2 split pairs are also selected. Of any two of the three split pairs, at least one contains `A+C` or `B+C` (the only split pair without either is `(A+B,C+D)`). Thus ell contains A,B and (say) A+C (other orientation symmetric). If the affine line ell passes through 0, A and B are linearly dependent: (b). Otherwise ell has direction B-A and also contains (A+C)-A=C, whence segment AB is parallel to segment 0C. Because all 14 sums are distinct, A,B,C and 0 are distinct (if any original were 0, adding another original would cause a collision); hence 0,A,B,C form a genuine trapezoid: (d). This does not assume nonparallel opposite sides except as stipulated by the ordinary trapezoid premise; a parallelogram is a trapezoid under the source's inclusive treatment.

If m=1, relabel its original A. The other three selected complementary pairs MUST be all three 2+2 split pairs, so ell contains `A+B,A+C,A+D`; translating ell by −A proves original B,C,D collinear: (c). No m=0 case exists because only three split pairs exist. This exhausts all four-pair cases including the minimum singleton pair count.

**III. Twelve points from six complementary pairs on one proper conic Γ, assuming the fourteen sums distinct.** The ONE omitted pair can be either a singleton/complement pair or a 2+2 split pair. We can relabel A,B,C,D to ensure four **included** pairs are `(A,B+C+D)`, `(B,A+C+D)`, `(A+C,B+D)`, `(A+D,B+C)`: if the omitted pair is singleton-type, choose A,B among the three remaining singleton types (all three split pairs then remain); if omitted split-type, choose A,B from one side of its 2+2 partition, and C,D from the other, so the two cross-split pairs remain. Thus Γ contains the SEVEN DISTINCT points
```
 A, B, A+C, B+C, A+D, B+D, A+C+D.
```
(The first two included pairs furnish A,B and A+C+D; the two cross-split pairs furnish A+C,B+D,A+D,B+C.) Translate every geometric point by −A. Translation sends proper conics to proper conics: the leading quadratic part is unchanged. The seven points become
```
 0, X=B−A, Y=C, Z=D, X+Y=B+C−A,
 X+Z=B+D−A, Y+Z=C+D.
```
They are still seven distinct points, so the JUST-PROVED Observation9.1 applies. The printed call to **"Observation10.1" is an internal numbering error**: the original earlier result is Observation9.1, and Proposition10.1 is a completely different later result NOT used here. Therefore either C,D are linearly dependent, yielding (b); or B−A is dependent with C or D. In the latter case (say C), the line through A and B also contains A+C. If this line contains 0, A,B are linearly dependent (b); otherwise AB is parallel 0C, and 0,A,B,C are four distinct trapezoid vertices (d). The D case is identical with C,D interchanged. Translation is only in the geometric argument; it is **not asserted** to preserve cloudy or zero-sum sequence hypotheses.

Those three cases exhaust every way (g) can fail. Hence (a)–(g) is proved, and the requested STOP is **immediately after Lemma9.2**. No Example8.2, quartic/Definition9.3 consequences, Observation9.4/9.5, Lemma9.6, Proposition10.1, universal Property B/C, rank-three eta7 or conjecture proof.

## Provenance and frontier limits

S018 source-view access: original Reiher PDF live rendered as 29-page primary source and printed pp19–20 visually examined; no S018 fresh binary bytes or SHA256. Original university Sheikh2017 137-page thesis PDF link through Royal Holloway official portal again HTTP403 Forbidden **in S018**; Chapter4/Remark4.3.11 still not fully read, distinct from S017/S016/S015/S014/S013 access events. GHST2007 printed original C53.html both CODE and OUTPUT cannot be reached via web retrieval; neither inspected nor executed. arXiv2609.04950v1 original author HTML/read-only manuscript accessible, source tar/gzip retrieval unsupported in web view, no independent final M1 three-disjoint predicate logs/code/certificate authenticated in S018. Historical S013 16680 bytes SHA256 99dc658b3381038fe0c7b2f89145c52a9687e185883cf2a6fdcc0cb8860b1e21 is not freshly hashed; repeated 98622 generators/230983 extensions are not an independently repeated FINAL M1 predicate, M2s<=6=24 and M3s<=7=19 are different checks. Keep GG1999 SRC-0026 B=>C conditional; BSP2012 SRC-0021 stronger coefficient unproved beyond R=(3p−1)/2 split; BSP2007 original diagrams and upper induction unproved, D_3(C3^3)=15 and D_4=18 differ from D^(<=3) threshold17.

All n=1..30 in BOTH frontier mirrors retained; original exact families are historical SOURCE_STATED and the five intervals n15 43..45, n20 58..59, n21 61..63, n28 82..83, n30 88..90 are not proof of present-day openness. No exact new primary update authenticated in bounded S018 search. Inherited 14/17,+5,43/699/5553 remain quarantined. Phase1 stays IN_PROGRESS because later quartic/Prop10.1 and other source inputs are unclosed; Phases2/3 NOT_STARTED, CAM-0001 PROPOSED / NOT RUNNING with activation BLOCKED by published n6=16.
