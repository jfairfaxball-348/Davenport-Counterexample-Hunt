# S014 — Reiher's strategic equation and three-support cloudy sequences

Date 2026-10-11. ONE bounded Phase-1, original-primary-source hand-proof and provenance pass. Live entry main 8d16ecd63b769e6c138861f78a1dfbff6fd891b3 (S013 non-force merge PR13). Author's 29-page original PDF: https://www.math.uni-rostock.de/math/pub/preprints/preprint/2010/pre10_01.pdf , SRC-0025, known S013 byte count 289379 and SHA256 7d94931bcbf8fb4ce77c0ed94206659df74e8cb5543e1615e7dde23e86b994d8 (NOT freshly rehashed in S014). Original printed pp4–6,10–12,15–16 and 26; rendered polynomial and factorial displays directly checked. The 2010 published proof of full Property B remains source-stated, not programme-certified. No numerical or computational mathematical search, brute-force, CAS, orbit enumeration, author code, solver, Lean or campaign.

## Definitions and independent coefficient lemma (CLM-0094)

Let p be prime, F=F_p, and let a sequence mean *indexed positions*. A suspicious sequence is a length 2p−2 sequence in F² with no nonempty zero-sum index subset. Its cloudification appends its negative total sum to give a length 2p−1 zero-sum sequence with no nonempty proper zero-sum subset (cloudy); indeed a proper zero block in the extension either avoids the new term or has a nonempty complementary zero block in the old sequence. Conversely deleting any cloudy term makes a suspicious sequence. Cloudy sequences contain no zero term, and cannot contain p copies of any point.

For N points P_i=(a_i,b_i), define µ_m(P_1,…,P_N) as the coefficient of X^m Y^(N−m) in the product of (a_i X+b_i Y); let µ=µ_(p−1) for N=2p−2. In particular µ is symmetric and multilinear in its N point arguments.

**Boolean-cube coefficient lemma:** If a polynomial Q in N variables has total degree at most N, the coefficient of the squarefree monomial ε_1…ε_N equals
  sum_{I subset [N]} (−1)^(N−|I|) Q(1_I).
Proof: compute the right side on a monomial. It vanishes unless every variable appears with positive exponent, in which case its degree is at least N and thus, by the degree bound, it must be precisely ε_1…ε_N. Consequently a polynomial with nonzero squarefree top coefficient cannot vanish on the whole Boolean cube. This is the exact restricted combinatorial Nullstellensatz implication needed below, proved rather than imported.

Finite-field inputs: a^(p−1)=1 for nonzero a by permuting the nonzero field elements under multiplication by a and cancelling their product; and (p−1)!=−1 by pairing each field element with its inverse (only 1 and −1 are fixed for odd p; p=2 is immediate).

**Observation 2.2.** Under invertible linear map φ with determinant d, µ(φP_1,…,φP_(2p−2))=d^(p−1)µ(P_1,…). Verify on generators of GL₂(F): (a,b)↦(ka,b) multiplies the µ coefficient by k^(p−1); swapping coordinates exchanges the two degree p−1 exponents, leaving µ invariant and d^(p−1)=1; and (a,b)↦(a+b,b) expands µ to sum_{i=0}^{p−1} binom(2p−2−i,p−1) µ_i. For i≤p−2 the binomial numerator has a factor p while both denominator factorials are prime to p, so those terms vanish; the i=p−1 coefficient is 1. Diagonal rescalings, swaps and shears generate GL₂(F); determinant multiplicativity completes the identity. For F_p in particular d^(p−1)=1.

**Lemma 2.3.** For suspicious indexed length 2p−2 P_i, set U=sum a_i ε_i and V=sum b_i ε_i, and
  Q=product_i(1−ε_i) − (1−U^(p−1))(1−V^(p−1)).
At the empty subset both terms equal 1; at any nonempty index subset the first term is zero and, by suspiciousness, at least one of U,V is nonzero, making the second zero. Thus Q vanishes on the Boolean cube and its squarefree degree-2p−2 coefficient is zero. Direct binomial expansion gives 1−[(p−1)!]² µ(P)=0; Wilson implies µ(P)=1.

**Corollary 2.5.** For cloudy P_1,…,P_(2p−1), deleting any one term gives a suspicious sequence, and its µ equals 1. If αP_1+βP_2=0 for not-both-zero α,β, multilinearity gives
  αµ(P_1,P_3,…)+βµ(P_2,P_3,…)=0,
hence α+β=0. Since cloudy terms are nonzero, α and β are each nonzero, so P_1=P_2. Thus distinct cloudy points are pairwise linearly independent. The cloudification argument gives this conclusion for distinct suspicious terms as well.

**Observation 2.6.** If a cloudy sequence has p−1 pairwise dependent points, they are p−1 copies of the same nonzero e₁. After a GL₂ change let e₁=(1,0). The other p points (a_i,b_i) have b_i≠0, and each set of p−1 of their quotient b-coordinates is zero-sumfree in C_p: otherwise the corresponding nonempty proper quotient-zero block lifts to a zero block using between 0 and p−1 available e₁ copies. The independently established cyclic extremal lemma (S013 section 4: all zero-free length p−1 cyclic sequences are constant) forces all p projected b_i to coincide at one nonzero k, by overlapping p−1 subsets. Rescale the second coordinate by k^−1. Total zero gives sum_i a_i=1, precisely the simple cloudy normal form: e₁^(p−1) followed by p points (a_i,1) whose sum is e₁. Nothing is assumed about unconditional Property B.

## CLM-0095 — Proposition 4.1, the complete three-case strategic equation

We prove it for p≥5, the range needed after separately settling p=2,3 through Obs2.6 and the four one-dimensional lines in F_3². Take a suspicious (A,B,C,P_1,…,P_(2p−5)). Define µ*(X,Y,Z)=µ(X,Y,Z,P_1,…). We claim
 [BC]µ*(A,A,A)+[CA]µ*(B,B,B)+[AB]µ*(C,C,C)
 +3([BC]+[CA]+[AB])µ*(A,B,C)=0,
where [XY]=det(X,Y). If two of A,B,C are equal, the cancellations are immediate. Otherwise Cor2.5 after cloudification makes them pairwise independent. By Obs2.2 and determinant covariance, normalize A=(1,0), B=(0,1), C=(x,y), with xy≠0. Let q_j=µ_j(P_1,…,P_(2p−5)); this is defined for 0≤j≤2p−5 and the displayed indices p−4,…,p−1 are available for p≥5. Trilinearity, [BC]=−x,[CA]=−y,[AB]=1 and µ*(A,B,C)=xq_(p−3)+yq_(p−2) reduce the claim EXACTLY to
  E=(x³−x)q_(p−4)+3x(x−1)(y−1)q_(p−3)
    +3(x−1)y(y−1)q_(p−2)+(y³−y)q_(p−1)=0.

Let U=sum_i u_i ε_i, V=sum_i v_i ε_i for P_i=(u_i,v_i), N=2p−5. In all three cases construct Q of degree N that vanishes on the Boolean cube, so its squarefree coefficient is zero by the independently proved coefficient lemma.

Case I, x=1 or y=1: symmetry permits x=1. If y is 0,1 or −1, E is visibly zero. Otherwise the four values 0,1,y,y+1 are distinct. Take
  Q = product_{m ∈ F_p\{1}}(U+m) · product_{n ∈ F_p\{0,1,y,y+1}}(V+n).
Nonzero evaluation forces U=−1 and V one of 0,−1,−y,−(y+1), respectively cancelled by the NONEMPTY selected subsets J={A},{A,B},{C},{B,C}. Thus Q vanishes. Its squarefree coefficient is (p−1)!(p−4)!q_(p−1); the nonzero factorials force q_(p−1)=0, giving E=0.

Case II, x=−1 or y=−1: take x=−1. For y=1 the factor y−1 gives E=0; y=0 is forbidden; y=−1 would give the forbidden A+B+C=0. For the remaining y let
  H'(ξ,η)=(y²+y)ξ²−2yξη+2η²+(y+1)(yξ−2η),
  Q'=product_{m ∈ F_p\{−1,0,1}}(U+m) · product_{n ∈ F_p\{0,1,y,y+1}}(V+n) · H'(−U,−V).
The first two factors restrict (−U,−V) to {−1,0,1}×{0,1,y,y+1}. Direct substitution shows H' vanishes on six pairs
  (1,y),(1,y+1),(0,0),(0,y+1),(−1,0),(−1,1).
Every remaining nonzero-evaluation pair corresponds to one of the six NONEMPTY forbidden-subset sums J:
  (U,V)=(−1,0)→A; (−1,−1)→A+B; (0,−1)→B;
  (0,−y)→A+C; (1,−y)→C; (1,−y−1)→B+C.
Hence Q' vanishes on the Boolean cube. Its degree-N squarefree coefficient is
  −(p−2)!(p−4)![(y²+y)q_(p−1)−6yq_(p−2)+6q_(p−3)].
Factorials nonzero; multiplying the vanishing bracket by (y−1) gives E=0. The coefficient is obtained by taking ONLY the degree-two part of H', with (p−1)!(p−4)! for U², (p−2)!(p−3)! for UV, and (p−3)!(p−2)! for V², then reducing factorial ratios modulo p.

Case III, x,y each outside {0,1,−1}. The four residue values 0,1,x,x+1 are distinct, as are 0,1,y,y+1. Put
  H''(ξ,η)=(y³−y)ξ(ξ−x)(ξ−x−1)
     +(x−1)(y−1)ξη(yξ+xη−2xy−x−y)
     +(x³−x)η(η−y)(η−y−1),
  Q''=product_{m ∈ F_p\{0,1,x,x+1}}(U+m)
      ·product_{n ∈ F_p\{0,1,y,y+1}}(V+n) · H''(−U,−V).
Direct expansion/substitution gives H''=0 at the ten coordinate pairs
  (0,0),(0,y),(0,y+1),(1,y),(1,y+1),
  (x,0),(x,1),(x+1,0),(x+1,1),(x+1,y+1).
The six other grid pairs correspond exactly to NONEMPTY sums:
  (U,V)=(0,−1)→B; (−1,0)→A; (−1,−1)→A+B;
  (−x,−y)→C; (−x,−y−1)→B+C; (−x−1,−y)→A+C.
Hence Q'' vanishes everywhere on the cube. Its degree-N squarefree coefficient is
  −(p−1)!(p−4)![(y³−y)q_(p−1)
      +3(x−1)(y−1)y q_(p−2)
      +3(x−1)(y−1)x q_(p−3)
      +(x³−x)q_(p−4)] = −(p−1)!(p−4)! E.
Indeed use the homogeneous cubic part of H'', the factorial pairs (p−1)!(p−4)!, (p−2)!(p−3)!, (p−3)!(p−2)!, (p−4)!(p−1)!, and (p−3)/(p−1)≡3 mod p. The nonzero factorial product forces E=0. All configurations x,y were covered; Proposition 4.1 is independently reconstructed in this required range. No unspecified Nullstellensatz lemma or inspection-only table is being promoted.

## CLM-0096 — Observation 7.1 factorial determinant identity

For pairwise independent A,B,C and nonnegative α+β+γ=2p−2,
  [BC]^α[CA]^β[AB]^γ µ(A^α,B^β,C^γ)=α!β!γ! in F_p.
GL₂ reduction (Obs2.2) yields A=(1,0),B=(0,1),C=(x,y), xy≠0; all determinant factors are nonzero. If any exponent ≥p, its factorial is 0. The µ coefficient vanishes as well: for α or β≥p the required complementary degree is negative; for γ≥p with α,β<p, the relevant binomial coefficient binom(γ,p−1−α) vanishes modulo p because (1+T)^γ=(1+T^p)(1+T)^(γ−p) and p−1−α>γ−p. Otherwise α,β,γ≤p−1, and
  µ=binom(γ,p−1−α)x^(p−1−α)y^(p−1−β).
The left side is (−1)^(α+β) γ! /[(p−1−α)!(p−1−β)!] by Fermat. Wilson's paired-factor identity
  a!(p−1−a)!=(−1)^(a+1)
gives precisely α!β!γ!. This establishes the required entire factorial identity independently.

## CLM-0097 — Lemma 7.2, at most three support points

For p=2, a cloudy sequence of length3 must have p−1=1 repeated (any term), hence Obs2.6 makes it simple. For p=3, a cloudy sequence has five nonzero terms; there are only four 1-dimensional subspaces in F_3², so two distinct positions are linearly dependent; Cor2.5 and Obs2.6 give simplicity. Let p≥5 be odd. If a cloudy sequence has one or two distinct points, total length 2p−1 forces ≥p copies of one point, impossible. Suppose three distinct points A,B,C occur α,β,γ≥1, summing to 2p−1; each multiplicity ≤p−1. If one is ≤2, one of the other two must equal p−1, and Obs2.6 finishes. We may thus assume α,β,γ≥3. In particular γ−2≥1 and the choice of an extra omitted C position is legitimate.

Deleting one C produces a suspicious sequence length2p−2. Singling out indexed A,B,C, leaving α−1,β−1,γ−2 others, apply the completed strategic equation (CLM-0095):
  [BC]µ(α+2,β−1,γ−2)+[CA]µ(α−1,β+2,γ−2)
  +[AB]µ(α−1,β−1,γ+1)
  +3([BC]+[CA]+[AB])µ(α,β,γ−1)=0.
Here µ(a,b,c)=µ(A^a,B^b,C^c), with a+b+c=2p−2. Multiply by [BC]^(α+1)[CA]^(β+1)[AB]^γ; divide by nonzero (α−1)!(β−1)!(γ−2)! and invoke CLM-0096. Writing d1=[BC],d2=[CA],d3=[AB] yields
  d2²d3² α(α+1)(α+2)+d1²d3² β(β+1)(β+2)
 +d1²d2²(γ−1)γ(γ+1)
 +3d1d2d3(d1+d2+d3)αβ(γ−1)=0.
Total cloudy sum αA+βB+γC=0; also d1 A+d2 B+d3 C=0. As A,B independent, the relation space among A,B,C is one-dimensional; d1,d2,d3 are each nonzero by Cor2.5. Therefore some k≠0 satisfies (d1,d2,d3)=k(α,β,γ). Since α,β,γ ∈ {3,…,p−1} and the p−1 case would already finish, all required divisors k,α,β,γ are nonzero. Divide by k⁴αβγ:
  βγ(α+1)(α+2)+αγ(β+1)(β+2)
  +αβ(γ−1)(γ+1)+3(α+β+γ)αβ(γ−1)=0.
The left side equals
  2(α+1)(β+1)(γ+1)
  +(4αβγ−3αβ−2)(α+β+γ+1);
this follows by expansion, using no extra input. Since α+β+γ+1=2p=0 in F_p, p is odd and therefore (α+1)(β+1)(γ+1)=0. An integer multiplicity from 3 through p−1 equals −1 modulo p only if it equals p−1. Hence Obs2.6 makes the cloudy sequence simple. This PROVES the support≤3 route used at the start of Theorem 10.2; it does not prove the theorem's general four-support-plus branch.

## Exact stopping boundary and preserved scopes

The next first unclosed original proof input in Theorem10.2's four-distinct-point branch is Proposition 5.1's collinear reconstruction, using the now-proved strategic equations; the clean-triple Proposition 6.2/8.1 and Section9 conic/quartic/general-position/Proposition10.1 chain remain unproved. This session STOPS expansion before reconstructing Proposition5.1. Original Theorem10.2 prime Property B remains SOURCE_STATED; S013 CLM-0093 conditional B=>C is NOT upgraded to unconditional. Therefore eta(C7³)≤116 remains conditional. S012 CLM-0084–0088 p7 and S013 CLM-0089–0093 are unchanged, including the printed false sum, valid repair, actual all-1 t-sum condition and narrow exact p/2p translation. BSP2012 coefficient is only (3p−1)/2 from original split, not 3(p−1)/2.

Source/provenance: this pass viewed original Reiher pages and attempted fresh lawful web read of official Sheikh PDF, returning 403 Forbidden; original C53.html page was inaccessible via the web tool (not authenticated output); arXiv Yiu2609.04950v1 abstract page remains accessible and advertises ancillary files, but no newly authenticated M1/M2/M3 implementation, log, certificate or final three-disjoint predicate was retrieved, and no code was executed. Earlier precise S013 bytes/hashes/access errors are preserved, not replaced by a new invented fresh hash or a global absence inference. No new exact literature statement independently authenticated for the five frontier intervals; none is declared open on this basis. Every n=1..30 numeric frontier field stays unchanged, with 25 source-exact/trivial and five conditional intervals. Schmid2011 n6=16 and original historic 1969 source-stated rank-three families remain exactly scoped; CAM-0001 is blocked, not activated. Quarantine inherited14/17, tripling+5, orbits43/699/5553. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED / NOT RUNNING. One future S015 handoff, strictly UNEXECUTED.
