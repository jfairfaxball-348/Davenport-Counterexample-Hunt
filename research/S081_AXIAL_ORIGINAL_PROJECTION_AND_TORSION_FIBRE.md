# S081 — axial U22: exact mod-5 shadow, original rank-one elimination, and the first rank-two lift collision

15 October 2026. Authorised S081 alone by the owner message "Run next session". Entry GitHub main c456d91f39bf4bfb74a71e16ab78d29f682ac2ca and its actual Git root tree 7e34573938310422a709b4d03c413345f2ccd294; prior S080 authored a98bd42fdd9a382e0003991753aecbf74f3127ef has one parent a24b40bf03910ca80dc783238414a3dc9793bd38; S080 ordinary merge c456d91... has exactly two parents a24b40... and a98bd42.... Entry open PR zero, workflow runs zero, combined status contexts zero ABSENT_NOT_PASS, rulesets zero, branch protection 403 UNKNOWN. These are GitHub observations, not mathematical validation.

All mathematics below is symbolic, INTERNAL SAME_EXECUTOR, under the SOURCE-CONDITIONAL canonical actual 59-original-index profile. No numerical mathematical search, solver/orbits, CAS/SAT/ILP, Lean/Palomar, source promotion, campaign, independent mathematical certification, outreach, or publication. Rank-three Davenport equality and n=20 remain OPEN.

## 1. Exact original parity and axial extension conventions

G=(Z/20)^3, H=(Z/10)^3 with iota(h)=2h. Fix actual original q=(0,0,1) nonzero parity, 22 original indexed pairs (a_i,b_i) with a_i+b_i=iota(u_i) and same nonzero quotient parity, eight individually labelled g_1,...,g_8 of parity q, and genuine six other singleton positions X_1,Y_1,X_2,Y_2,X_3,Y_3 plus s_q. Their three disjoint genuine *groups* V_i=X_i+Y_i have parity q. There are twelve real, mutually disjoint q-supervertices: eight g, s_q, V_1,V_2,V_3. Each even-cardinality subcollection of them is an actual q-only original support. We never identify G with a direct sum Q+H.

Fix U*=e1^8 e2^8 e3^6 as the H values of the 22 full pair sums. The exact ordinary indexed H subset-sum set is the box
    Sigma(U*)=[0,8] x [0,8] x [0,6] modulo 10,
and the exact extension set is
    E=H\(-Sigma(U*))={h:h1=1 OR h2=1 OR h3 in {1,2,3}}.
The sum U*=(8,8,6); the total H sum of all twelve q-supervertices is c=(-sum U*)=(2,2,4). The original G sum is iota(c)=(4,4,8).

For an EVEN subcollection I of the 12 supervertices let h(I)=iota^-1(sum_{j in I} z_j) in H. A proper nonempty original q-only zero exists precisely when some proper nonempty even I has h(I) NOT in E: choose real indices B with sum_{i in B}u_i=-h(I), then take all ORIGINAL endpoints of B and every ORIGINAL member of the q-supervertex groups indexed by I. This is an actual disjoint original index selection, no fictitious pair rearrangement. The all-12 case gives c in -Sigma(U*) and must EXPLICITLY be exempted because it combines with all pairs to form the full 59-original total zero.

The matching formulation is equivalent at this m=0 level: every proper nonempty even I can be paired internally and its complement can be paired; conversely a proper subset of the six edges of any perfect matching is even. This does NOT automatically pass the 2048 outsider partial-singleton/Fano or q-pair-split E(U\I) gates.

## 2. CLM-0282: exact mod-5 shadow and why every proper *linear quotient* loses it

Write pi5:H->P=C5^3 for coordinate reduction modulo5. The exact projection of the real axial E is
    pi5(E)=E5={x in P:x1=1 OR x2=1 OR x3 in {1,2,3}}.
Indeed membership in E projects into the displayed union, and a projected point satisfying one displayed disjunct has a lift with that EXACT H coordinate 1,1 or 1/2/3 respectively. Hence zero is NOT in E5; equivalently E has NO point of 5H={0,5}^3. Moreover for EVERY nonzero F5-subspace K of P, the quotient image of E5 in P/K is ALL P/K. Given x+K and any nonzero v in K, choose an index j with v_j nonzero; over F5 choose t so (x+tv)_j=1. Then x+tv lies in the actual E5. This proves every rank-one or rank-two (indeed every proper nontrivial) mod5 linear quotient is saturated. A zero-avoiding *proper quotient* sieve cannot eliminate U*. This is a rigorous limitation of linear quotient projections, not full rank-three compatibility.

IMPORTANT positive complementary fact: if an even original q-supervertex subcollection I has pi5(h(I))=0, then h(I)=5d for some d in {0,1}^3. Because U* contains AT LEAST five copies of EACH coordinate basis e1,e2,e3, choose exactly five distinct indexed full U-pairs of type e_j for each d_j=1. The chosen full original pair sums equal iota(5d)=-iota(5d) in G, so they cancel the actual selected supervertices. The original subset is proper when 0<|I|<12. Thus a full original q-only gate forces EVERY proper nonempty even subcollection to have NONZERO mod5 total. The quotient-saturation statement and this *full three-coordinate zero test* must not be confused.

## 3. CLM-0283: rank-one is excluded by a literal ten-index argument

For each q-supervertex z_j define y_j=(1/2) pi5(z_j) in P; the inverse 1/2 is multiplication by 3 in C5. For even I, sum_{j in I}y_j=pi5(h(I)). Also all twelve z_j have the SAME nonzero quotient parity q, so |I| being even is the genuine condition for their sum to be even in G.

**Theorem.** In a fully original q-only-compatible axial U* configuration, the twelve y_j cannot all lie in a common one-dimensional F5 *linear* subspace L (nor in {0}). Suppose they do. Identify L additively with C5. Form ten indexed elements (1,y_j) in C2 x L, which is cyclic of order10. The ten successive prefix sums, together with zero, either include a zero nonempty prefix or repeat, by pigeonhole in a ten-element group. Their difference is a NONEMPTY consecutive original-group index set I of size at most10 with even size and P sum zero. By §2, the literal original support of these q-supervertices plus five actual full basis-U pairs in each required order-two coordinate has sum0 in G, and I leaves at least two of the twelve q-supervertices unselected, so it is PROPER. Contradiction.

This is a self-contained C10 pigeonhole argument, NOT use of an unauthenticated D3(C5^3) numerical input. The exact remaining projected rank-two case is NOT killed by this argument: D(C10 x C5) length14 is above twelve, and the following genuine rank-two *projected shadow* exists.

## 4. Rank-two projected shadow, actual 59-index realisation, and first literal failure

Choose in P
    a=(1,3,1), b=(1,0,0), c=(2,2,4)=4a+3b.
The vectors a,b are independent. Take N= nine separately labelled projected q-supervertex values a and three b. ANY nonempty even index subcollection with P sum zero would use r of the nine a and s of the three b with r=0 or5 modulo5, s=0, and even r+s. The sole possible nonzero choice r=5,s=0 has ODD cardinality. Thus N is *zero-free in the C2 x C5^2 projected parity shadow*, exactly twelve original groups, with full projected total 9a+3b=4a+3b=c. The rank-one result CANNOT be extrapolated to a rank-two projected zero.

We can even lift these *projection-only* data into the correct literal G and singleton/parity bookkeeping without any numerical search. Take
    A=(2,6,7), B=(2,0,5), B'=(2,10,15) in G.
All three have parity q; their half-reduced mod5 values are a,b,b respectively. Let all eight original g_j=A and the actual singleton s_q=A; let V1=B, V2=B, V3=B'. Let
    X1=(1,0,0), X2=(0,1,0), X3=(1,1,0);
    Y1=V1-X1, Y2=V2-X2, Y3=V3-X3.
The six X/Y parities are the distinct six nonzero classes other than q (r1,r1+q,r2,r2+q,r3,r3+q), literally on the SAME six original positions in every Fano transversal. For each of the eight e1, eight e2 and six e3 original U pairs, take actual a_i=e1 and b_i=2e_j-e1 where that pair's H value is e_j. Both original pair members then have the same nonzero quotient parity e1, which is NOT q; their true G sum is iota(e_j). This specifies all 44+8+7=59 original index values; repetitions of VALUES do not merge original indices.

Check the TRUE G total:
    9A+2B+B'=(4,4,8) mod20;
    sum_i(a_i+b_i)=2(8,8,6)=(16,16,12) mod20;
    total=(0,0,0) mod20.
All 12 q-supervertices pass the NECESSARY *proper even projected-zero* avoidance, because of the r,s argument. The four actual singleton Fano tuples share real X/Y and must NOT be treated as arbitrary independent H values.

**Crucial failure: this is NOT an original q-gated survivor.** Already the literal original indices g1 and g2 contribute 2A=(4,12,14). Choose all eight complete original e1 pairs, four complete original e2 pairs, and three complete original e3 pairs. These 15 disjoint full pairs contribute (16,8,6) in G, giving actual G sum (20,20,20)=0. Exactly 32 out of 59 ORIGINAL indices are selected (two g indices and 30 pair endpoints), so this is nonempty and PROPER. Equivalently h({g1,g2})=(2,6,7) is outside E, despite projected h=(2,1,2) lying in E5. Thus the full H-fibre, not merely mod5 zero, is a strict indispensable gate.

## 5. CLM-0284: a four-colour original torsion-fibre packing cut

The preceding r=9/s=3 shadow fails for **EVERY possible 10-torsion lift of those nine a-group ORIGINAL values**, not just for the displayed choice A. Fix q=(0,0,1), and take a projected q-supervertex y=a=(1,3,1). Both the original parity q and pi5(z)=2a prescribe the reduction z mod10 exactly as A=(2,6,7). Consequently EACH such actual original group has value z=A+10t in G for one t=(t1,t2,t3) in F2^3. For two distinct such labelled groups z,z', their even-G sum has actual H preimage
    h=iota^-1(z+z')=(2,6,7)+5(t+t') mod10.
The first coordinate is 2 or7, NEITHER is1. The second coordinate equals1 iff t2 != t2'. The third coordinate equals2 iff t3 != t3'; otherwise it is7. Hence
    h in E  IFF  (t2,t3) != (t2',t3').
In a fully actual q-only gate, AT MOST FOUR separate q-supervertex groups can have the half-reduced mod5 value a, because the four (t2,t3) labels must be pairwise distinct. With FIVE such original q groups, two share (t2,t3). Their true h is either (2,6,7) or (7,6,7), both outside E; the literal original zero uses those two genuine q-supervertices plus 8 e1 pairs if h1=2, or 3 e1 pairs if h1=7, plus FOUR e2 pairs and THREE e3 pairs. All choices lie within the actual eight/eight/six inventory, and omission of the other ten q-supervertices makes them proper. This is a FORCED original G-zero, without assuming the two q groups are themselves equal as G values; the discarded torsion t1 is handled exactly.

Thus the explicit rank-two 9a+3b shadow cannot be lifted to even the un-split q-only original gate, independently of how those nine positions are distributed among g,s_q,V_i, or how the order-two 10-torsion lifts are chosen. It is an explicit, original-index obstruction for one large fibre, NOT a theorem that arbitrary rank-two projected data or all broad-spectrum U22 are impossible.

## 6. CLM-0285: no matching has four equal axial H-block values

For ANY h in H, it is impossible that both 2h and 4h belong to E. Indeed their first two coordinates are even and so cannot equal1. If (2h)_3 belongs to {1,2,3}, its evenness forces (2h)_3=2, and then (4h)_3=4, outside {1,2,3}; otherwise 2h is itself outside E. Therefore in an actual perfect matching of the twelve q-supervertices into six even H blocks, FOUR blocks cannot have the same H value h. If they did, the union of either two or four of those DISJOINT ORIGINAL matched groups would have H sum outside E, immediately supplying a literal original zero after adding indexed full U pair complements as in §1. This is all-matching original-index necessity (not a proof of existence of such repetition). Three equal h=e3 pass the individual 1,2,3 multiples of E, showing why the local "four" threshold cannot simply be replaced by three without other constraints.

## 7. Aggressive obstruction audit and exact remaining bridge

What is established: full three-coordinate mod5-zero is forbidden on every proper even q-supervertex subset; projected rank≤1 cannot occur; every proper quotient P/K is nevertheless saturated by E5 (so projected rank-two scalar images cannot detect the full forbidden box); one explicit rank-two zero-free projected model has a complete 59-index total-zero original lift, but a G q-only zero at g1,g2+fifteen original full pairs; *every* lift of its nine-a fibre violates a four-colour t2/t3 packing bound; any genuine matching has no four equal H completion blocks. These results are exact necessary conditions, not proofs of the full S060 test.

What remains open: existence or impossibility of a completely S060-gated original T59 for axial U* or arbitrary broad-spectrum U22. There is NO general bound on all 125 possible half-projected q-fibres, no universal rank-two elimination, no treatment of all 2048 outsider transversal cases including the four TRUE same-six-original-position Fano x, no genuine E(U\I) with q pair splits, no actual non-q signed w_i and four coupled tau_epsilon occupied K-fibres, no FULL8/exact12 chi0 or chi!=0/13/14/≥15 danger exclusion, no all-26 hub, three-hub or (0,4),(0,6),(1,7) P26 resolution. The candidate partial model is intentionally a FAILED q-only example, never G58 or a zero-free T59.

The immediate mathematical bridge is to classify actual 12 q-supervertex mod5 rank-two/three spectra and their 2/4/6/8/10 original-subset H lifts under the rectangular E slabs; any attempted survivors must then face true coupled original Fano and 2048 outsiders and signed non-q K occupancy. No source-dependent D3 claim was used. The 29 existing source objects and 30 existing frontier rows must remain unchanged; Phase1 IN_PROGRESS, CAM-0001 BLOCKED, hosted CI ABSENT_NOT_PASS.
