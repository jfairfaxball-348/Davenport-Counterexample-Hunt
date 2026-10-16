# S093 — the shared-original non-q/Fano rectangle bridge and its exact boundary

**16 October 2026. INTERNAL SAME_EXECUTOR, HAND MATHEMATICS ONLY.** Entry remote main b808c846e564124520f634b5a9f86f431a899d31; entry Git root tree *reconstructed*, not independently retrieved, as b3324ac24fa424fd4e9716f318a6cd28f0006581 using the historically recorded S091 tree plus the 19 S092/current prompt blobs. The session attempts the S093 owner's original-index incompatibility, NOT another projected multiplicity campaign. The result below is a genuinely original-index, signed, coupled necessary forcing criterion but NOT the universal incompatibility theorem and NOT a new 58-term zero-sumfree counterexample.

## 1. Hypotheses; retain all 59 actual indices

Let G=(Z/20Z)^3, H=(Z/10Z)^3, Q=F2^3. The homomorphism \iota:H→G sends h↦2h, with image 2G. Write \rho:H→Q for reduction modulo 2 and \bar z for the image in H of any z∈G by reduction modulo10. Importantly there is **no** assumed splitting G=Q⊕H.

Work with a *single* source-conditional S060 59-index object T: 22 genuine, disjoint, original pairs (a_i,b_i) with \pi(a_i)=\pi(b_i)=t_i≠0 and u_i=\iota^{-1}(a_i+b_i)∈H; eight distinct original g_j of parity q≠0; one original singleton s_r for every r∈Q\{0}; and total original sum 0. The 22 indexed U terms are H-zero-sumfree if T has no proper original zero. Let S=s_q. For a chosen q and r_1,r_2 independent modulo q, set r_3=r_1+r_2 and X_l=s_{r_l}, Y_l=s_{r_l+q}, V_l=X_l+Y_l for l=1,2,3. Distinct s_r are distinct *indices* even when their G values coincide. Four actual q-avoiding Fano triples are

L_0=(X1,X2,X3),  L_12=(Y1,Y2,X3),
L_13=(Y1,X2,Y3), L_23=(X1,Y2,Y3).

All four have even parity in G, so x_e=\iota^{-1}(sum_G L_e)∈H. Every pair of Fano triples intersects in exactly one of the six original singleton indices, and each of those six indices occurs in precisely two Fano triples. This is the edge-incidence graph K4 on the *same* six original positions, not four independently chosen Fano values. The known S060 constraints are sum_e x_e=\overline{V1+V2+V3} and three prescribed mod2 differences; these remain mandatory.

For any indexed deletion U\i of one actual complete pair, define
E_i=H \ { -sum_{j∈B}u_j : B⊆[22]\{i} }.
No q group, pair endpoint, singleton or Fano line is freely regenerated in this session.

## 2. CLM-0326: the two-real-Fano/four-real-endpoint rectangle

Fix a genuinely non-q pair index i with t=t_i≠q. Exactly one original singleton s_t occurs among the six X_l/Y_l. Let l be its q-coset; write s_t^\vee for its genuine mate in {X_l,Y_l}. Let {j,k}={1,2,3}\{l}. Of the FOUR even Fano triples, exactly TWO, say L_e and L_f, omit the physical original index s_t. Both contain s_t^\vee, and their choices in q-cosets j and k are complementary. Consequently, as identities of genuine G-original sums,

    sum L_e + sum L_f = 2 s_t^\vee + V_j + V_k.       (2.1)

This statement is independent of which of X_l,Y_l equals s_t. Put

    K_t = \overline{s_t^\vee}+\iota^{-1}(V_j+V_k) ∈ H,
    sigma_a = \iota^{-1}(a_i+s_t),   sigma_b=\iota^{-1}(b_i+s_t),
    delta_i = sigma_b-sigma_a = \iota^{-1}(b_i-a_i),
    lambda_t = x_f-x_e ∈ H,
    c_i = u_i+\overline{V_l}+\iota^{-1}(V_j+V_k) ∈ H.      (2.2)

All halves in (2.2) are legitimate: a_i,s_t have the *same* parity t; b_i-a_i is even; V_j+V_k is even. From (2.1),

    x_e+x_f=K_t,    sigma_a+sigma_b=u_i+\overline{s_t},
    rho(delta_i)=rho(u_i)+t.                          (2.3)

The final parity formula follows exactly from delta_i=u_i-\overline{a_i} in H; it does not assume freely selectable endpoint torsion. In particular, the Fano difference parity is rho(lambda_t)=rho(K_t). Do NOT blindly substitute the baseline S060 Delta_jk: if s_t=X_l, the two omitted-line transversals have an oppositely oriented pair of switches and the extra q parity matters.

**Theorem (actual four-corner gate).** Absence of a proper original zero forces all four values

    y_ea=x_e+sigma_a,   y_eb=x_e+sigma_b,
    y_fa=x_f+sigma_a,   y_fb=x_f+sigma_b

to lie in E_i. These are the four corners of **one common** parallelogram

    y, y+delta_i, y+lambda_t, y+delta_i+lambda_t ∈ E_i,       (2.4)

where y=y_ea, and their opposite diagonal sums satisfy the same literal H identity

    y_ea+y_fb = y_eb+y_fa = c_i.                             (2.5)

In particular the following **single exact mixed original-index compatibility set** must be nonempty:

    R_i = { y∈H :
          2y=c_i-delta_i-lambda_t,
          y,y+delta_i,y+lambda_t,y+delta_i+lambda_t∈E_i }.   (2.6)

If R_i is empty, T has an EXPLICIT nonempty proper original zero subset (though its choice depends on which of four corners fails). This is a true hand-proved forcing criterion valid for every U22 and every source-conditional canonical 59-index object, not only the axial U*.

**Proof with the actual subset.** Select one of the two actual Fano triples L_e/L_f, one endpoint alpha=a_i/b_i from the actual pair i, and the one actual unused singleton s_t. The first three indices are disjoint from s_t by construction; alpha belongs to a separate original pair. Parity is 0+t+t=0, and the true H half-sum of these FIVE original indices is x_e+sigma_alpha or x_f+sigma_alpha. Given any B⊆[22]\{i}, adding BOTH original endpoints of every full pair indexed by B changes the H half-sum by sum_B u_j. If a displayed corner is absent from E_i, by the definition of E_i one such B has sum_B u_j equal to minus that corner. The literal original subset

    L_e or L_f  ∪ {s_t,alpha} ∪ ⋃_{j∈B}{a_j,b_j}              (2.7)

then has G-sum 0. It uses 5+2|B| original positions with 5≤5+2|B|≤47<59 and is nonempty and proper (the original mate of alpha is omitted). It reuses NO singleton and NEVER the full12/full59 original support. Thus no-proper-zero implies four E_i memberships.

The identities y_eb-y_ea=delta_i and y_fa-y_ea=lambda_t are literal equalities in H. By adding diagonals and using (2.3),
y_ea+y_fb=(x_e+x_f)+(sigma_a+sigma_b)
=K_t+u_i+\bar{s_t}
=u_i+\overline{V_l}+\iota^{-1}(V_j+V_k)=c_i;
same for the other diagonal. Equations (2.4)–(2.6) follow. Conversely, (2.6) characterises precisely the four stated E_i restrictions for these *fixed* shifts; it is NOT equivalent to the absence of all original zero subsets or to global S060 feasibility. QED.

**Algebraic audit of the finite fibre (NOT a numerical search).** Multiplication by 2 on H has kernel 5Q={0,5}³, size exactly eight. Thus 2y=c_i-delta_i-lambda_t has no solutions unless its right side lies in 2H, and otherwise has exactly eight possible solutions related by 5Q. For *genuine labelled* data the consistency condition automatically holds because y_ea exists; the unresolved gate is whether its eight algebraically permitted shifts contain any full four-corner E_i rectangle. These are at most eight shared torsion possibilities, not four independent Fano witnesses or 2048 independent outsider masks. No enumeration was run.

## 3. CLM-0327: one actual Fano pair must satisfy EVERY non-q pair of its parity class

For each t∈Q\{0,q}, let N_t={i : t_i=t}. The same actual singleton s_t, the same two omitted Fano lines L_e(t),L_f(t), and their same H values x_e,x_f are used for *every* i∈N_t. Define

    Omega_t = ⋂_{i∈N_t} [(E_i-sigma_{i,a}) ∩ (E_i-sigma_{i,b})] ⊆H.  (3.1)

When N_t=∅ take Omega_t=H. Theorem (2.4) gives the **simultaneous original-index condition**

    x_e(t), x_f(t) ∈ Omega_t,
    x_e(t)+x_f(t)=K_t,
    hence Omega_t∩(K_t-Omega_t) ≠∅ whenever N_t≠∅.          (3.2)

If Omega_t∩(K_t-Omega_t)=∅ for some t with N_t nonempty, a specified one-split original zero (2.7) exists. This is an *honest conditional forcing theorem* simultaneously using all pairs of a given parity class and the fixed, physically shared six singleton indices. It does NOT license choosing an independent element of Omega_t for each i, or an independent pair of Fano values for each t. A hypothetical full T must satisfy (3.2) for all six non-q parities with the SAME four values x_0,x_12,x_13,x_23, plus the full S060 C/Delta, split-q, signed multi-non-q, and 26-hub constraints. There is NO claim that one of these intersections is always empty.

**The direct original-index bridge as a precisely unproved statement.** The attractive sufficient statement

    For every S060-q-gated genuine axial T with U*=e1^8e2^8e3^6
    and N≠∅, some nonempty N_t has Omega_t∩(K_t-Omega_t)=∅      (OPEN)

has NOT been established and may be false. Even if it were proved, the N=∅ canonical case and all alternate U22/P26/hubs would still require separate work. The theorem proved in this section is the exact implication (3.2), not the displayed universal emptiness hypothesis.

## 4. CLM-0328: axial sumset obstruction fails; the true bridge needs the four corners

Set U*=e1^8 e2^8 e3^6 in H, the same conditional original axial profile studied in S080–S092. Deleting ANY one indexed u_i leaves at least seven copies of e1, seven of e2, and five of e3 (the actual count is 7/8/6, 8/7/6 or 8/8/5). Therefore E_i contains **both entire affine coordinate planes**

    P1={h∈H:h1=1},    P2={h∈H:h2=1}.                           (4.1)

Indeed a subset sum of the remaining e1 terms is k e1 for 0≤k≤8; its negative first coordinate can never be 1 (that would require k=9). Same for e2. Thus for ANY c=(c1,c2,c3)∈H,

    (1,c2−1,0)∈E_i,   (c1−1,1,c3)∈E_i,
    and (1,c2−1,0)+(c1−1,1,c3)=c.

Hence

    E_i+E_i=H                                                    (4.2)

for every deleted index i. The weak condition c_i∈E_i+E_i is automatically true, even for a full real original 59-index configuration. **A strategy that treats the two diagonal values independently and hopes their fixed total is forbidden cannot close the axial case.** The difference-constrained rectangle (2.4) and original Fano K4 incidence are essential.

Likewise 5Q∩E_i=∅: for every z∈5Q choose five ACTUAL remaining full U pairs in each coordinate with z-coordinate 5, none for coordinate 0. Their H sum is z=−z. Thus any one of the four genuine five-original mixed base sums landing in 5Q produces the concrete zero (2.7) using those very complete pairs. This is a correct *conditional literal witness*, not proof that such a base is universally forced. It shows a sum-and-torsion escape must be confronted, rather than counting projected Fano members.

These two statements are exact hand algebra for the source-conditional U*. No computation, search, CAS, SAT, Lean or independent certification was used.

## 5. Attempts at the main S093 incompatibility, and where each stopped

**Attempt A: q projection to mixed Fano.** S082–S092 remove sixfold or higher projected fibres for twelve physically distinct q supervertices. Those q constraints by themselves depend on each *whole* V_l=X_l+Y_l and on g_j and U*, not on the allocation X_l versus Y_l. The rectangle depends on s_t^\vee, individual a_i/b_i, and x_e/x_f. The strongest valid transfer is the simultaneous condition (3.2), not a claim that the q-fibre cap determines an empty Omega_t. No such forcing identity was obtained.

**Attempt B: independent diagonals.** Equation (2.5) initially suggests showing c_i∉E_i+E_i. Section 4 proves this entire route is impossible for the axial U*: the sumset is all H. It is a mathematically closed *negative* route, not a general forcing theorem.

**Attempt C: free x_e assignments.** The four Fano triples form a K4 incidence graph on the same six original labels. The two omitted-line pairs vary with t; one may not choose x_e separately for different t, and the S060 sum/parity constraints remain. Equation (3.2) supplies a necessary joint test, but no theorem forces one of the six t classes to fail, even assuming the S092 multiplicity≤5 statement.

**Attempt D: torsion completion.** The scalar equation 2y=c−delta−lambda has exactly an eight-element 5Q fibre when soluble. Axial U deletion has E_i disjoint from 5Q but not from all eight translates of an arbitrary base. No argument forces one of the four corners to land in 5Q, nor makes all eight fibre representatives fail E_i. We did not silently apply a mod5 zero to conclude a mod20 zero.

**Attempt E: original non-q multi-splits.** The new five-index construction uses precisely one split pair. S065 CLM-0232 describes every non-q split mask and arbitrary extra q splits via E(U\I). One-split rectangles are a *strict subset* of those true masks, not a replacement. FULL8, exact12, 13/14/15+ and all 26 hubs may present witnesses invisible to (3.2). No count or covering rigidity was promoted to a contradiction.

**Attempt F: arbitrary U22/P26.** Sections 2–3 are formally valid for every U22 under the S060 22+8+7 source-conditional profile. Section4's surjective sumset conclusion uses ONLY axial U*, and does not say arbitrary E(U\i) is broad. No proof reduces all G59 to S060's canonical profile, or every canonical U22 to U*. Alternate profiles (0,4),(0,6),(1,7), three-hub configurations, and unrestricted T∈G^59 remain outside any claimed theorem.

**Result type**: the universal forcing bridge is **UNPROVED**. No hand-parametrised actual 59-original jointly passing ALL q/H/Fano/2048/non-q/multi-split/hub gates was produced; hence no Outcome-B fully coherent obstruction model is claimed either. The precise new missing bridge is to prove a literal emptiness in the common-original intersection (3.2), or to combine this indexed rectangle with exact E(U\I), weighted XOR carries, and the six shared X/Y labels to produce a *specified* proper zero for every genuine configuration.

## 6. Coverage / non-promotion table

| Original obligation | Rigorous mechanism available | Full incompatibility at S093 |
|---|---|---|
| Projected F5 twelve genuine q groups, axial multiplicity | S082–S092 conditional fibre≤5, INTERNAL | OPEN for all twelve; no projected shadow promoted |
| H10 even genuine q supports / all-matchings | S059/S060 exact atom gate, source-conditional | OPEN globally |
| Four SAME-original Fano x values; C/Delta | S060 CLM-0222 exact realisation; S093 actual K4 identity (2.1) | OPEN globally |
| 2048 original outsider masks | S060 CLM-0221 precise canonical criteria | OPEN universal exclusion |
| q split I, alpha, E(U\I), including multi-splits | S060 exact criteria | OPEN universal exclusion |
| Signed non-q original one-split | S065 exact mask theorem, S093 four-corner and shared-parity-class forced tests | CONDITIONALLY PROVED tests; universal exclusion OPEN |
| Signed non-q multi-splits and weighted original overlap carries | S065–S074 partial exact identities | OPEN |
| All 26 hubs and three-hub interactions | historical alternative hub obligations | OPEN |
| FULL8, exact12, 13/14/15+ torsion masks | S064–S070 covering consequences at specified scope | OPEN as actual common-original contradiction |
| Arbitrary U22, alternate P26 | only S093 rectangle applies if canonical hypotheses hold | OPEN |
| Unrestricted total-zero original 59-term G20 and D(C20³)=58 | none | OPEN / UNPROVED |
| Zero-sumfree G58 counterexample | no constructed sequence | NONE |

All 29 source records, original 30 frontier rows and prior proofs are frozen. Programme status stays Phase1 IN_PROGRESS/HOLD; CAM-0001 PROPOSED / NOT RUNNING / BLOCKED; Phases2/3 NOT_STARTED; Phase4 OWNER_GATED. The three new claims are INTERNAL same-executor hand results **only** at their exact quantified scopes, not certification and not a solution of the rank-three Davenport conjecture.
