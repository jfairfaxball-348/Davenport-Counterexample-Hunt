# S045 — simultaneous all-index Fano pencil exchange (CLM-0172)

13 October 2026. Phase1 symbolic proof, **conditional** on the SOURCE_STATED historical D(C10³)=28 input used by S041 to force the six-odd-class quotient profile of a hypothetical C20³ zero-sumfree S58. Not a candidate, composite equality or independent source authentication.

## Indexed setup and the new exact compatibility requirement

Fix the 58 **distinct indexed** original positions of hypothetical zero-sumfree S in G=C20³. Its mod2 classes (Q=F2³) are nonzero, exactly six nonzero classes have odd multiplicity, and the seventh class w has even multiplicity (S041 CLM-0151, conditional on historical D(C10³)=28). Append ONE new z=-sum_G S with parity w. The 59-term T=S*z is minimal zero-sum in G, with all seven nonzero classes occurring oddly.

Choose one ORIGINAL index in each of the six odd classes and choose z for the seventh; denote the seven singleton G terms s_v, v in Q\{0}. Pair every other original index within its **original G mod2 class**. This yields 26 disjoint indexed equal-parity pairs P_j. Identify H=2G≅C10³ using the **non-split** injection iota(h)=2h (mod20). Each original pair sum is in 2G and has unique H decoration p_j. P=(p_1,...,p_26) is zero-sumfree in H because a nonempty zero-sum subcollection would give an original G zero in S. Set c=iota^{-1}(sum_v s_v) in H; the seven singleton parity vectors sum0, so this is defined. Minimality T gives c=-sum_j p_j.

For EVERY one of the seven Fano lines L in Q\{0}, the indexed triple of singleton positions L and complementary indexed quadruple L^c both have parity sum0. Write a_L=iota^{-1}(sum_{v in L}s_v), b_L=iota^{-1}(sum_{v in L^c}s_v). Their exact C10 values satisfy a_L+b_L=c. The 28 decorated H blocks P,a_L,b_L are a **minimal zero-sum sequence** (because their disjoint original unions partition minimal T). In particular P*a_L and P*b_L are zero-sumfree; **all seven lines, not just one K4 star/cut tuple, are simultaneously realised on the same 59 indices.**

**Hostile qualification: the seven partners alone are not an extra inverse theorem.** For ANY zero-sumfree sequence P and c=-sum P, its one-point extension set E(P) obeys E(P)=c-E(P). Proof: P*x contains a zero subset iff some U⊆P (possibly empty) has sum U=-x. Under y=c-x, the complementary indexed P\U has sum -y, giving a zero subset of P*y; the converse is symmetric. P itself has no nonempty zero subset, so no missing case. Consequently a_L∈E(P) already forces b_L=c-a_L∈E(P); the Fano two-block pairings are geometrically simultaneous but do not double the independent E(P) constraints.

## Full 25-pair / three-line pencil, for EVERY eligible hub pair

Fix ANY one of the 26 indexed G pairs (x_h,y_h) with common nonzero original quotient class h∈Q. Remove just this pair from P, obtaining a 25-term zero-sumfree H sequence P' and removed decoration p_h=iota^{-1}(x_h+y_h). The three Fano lines through h pair the OTHER six singleton parity values into three prescribed disjoint two-sets {u_i,v_i}, i=1,2,3, with u_i+v_i=h.

There are exactly THREE distinct hub-index positions with parity h: the reserved singleton s_h and the two ORIGINAL positions x_h,y_h of the broken pair. For EACH of their 3!=6 bijections σ onto the three lines, let X_i^σ denote its assigned hub G term and define
  τ_i^σ = iota^{-1}(X_i^σ+s_{u_i}+s_{v_i}) ∈H.
These are exact C20 sums inside 2G; **no coordinatewise split C20≅C2⊕C10 is used.** The three triples are pairwise index-disjoint, contain nine original-plus-new positions, and each has Q-sum0. Together with the remaining 25 pairs they partition ALL 59 original-plus-one indices into28 Q-minimal zero blocks. Therefore, for every one of the 26 hub-pair choices and every one of the six assignments,

  (P', τ_1^σ, τ_2^σ, τ_3^σ) is a 28-term H minimal zero-sum sequence.

Equivalently EVERY proper nonempty selection of these 28 indexed H terms is nonzero. In particular P' plus any one OR any two of the three τ values is zero-sumfree: **the triple is a joint critical extension**, not three unrelated elements of E(P'). Directly from indexed C20 additions,
  τ_1^σ+τ_2^σ+τ_3^σ = p_h+c = -sum P'
for all σ and every fixed hub pair. In the H quotient mod2, all those relations retain carries through iota and cannot be rewritten as arbitrary split lifts.

For two permutations differing by swapping the assignments of x_h and y_h between lines i,j, define δ=iota^{-1}(x_h-y_h)∈H, possible because x_h,y_h share parity in original G. Their decorations change by (τ_i,τ_j)↦(τ_i-δ,τ_j+δ) for one consistent swap direction; the third τ is fixed. Both the original and switched **joint two-extension** conditions must hold for their common P'. This is the exact simultaneous hub-transposition inverse condition. P's H mod2 profile may be (z,r)=(0,4),(0,6),(1,7) as in S043: the original G parity h of a PAIR is not the H parity of its SUM p_h. None of those three surviving profiles is excluded by this argument.

## Global multiplicity and hostile bounds

P has 26 indexed pairs distributed over seven original quotient classes, hence at least FOUR distinct hub-pair choices have the same quotient class h (pigeonhole). All 26 choices, including these four, must each satisfy six labelled critical-extension tests; local one-tuple K4 feasibility (S043 CLM-0165) is not enough. Conversely no contradiction follows merely from 'six assignments': the original pair can have x_h=y_h as G VALUES at two distinct indices, making δ=0 and permutation changes trivial. This is a hostile **local twist countermodel**, NOT a full zero-sumfree S58. Nor can two pairs simply be broken while retaining 28 quotient blocks: 24 retained pairs would leave 11 positions for four nonzero-class Q-zero blocks, each of size≥3, impossible since 4*3>11. S041 P10 inverse and all three P26 profiles remain OPEN.

**Indispensable new inverse lemma:** show that NO zero-sumfree P26 with one of the three S043 profiles, arising from 26 genuine C20 index-pairs, supports all seven a_L/b_L relationships AND all 26 six-permutation maximal-minimal P' critical triples; alternatively exhibit an actual full-length indexed G lift and certify it under the repository's separate rules. The present proof establishes NECESSARY conditions only. Historical D(C10³)=28 remains SOURCE_STATED.
