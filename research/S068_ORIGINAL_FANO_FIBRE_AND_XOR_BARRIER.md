# S068 — True original Fano fibres and the endpoint-orbit XOR barrier

14 October 2026. Sustained symbolic Phase-1 original-index investigation, INTERNAL SAME_EXECUTOR. **No** universal proof of D(C20^3)=58, no zero-sumfree 58-term sequence and no fully S060-compatible 59-term hostile model. No numerical mathematical search, CAS/SAT/ILP, candidate/orbit enumeration, source-code execution, Lean/Palomar, campaigns or publication. Claims CLM-0241–0243 are conditional ORIGINAL-INDEX lemmas, not an exhaustion of the conjecture.

## 1. Genuine 59 labelled positions, notation, source limits

G=C20^3, H=C10^3, Q=F2^3; iota(h)=2h in G. Write rho:H→Q for reduction mod2, lambda:H→C5^3 for reduction mod5; ker(lambda)=5Q. **Do not** replace G by a false direct sum of Q and H. Let the 59 original indices be (a_i,b_i), i=1,...,22, eight q-parity g_j and seven original singleton s_r for all r≠0 in Q. All original pair parities t_i=pi(a_i)=pi(b_i) are nonzero, all u_i=iota^{-1}(a_i+b_i) make U22 zero-sumfree in H, and sum_G(T)=0. Fix q≠0 and all actual S060 q-matchings, q-selected single/multi-splits with **E(U\\I)**, mixed odd g tests and four genuine Fano values, as a **conditional assumption**, not an existence theorem. N={i:t_i≠q}, m=|N|; for each nonempty M⊆N, D_M⊆Q is the actual set of torsion colours v from nonempty proper original subsets splitting exactly non-q pair indices M, with full-G sum 10v. The fixed q-only gate excludes a proper zero with M=empty. Non-q torsion pair-gauges survive iff theta(M)∉D_M for every nonempty M.

Seven original singleton values are indexed as S=s_q, X_k=s_{r_k},Y_k=s_{r_k+q}, k=1,2,3, r1+r2+r3=0. The four **actual** even Fano original triples L_eps select X/Y by eps=000,110,101,011; their true H values are x_eps=iota^{-1}(sum_G L_eps). Set C=overline(V1+V2+V3) in H, V_k=X_k+Y_k; S060 proves sum_eps x_eps=C and rho(x_ij−x_000)=Delta_ij, where Delta_ij are fixed from the **actual** V and singleton quotient labels.

## 2. CLM-0241 — Endpoint torsion directions are *locked* by U and original parity

**Theorem.** Fix an original pair (a_i,b_i) with equal parity t_i∈Q, and its genuine H pair sum u_i. If its full-G endpoint difference is b_i−a_i=10d_i for d_i∈Q, then

    d_i = rho(u_i)+t_i   in Q.                               (1)

In particular no nonzero order-two endpoint direction is freely assignable after fixing BOTH t_i and u_i. For a given u_i,t_i the torsion endpoint condition is equivalent to the reduction of a_i modulo5 equalling the reduction of u_i modulo5; when this holds the unique d_i is (1). These are genuine labelled original constraints and remain unchanged under S063 simultaneous 10theta twists of both endpoints.

**Proof.** The two original congruences a_i+b_i=2u_i and b_i=a_i+10d_i in C20^3 imply 2u_i=2a_i+10d_i. Under the canonical H→2G isomorphism, dividing this EVEN congruence by two gives u_i=overline(a_i)+5d_i in H, where overline(a_i) is reduction mod10. Taking rho gives rho(u_i)=pi(a_i)+d_i=t_i+d_i. This is (1). Conversely b_i=2u_i−a_i always, so b_i−a_i=2(u_i−overline(a_i)) in G. It lies in G[2]=10Q iff u_i−overline(a_i)∈5Q in H, iff lambda(overline(a_i))=lambda(u_i). Then the unique difference is 10(rho(u_i)+t_i). All calculations originate in full G, with no division of odd G elements by two. Changing both original endpoints by 10theta leaves their sum and difference unchanged, because 2(10theta)=0 and (b+10theta)−(a+10theta)=b−a. QED.

**Independent projected block corollary (coupled with S066 packing).** If B_1,...,B_k are pairwise disjoint nonempty **original U-index** subsets with lambda(sum_{i∈B_j}u_i)=0, their torsion colours w_j=rho(sum_{i∈B_j}u_i)∈Q are F2-linearly independent. Otherwise a nonempty union of the disjoint B_j has both mod5 and mod2 sum zero in H, contradicting the H-zero-free U. Hence k≤3 and k=3 gives a basis. If every i in B_j additionally has endpoint torsion d_i, then the actual original-index formula is

    w_j = sum_{i∈B_j}(t_i+d_i) .                             (2)

Thus all nonempty projected-zero blocks made of genuine endpoint-torsion pairs have nonzero, and mutually independent when disjoint, **specific** t+d colours. This is a necessary cross-prime support constraint, not proof that any such blocks exist or that any endpoint difference is torsion.

**Hostile application.** CLM-0240's conditional m2 independent d1,d2 case now has an **exact check**: if both endpoint differences really lie in G[2], the directions must equal rho(u1)+t1 and rho(u2)+t2. It does not force their independence or low N_danger. The local S066 pairs a_i=e_i,b_i=11e_i have u_i=6e_i, rho(u_i)=0 and t_i=e_i, hence d_i=e_i, confirming (1); that local gadget is not a full U22/G59.

## 3. CLM-0242 — SAME original four-Fano support creates a determined danger quartet

**Theorem (genuine Fano-shift fibre, conditional on one real witness).** Fix a **nonempty** original non-q split mask M⊆N. Pick genuine selected-original split index set I=M∪J with J⊆P_q, one actual member alpha_i of each pair i∈I, a fixed set R0 of original outsiders from {g_1,...,g_8,s_q}, and original full-pair indices B⊆[22]\\I. Require the full-G parity of

    A=sum_{i∈I}alpha_i+sum_{z∈R0}z+sum_{i∈B}(a_i+b_i)

to be zero, so w=iota^{-1}(A)∈H is well-defined. For EACH of four even Fano triples L_eps, form the **actual original** subset

    Z_eps= {alpha_i:i∈I} ∪ R0 ∪ (⋃_{i∈B}{a_i,b_i}) ∪ L_eps. (3)

Because M≠empty, every Z_eps is nonempty and proper, split mask exactly M, with sum_G Z_eps=2(x_eps+w). Its actual complement consists of the three opposite Fano singleton positions, complemented R0 (including the other g and s_q), mates of selected split pair endpoints and the complementary full/empty unsplit pairs. Total_G T=0 gives the same torsion colour for its complementary witness; neither original Z nor its complement is the empty/full trivial subset.

Suppose the four actual Fano projections have a COMMON C5 value:

    lambda(x_000)=lambda(x_110)=lambda(x_101)=lambda(x_011). (4)

If **one actual Z_eps** is a torsion witness, equivalently lambda(x_000+w)=0, then ALL FOUR Z_eps are genuine torsion witnesses, with unique colours

    v_000=rho(x_000+w),
    v_ij=v_000+Delta_ij  (ij=12,13,23),                  (5)

so

    {v_000,v_000+Delta_12,v_000+Delta_13,v_000+Delta_23} ⊆ D_M. (6)

The full-original three Delta values cannot be replaced by freely chosen abstract mask colours. Also v_000+v_12+v_13+v_23=rho(C), exactly as the original full-H Fano sum identity requires. For an arbitrary fixed tuple WITHOUT (4), at most those eps for which lambda(x_eps+w)=0 are torsion; no fourfold upgrade is allowed.

**Proof.** Each L_eps has even quotient parity, and (3) includes one original endpoint in precisely the named split pairs, so pi(sum_G Z_eps)=0 and iota^{-1}(sum_G Z_eps)=x_eps+w. A G subtotal is in G[2] iff its H preimage lies in 5Q=ker(lambda). Under (4), lambda(x_eps+w) is the SAME for all eps, so one is zero iff all are. For x_eps+w=5v_eps, rho(x_eps+w)=rho(5v_eps)=v_eps; take differences and invoke the true S060 original-lift identities rho(x_ij−x_000)=Delta_ij to obtain (5) and (6). Summing (5) and using sum x=C yields the colour-sum formula. Original complement handling above is literal indexed T, not a synthetic H edge. QED.

**A conditional EXACT12/13+ collision test.** Suppose the ACTUAL D sets form an exact twelve-condition no-full cover D_A=a+L,D_B=b+L,D_{A△B}=a+b+L for common rank2 L, or merely CONTAIN these three four-cosets as an aligned subcover. If a supported mask P∈{A,B,A△B} has the REAL Fano-shift witness (3),(4), then in the EXACT12 case (6) forces

    span(Delta_12,Delta_13,Delta_23) ⊆ L.                  (7)

In particular rank3 Delta is impossible in exact12 if a supported mask has such a true witness. For a 12-SUBCOVER contained in larger D_P, rank3 Delta produces FOUR affinely independent Q points, of which at most three lie in ANY affine 2-plane. Therefore actual D_P must contain ≥ONE further danger point beyond its chosen four-coset. More generally, if s of the three supported masks EACH has its own genuinely witnessed shared-projection quartet and rank Delta=3, then

    N_danger ≥ 12+s.                                        (8)

Thus if s=3, any such cover demands N_danger≥15, excluding BOTH exact12 and augmented13/14, **but ONLY IF** the original witness condition has been proved for all three masks. A 13/14 enlargement cannot be treated as exact D_P geometry, as S067 warned.

This is a new direct SAME-Fano-to-true-mask bridge, not a proof that (4), one common-shift witness, rank3 Delta, a 12-subcover or budget≤14 is **forced** by S060. The strong simultaneous existence claim is still the missing theorem.

## 4. CLM-0243 — Every even-order XOR of one split-endpoint torsion orbit is q-only zero-immune

**Theorem (full-original affine cube obstruction to the naive XOR tactic).** Fix ANY original nonempty proper subset Z with nonempty non-q split mask M. Fix a set K⊆M of split indices where b_i−a_i=10d_i, and for each eta∈F2^K obtain Z_eta by selecting the opposite original endpoint exactly at indices with eta_i=1, leaving every other original index in/out as in Z. If sum_G Z=10v, then

    sum_G Z_eta=10(v+sum_{i∈K}eta_i d_i).                  (9)

All Z_eta remain original proper mask-M torsion witnesses. When the available d_i span Q, one such original witness generates D_M=Q (a full-eight obstruction), irrespective of whether any pair sum u_i has order2.

For ANY nonempty collection of k (distinct) members of this SAME orbit, take the ORIGINAL index-set symmetric difference X of its member subsets.

* If k is odd, M(X)=M, so X is **not q-only**.
* If k is even, there is a subset J⊆K such that **EXACTLY**
      X= ⋃_{i∈J}{a_i,b_i}.
  In particular X is empty (if J empty), or has full-G sum
      sum_G X=2sum_{i∈J}u_i ≠0
  since U is genuinely H-zero-sumfree.

Therefore NO XOR of an even number of witnesses from one endpoint-swap orbit can ever be a proper q-only **ZERO**. Its only zero possibility is the EMPTY XOR, which S060 correctly does not forbid. Even the four witness values of an affine 2-plane in F2^K give XOR empty: each flip coordinate takes each binary value 0,2 or4 times across that plane; every original index appears an even number of times. This proves a complete no-go for pair/triple/quadruple or higher raw XOR collision arguments **within that single orbit**.

**Proof.** Equation (9) is direct in full G: selecting b in place of a adds 10d, selecting a in place of b subtracts 10d which is equal to 10d. An index outside the K switched endpoint positions has identical membership in all Z_eta; it cancels in an even XOR. For i∈K exactly one of a_i,b_i belongs to each orbit subset. For even k the parity counts of a_i and b_i are equal (their sum is k mod2=0), hence either both or neither survive XOR. For odd k exactly one survives at each i∈K, while each i∈M\\K remains split; M(X)=M. If even k and J≠empty, its genuine original full-pair sum equals iota(sum_J u_i), nonzero as U is H-zero-sumfree. The four-affine-plane statement follows because every affine coordinate F2-linear function on a 2-plane is either constant or balanced, with 0,2 or4 occurrences of a selected endpoint, all even. QED.

**Precisely what this does NOT say.** Combining witnesses from DIFFERENT orbit bases, different outsider/Fano supports or different masks may have a nonempty proper XOR zero; CLM-0231/0234 remain valid targeted routes. This argument does not prove a FULL8 D_M is feasible inside a fully gated 59-original dataset, only that if it is generated by endpoint swaps from one genuine original torsion witness, internal XOR counting alone CANNOT refute it. The three-local-endpoint gadget from S066 demonstrates algebraic plausibility, not a model.

## 5. Long universal-bridge attack: failures, honest boundary

**Full8.** Attempt: choose pairwise or higher symmetric differences among all eight values of a rank3 endpoint orbit, hoping the 5(v+w) carry vanishes. CLM-0243 rules this attack out *uniformly* for all even-order XORs: genuine zero-free U ensures each nonempty even XOR is a nonzero union of original complete pairs. Three complete U[2] pair toggles remain impossible by S066 CLM-0235; split ENDPOINT orbit is different and survives this audit. To exclude full8, force a zero involving DIFFERENT support strata, e.g. a Fano-switch relative to the endpoint orbit, not another combination within it.

**True Fano/exact12.** Attempt: promote four free Fano colours into four actual non-q dangers. Invalid unless SAME original I, alpha, R0, B in (3) and all projected Fano values coincide; CLM-0242 supplies the precise successful conditional transfer and a rank3 Delta lower-bound on extra dangers. At present S060's necessary/sufficient four-value gate requires x_eps∈F_* but does NOT force lambda(x_eps) all equal, rank Delta3, nor the same original non-q witness shift. Consequently (7) and (8) are genuinely conditional, not a new global contradiction. The full sum C and three Delta constraints are honoured, not replaced by an abstract diagram.

**Danger-budget ambition.** No proof bounds N_danger from above for all actual U22, and no argument converts arbitrary ≥15 no-full covers into a 12-subcover. S067's classification is strictly bounded. CLM-0242 helps under real support-sharing but does not supply the universal support-sharing itself. For m0 a genuine all-gated dataset would be minimal; no existence result. For m1 all-twist failure still needs actual full D_{1}; for m2 independent endpoint d directions are now pinned by (1), but their existence and N≤14 are not forced; for m≥3 arbitrary mask covers remain open.

**Parallel fully labelled hostile route.** S059 matching-only total-zero G59 with U=e1^9 e2^9 e3^3 (e1+e2+e3) still fails the true F_* by the original third-coordinate slab: four candidate x third=1 sum4 whereas overline(V1+V2+V3) third=3. Changing only non-q members via 10theta cannot repair Fano failures because it preserves U,V,g,S and F_*. The S066 local three endpoint pairs do NOT furnish the remaining 56 original positions and all q gates. Without a concrete 59-tuple, giving a purported 'first' proper non-q zero/complement would fabricate evidence. **NO** fully labelled total-zero original 59 survivor of all S060 q-only gates was constructed, and NO 58-term zero-sumfree counterexample was produced.

**External/other profiles.** The 22+8+7 canonical setup relies on historical SOURCE_STATED C10 D28 reduction and is not a full proof of 26 hubs, three-hub geometry or alternative P26 (z,r)=(0,4),(0,6),(1,7). SRC-0029 D2(C5^3)=20 remains ABSTRACT_INSPECTED/SOURCE_STATED and was not invoked to prove CLM-0241–0243. First 28 source records and all 30 frontier rows are frozen. No progress in published-priority authentication, numerical campaigns or certification.

## 6. Strongest achievable session conclusion / next real bridge

There is a rigorous ORIGINAL pair/Fano connection (24.1–24.2) and a rigorous proof that one tempting FULL8 attack is categorically futile (24.3). The decisive missing implication is still: from EVERY S060 q-matching + E(U\\I) + SAME full-H and rho-Delta four Fano constraints and total0, force the existence of true shared-shift original non-q witnesses meeting the projected condition, or force another original proper q-only zero by some cross-support collision. Neither is proved. Alternatively provide all 59 original values and the first non-q proper zero/complement after verifying EVERY q-only gate. No D(C20^3)=58 proof, no G58 counterexample, no Phase1 PASS. S069 must pursue genuine cross-stratum shared support or an actual fully labelled hostile model, not another purely abstract covering count.
