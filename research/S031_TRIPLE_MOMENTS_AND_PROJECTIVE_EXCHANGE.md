# S031 — Pair-sum boundary moment, quantitative support and projective exchange

2026-10-12. One independently owner-invoked Phase-1 **symbolic** proof/provenance session only, remote entry main `eed11ce4a6e05515198e48a32ba8cc8165bc375c`, tree `52259fe721a498423a15a653b245d07ddb1ecb8e`. S030 branch commit `10a425848606e68a3c1cdf6e795ea80eed84ca67` has sole parent `6263732628029ef7b31dbf0fbb3ae94a01d30e9e` and tree `52259fe721a498423a15a653b245d07ddb1ecb8e`; genuine merged PR30 has non-force two-parent merge `eed11ce4a6e05515198e48a32ba8cc8165bc375c`. No mathematical numerical or computational search, CAS, SAT/ILP, candidate construction, source-code execution, Lean, Palomar, campaigns or publication.

## Hypotheses

Fix an odd prime p>=7. Let N=3p, b=(3p-1)/2, a=b-1, s=(-1)^b, t=(p+s)/2. Suppose an **indexed** zero-sum sequence Z=(z_i)_{i in I} in F_p^3 has |I|=N and no nonempty zero-sum subsequence of length <=a. Let F be the **complete** family of indexed b-subsets B with sum_{i in B} z_i=0, m=|F|, r_i=#(B containing i), lambda_ij=#(B containing distinct i,j), tau_ijk=#(B containing three distinct i,j,k). By S029, m=kp with k>=2, r_i=t mod p; by S030,

Psi_ijk := Psi(I\\{i,j,k}) = -1/2+s(lambda_ij+lambda_ik+lambda_jk-2tau_ijk) (mod p).

The coefficient Psi(T) is the ordered, three-colour balanced (p-1,p-1,p-1) coefficient defined in CLM-0128. All division by 2 and 3 in this note is modulo p (p>=7).

## CLM-0129 — exact pair-sum of the critical coefficient (PROGRAMME_PROVED)

**Theorem.** For every two distinct original indices i,j,

    sum_{k in I\\{i,j}} Psi_ijk = -1/2+s lambda_ij = s(lambda_ij-t)  (mod p).

**Self-contained incidence proof.** Sum the exact CLM-0128 identity over the N-2 possible third indices k. All index sets are literal, and k is distinct from i,j throughout. The four incidence contributions are

    sum_k lambda_ij = (N-2)lambda_ij;
    sum_k lambda_ik = (b-1)r_i-lambda_ij;
    sum_k lambda_jk = (b-1)r_j-lambda_ij;
    sum_k tau_ijk = (b-2)lambda_ij.

For example, a block containing i has exactly b-1 choices for its second index, and the forbidden choice j is counted lambda_ij times; a block containing i,j has exactly b-2 further choices. Thus the bracket is exactly

    (b-1)(r_i+r_j)+(N-2b)lambda_ij
    = (b-1)(r_i+r_j)+lambda_ij,

because N=2b+1, an INTEGER equality. Hence

    sum_k Psi_ijk = -(N-2)/2 + s(b-1)(r_i+r_j)+s lambda_ij.

Reduce N=0, b=-1/2, r_i+r_j=s in F_p. The constant is 1+(b-1) = b = -1/2, so this is -1/2+s lambda_ij. Finally st=1/2 mod p. No assumption Psi_ijk=0 has been used. QED.

**Consequences.** Whenever lambda_ij is not congruent to t mod p, at least one of the N-2 actual three-deletion coefficients Psi_ijk is NONZERO. This is a value-sensitive constraint, NOT a forbidden zero-sum or a contradiction. Conversely, setting all Psi_ijk to zero would force every lambda_ij=t mod p; it is invalid to infer universal vanishing from equality in the Chevalley–Warning degree threshold.

## CLM-0130 — mandatory many nonzero triples at m=2p (PROGRAMME_PROVED, conditional)

**Theorem.** Suppose in addition m=2p. S029 gives the exact two-level census r_i=t or t+p, with H=(3p-2-3s)/2 high-degree indices and L=(3p+2+3s)/2 low-degree indices (r_i=t). Then the number of unordered three-index deletion sets {i,j,k} for which Psi_ijk is nonzero in F_p is at least

    ceil( L(b+1) / 6 ).

**Proof without enumeration.** For each low-degree index i, r_i=t>=1, so choose ANY b-block B_i containing i. At least N-b=b+1 other indices j lie outside B_i. For each such j, not all r_i=t blocks through i contain j; thus 0<=lambda_ij<=t-1 as exact integers. In particular lambda_ij != t mod p because 1<=t<p. CLM-0129 says sum_{k distinct from i,j} Psi_ijk = s(lambda_ij-t) !=0. Consequently some distinct k gives Psi_ijk !=0.

There are at least L(b+1) *directed* such pairs (i,j) with low first index, hence at least L(b+1)/2 distinct unordered pairs (since a pair has at most two orientations). Each nonzero unordered triple can witness at most its three constituent unordered pairs. Covering every such pair therefore requires at least L(b+1)/6 distinct nonzero triples; round up to the nearest integer. This bound is conditional on **an actual indexed Z with m=2p**. It does not establish existence of Z, does not contradict m=2p, and leaves m=3p,4p,... wholly unresolved. QED.

**Exact p=7 hand check.** b=10, s=+1, t=4, H=8, L=13, m=14. The lower bound is ceil(13*11/6)=24 nonzero coefficients among C(21,3) formal deletion triples. This is symbolic arithmetic only; no vector instance was generated or searched.

## CLM-0131 — projective interpretation, blocking criterion, four-index exchange (PROGRAMME_PROVED identities)

For each index v define the linear form L_v(X)=z_{v1}X_1+z_{v2}X_2+z_{v3}X_3. For every T of size 3(p-1), coefficient extraction gives exactly

    Psi(T) = [X_1^(p-1)X_2^(p-1)X_3^(p-1)] product_{v in T} L_v(X).

This is because each factor contributes one coordinate and the coefficient records ordered colour classes of size p-1. The full homogeneous product has degree 3(p-1). Sum it over X in F_p^3: every monomial vanishes in the field sum except the central monomial, whose variable power sums are (-1)^3=-1. Therefore

    Psi(T) = -sum_{X in F_p^3} product_{v in T} L_v(X)
           =  sum_{[X] in P^2(F_p)} product_{v in T} L_v(X) (mod p).

The projective product is well defined because scaling X by c!=0 multiplies it by c^{3(p-1)}=1, and the p-1 nonzero representatives of each point contribute -1 mod p. Consequently Psi is invariant under any invertible simultaneous linear change of the z_v basis. If the directions {F_p z_v:v in T} meet the kernel of EVERY nonzero functional X, then every projective product is zero and Psi(T)=0. In particular this is true if T contains all p+1 distinct one-dimensional directions of some two-dimensional vector subspace: each kernel plane intersects that subspace in a nonzero direction. This is a conditional **blocking-set vanishing**, not a claim it holds for every deletion T. All z_v are nonzero by the no-short hypothesis.

**Four-index exchange.** Choose four distinct indices A={i,j,k,l} and let U=I\\A (size 3p-4). Write R_U(X)=product_{v in U}L_v(X), homogeneous of degree 3(p-1)-1. Let c_h(U) be the coefficient of X_h^{p-2} times the other two variables to exponent p-1 in R_U. For every q in A, the three-deletion T=U union {q} has

    Psi(I\\(A\\{q})) = sum_{h=1}^3 c_h(U) z_{qh}.

Thus if coefficients alpha_q in F_p satisfy sum_{q in A} alpha_q z_q=0, they necessarily satisfy

    sum_{q in A} alpha_q Psi(I\\(A\\{q})) =0.

Four vectors in three-dimensional space always have a nontrivial dependence; a determinant version follows from the alternating four-vector dependence when triple minors are nonzero. The exchange relation is exactly indexed and GL_3 invariant. It is a further constraint connecting vector coordinates to the pair/triple incidence expression for Psi, **not** a purely numerical exclusion of any permissible m. QED.

## Independent adversarial reconstruction (separate INTERNAL same-executor pass)

* Re-sum the four incidence counts with k excluded from {i,j}, confirming lambda_ik contributes (b-1)r_i-lambda_ij, tau contributes (b-2)lambda_ij; N-2b=+1, NOT -1. Reducing -(N-2)/2+s(b-1)s gives exactly b=-1/2. Check s t=1/2 because t=(p+s)/2. No missing factor of three.
* The low-degree count L=3p-H uses exact r_i values, not residues. For each i selected B_i contains i and exactly b positions, so b+1 outside choices; they are all distinct from i. Each undirected pair has at most 2 directed orientations and each deletion triple has exactly 3 constituent unordered pairs. The bound is valid without assuming different witnesses k for different pairs.
* Projective field-sum sign: in three variables the central monomial sums to (-1)^3=-1; projectivizing multiplies by (p-1)=-1, yielding the POSITIVE projective point sum. Degree 3(p-1) is critical. Full line in a two-plane means exactly p+1 *distinct vector directions*, not merely p+1 vectors with repetitions.
* Exchange coefficient c_h has exponent p-2 in position h, degree 3p-4, including p=7. The formula for retained q uses z_{qh} and no factorial. All four complements have exactly three deleted original indices; exchange does not assume their Psi values vanish.
* Counterargument to overclaim: the proven support bound counts allowed **nonzero** Psi values, whereas strict CW gives no requirement Psi=0 at three deletions. Neither m=2p nor higher k is ruled out, and an abstract S028 whole-cell configuration is still not an indexed sequence.

## First essential STOP and provenance

FIRST unclosed extension: prove a geometric/projective restriction or nontrivial upper bound on the number/placement of nonzero Psi triple deletions strong enough to contradict CLM-0130, or exploit exchange plus full indexed zero-sum block geometry to exclude m=2p; even then m>=3p remains. No such restriction is established. Optional Route B D2(C_p^3)<=6p-6 was NOT preregistered for activation; the S024/S025 safe recurrence still gives M+2 for M=3p^2-4p-3. No theorem/proof of p>=7 strong extraction or original omitted rank3 BSP2012 Lemma2.3, no classic D(C_n^3)=3n-2 proof/counterexample, no novelty or priority claim.

Read-only definitive original Bhowmik–Schlage-Puchta publisher offprint SRC-0021 printed pp22-24 and the printed p23 page inspected: Lemma2.1 states weaker (3p-1)/2, later split uses unsupported stronger 3(p-1)/2, Lemma2.3 explicitly omits the rank3 proof. CLM-0129–0131 are programme-internal identities, NOT attributed to that source. Sheikh2017 full Chapter4 remains unread, GHST full C53 code/output unread and never run, Yiu v1 repeated-generator numbers are NOT independently authenticated final M1 test. Focused primary-exact searches for n15/20/21/28/30 found no newly authenticated exact original theorem; non-discovery is not present-day openness evidence. No source access enum changes.

All 30 original JSON rank-three D1 row objects and 30 Markdown numerical/status/ordered evidence table rows preserved, including n15 43..45, n20 58..59, n21 61..63, n28 82..83, n30 88..90. Historical Schmid n6=16 and van Emde Boas/Yiu retain SOURCE_STATED. CAM-0001 remains PROPOSED/NOT_RUNNING/BLOCKED n6=16. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; zero hosted checks is NOT CI PASS.
