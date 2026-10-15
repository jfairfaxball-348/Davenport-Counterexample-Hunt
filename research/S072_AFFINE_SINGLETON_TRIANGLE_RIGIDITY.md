# S072 — sixteen actual mixed-status zero-colour triangles: affine rigidity, stabilisers and the m=2 majority dead end

15 October 2026. Owner invoked exactly S072 by "Run next session" in Davenport project. Internal same-executor Phase 1 **symbolic** mathematics, not external peer review or proof of the Davenport conjecture. There was no numerical mathematical search, CAS/SAT/ILP, generated candidate/orbit enumeration, Lean/Palomar or campaign. Every witness below is an actual ORIGINAL subset of the **hypothetical** source-conditional 59-labelled canonical total-zero sequence T in G=(Z/20)^3; no claim such a fully S060-gated T is constructed.

## 1. Frozen original-index setting and real colours

Keep S060/063/064/065/066/069/070/071 definitions. Original T has 22 pairs (a_i,b_i), eight g_j of quotient parity q, and seven individually labelled singletons s_r, r∈Q\\{0}; H=(Z/10)^3, Q=F2^3, pi:G→Q, V=Q/<q>. Let N={i:pi(a_i)=pi(b_i)=t_i≠q}; m=|N|. In the three q-coset singleton pairs (X_j,Y_j), h_j(Z)=1 exactly when the ORIGINAL Z selects precisely one endpoint. For an actual G[2] torsion witness with non-q mask M, the S071 quotient identity is R(h)=Phi(M), and the two admissible original singleton status patterns differ by 111. The full S060 q-only H28/Fano/E(U\\J) gate is assumed only conditionally.

Consider the **EXACT12** obstruction of S064 with genuinely witnessed nonempty masks A,B,C=A△B and four original torsion colours each:

D_A=a+L,  D_B=b+L,  D_C=a+b+L,  dim_F2 L=2.

By S070, for EVERY pair u,v∈L the colours a+u, b+v, a+b+u+v admit actual ORIGINAL witness choices Z_A,Z_B,Z_C and their sum in G is 10((a+u)+(b+v)+(a+b+u+v))=0. Thus there are sixteen ordered zero-colour **colour triangles**; possibly multiple original witness triples per colour triangle. Their actual XOR X has non-q mask empty, and h(X) is 000 (grouped) or 111 (Fano and automatically nonempty proper) by S071.

## 2. CLM-0255 — exhaustive support-type affine rigidity, with real original witnesses

**Theorem.** Choose any permitted singleton status representatives h_A^0,h_B^0 with R(h_A^0)=Phi(A), R(h_B^0)=Phi(B), and define h_C^0=h_A^0⊕h_B^0⊕111. Then R(h_C^0)=Phi(C), and h_A^0⊕h_B^0⊕h_C^0=111. For P∈{A,B,C}, write H_P(w)⊆F2 for the **actually witnessed** statuses of colour w: eta∈H_P(w) iff some original nonempty proper torsion witness Z of mask P and sum 10w has h(Z)=h_P^0⊕eta·111. H_P(w) is nonempty for w∈D_P, but can a priori be either singleton or {0,1}.

Either

(i) there is a genuine colour-zero original witness triple whose XOR is in the TRUE Fano stratum h(X)=111 (and is automatically nonempty proper), **or**

(ii) EVERY one of the twelve supported mask-colour classes has a UNIQUE eta status; writing the singleton functions f_A(u),f_B(v),f_C(w) for their respective coset coordinates in L, there is a COMMON linear functional chi:L→F2 and constants beta_A,beta_B,beta_C∈F2 with beta_A⊕beta_B⊕beta_C=1 such that

 f_A(u)=chi(u)⊕beta_A,
 f_B(v)=chi(v)⊕beta_B,
 f_C(w)=chi(w)⊕beta_C

for ALL u,v,w∈L. In case(ii), ALL sixteen actual colour-zero triangles are forced to have grouped h(X)=000 (including possible empty/full X). The support-type projection of the no-Fano possibility has exactly four chi choices times four beta triples, i.e. sixteen formal patterns once reference statuses and affine coset origins are fixed. This counts formal status rules, **NOT** 59-labelled models or original feasibility.

**Proof.** If a fixed supported colour w of any mask has both actually witnessed statuses, hold arbitrary genuine witnesses for the other two masks at the unique complementary zero-colour values fixed; replacing only the chosen witness changes h(X) by 111. One of the two XORs is h=111, proving (i). Consequently failure of (i) implies all H_P(w) are singletons. For u,v∈L, choose actual witnesses; original XOR signature equals

 h(X)=111⊕(f_A(u)⊕f_B(v)⊕f_C(u+v))·111.

As h(X)∈{000,111}, it is grouped in every triple precisely if

 f_A(u)⊕f_B(v)⊕f_C(u+v)=1                         (S72.1)

for all u,v. Substituting v=0 and u=0 into (S72.1) gives

 f_A(t)⊕f_A(0)=f_B(t)⊕f_B(0)=f_C(t)⊕f_C(0)=chi(t).

The full functional equation then yields chi(u+v)=chi(u)⊕chi(v), so chi is linear and the three base values have XOR1. Conversely these formulas imply (S72.1) for every u,v. Every step uses **real original witnesses for each supported colour**, not independent Fano supports or invented mod5 values. QED.

**Distinct-class m=2 specialisation.** If N={1,2} with [t_1] and [t_2] distinct in V, choose h_A^0=100,h_B^0=010,h_C^0=001 for A={1},B={2},C={1,2}. In the no-Fano case the one-/two-split type functions (eta=0/1) MUST be affine with the same chi and odd total beta. The examples eta_A=0, eta_B=0, eta_C=1 at all four colours give a formal always-grouped pattern. It is compatible with the quotient constraints but **is not** a full original G59 model. Complementing a witness and non-q 10theta paired gauges leave h invariant, and cannot create a missing status.

## 3. CLM-0256 — actual original-index subgroup symmetries annihilate the affine slope

Recall the *conditional genuine* S066 stabiliser W_P≤Q: directions d_i from split ORIGINAL endpoint differences b_i−a_i=10d_i when i∈P, and e_i from complete unsplit ORIGINAL pairs u_i=5e_i when i∉P, span W_P. There is NO claim every same-parity endpoint difference lies in 10Q. For every such available generator, S066's explicit original operation transforms ANY actual torsion witness of mask P and colour w into a witness of colour w+generator, changing no singleton positions. Therefore it preserves h exactly, and W_P≤L in an exact12 model.

**Theorem.** Under CLM-0255 alternative(ii), the common chi must satisfy

 chi(w)=0 for every w∈W_A+W_B+W_C.               (S72.2)

In particular if the SUM of genuine original stabilisers spans all L, then chi=0; all three mask supports must have CONSTANT singleton status types across their own four colours, with odd XOR of the three constants. Thus any witnessed status ambiguity, or any measured NONconstant support-type behaviour that violates (S72.2), FORCES a genuine proper Fano XOR triangle. This is not a full zero-sum collision.

**Proof.** For each P and generator d/e of W_P, the original endpoint switch/full-pair toggle preserves actual singleton support and sends any witness at w to another at w+d/e. Under alternative(ii) each colour has a unique support type, so f_P(w+d/e)=f_P(w). Since f_P=chi+beta_P, we have chi(d/e)=0. Span and linearity give (S72.2). If the stabilisers span L then chi=0. QED.

**More local endpoint agreement audit.** In m=2, pair1 is split by A and C, pair2 by B and C. Let d1,d2 be genuine nonzero order-two endpoint differences when available. Switching the selected original endpoint at one such split in one witness translates only that witness's torsion colour by d_i, leaving its h status fixed. To preserve the zero-colour equation, a collection of switches must have total d-weight zero. If d1,d2 are linearly independent, the number of endpoint flips across the TWO splitting witnesses of EACH i is even, so their same-endpoint/opposite-endpoint relation is unchanged. Therefore the S070 majority mask E(K) is INVARIANT under all colour-zero-preserving operations consisting solely of these four split-endpoint switches. If d1,d2 are dependent, compensation can mix the two pairs, so the assertion requires independence. No other witness reselection is claimed covered.

This is a distinct, scope-limited gauge NO-GO: even available local original index flips cannot generally repair the desired majority support while holding zero colour; it does not establish a fourth mask, mod5 zero, or majority parity.

## 4. CLM-0257 — exact m=2 has no fourth non-q majority mask to discover

**Theorem.** In a genuine m=2 exact12 triangle, after relabelling A={1}, B={2}, C={1,2}. For ANY actual three witnesses (not necessarily zero-colour), the S070 majority original subset K has non-q split mask E(K)⊆{1,2}. Hence E(K) is **one of** empty,A,B,C. In particular the S070 proposed route "prove K∈G[2] with a FOURTH new non-q mask" is categorically IMPOSSIBLE for m=2: the required fourth nonempty non-q mask does not exist. This does NOT say K cannot be torsion; nor does it refute exact12.

**Proof.** By S070's actual-index majority theorem, E(K) consists only of those original i split by precisely two of Z_A,Z_B,Z_C that pick the same original endpoint. Their mask union is A∪B={1,2}; its only nonempty subsets are exactly A,B,C. QED.

**Sharper practical comment.** For a zero-colour triple with nonempty proper X, the q-only gate and sum_G(X)=−2sum_G(K) already prohibit sum_G(K)∈G[2], independently of the majority mask: if K were torsion, 2sum K=0 and X would be an actual forbidden q-only zero. For X empty/full the q gate supplies no such contradiction. Thus attempting to force a genuinely new mask is not a hidden substitute for proving properness and the carry, especially when m=2.

## 5. Direct attack on the remaining original mod5 carry; unsuccessful routes

For an actual colour-zero triple define K=majority and X=XOR. The exact original-G identity, NOT any artificial splitting G=Q⊕H, is sum_G(X)=−2sum_G(K). Reduce modulo5:

 lambda_G(sum X)=−2lambda_G(sum K).                  (S72.3)

Consequently projected-zero X is equivalent to projected-zero K, but parity-even K is still independent data. If X is a true Fano transversal and projected zero, the S060 gate makes sum X a NONZERO element of 10Q and forces sum K to have order four with odd quotient parity (S070). Nothing in the unique/affine support-type theorem controls sum K modulo5: h records only how many of each ORIGINAL singleton coset pair are split, not the coordinates of the original selected values or their majority overlaps.

- **All sixteen triangles:** They yield only sixteen forced torsion-colour equations, not sixteen equations on intersection/majority full-G values. The rule chi/beta is a consistent **formal support colouring**; the constant case gives an explicit parity-level escape with every triangle grouped. The q-hub gate forbids zero sums of proper grouped XORs but does not ban grouped XORs themselves.
- **S060 F_*, true C and Delta:** They constrain q-only exact sums and four TRUE even-Fano positions. They do not by themselves grant re-selection of a mixed mask's singleton signature without changing the actual mod5 sum and other original membership. No complete proof converting the full S060 prerequisites into an affine-type contradiction was found.
- **Independent endpoint switches:** When their genuine order-two directions span L, chi must be constant, but constants beta_A⊕beta_B⊕beta_C=1 remain possible at the quotient/support-projection level. The local zero-colour switch orbit can preserve the majority mask. Hence no unconditional forcing of the Fano branch, let alone of lambda_X=0 and pi_K=0.
- **FULL8:** A single fully dangerous mask D_M=Q need not give any A/B/C triangle; one h status per colour could remain constant. The exact12 affine theorem does NOT eliminate FULL8.
- **13/14/≥15 no-full covers:** A twelve-subcover may exist (S067) but extra actual dangerous colours/masks need not be absent, so neither an exact12 conclusion nor a new contradiction follows. For m≥3 the fourth-majority-mask route remains logically available but unforced.
- **Global cases:** m0/m1/m2/≥3, all 26 q hubs, three-hub and alternative P26 profiles require independent work. No one may promote source-stated D2(C5³)=20 or computational historical sources to programme proved.

## 6. Hostile original-labelled 59-element alternative: not achieved

A genuine hostile route would provide all 22 ORIGINAL pairs + 8 g + 7 singletons (59 labels), actual total0 in C20³, U22 H-zero-free, every q matching/E(U\\I), all 2048 outsider transversals, the four actual x_epsilon with full C and Delta and all proper complements; then identify a first non-q exact zero original subset. Neither a constant formal support colouring, an abstract cover, nor S059's q-matching-only nonminimal example passes that specification. NO such labelled original sequence was constructed in S072; no G58 zero-sumfree witness or D(C20³)=58 proof.

## 7. Verdict and exact next bridge

CLM-0255–0257 are INTERNAL PROGRAMME_PROVED, as conditional original-index implications of the source-conditional S060 canonical/exact12 framework. No mathematical search, new source examination, numerical theorem, external check, hosted CI pass or certification. Sources29 and the immutable original30 frontier are unchanged; Phase1 IN_PROGRESS. The stronger remaining exact12 target is now: **eliminate every actual affine-compatible singleton-support assignment (including constant chi=0), OR construct a proper Fano zero-colour XOR and force the ORIGINAL majority to be both C5-projected zero and parity-even**. The latter conditions are prohibited by the S060 q-only gate and would finish exact12. For m=2 discard the impossible fourth-mask route. Full8/13+ and global profile gates remain untouched.
