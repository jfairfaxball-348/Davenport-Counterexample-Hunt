# S028 — Six-class aggregate incidence countermodel and exact indexed-lift gap

Date: 2026-10-12. ONE owner-invoked Phase-1 ORIGINAL-PRIMARY-SOURCE symbolic mathematics/provenance session. Entry LIVE main `64e7cdee9b6acf97aafec51536042d67607a67a6`, tree `086538c6044e024d4ef9ad771ef7949e590d9b74`; S027 one atomic commit `269486e7f8bce58f028a55d1b064f93217f1ecb9`, sole parent `362bb53e39131a134c072cdf69c2a0358b66c1aa`, same tree, genuine PR27 non-force two-parent merge to entry main. No mathematical computer search, CAS, orbit/candidate enumeration, SAT, historical author code, Lean, Palomar, campaigns, manuscripts or outreach.

## Premises and preregistered bounded gate

Let p be an odd prime p>=7 and put a=3(p-1)/2, b=(3p-1)/2, so |Z|=3p=2b+1. Prior CLM-0120/0122/0123 use the original BSP2012 Chevalley–Warning argument plus CLASSICAL SOURCE_STATED Olson D(C_p^3)=3p-2. In a hypothetical no-nonempty-zero-sum-of-length-<=a sequence S of length 6p-3, any 3p-term zero-sum Z has only b/b+1 proper zero sums. If precisely four indexed b-blocks B1..B4 exist, S027 proves there are at least six occupied 4-bit signatures. We attempted FIRST to close this six-cell obstruction, allowing only hand algebra and indexed logical deductions. STOP at the first essential missing individual-position lift. Separate Route B D2(C_p^3)<=6p-6 remained optional, and was only arithmetically checked. All claims here concern an ABSTRACT PARTITION WITH AGGREGATE CELL SUMS, not a certified indexed zero-sumfree sequence.

## CLM-0124 (PROGRAMME_PROVED, abstract aggregate consistency and sharpness of S027 six-cell gate)

**Exact theorem.** For every odd prime p>=7, there is a six-vertex 4-cube incidence support with positive integer cell cardinalities totaling 3p and assigned nonzero aggregate cell sums in F_p^3, such that:

1. exactly FOUR distinct unions of whole cells have cardinality b and sum zero; their complements are the exactly four proper whole-cell zero-sum unions of cardinality b+1;
2. no other nonempty proper union of WHOLE cells has sum zero, in particular none has size <=a;
3. every pair of occupied 4-bit signatures agrees in some block bit (the S026 pair-cover), and for each omitted coordinate the other three have a witness pair differing in all three (the S026 triple-separation / S027 distance-three edge requirement);
4. precisely six occupied signatures occur, so S027's >=6 bound is sharp **for this aggregate incidence relaxation**.

This theorem DOES NOT assert that 3p individual indexed vectors can be chosen with these cell sums so that all nonempty *partial-cell* zero-sum subsequences are excluded. It does NOT construct S or a counterexample to strong short extraction, prove D2 or any classical rank-three D1 value.

**Proof, symbolic parameters (no search).** Choose nonzero u in F_p^3. Choose ell=1 if b is even, ell=2 if b is odd; since b>=10, the positive integer d=(b+1-3ell)/2 exists (d>=1). Introduce six NONEMPTY formal indexed cells A,B,C,D,E,F with cardinalities

| Cell | A | B | C | D | E | F |
|---|---:|---:|---:|---:|---:|---:|
| Size | d+ell-1 | d+2ell | d+ell | d | ell | ell |
| Aggregate sum /u | +1 | -1 | +1 | +3 | -2 | -2 |
| (B1,B2,B3,B4) signature | 1111 | 1000 | 0110 | 0001 | 0101 | 0011 |

Every size is positive, and sum of sizes is 4d+6ell-1=2(2d+3ell-1)+1=2b+1=3p. All coefficients are nonzero mod p. The total aggregate sum is (1-1+1+3-2-2)u=0. Put
B1=A union B,
B2=A union C union E,
B3=A union C union F,
B4=A union D union E union F.
Their sums are 0 respectively by 1-1, 1+1-2, 1+1-2 and 1+3-2-2. Their sizes are respectively 2d+3ell-1, (d+ell-1)+(d+ell)+ell (twice), and (d+ell-1)+d+2ell; each equals b. These four are DISTINCT unions of formal positions, independently of their group labels.

**ALL whole-cell zero-sum unions — exact symbolic check.** For cell choices alpha,beta,gamma,delta,epsilon,phi in {0,1}, their aggregate sum is
(alpha-beta+gamma+3delta-2epsilon-2phi)u.
The integer coefficient lies between -5 and +5; since p>=7, it is 0 in F_p iff it is 0 in Z. Write r=epsilon+phi in {0,1,2}.
If delta=0, the equation is alpha+gamma-beta=2r. For r=0 it gives only empty and the two pairs {A,B},{B,C}; for r=1 it forces alpha=gamma=1,beta=0, producing {A,C,E} or {A,C,F}; for r=2 it is impossible.
If delta=1, alpha+gamma-beta+3=2r. For r=0 it is impossible; for r=1 it forces alpha=gamma=0,beta=1, producing {B,D,E} or {B,D,F}; for r=2 it forces alpha+gamma-beta=1, producing {A,D,E,F},{C,D,E,F}, or the full six cells.
Thus the EXACT list is empty, full, and the four complementary pairs:
{A,B} <-> {C,D,E,F};
{A,C,E} <-> {B,D,F};
{A,C,F} <-> {B,D,E};
{A,D,E,F} <-> {B,C}.
The displayed left-hand unions have size exactly b; the right-hand complements size b+1. No other whole-cell zero-sum union exists. No enumeration or machine arithmetic was used; the three possible r values were exhausted symbolically.

**S026/S027 incidence constraints.** The six strings 1111,1000,0110,0001,0101,0011 have no bitwise complementary pair (their absent complements are 0000,0111,1001,1110,1010,1100). Thus every pair of INDEX POSITIONS (including two in the same cell) is co-contained or co-excluded by at least one B_j. For each j the signatures of these two cells agree in coordinate j and disagree in the other three: j=1: A,B; j=2: B,F; j=3: B,E; j=4: B,C. Hence every distinct triple of the four blocks has a separating witness pair; the four selected distance-three edges form a star at B, a forest on five vertices, with D the sixth vertex. All necessary S026 and S027 pair/triple/incidence conditions are met. This finishes the theorem.

## Adversarial gate and first essential STOP

The entire six-class construction is a **countermodel to sufficiency of aggregate whole-cell equations and block size / pair-cover / triple-cut axioms** for excluding six cells. It is not a sequence of vectors z_1,...,z_{3p}; specifying only each cell's cardinality and TOTAL group sum leaves individual values unconstrained. A shorter zero sum can use SOME but not all indices of one or more cells. Excluding every such partial-cell combination (or proving this impossible) is the first essential unclosed step. In particular, one must not "realise" a cell by identical group elements or arbitrary divisions without checking all mixed subsequences. We do not assert existence or nonexistence of such an indexed lift. We also did NOT examine 7/8 cells or five-plus balanced b-block families after this FIRST essential STOP; those remain possible mathematically. Thus strong p>=7 <=3(p-1)/2 extraction, BSP omitted rank-three Lemma2.3, D2<=6p-6, and the classical D(C_n^3)=3n-2 conjecture all remain unproved by S028.

**p=7 exact hand boundary:** b=10, ell=1, d=4; six sizes (4,6,5,4,1,1) sum21; each displayed B_j has exactly10 positions. No group element list, computation or search is asserted. The construction also covers all odd p>=7 because ell enforces integral d and 2d+3ell-1=b.

**Route B arithmetic only.** Safe recurrence from S024/S025 is D_{k+1}<=max(D_k+b,6p-4). With unproved D2<=6p-6 it would yield D_{2p-4}<=6p-6+(2p-6)b =3p^2-4p-3=M. p5 gives b7,k0=6,M52,target D2<=24 (externally SOURCE_STATED p5 D2=20 does not prove the prime-uniform target); p7 gives b10,k0=10,M116,target D2<=36. Proven generic D2<=6p-4 yields M+2. No new D2 inequality was proved and no printed omitted rank-three Lemma2.3 is used.

## Original sources / unchanged D1 frontier

The definitive publisher offprint Bhowmik–Schlage-Puchta 2012, SRC-0021, original printed p23 (PDF index2), was directly read again, verifying weak printed <=(3p-1)/2 lemma and an unprovided rank-three Lemma2.3 proof; printed subsequent split speaks of <=3(p-1)/2 without a valid stronger derivation in the read text. Historical Olson rank3 D1 input SRC-0003 remains SOURCE_STATED, not independently rebuilt original proof. Sheikh2017 official full Chapter4/Remark4.3.11 reattempt returned inaccessible fetch/internal error (earlier observed HTTP403); not authenticated. GHST C53 original author code/output endpoint again inaccessible, NOT RUN. Yiu2026 original v1 HTML readable but no independent terminal M1 triple-disjoint predicate/log/certificates authenticated; generator counts 98622/230983 differ from final M1 decision and M2/M3 are different. Focused exact-source checks n15/20/21/28/30 authenticated no new original exact theorem; failure to find is not evidence of present-day openness. All access enums unchanged.

Every original n1..30 JSON row object and corresponding Markdown table cell (group, D*, bound, status, ordered complete evidence) preserved, 30/30 mirrors checked with zero discrepancies; 25 settled/trivial historical/source rows and n15:43..45, n20:58..59, n21:61..63, n28:82..83, n30:88..90 unchanged. Schmid n6=16 / van Emde Boas 2p^a and 3*2^a historical exact families/Yiu claims SOURCE_STATED. Inherited14/17,+5,43/699/5553 quarantined. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED; CAM-0001 PROPOSED/NOT_RUNNING activation BLOCKED by n6=16. NO new exact D1 frontier value, mathematical computer search, solver, candidate sequence, Lean, Palomar, outreach, publication or hosted CI PASS.
