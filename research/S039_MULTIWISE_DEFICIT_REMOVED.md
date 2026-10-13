# S039 — A direct multiwise route removes the two-position deficit

2026-10-13. One S039 sustained Phase1 symbolic session. Entry main `99018af95fe5dd35a915cf5171a40aa0bc86a5e0`; S038 reconciliation and intervening handoff-only PR39 are recorded separately. These are independently reconstructed elementary proofs, NOT a novelty claim or a reconstruction of the omitted original BSP2012 rank-three Lemma2.3. No numerical mathematical search, CAS, solver or author code was used.

## Definitions and elementary polynomial divisibility

For an indexed sequence S in G, D_k(G) is the least length guaranteeing k pairwise disjoint NONEMPTY zero-sum index subsets. Write D=D_1. Subsets and counts always refer to original indexed positions, even for repeated values.

We use the following elementary Chevalley–Warning argument, including its proof. For coordinate polynomials P_h in n variables over F_p with sum of degrees less than n, the indicator of their simultaneous zero set is product_h(1-P_h^(p-1)). Its degree is less than n(p-1). In its field sum, a monomial can survive only if each variable has a positive exponent divisible by p-1; the exponent-zero power sum is p=0 in F_p, and other nonmultiples have zero power sum. Such a monomial would need degree at least n(p-1). Therefore the number of simultaneous zeros is 0 modulo p. A zero-sum support B for polynomials sum_i z_ih x_i^(p-1) corresponds to (p-1)^|B| assignments, hence contributes (-1)^|B| modulo p. Adding the cardinality polynomial sum_i x_i^(p-1) restricts supports to sizes divisible by p. These statements hold even if a polynomial vanishes identically.

## CLM-0142 — source-independent reconstruction of prime rank-three D1

**Theorem.** For every prime p, D(C_p^3)=3p-2.

Take any sequence of n=3p-2 indexed vectors, and its three coordinate polynomials P_h=sum_i z_ih x_i^(p-1), h=1,2,3. Their degree sum is at most 3(p-1)=3p-3<n. The divisibility argument above applies. If there were no nonempty zero-sum index subset, the only simultaneous zero assignment would be the all-zero assignment, giving count 1, contrary to divisibility by p. Thus D<=3p-2. The standard basis sequence with p-1 copies of each basis vector is zero-sumfree: each coordinate count belongs to 0..p-1 and must be 0 if the sum vanishes modulo p. Its length is 3p-3, giving the opposite inequality. QED.

This reconstructs the PRIME rank-three statement directly. It is not an inspection of Olson's original full p-group proof and does not authenticate arbitrary p-power or composite historical source records. Frozen original frontier rows retain their existing evidence categories. Earlier statements that the local S030 proof did not claim a global reconstruction remain accurate at their historical cutoff; this new general proof expressly removes the imported premise from the new arguments.

## CLM-0143 — D2(C_p^3)<=5p-3 for every odd prime

**Theorem.** Every indexed sequence of length 5p-3 in C_p^3, for an odd prime p, contains two disjoint nonempty zero sums. In particular D2<=6p-6 for every p>=5, including the entire requested p>=7 range.

Let S have length 5p-3 and suppose it has no two disjoint nonempty zero sums. Put D=3p-2, now independently proved in CLM-0142.

1. S cannot contain a zero-sum subset of length p: its complement has length 4p-3>=D and hence contains another zero sum, disjoint from it.
2. ANY zero-sum subset B of length greater than D would itself split into two nonempty zero sums. Indeed choose any D of its positions, find a nonempty zero-sum Y among them by CLM-0142, and take B minus Y. Since |Y|<=D<|B|, the complementary zero sum is nonempty. Thus S has no zero sum of length 3p or 4p (or any larger-than-D length). This implication requires sigma(B)=0; it is NOT a claim that every long arbitrary subset splits.
3. Apply the four-polynomial divisibility argument (three coordinates AND cardinality) to any T of size at least 4p-3. Its degree sum is at most 4(p-1)=4p-4<|T|. Every nonempty simultaneous-zero support has size a positive multiple of p. For S itself, and for every T subset S of size 4p-3, only length 2p is possible by 1 and 2: length p is forbidden, and multiples >=3p exceed D. The empty support contributes 1 and a 2p support contributes +1 because 2p is even. Therefore, writing X=N_(2p)(S),

       1+X=0 mod p,
       1+N_(2p)(T)=0 mod p for every |T|=4p-3.

4. Sum the latter congruence over ALL indexed T of that size. Each indexed 2p zero-sum support in S is contained in exactly binom(3p-3,2p-3) such T. Thus

       binom(5p-3,4p-3)+binom(3p-3,2p-3) X=0 mod p.

The two binomial coefficients are respectively 4 and 2 modulo p. To check directly, write 5p-3=4p+(p-3), 4p-3=3p+(p-3), and similarly 3p-3=2p+(p-3), 2p-3=p+(p-3). The identity (1+x)^p=1+x^p modulo p shows the indicated coefficients are binom(4,3)=4 and binom(2,1)=2. This also holds at p=3, where high-digit carries merely reduce 4 modulo 3; low exponents are p-3=0. Hence 4+2X=0. Substituting X=-1 from the whole-S congruence gives 2=0 in F_p, impossible for an odd prime. Contradiction. QED.

No short-extraction assumption, hypothetical balanced-only Z, Psi vanishing, universal pair positivity, eta bound, omitted BSP induction or unreconstructed external D1 theorem entered this proof. p2 is expressly excluded from the lifted contradiction because 2=0 there; no all-prime extrapolation is made.

**Boundary checks, by hand:** p3 D2<=12; p5 <=22<=24; p7 <=32<=36; p13 <=62<=72. These are upper bounds, not claims of exact D2 values. Both p7 and p13 satisfy strict four-polynomial CW (4p-3>4p-4), the plus sign on 2p supports, and the same nonzero residual 2.

## Continuation beyond the first D theorem: the one-position stronger attempt

The initial extraction-only D attack gave D2<=5p-2: CW on a 4p-3 subsequence yields a p,2p or3p zero sum; the first two leave >=D positions in a sequence of length 5p-2, and the last splits internally. The lift above then genuinely removes one more position. We did NOT stop at the first theorem.

Try the same contradiction at 5p-4, for p>=5. Under a no-two assumption, p supports are still forbidden since their complement has 4p-4>=D positions; supports >=3p still split internally. So the whole sequence again gives 1+X=0. However lifting the 4p-3 congruence gives coefficients

   binom(5p-4,4p-3)=0 mod p,
   binom(3p-4,2p-3)=0 mod p,

because the low base-p digit p-3 required by the selected size exceeds p-4. The resulting lifted equation is 0=0, not a contradiction. Choosing 4p-4 variables instead reaches EXACT equality with four polynomial degrees; strict CW no longer supplies divisibility. Adding an auxiliary zero to repair length also creates a trivial zero sum; a two-sum conclusion involving that new zero cannot be pulled back to two disjoint sums in the original sequence. These are precise failures of this attempted extension, NOT a proof that 5p-4 is impossible or best. No D2<=5p-4 assertion is made.

## CLM-0144 — composed weak-extraction recurrence closes M with slack

**Theorem.** For every odd prime p and integer k>=2,

   D_k(C_p^3) <= B_k := 5p-3+(k-2)(3p-1)/2.

For p>=7, put k0=2p-4 and M=3p^2-4p-3. Then

   D_(k0)(C_p^3) <= 3p^2-5p = M-(p-3) < M.

**Proof.** CLM-0143 proves the k2 base B2=5p-3. S025's reconstructed p-or-3p theorem on length 6p-3, composed with the newly reconstructed CLM-0142, supplies a zero sum of length at most b=(3p-1)/2: a p-block already suffices, while a 3p zero block splits into proper complementary zero sums and one side has length <=floor(3p/2)=b. This is exactly the weaker bound, not the still-unproved b-1 assertion.

For the induction from k-1 to k, k>=3, B_k>=B3=(13p-7)/2>=6p-3 because the difference is (p-1)/2>0. Thus a sequence of length B_k contains a nonempty zero-sum block of length <=b. Remove it; at least B_k-b=B_(k-1) positions remain and the induction gives k-1 more pairwise disjoint nonempty zero sums. All disjointness is by original positions. QED.

Substitute k0: (k0-2)b=(2p-6)(3p-1)/2=3p^2-10p+3. Adding 5p-3 gives 3p^2-5p. Since M=3p^2-4p-3, the slack is p-3. At p7: k0=10, B=32+8*10=112, M=116, slack4. At p13: k0=22, B=62+20*19=442, M=452, slack10. This repairs the EXACT S025 M+2 deficiency using weak extraction and a better base. The old weak estimate was an upper bound, never a lower bound on true D_k.

**Endpoint scope.** Independently of all Psi cases, the requested D2 saving and multiwise comparison D_(2p-4)<=M are now established. If a separately valid rank-three eta(C_p^3)<=M is available, choose this M and k0: also M<=p^2+pk0=3p^2-4p. This supplies the two numerical premises of the BSP downstream criterion. The eta premise is PROGRAMME_PROVED at p7 (CLM-0112, eta<=116); the general p>=7 eta proof is not reconstructed here, and the remaining global inductive argument must be checked separately. Neither a new composite D1 frontier value nor a proof/counterexample for D(C_n^3)=3n-2 follows merely from these inequalities. The stronger b-1 extraction and exact omitted BSP Lem2.3 coefficient remain unproved and are no longer prerequisites for THIS repaired comparison.

## Provenance / validation

Read-only original definitive SRC-0021 publisher-author offprint, printed pp22-24, and p23 page image re-inspected. Its printed weak extraction, stronger unaccounted split and omitted rank-three proof remain distinct. The proofs here are internal deductions using elementary CW, not author-attributed assertions or a novelty determination. CLM-0142 does not upgrade access to Olson's original general p-group proof; original28 source objects and original30 frontier rows remain frozen. Same-executor hostile validation checks every maximum length, proper complement, sign, indexed lift multiplicity, base-p carry at p3, both p7/p13, and the k3 induction threshold. No external referee, formal proof, search, Lean, Palomar, campaign or hosted CI pass. Companion geometry dossier records the continued A/B/C attacks; S040 is future only.

## Historical dependency reconciliation (binding qualification)

S004 CLM-0068 and S005 section1 already supplied a weaker CONDITIONAL bypass with D2<=5p-2, weak extraction and slack p-4. Later M+2 calculations referred to an inferior safe base and must not be read as disproving that old route or establishing that no bypass had been derived. S039 improves the old base by ONE position, reconstructs its prime D1 premise without external source dependence, and restores the route to current authority. Its multiwise theorem is a strengthened and freshly validated route, not a novelty claim or a first historical discovery of the bypass. General eta and global inductive provenance remain separate. See the companion dossier for this correction and all continued A/B/C attacks.
