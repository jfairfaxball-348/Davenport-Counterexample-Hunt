# S043 — Exact indexed CRT replacement window and p5 core hostile checks
13 October 2026. CLM-0166. SOURCE_STATED hypotheses explicitly retained.

Let G=C_(5m)^3≅Q⊕H, Q=C5^3 and H=C_m^3, m∈{3,4,6}, k=D(H)=3m−2∈{7,10,16}. For m=6 the historical equality is SOURCE_STATED; the p5 multiwise upper D_j(Q)=5j+10 and η(Q)≤33 remain SOURCE_STATED with unauthenticated finite predicates. For an actual hypothetical zero-sumfree S of length5k+8, S041/042 conditionally supply k−1 disjoint Q-zero blocks B1,...,B_(k−1) and remainder L, Q-zero-sumfree, |L|≤12; their H block sums V=(v1,...,v_(k−1)) form maximal zero-sumfree H sequence of length k−1 and Σ(V)=H.

### Local one-block exchange gate
Fix i and put V_i=V with index i deleted (length k−2). Every nonempty ORIGINAL-INDEX subset W of B_i∪L satisfying sum_Q(W)=0 must have sum_H(W)∈E(V_i), where E(V_i)={h: V_i*h is H-zero-sumfree}. If not, an H-zero-sum subcollection of V_i plus the new h corresponds to a genuine zero sum of S, using W and whole B_j for j≠i, all index-disjoint.

For ANY h,h'∈E(V_i), allow two new distinct formal extension indices, even if h=h'. The k-element sequence V_i*h*h' must have a nonempty zero sum by D(H)=k. Because V_i*h and V_i*h' are both zero-sumfree, this zero sum contains BOTH new extension indices. Consequently
h+h'∈−Σ(V_i), where Σ contains EMPTY and nonempty indexed subset sums.
This two-point necessary relation is exact and source-independent once k=D(H) is accepted; it is NOT an inverse classification of E(V_i).

If TWO index-disjoint nonempty Q-zero subsets W,W' lie in B_i∪L, then with the k−2 unchanged blocks there are k disjoint Q-zero blocks, so D(H)=k forces a true zero sum. Thus no such pair can occur. Under additionally SOURCE_STATED D2(C5^3)=20, it follows that **|B_i|+|L|≤19 for every i**. More generally no t+1 pairwise disjoint Q-zero blocks can be formed from L and the union of ANY t original B_i. This is the precise overlapping-block replacement restriction. It does not follow just by saturating Σ(V).

### Numeric/index hostile gates
n15:m3,k7:6 blocks, leftover≤12; n20:m4,k10:9 blocks; n30:m6,k16:15 blocks. All have exactly5k+8 original positions. Their 28/29 critical Q-cores can be the symbolic A4 and A4' of S042 CLM-0160, which really have no short≤4 Q-zero and <4 disjoint Q-zero blocks. A purported purely local Q-core contradiction is therefore false. Similarly, Σ(V)=H does NOT allow adding a leftover single ORIGINAL index: its Q coordinate need not vanish, and its combination with existing blocks can overlap those blocks. The new gate requires a concrete Q-zero replacement W plus its H extension admissibility, or t+1 fully DISJOINT Q-zero blocks. This is still missing for general candidates.

No numeric search, enumerator, SAT/CAS, Lean or candidate was used. All bounds are necessary, no two-position saving or D(C15³)/D(C20³) resolution is claimed.
