# S089 — Sixfold axial q-fibres: true mod-10 pure-fibre exclusion and six-outsider origin no-go

16 October 2026. **INTERNAL SAME_EXECUTOR hand proof, source-conditional.** Entry genuine `main` commit `50f289728d02c62c00fef70ba231b0ad245772ae`, ORIGINAL Git root tree `8c3866a0262f212a39091e8c958a0d1c68202cfc`. S088 authored `32f4e314d7e6f560967a8a6c84474f37cdf4559d` has one parent `0b4825905541b212ecb3e8f4e21000f1ed25f863`; S088 ordinary merge `50f289728d02c62c00fef70ba231b0ad245772ae` has parents `0b4825905541b212ecb3e8f4e21000f1ed25f863` and that authored commit. No numerical mathematical search, orbits, CAS/SAT/ILP, Lean/Palomar, new campaign, independent certification, source promotion or publication.

## 1. Original positions, extension and genuine proper subsets

Retain the **59 distinct ORIGINAL positions** from S060/S081: 22 indexed full pairs whose pair-sum halves in H=(Z/10)^3 give U*=e1^8 e2^8 e3^6; eight actual g positions, s_q, and the SAME six original X_i,Y_i positions grouped into three disjoint V_i=X_i+Y_i. These make twelve disjoint, genuine q-supervertices z_j in G=(Z/20)^3, parity q=(0,0,1). A V_i selection always selects BOTH its original X_i and Y_i, not an invented vertex. Their half-reduced projected values y_j in F5^3 total (2,2,4). The exact axial extension and shadow are
```
E(U*)  = {h in H: h1=1 or h2=1 or h3 in {1,2,3}},
E5     = {x in F5^3: x1=1 or x2=1 or x3 in {1,2,3}},
C      = {(x,y) in F5^2: x=1 or y=1}.
```
For any NONEMPTY PROPER EVEN q-supervertex set I whose sum of y_j is outside E5, the actual even G sum has unique H half h(I), and k_l=(-h_l mod10) is in [0,8], [0,8], [0,6]. Select the first k_l individually labelled real U* pairs of type e_l (BOTH their original endpoints) and ALL actual originals represented by I. Their G sum equals 2(h(I)+sum k_l e_l)=0. At least one q group is selected and at least one omitted, so the 59-index support is strictly nonempty and proper. This constructive witness converts every *failed available projection gate* below into a literal original-index contradiction. Passing projection gates is only necessary and is NOT a survivor.

## 2. CLM-0311 — corrected sixfold normalisation, exact proper cross rules and complement

Suppose exactly six labelled q groups share projected y=(a,b,t)=(v,t) and six different labelled outsider groups have projections (e_i v+w_i,t e_i). If t=0, three even pure repeat sizes 2,4,6 project to third0, requiring each of 2v,4v,6v=v to lie in C. This would require three distinct coordinate values 3,4,1 in the two coordinates of v: impossible. Hence t!=0. Put beta=4/t. By the *actual twelve-group total*,
```
sum_{i=1}^6 e_i = beta-1,          W:=sum_{i=1}^6 w_i=(2,2)-beta v.
```
This W is NOT the sevenfold W. For any outsider J with 1<=|J|<=5 write e_J,w_J as its sums. The available repeated counts r in {0,2,4,6} for EVEN J (residues 0,2,4,1) and {1,3,5} for ODD J (residues 1,3,0) give the following *necessary* implications:
```
even J: e_J != 2                 => w_J in C
        e_J != beta-3            => w_J+beta*v in C
odd J:  e_J notin {1,3}          => w_J in C
        e_J notin {beta-2,beta-4}=> w_J+beta*v in C.
```
For each implication, respectively r=-e_J or r=beta-e_J mod5 is one of the available distinct original repeat counts and the q selection has at most 11 of twelve groups (odd J up to5 uses r<=5; even J up to4 uses r<=6). Never select all twelve. For J all six, a fourth-layer cancellation would require r=6 and is the EXEMPT full-twelve set; no such gate is imposed. At beta=3, its third-zero cancellation would demand unavailable even r=3, so neither all-six gate may be asserted for the surviving t=3 case.

**Exact complement duality.** For K=[6]\\J, e_K=(beta-1)-e_J and w_K=W-w_J. Because W=(2,2)-beta*v, reflection w -> W-w interchanges the two crosses C and C-beta*v. Precisely, w_J in C iff w_K+beta*v in C, and w_J+beta*v in C iff w_K in C. The even missing e values 2 and beta-3, and odd missing sets {1,3} and {beta-2,beta-4}, likewise interchange under e->beta-1-e. Hence each proper gate on a nonempty J is *equivalent as a clause* to the opposite-layer gate on its nonempty proper complement. It suffices to check both layers for six singleton supports, fifteen pairs, and ten representatives of the twenty triple/complement-triple pairs (31 representatives). This is **62 paired clauses**, not a claim that 31 projected sums are sufficient for the original H/Fano problem. All J with sizes 1..5 are physically available; J=all six is separately exempt as above.

## 3. CLM-0312 — six repeated genuine q groups force t=3: true H modulo10

Fix six REAL q groups with common projection y=(v,t). Because every group has q parity, its actual G coordinates are z0+10 alpha_j with alpha_j in F2^3, with z0 in (Z/10)^3 uniquely determined by y and parity. For any even r-member repeated support, its genuine H half equals (r/2) z0+5 XOR(alpha_j in selected r) mod10. All sizes 2,4,6 are nonempty PROPER q supports (six other genuine groups are omitted).

* **t=0:** excluded in section2 by the three pure projected residues.
* **t=1:** the third projection of any FOUR repeats is 4, so its H value must be rescued by a horizontal coordinate with 4a=1 or 4b=1 (i.e. that coordinate of v equals4). For such a coordinate z0_l=8, and the genuine H four-sum is 6+5 XOR(alpha_{j,l}) mod10; it equals 1 exactly when the four selected torsion bits XOR to1. However, among ANY SIX binary colours in F2^d, d<=2, there exist four distinct labels whose colour XOR is zero. Indeed: four of a colour work, or two pairs of duplicate colours work; if neither exists, six positions across at most four colours force multiplicities (3,1,1,1), and one of each of the four F2^2 colours XORs to0 (the lower-dimensional cases are covered by repetitions). Those four real labels have third outside {1,2,3} and every possible horizontal rescue equals6, not1. Their genuine H sum lies outside E, giving the original proper G zero from section1. So t=1 is impossible.
* **t=2:** every PAIR has projected third 4, and can be rescued only at a horizontal coordinate with 2a=1 or 2b=1, i.e. y_l=3. Then z0_l=6, and H pair coordinate 6+5 XOR(alpha_{i,l},alpha_{j,l}) is 1 only if the two bits differ. Thus all six separately labelled repeated groups would need pairwise distinct binary colours on <=2 eligible coordinates. There are only four possible colours. Contradiction. This includes **v=0,t=2**, previously left open by the outsider-only sieve.
* **t=4:** the proper six-repeat support has third projection4, so at least one horizontal coordinate must have y_l=1 (otherwise it itself violates E5). If neither horizontal coordinate is4, then each genuine FOUR-repeat support has third H equal 6+5 XOR(third four torsion bits) and neither horizontal projection can equal1 (a rescue for r=4 would require y_l=4). Every four-subset would therefore require third-bit XOR1. This is impossible: comparing four-subsets with a common three indices forces all six bits equal, whence each four-XOR is0. Hence some horizontal coordinate must equal4 too, forcing v=(1,4) or (4,1). In either case every repeat PAIR has horizontal projected coordinates (2,3), neither1, so its third H must equal3. Since t4 gives z0_3=3, all pairs force equal third torsion bits. Every four of six then has third XOR0 and H third6; rescue is possible only through the unique horizontal coordinate with y_l=4. At that coordinate z0_l=8, the H four-sum is 6+5 XOR(horizontal bits), requiring XOR1 for **every** four-subset. The same six-bit exchange contradiction finishes t=4.
* **t=3:** these pure-fibre arguments do not rule out arbitrary v. For this t, z0_3=1, and r=2,4,6 repeated H third equals respectively 1,2,3 plus 5 times the XOR of the chosen third torsion bits. The potential horizontal rescues for r=2,4,6 demand y_l=3,4,1 respectively. If v is NOT (3,4) or (4,3), at least one of r=2 or r=4 lacks any horizontal rescue; then every such r-subset must have third torsion XOR0. Exchanging one of six original labels while retaining r-1 common labels (possible for r=2 or4) proves all six third torsion bits equal. Thus all six genuine repeated q-group G third values are uniformly 1 or uniformly 11 mod20. For v=(3,4) or (4,3), this argument alone only forces XOR of ALL SIX third bits zero from the size-six support (because neither coordinate is1). These two exceptional cases are still OPEN; no uniformity is claimed.

**Conclusion:** the only possible SIXFOLD projected q half-value has third coordinate t=3. The proof uses actual H modulo10 and *real repeated original q groups*, not a mod5-only or synthetic lift. It does not exclude sixfold t3 for any nonzero v.

## 4. CLM-0313 — exact six-point cross-pair geometry at W=(2,2)

**Finite-field lemma (hand proof).** Let w1,...,w6 in F5², with sum W=(2,2), and every PAIR w_i+w_j in C={x=1 or y=1}. Then, up to exchanging horizontal coordinates and relabelling, the exact multiset is
```
(3,4), (3,4), (3,4), (3,4), (3,4), (2,2).
```
The only other orientation is five (4,3) and one (2,2).

**Proof.** Colour each edge ij of K6 RED when x_i+x_j=1; otherwise BLUE, in which case necessarily y_i+y_j=1. Every two-colouring of the edges of K6 contains a monochromatic triangle: take any vertex and three incident edges of the same colour; among their three other endpoints, an edge of that colour makes a triangle, and otherwise those endpoints themselves make a triangle in the other colour. A red triangle forces its three first coordinates to be 3, since x_i+x_j=x_i+x_k=x_j+x_k=1 and 2*3=1 in F5. Blue is symmetric. After horizontal swap, at least three labels have x=3.

Let k of the other labels have x!=3. k>=1, because six x=3 would total 18=3 rather than W_1=2. Any label j with x_j!=3 must have y_j+y_i=1 for EVERY x_i=3 label i. Thus all 6-k labels with x=3 have one common second coordinate h and all k labels with x!=3 have second coordinate 1-h. If h=3 then every y=3, total y=18=3, impossible. For h!=3, two x!=3 labels have second sum 2(1-h)!=1, so their first coordinates must sum1. Three such labels would all have first coordinate3, contradicting their definition; hence k<=2. If k=2, their first-coordinate sum must be W_1-4*3=2-12=0, contradicting their necessary pair first sum1. Thus k=1. Five labels have x=3, the sixth has x=2 from W_1=2. Their second total is 5h+(1-h)=1-h=2, hence h=4 and the last y=2. The asserted pattern follows. No numerical enumeration or solver was used.

## 5. CLM-0314 — SIXFOLD horizontal origin is impossible, including the exceptional odd layer

Assume the surviving t=3, v=(0,0). Now beta=3, e_all=2 and W=(2,2). For any genuine outsider pair J, the even-layer omitted e values are 2 and beta-3=0, which are distinct. At least one 0/fourth gate is available, and because v=0 the two horizontal crosses coincide. Thus **every one of the 15 real outsider pairs satisfies w_i+w_j in C**. CLM-0313 says that, after swapping axes and labels, FIVE distinct actual outsider groups have residual u=(3,4) and the sixth has residual (2,2).

For any genuine triple J chosen from those five u labels, w_J=3u=(4,2) is outside C. At beta=3 the ODD J zero-layer exceptions are e_J in {1,3}, and the fourth-layer exceptions are e_J in {1,4}; to evade BOTH genuine proper third0/fourth4 tests, e_J MUST equal 1. Since every triple among five satisfies e_i+e_j+e_k=1, comparing two triples with two common labels forces all five e_i equal. Their common value solves 3e=1, namely e=2 in F5. But the genuine outsider support consisting of ALL FIVE u labels has residual 5u=0 outside C and e_J=5*2=0, **not** the sole exceptional value1. Hence one of its proper third0/fourth4 gates is available, fails, and yields a literal nonempty PROPER 59-original G zero via section1. The five-outsider support uses r in {1,3,5}, so at most ten of twelve q groups are selected; this is emphatically NOT the sevenfold full12 exception. Swapping axes handles u=(4,3).

Together with CLM-0312 this excludes **every sixfold projected value with (a,b)=(0,0)**, including t=2/3 left open in S086. In particular any surviving sixfold projected half-value must be (a,b,3) with (a,b)!=(0,0). No sixfold with nonzero v is eliminated here, and no full twelve-q obstruction is established.

## 6. CLM-0315 — true third torsion boundary and exact next target

For t=3 and v not in {(3,4),(4,3)}, all six repeated REAL q groups have identical actual G third coordinate either1 or11, by section3. For the two exceptional v, only their sixfold total third-bit XOR0 follows from pure fibres, not pairwise agreement. These are actual G-coordinate restrictions but **do not** claim that sixfold t3 with nonzero v survives all proper outsider gates.

The remaining mathematically live sixfold target is precisely t=3, v!=(0,0), plus the outsider residual e_total=2 and W=(2,2)-3v, exact 31 complement representatives, true H torsion, and all proper q supports. If any projected necessary pattern survives, it MUST separately be tested against four SAME-six-ORIGINAL Fano transversal H values and C/Delta, 2048 original outsider masks, q split I/alpha with real E(U*\\I), all signed non-q pair splits, all 26 hubs, FULL8/exact12/13/14/>=15 mixed carries, arbitrary U22, alternative P26. Neither this session nor earlier work constructs a fully-gated original T59, a length58 zero-sumfree G20 sequence, proves D(C20³)=58, or resolves general rank-three Davenport equality. Source29/frontier30 unchanged, Phase1 IN_PROGRESS, CAM-0001 BLOCKED, hosted CI ABSENT_NOT_PASS and review INTERNAL SAME_EXECUTOR.
