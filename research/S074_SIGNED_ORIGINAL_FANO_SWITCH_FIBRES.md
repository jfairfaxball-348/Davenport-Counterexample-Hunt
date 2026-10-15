# S074 — genuine original-index Fano status-switch fibres and the constant-type saturation obstruction

15 October 2026. Owner invoked **exactly S074** by “run the next session” in the Davenport project, from merged main `0fe98a25377e3319b0bcdebe35a174f7bf06f525`. This is INTERNAL, same-executor, symbolic mathematics. Nothing below is a computation, certified model, universal proof of D(C20^3)=58, or 58-term zero-sumfree counterexample. All existence claims are conditional on the S060 original 59-position canonical configuration and, when stated, on S064 exact12 and S072 no-Fano-triangle.

## 1. Live original data and rigorously limited target

Use G=(Z/20)^3, H=(Z/10)^3, Q=F2^3, the **embedding onto the even subgroup** iota(h)=2h, parity pi:G→Q and lambda:H→C5^3. The torsion subgroups are G[2]=10Q and H[2]=5Q; G is NOT Q⊕H. A hypothetical ORIGINAL total-zero 59-position T consists of 22 indexed actual pairs (a_i,b_i), eight actual q-parity g labels, and seven original parity-distinct singleton labels s_r. Their H pair sums u_i=iota^-1(a_i+b_i) form a zero-sumfree indexed U22. Let N={i:pi(a_i)=pi(b_i)=t_i≠q}. The fixed three q-coset singleton original pairs are (X_j,Y_j), j=1,2,3. Write T_eps for the genuine transversal of three original singleton labels, one per pair, with eps in {000,110,101,011}; its full G sum is even, with iota^-1(sum_G T_eps)=x_eps. ALL S060 q matchings, E(U\\I) multi-splits, outsiders and coupled original x_eps/C/Delta gates are assumed only CONDITIONALLY, NOT proved feasible.

A genuine original torsion witness Z with nonempty mask P⊆N and sum_G Z=10(z_P+u) is proper automatically. Under the exact12 obstruction D_A=a+L,D_B=b+L,D_C=a+b+L (dim L=2), assume S072's **NO three-mask Fano XOR** branch: each colour of P=A,B,C has a unique original singleton status, affine with common chi:L→F2. We attack chi=0 first, without inventing independently selectable D sets.

## 2. CLM-0260 — one SAME-original-data Fano toggle, exact 5Q fibre and the 0-or-2-point bound

Fix ANY genuine torsion witness Z of one supported nonempty mask P. For each of four actual even Fano singleton transversals T_eps define its *signed original* full-G subtotal

    s_eps(Z) = sum_{ell in T_eps} (1-2·1_{ell in Z}) value(ell).

Because signs do not alter quotient parity, pi(s_eps(Z))=0; let tau_eps(Z)=iota^-1(s_eps(Z)) in H.

For **each** of the 22 actual pair indices define the signed full-pair increment in H

    w_i(Z)=iota^-1((1-2·1_{a_i in Z})a_i+(1-2·1_{b_i in Z})b_i).

This is always defined: a_i and b_i have the same parity. Its exact ORIGINAL cases are:

* neither original endpoint in Z: w_i=+u_i;
* both original endpoints in Z: w_i=-u_i;
* only a_i in Z: w_i=iota^-1(b_i-a_i);
* only b_i in Z: w_i=iota^-1(a_i-b_i).

The last two are **even differences**, NOT generally order-two directions. We make NO assumption b_i-a_i=10d_i.

For each B⊆[22] take the ACTUAL original q-only Fano set D_(eps,B)=T_eps ∪ {a_i,b_i : i in B}. It selects one of each of the three singleton coset pairs, splits NO non-q pair, and has even total quotient parity; it is nonempty proper regardless of B. Since its index set is disjointly specified, direct elementwise original XOR accounting gives the full G equality

  sum_G(Z △ D_(eps,B))
    = 10(z_P+u) + 2( tau_eps(Z) + sum_{i in B}w_i(Z) ).       (74.1)

It retains EXACTLY the non-q mask P; its singleton status is h(Z)⊕111. It is automatically proper because P remains split. Thus the status-switched original subset is torsion **if and only if**

    tau_eps(Z)+sum_{i in B}w_i(Z) ∈ 5Q⊂H.                    (74.2)

When (74.2) holds, write the unique element on the left as 5e, e∈Q. Then the new torsion colour is (z_P+u+e), and EXACT12's actual D_P=z_P+L forces e∈L. Uniqueness of S072 affine statuses forces

    chi(e)=1.                                               (74.3)

This is an original-index necessity, not an independent-colour heuristic: the same pair endpoints, same singleton values, original pair full/absent choices, and all original overlaps enter (74.1).

Define the exact **signed Fano fibre**

   K_eps(Z) = ( tau_eps(Z) + Sigma((w_i(Z))_{i=1}^{22}) ) ∩ 5Q,

where Sigma is the set of indexed subcollection sums INCLUDING empty. Then for ALL four coupled eps and EVERY genuine exact12 no-Fano torsion witness Z,

   K_eps(Z) ⊆ {5e : e∈L and chi(e)=1}.                      (74.4)

Therefore if chi=0, **every K_eps(Z) is EMPTY**; if chi≠0, every K_eps(Z) contains at most TWO different elements of H (though many B can represent the same one). Equivalently a single projected-zero switch in chi0, or THREE different 5Q values in chi≠0, conclusively refutes that exact12/no-Fano original configuration. The theorem does NOT assert that such a switch exists for arbitrary zero-free U.

**Proof.** For each selected literal original label ell in D, membership in XOR Z△D replaces its original contribution z_ell x_ell by (z_ell⊕1)x_ell; the difference is (1−2z_ell)x_ell. Sum the three signed singleton and selected two-endpoint pair contributions; iota(τ)=s and iota(w_i)=signed original pair, giving (74.1) in full G. T_eps is even and each full pair is even, hence the increment is even; it belongs to 10Q precisely when its H preimage belongs to 5Q (mod5-zero). On torsion, the exact12 definition of D_P fixes e∈L. At each singleton coset pair T_eps toggles exactly one original endpoint, so h flips in every bit. Original full-pair toggles change neither h nor P. The unique affine rule therefore gives chi(u+e)+beta=chi(u)+beta+1, hence chi(e)=1, and the bound follows. The proof uses original selected indexes and neither a fake splitting of G nor an unproved stabiliser. QED.

**General q-only Fano extension, also proved.** Replace D_(eps,B) with ANY actual even-parity ORIGINAL q-only Fano subset D (allowed q original pair splits, all g/s_q selections and unsplit original full pairs); define Delta_Z(D)=sum_G D−2sum_G(Z∩D). The identical argument shows that if Delta_Z(D) reduces to 0 modulo5, then Delta_Z(D)=10e with e∈L,chi(e)=1. This does not identify the entire general switch family with just four transversals; (74.4) is a rigorous **subfamily** of it, sufficient for exclusion when its 5Q slice is too large.

## 3. CLM-0261 — a rigorous obstruction to chi=0 using indexed projected subset-sum saturation

For Z with non-q split mask P, at every ORIGINAL full unsplit pair i∉P the signed increment above is either +u_i or −u_i. Let U_{¬P} be the 22−|P| original indexed H pair sums (not a guessed new sequence). Define its mod5 subset-sum set S5(U_{¬P})={lambda(sum_{i in B}u_i):B⊆[22]\\P}⊆C5^3.

**Saturation implication (same real original labels).** If S5(U_{¬P})=C5^3 for even ONE supported nonempty P, then the S072 **chi=0** no-Fano EXACT12 branch is IMPOSSIBLE. Indeed for every witnessed Z with mask P and any actual even transversal eps, the signed subset sums from i∉P still cover C5^3, because replacing u_i by −u_i merely translates its {0,u_i} two-point choice set. We can thus choose B⊆[22]\\P making lambda(tau_eps(Z)+sum_{i∈B}w_i(Z))=0, so (74.2) gives a real, proper opposite-status torsion witness, forbidden by (74.4) for chi=0. No use of the split pair increments i∈P, g, s_q or q-pair splits is needed. The implication is **sufficient**, not a statement that all source-conditional U22 saturate.

**Concrete checkable symbolic sufficient condition.** If the projected indexed terms of U_{¬P} include at least four copies of each of THREE linearly independent elements e_1,e_2,e_3 of C5^3, their subset sums contain every c_1e_1+c_2e_2+c_3e_3 (0≤c_i≤4), hence saturate. In m=2, P⊆N has |P|≤2, so a U22 with eight e1 terms, seven e2 terms and seven e3 terms (in H=C10^3 using coordinate basis representatives) retains at least six, five and five respectively after deleting the mask positions. This U22 itself is H-zero-sumfree: every nonempty indexed subset has at least one coordinate count 1..8 or 1..7, so cannot sum to0 modulo10. Thus a non-vacuous family of **genuinely H-zero-sumfree U** obeys the saturation condition. This only RULES OUT a hypothetical no-Fano chi0 exact12 completion with that U; it is NOT a full 59-original-label S060-gated construction, not a contradiction for arbitrary U22, and not a G58 candidate.

**Rank-one projection exclusion, separate and weaker.** Any zero-sumfree length≥20 indexed sequence in H=C10^3 has projected terms spanning at least a 2-dimensional F5 subspace. If all projected terms lay in one F5 line (possibly 0), from any 20 terms extract four successive pairwise disjoint nonempty projected-zero blocks: in C5 every five terms have a nonempty zero-sum subset of ≤5 terms, so after three such extractions at least five original terms remain. Each block's actual H sum belongs to H[2]=5Q; four such sums in rank-three F2 space are dependent, so a nonempty union of blocks has true H sum0, contradicting zero-freeness. In particular, with |P|≤2, U_{¬P} has ≥20 terms and its mod5 *span* has dimension at least2. This DOES NOT imply its subset-sum set is all C5^3. The saturation criterion above is a genuine extra hypothesis, not a hidden consequence of this elementary rank bound.

## 4. CLM-0262 — the FOUR signed original Fano bases remain C/Delta-coupled

Let ~X_i=(1−2·1_{X_i in Z})X_i and ~Y_i=(1−2·1_{Y_i in Z})Y_i in G and ~V_i=~X_i+~Y_i. These are **genuine signed values of the SAME six original singleton labels**, not independently chosen hypothetical Fano line lifts. Signs preserve original quotient parities pi(~X_i)=r_i, pi(~Y_i)=r_i+q, pi(~V_i)=q. Define ~tau_eps=tau_eps(Z). Then the exact S060 four-line calculation applies verbatim:

  ~tau_000+~tau_110+~tau_101+~tau_011
      = overline(~V_1+~V_2+~V_3) in H,             (74.5)

  rho(~tau_ij−~tau_000)
      = rho(iota^-1(~V_i+~V_j))+r_i+r_j in Q             (74.6)

for ij=12,13,23; overline:G→H is coordinatewise reduction modulo10. More explicitly ~V_i=V_i−2 sum_{ell∈Z∩{X_i,Y_i}}value(ell). Hence the signed C and Delta depend on **the actual intersection of the mixed witness with the ORIGINAL singleton endpoints**, not on an independently chosen member of F_*.

**Proof.** Each signed original singleton occurs in exactly two of the four even epsilon transversals. Their four G sums total 2Σ~V_i; dividing through iota into H yields reduction modulo10, proving (74.5). Subtract the (000) signed transversal from the (ij) transversal: only the two selected endpoint choices flip, giving ~V_i+~V_j−2~X_i−2~X_j in G. The H quotient followed by rho yields (74.6) because reduction of signed ~X_i modulo2 is r_i. QED.

**Important negative conclusion.** The four slices K_eps(Z) from (74.4) are coupled through these SAME six original signed singleton values and the SAME 22 original signed pair increments. It is unsound to choose four arbitrary tau, four arbitrary 5Q escape values, or independent C/Delta data. Conversely (74.5)/(74.6) alone do NOT force any K_eps(Z) to be nonempty: the mod5 subset-sum geometry remains the missing step.

## 5. Aggressive bridge audit and failed universality attempts

* **Constant chi priority:** (74.4) converts *all* Fano opposite-status attempts into explicit projected-zero exclusion against SAME original data, and (74.5)/(74.6) couples the four bases. The claim “every length22 H-zero-free U saturates C5^3 after any relevant mask removal” is NOT established. The elementary span≥2 lemma is too weak; do not conflate span and subset-sum coverage.
* **Nonconstant chi:** Three distinct 5Q values in one signed fibre would contradict its two-point affine allowance. But an arbitrary 22-term signed sequence is NOT proved to yield such a slice; all 12 S073 true within-mask Fano XOR tests remain q-only NONZERO tests, not forced zeros. The new 5Q two-point bound can be tested against them only with their exact original intersections.
* **General legal supports:** The signed increment w_i(Z) is defined for ALL original pair indices, including split ones, without assuming b_i−a_i∈10Q. It becomes a torsion generator only under the stronger original equality b_i−a_i=10d, as S066 required. An indexed projected-zero U block can be toggled without changing its simple ±u contribution only if disjoint from the original split indices; otherwise the signed w_i, not u_i, is required. We did NOT silently switch q splits or independent original outsiders in (74.4).
* **Triangle/majority route:** Fano status switching creates an actual new original torsion witness only when the mod5-zero signed equation holds. It does not force the S070 three-witness XOR to be proper, or its majority to have even parity. The valid nonzero order-four escape remains. Neither the exact12 original carry nor the S060 q-gate is globally contradicted.
* **Hostile 59-label route:** No fully labelled all-q S060-gated 59-element total-zero G instance is exhibited. No S059 matching-only slab is recycled as a survivor. No first non-q proper G-zero/complement is invented.
* **Other cover and hub obligations:** FULL8, no-full 13/14/≥15, m0/m1/m2/m≥3, all 26 q hubs, three-hub alternatives and P26 (0,4)/(0,6)/(1,7) remain OPEN. The present exact12/no-Fano deduction does not settle these. SOURCE_STATED D2(C5^3)=20 and D3 historical values retain original provenance.

## 6. Outcome and honest next bridge

CLM-0260–0262 are INTERNAL conditional mathematical deductions, with explicit original-labelled proofs; all apply only on the frozen source-conditional G59/exact12 hypotheses where stated. They replace the “independent A_(P,h)” dead end by the **same-data signed four-Fano fibre** obstruction: for every actual torsion witness Z and four actual signed Fano basepoints, forbid a nonempty 5Q fibre if chi0, or a fibre with >2 points if chi≠0. A broad, explicitly zero-free U class rules out chi0 **conditionally**, but NO universal real U22/S060 theorem forces saturation or a >2-point fibre.

Therefore Phase1 remains IN_PROGRESS. No proof/refutation of the Davenport rank-three conjecture, no D(C20^3)=58, no zero-sumfree 58-term original sequence, no certified/fully gated 59-original hostile construction. No mathematical numerical search, CAS/SAT/ILP, candidate/orbit generation, historic code, Lean, Palomar, campaign, publication, or outreach; no source promotion. Claims259→262, 29 source objects and original30 frontier rows retained, hosted CI ABSENT_NOT_PASS, hostile review internal same executor.

For S075, **force a signed 5Q fibre contradiction from S060 global constraints across real m2/exact12 status witnesses**, or find an actual fully labelled S060-gated hostile G59 with first original zero. Do not assume global saturation or turn a conditional fibre theorem into a global n20 proof.
