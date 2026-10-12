# S030 — Olson-free pair cover, complete degree levels, and the exact three-deletion polynomial boundary

Date: 2026-10-12. Exactly one owner-invoked Phase-1 symbolic proof/provenance session; no mathematical computer search, solver/CAS, generated candidate, author code, Lean or Palomar. Entry remote main `6263732628029ef7b31dbf0fbb3ae94a01d30e9e` (tree `d859f6fc8d860666b1776c23d4981c8e6e68728f`). S029 single commit `4a568eb851ca9b5f607ab69deda83b7dde2933da` has sole parent `5fa1f4c645f4d9454341e17eb3ba104f75b44487` and tree `d859f6fc8d860666b1776c23d4981c8e6e68728f`; PR29 ordinary two-parent non-force merge has precisely those parents and equals entry main.

## Hypotheses and bounded scope

Let p be an odd prime >=7, let a=3(p-1)/2 and b=(3p-1)/2=a+1. Let Z=(z_i)_{i in I} be a *zero-sum* indexed sequence over F_p^3 with |I|=3p=2b+1 and **no nonempty zero sum on <=a indices**. The complete family F of b-subsets of I summing to zero has m members. Let r_i count F-blocks containing i and lambda_{ij}, tau_{ijk} count F-blocks containing both indices and all three indices respectively (distinct indices throughout). Every nonempty proper zero-sum subset of Z has length exactly b or b+1, and complementation bijects these families, as proved in S029.

Preregistered route A FIRST: test one- and two-deletion Chevalley–Warning with exact index counting and determine whether this strengthens m>=2p and removes Olson dependency; then inspect the STRICT degree boundary for three deletions by a full symbolic finite-field coefficient identity. Hard STOP after closed scoped lemmas and the first essential unproved implication. Route B, the separate D2<=6p-6 two-position saving, is optional and was not activated once Route A exposed its exact boundary obstruction.

## CLM-0127 (PROGRAMME_PROVED): elementary pair-cover and all multiplicity layers

**Lemma 1 (source-independent pair-cover).** For every two *distinct* original positions i,j of Z, some B in F contains both or contains neither. This consequence of no-short Z does **not** import Olson's general D(C_p^3)=3p-2 theorem.

**Proof.** Delete i,j; 3p-2 variables remain. For h=1,2,3 let P_h(X)=sum_{v!=i,j} z_{vh}X_v^(p-1). There are n=3p-2 variables, the sum of the three polynomial degrees is <=3(p-1)=3p-3<n. The elementary Chevalley–Warning argument expands the simultaneous-zero indicator product_h(1-P_h^(p-1)). A contributing monomial in the field-sum would need each of its n variables with positive degree divisible by p-1, hence total degree >=n(p-1); the indicator has total degree <=3(p-1)^2<n(p-1). Thus the number Q_{ij} of common zeros is divisible by p. The all-zero assignment contributes one. If no nonempty support summed to zero, it would be the **only** common zero, so Q_{ij}=1, a contradiction. Hence the remaining sequence has a nonempty zero-sum index subset W. It is proper in Z and therefore has size b or b+1. In the former case W itself avoids i,j; in the latter case its complement B=I\W is a b-block containing both i,j. Every index and support is literal; repeated group values do not identify positions. QED.

This proof removes SRC-0003 classical Olson as an essential **local** premise of the pair-cover part of S026 CLM-0122, and therefore of the S027 local incidence consequence. It does NOT reconstruct Olson's global D1 theorem or change a source access enum. The full rank-three numerical frontier still imports historical Olson where separately needed.

**Lemma 2 (all-layer degree census).** Write s=(-1)^b and t=(p+s)/2, 1<=t<p. By S029's independently proved one-deletion identity, 2r_i=m+s (mod p), m=kp for a positive integer k>=2, and r_i=t (mod p). There are consequently integers
j_i in {0,1,...,k-1} with r_i=t+p j_i, and exact incidence counting yields

sum_{i in I} j_i = kb-3t = [3(k-1)p-k-3s]/2.

**Proof.** The residue t solves 2t=s mod p; 0<=r_i<=m=kp and 0<t<p force exactly the stated possibilities for j_i. The integer identity sum_i r_i=mb=kp b gives 3p t+p sum_i j_i=kp b, hence the formula. All steps are exact; no new divisibility assumption is inserted. For k=2, j_i is 0 or1 and their sum H=(3p-2-3s)/2, reproducing S029; for k=3 the weighted level budget is 3p-3 when s=+1, or 3p when s=-1. The census alone does not make any level impossible. QED.

**Two-index support count is algebraically redundant.** By complementation, among zero-sum b-blocks avoiding i,j there are m-r_i-r_j+lambda_{ij}; among b+1 zero-sum blocks avoiding i,j there are *lambda_{ij}*, because their complementary b-blocks contain both. As (p-1)^d=(-1)^d modulo p, the same Q_{ij} obeys

0 = Q_{ij} = 1+s(m-r_i-r_j) (mod p).

It has no surviving pair-co-degree. Substituting m=0 and r_i=r_j=t modulo p gives 1-2st=0 automatically. Hence the naive two-deletion modular route CANNOT improve the one-deletion m>=2p census. This is not a proof that all other methods fail.

## CLM-0128 (PROGRAMME_PROVED): exact three-deletion boundary identity

**Theorem.** For any three *distinct* indices i,j,k, let T=I\{i,j,k}, so |T|=3p-3=3(p-1). Define, in F_p,

Psi(T) = sum over all ordered partitions (T_1,T_2,T_3) of T,
         with |T_1|=|T_2|=|T_3|=p-1,
         of [ product_{v in T_1} z_{v1} ][ product_{v in T_2} z_{v2} ][ product_{v in T_3} z_{v3} ].

Then the *exact* boundary relation is

Psi(T) = 1+s(m-r_i-r_j-r_k+lambda_{ij}+lambda_{ik}+lambda_{jk}-2tau_{ijk})
       = -1/2+s(lambda_{ij}+lambda_{ik}+lambda_{jk}-2tau_{ijk})  (mod p).

In the final expression 1/2 is the inverse of 2 in F_p. This identity does NOT assert Psi(T)=0.

**Proof from scratch.** Consider P_h=sum_{v in T} z_{vh}X_v^(p-1) and Q_T the number of simultaneous common zeros over F_p^T. Each assignment has support W with group sum zero and (p-1)^|W| choices, hence modulo p the support-count formula is 1+s(N_b(T)-N_{b+1}(T)). The b-blocks avoiding all three have count m-(r_i+r_j+r_k)+(lambda_{ij}+lambda_{ik}+lambda_{jk})-tau_{ijk}. Complements of b-blocks of size b+1 avoid all three precisely when the b-block contains all three, so N_{b+1}(T)=tau_{ijk}. This gives the first displayed formula.

For the polynomial expression let E(X)=prod_{h=1}^3(1-P_h(X)^(p-1)); its value is the characteristic-function indicator of a simultaneous common zero. Summing E over all X in F_p^T computes Q_T in F_p. Here n=3(p-1) is EVEN, and the TOP total degree equals n(p-1). For any field-summed monomial to survive, every variable must have positive exponent a multiple of p-1. The only possibility is exponent precisely p-1 for every variable; only the product of the three top factors contributes, with leading sign (-1)^3=-1. Each one-variable field-sum of X^(p-1) is -1, and (-1)^n=+1. Hence Q_T is minus the coefficient of product_{v in T} X_v^(p-1) in product_h P_h^(p-1).

Writing Y_v=X_v^(p-1), the coefficient of product_v Y_v in product_h(sum_v z_{vh}Y_v)^(p-1) selects exactly one of the three coordinate-polynomials for each original index and precisely p-1 indices in each class. Its coefficient is ((p-1)!)^3 Psi(T). By Wilson's elementary identity (p-1)!=-1 (mod p), this coefficient is -Psi(T). The preceding minus sign therefore gives Q_T=Psi(T) (mod p). Finally S029 yields m=0 and r_i=r_j=r_k=t=s/2 modulo p, and 1-3/2=-1/2, proving the second formula. QED.

**Pivotal strictness warning.** Three deletions give n=3p-3 EXACTLY sum_h deg(P_h); Chevalley–Warning's strict n>sum_h deg(P_h) condition fails. Dropping the boundary coefficient Psi, or incorrectly replacing it by 0, would be an invalid step. No vector-value-free argument forcing Psi(T)=0 has been proved, and even such a vanishing identity would require further control of lambda/tau to contradict the m=2p census.

**p=7 symbolic boundary.** b=10,s=+1,t=4; m=14 would require 8 positions of b-degree11 and 13 of b-degree4 (as before). For any triple T has 18 remaining positions; Psi(T) is the labelled three-way split into sextets using the three coordinate-products. The identity is Psi(T)= -1/2 +lambda_ij+lambda_ik+lambda_jk-2tau_ijk in F_7 (where -1/2=3). It does not force 0, so m=14 is not excluded. p=7 checks here are symbolic substitutions, NOT sequence enumeration.

## Adversarial reconstruction and STOP

Separate internal review independently redid: strict variable thresholds 3p-2>3(p-1) and 3p-3=3(p-1); the empty zero-assignment argument; complement directions in two-/three-deletion support counts; both top-degree (-1)^3 and (-1)^n signs; Wilson sign ((p-1)!)^3=-1; the exact integer level formula; p=7 parity, and the distinction between an abstract S028 cell-sum system and a complete indexed block family. An *initial plausible but invalid move* was to apply Chevalley–Warning at the three-index boundary; the strict inequality rejects it. This review is by the session executor, NOT external peer review or Lean/Palomar.

**FIRST essential unclosed extension:** derive universal usable constraints on the *value-sensitive* three-colour coefficient Psi(T) and the pair/triple co-degrees strong enough to rule out every complete indexed family m=2p (and later all m=3p,4p,...) OR find a truly different short-extraction route. No cancellation, contradiction, actual indexed lift/counterexample, rank-three equality, or D2<=6p-6 bound has been proved. Route B was not activated after bounded Route A closed and identified the exact first gap. The S024/S025 safe downstream estimate still stops at M+2 with M=3p²-4p-3. A separately established D2<=6p-6 would close the two-position deficit; no such establishment is made here.

## Primary provenance and immutable frontier

The original Bhowmik–Schlage-Puchta 2012 definitive publisher author offprint (SRC-0021), printed pp22–24, PDF page index2 visually inspected fresh in S030: it states the weaker <=(3p-1)/2 rank3 Lem2.1, subsequently prints a stronger <=3(p-1)/2 in the proof without the necessary extra derivation, and says the rank3 Lem2.3 proof is omitted. The local S030 indexed claims are INTERNAL mathematical deductions, not attributed to this source. SRC-0003 remains SOURCE_STATED. Royal Holloway Sheikh2017 doctoral thesis bibliographic page located, but Chapter4/Remark4.3.11 NOT proof-inspected; GHST old C53 original code-output link inaccessible, NEVER RUN; Yiu2026 repeated generator counts remain distinct from unauthenticated independent M1 terminal predicate verification, M2/M3 separate. Five exact-source n15/20/21/28/30 searches retrieved no newly authenticated original exact theorem; irrelevant/empty results are NOT proof of present-day openness.

All 30 original frontier JSON row objects and Markdown table rows (group,D*,bounds,status,full ordered evidence) are preserved exactly; 25 historical source-stated exact/trivial and intervals n15:43..45,n20:58..59,n21:61..63,n28:82..83,n30:88..90. Schmid n6=16, van Emde Boas and Yiu historical SOURCE_STATED; inherited14/17,+5,43/699/5553 quarantined. Phase1 IN_PROGRESS, phases2/3 NOT_STARTED, CAM-0001 PROPOSED/NOT RUNNING/BLOCKED n6=16. No candidate, search, D1/Dk numeric improvement, priority claim, formal certificate, hosted CI PASS, submission or outreach.
