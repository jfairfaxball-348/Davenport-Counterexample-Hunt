# S066 — Projection-zero packing kills the proposed rank-three bridge; endpoint-swap torsion acts on genuine original masks

14 October 2026. Explicit owner-invoked S066, sustained Phase-1 **symbolic** analysis of original-index (C_{20}^{3}). INTERNAL proofs and hostile audit. No mathematical numerical search, CAS/SAT/ILP, computer-generated candidates, Lean, Palomar, certified construction, active campaigns, manuscript or contact. **No universal (D(C_{20}^{3})=58) theorem and no zero-sumfree original (G_{58}).**

## 1. Exact scope and why the S065 proposal needed hostile correction

Retain all ACTUAL original indices of S060: 22 complete pairs ((a_i,b_i)), eight original (g_j), seven parity-distinct original (s_r), total-zero (T_{59}) in (G=C_{20}^{3}), quotient (Q=G/2G=C_2^3), (H=C_{10}^{3}), (iota(h)=2h), original pair sums (u_i=iota^{-1}(a_i+b_i)), non-q pair-index set (N={i:t_i
e q}), genuine q-matching and four SAME-c original Fano (F_*) gates, every (E(U\setminus I)), all original mixed odd (g), and every original q split. Assume the S060 q-only gate holds and (U=(u_i)_{1}^{22}) is zero-sumfree in (H), **conditionally** on the source-stated canonical reduction. For nonempty non-q original split mask (Msubseteq N), (D_Msubseteq Q) denotes genuine original parity-even proper subsets with full-G sum (10v). An all-(8^{|N|})-gauge obstruction means either (D_M=Q) for some mask, or at least 12 distinct ((M,v)), with exact12 supported on (A,B,C=A\triangle B) and aligned four-point affine cosets of (Lle Q) of rank2.

S065 CLM-0233 correctly established: **IF** three independent non-q complete original pair sums (u_i=5e_i) occur, exact12 is impossible. But this hypothesis is stronger than merely "not known to be forced": it is **inconsistent with a zero-sumfree (U_{22})**. The same three-full-pair toggle full8 illustration is impossible in this canonical (U_{22}) fibre. This is a correction of the *applicability* of S065's conditional statement, not a claim that its implication/proof is false. A different endpoint-swap mechanism below remains viable.

## 2. CLM-0235 — finite projection-block cancellation theorem (fully internal)

Let (K=H[2]={5e:einmathbf F_2^3}) and (ho_5:H\to C_5^3) be coordinate reduction modulo5, with kernel (K). Suppose a zero-sumfree indexed sequence (U) in (H) contains (r) distinct original **terms** (5e_1,\ldots,5e_r) with independent (e_jinmathbf F_2^3), (0\le r\le3); write (L=langle e_1,\ldots,e_r\rangle\lemathbf F_2^3). Remove these (r) particular terms and denote the indexed residual sequence by (V).

**Projection-packing theorem.** The projected sequence (ho_5(V)) cannot contain (4-r) pairwise disjoint, nonempty, indexed zero-sum blocks. In fact it contains **at most (3-r)** mutually disjoint projected-zero blocks.

*Proof.* If there were (4-r) blocks (B_1,\ldots,B_{4-r}), each full-(H) sum (w_j) lies in (ker ho_5=K); write (w_j=5f_j) for (f_jinmathbf F_2^3). Their cosets in the (3-r)-dimensional (mathbf F_2)-space (mathbf F_2^3/L) are linearly dependent, since any (d+1) vectors in dimension (d) are. Hence a **nonempty** collection of the (B_j) has aggregate (H)-sum (5f) with (fin L). The (r) original order-two terms form a basis of (5L), so a (possibly empty) subset of those (r) original indexed terms sums to (-5f=5f). Joining this subset to the nonempty union of the selected blocks gives a **nonempty original indexed zero-sum subsequence of U**, contradiction. The (B_j) are disjoint from the removed (r) terms by construction. No computation/source numerical constant is used. QED.

**Elementary independent proof that (D(C_5^3)=13).** Over (mathbf F_5), the group algebra of (C_5^3) is
[
R\cong\mathbf F_5[X_1,X_2,X_3]/(X_1^5,X_2^5,X_3^5),
]
where (X_j=[e_j]-1). The augmentation ideal (mathfrak m=(X_1,X_2,X_3)) satisfies (mathfrak m^{13}=0) (maximum surviving monomial total degree is (12)). For 13 arbitrary labelled elements (z_i) of (C_5^3), the product (prod_{i=1}^{13}(1-[z_i])inmathfrak m^{13}) is zero. If **no nonempty** subset summed to zero, its group-algebra identity coefficient would equal 1 (only the empty subset), contradiction. Thus any 13 terms have a nonempty zero-sum subset. Four copies of each coordinate basis element yield a zero-sumfree 12-term sequence, so (D(C_5^3)=13). This is an INTERNAL elementary proof, independent of historical SRC-0008 certification.

**Crucial corollary.** If (r=3), projected residual (V) must be **zero-sumfree** in (C_5^3), by the packing theorem (at most zero projected-zero blocks). Therefore (|V|\le12) and (|U|\le15). Consequently a zero-sumfree (U_{22}) can **never** contain three independent order-two terms, among q or non-q pairs. Even without the later external (D_2) statement, S065's rank-three exact12 exclusion is vacuous in the S060 canonical (U_{22}) setting, and its rank-three UNSPLIT full8 construction cannot be instantiated there. This does NOT eliminate general full8 via other genuine index mechanisms.

**Independence audit.** All order-two original (U) terms are independent: a nonempty (mathbf F_2)-dependence would itself be an original indexed (U)-zero. The theorem therefore covers ALL order-two terms, not merely a chosen subset. If (r=3), the bound 15 is absolute for any zero-sumfree (U), not peculiar to the 59-label display.

## 3. CLM-0236 — stronger conditional rank-two exclusion and exact provenance boundary

Define (D_2(C_5^3)) as the least length forcing TWO pairwise disjoint nonempty projected-zero subsequences. The **published-as-arXiv abstract** of Sze Chun Yiu, *The fourth generalized Davenport constant of (C_5^3)*, arXiv:2609.04950 (4 September 2026), explicitly reports (D_k(C_5^3)=5k+10) for all (k\ge2), in particular (D_2(C_5^3)=20). Registered as **SRC-0029 ABSTRACT_INSPECTED, theorem SOURCE_STATED**, NOT an independently reproduced computation, detailed source proof, or certification. The same abstract discusses externally machine-assisted (D_3=25) and (D_4=30); **SRC-0015's** historical computational (D_3=25) is NOT promoted by this mention.

**Conditional deduction, not an unconditional programme proof of (D_2).** If (D_2(C_5^3)\le20), two independent order-two (U)-terms in a zero-sumfree length-22 (U) are impossible. Indeed removing them leaves 20 terms, whose projections have two disjoint nonempty zero-sum blocks by the premise, while the already proved projection-packing theorem for (r=2) permits at most ONE such block. Hence, **conditional on the stated external (D_2=20), the total number of order-two (U_{22}) terms is at most ONE** (in all pair parity classes combined). This supersedes S065's suggestion that two or three could be available in the intended (U_{22}) configuration. No source promotion or replacement of SRC-0008/0015/0023 has occurred.

For (r=1), the residual has 21 projected terms, but the packing theorem only prohibits THREE disjoint projected-zero blocks. A SOURCE_STATED (D_3=25) is not sufficient to force three from 21; one non-q full-pair torsion direction remains arithmetically possible. For (r=0), it requires four disjoint blocks, and the reported (D_4=30) is not applicable at length22. The external theorem cannot by itself settle actual (F_*), original mask cover, or (D(C_{20}^3)).

## 4. CLM-0237 — a DIFFERENT, genuinely original pair-endpoint torsion symmetry

For a non-q ORIGINAL pair index (i\in N), distinguish two different structural conditions:
- **UNSPLIT toggle** (u_i=5e_i\in H[2]): its **complete** original sum (a_i+b_i=10e_iin G), and if (i\notin M) toggle both original members.
- **SPLIT endpoint swap** (b_i-a_i=10d_iin G[2]): whenever (i\in M), replace the **selected original endpoint** (a_ileftrightarrow b_i). This changes the full (G) sum by (\pm10d_i=10d_i), keeps its ORIGINAL split mask, keeps parity zero, and keeps the resulting subset nonempty and proper because exactly one endpoint of (i) remains selected.

**Exact stabiliser theorem.** For every nonempty mask (Msubseteq N), let
[
W_M=\operatorname{span}_{\mathbf F_2}\big(\{e_i:i\in N\setminus M,\ u_i=5e_i\}\cup\{d_i:i\in M,\ b_i-a_i=10d_i\}\big)\le Q.
]
Then **(D_M+W_M=D_M)**. Each individual ORIGINAL operation is an involution or an equality of the two possible endpoint-selected witnesses, applies to **every** witness with mask (M), and preserves the identity of all other labelled positions. Iterate the operations to obtain the full span; all outputs remain actual original proper subsets. Thus if (dim W_M=3), either (D_M=\varnothing) or (D_M=Q). No q split member, synthetic matching edge, arbitrary mask, or free (H)-term is silently toggled.

**New exact12 necessary condition.** For the genuinely witnessed 12-condition obstruction (D_A=a+L,D_B=b+L,D_C=a+b+L), (C=A\triangle B), (dim L=2):
[
\operatorname{span}\left(
\{e_i:u_i=5e_i,\ i\in N\}
\cup
\{d_i: i\in A\cup B,\ b_i-a_i=10d_i\}
\right)\subseteq L. \tag{S066-EQ12}
]
For a complete order-two pair, at least one of (A,B,C) omits (i), as S065 proved. For an endpoint difference, every index (i\in A\cup B) belongs to **exactly two** of (A,B,C); in either supported coset (D_P), the swap symmetry implies the direction lies in its translation stabiliser, precisely (L). Indices outside (A\cup B) do not contribute endpoint swaps to these three masks, so **they are not asserted to lie in L**. Three independent directions among the displayed **available** directions rule out exact12 even though the old rank-three (u_i)-only route was vacuous. Nothing proves that real q/Fano-feasible data force these endpoint directions or force their rank to be three.

**Hostile local full8 survival.** Endpoint torsion is not order-two (U)-torsion. For three labelled coordinate pairs (a_i=e_i, b_i=11e_i) in (C_{20}^3), each endpoint difference is (10e_i), but each (u_i=6e_i\in C_{10}^3) has order5, not order2. If a real reference torsion witness splits all three, swapping these three selected endpoints creates eight distinct true ORIGINAL mask-M torsion sums. The displayed three pairs form only a **local** original-valued gadget, not a zero-sumfree (U_{22}), a total-zero (G_{59}), or a S060-gate survivor. This is why excluding (r=3) full-pair torsion does **not** remove full8.

## 5. Extended direct-attack log on original equality12, FULL8, and >=13

**Equality12, no free synthetic masks.** Combine (S066-EQ12) with the exact CLM-0232 formula. Every (v\in D_M) still needs actual (I=M\cup J), actual selected split endpoints, all genuine 15 outsider index choices satisfying Q parity, and an original unsplit-index subset (B) with (\iota^{-1}(\sum\alpha+\sum R)+\sum_{i\in B}u_i=5v). If a witnessed exact12 triple of original masks supports three independent local toggle directions across the exact available sets, it is impossible. No theorem forces three such endpoint directions, and a rank0/rank1/rank2 stabiliser is still compatible with an abstract four-coset picture. The zero-free projection-packing lemma does not introduce an original Fano support collision. Explicit ORIGINAL triple XOR carries remain exactly S065 CLM-0234 and require a genuinely witnessed weighted-intersection equality; equal-coset cardinality does NOT force it.

**FULL8.** The three-**complete**-order-two-unsplit-pair gadget from S065 cannot occur in the canonical U22, independently of Fano restrictions. It remains logically possible to obtain (D_M=Q) through three independent **split endpoint differences** or mixed available (W_M) directions. Local endpoints with (b_i-a_i=10d_i) allow eight torsion labels without any paired XOR having full-G zero; their symmetric differences contain complete original pairs with sums (2u_i), typically nonzero. No valid pairwise/triple collision was deduced from eight labels alone. If (W_M) has rank0/1/2, the remaining full-eight value coverage still needs extra genuine E/Fano support witnesses, not counting.

**13+ nonfull masks.** S064's all-m threshold is sharp only at 12. Neither the block-packing theorem nor endpoint symmetry proves a general \(N_{\rm danger}\le12\), or that every 13+ cover contains the exact12 three-mask pattern. It is UNSOUND to infer 13+ impossibility from (S066-EQ12); new original witness-carry or extra-mask constraints are needed.

**Small m / 26 hubs.** If (m=0), q-only S060 success WOULD already imply minimality of that particular original total-zero 59-labelled configuration; existence of a compatible full original dataset remains unproved. For (m=1), an all-gauge obstruction still requires a full (D_{\{1\}}=Q); endpoint swaps alone supply at most one nonzero direction and cannot force eight. For (m=2), exact12 remains a possible three-mask cover, with subgroup (L) required to contain its actual local endpoint directions; conditional rank-two complete order2 pairs are forbidden by SOURCE_STATED (D_2=20), not by local mask algebra. All 26 possible hubs, three-hub alternatives, and P26 ((z,r)=(0,4),(0,6),(1,7)) remain OPEN; S060 canonical display is not a verified exhaustion theorem for original (G_{58}).

**Hostile construction attempt.** The S059 matching-only real total-zero G59 still fails the actual SAME-c four-Fano original lift gate, so cannot be upgraded by a non-q pair twist or the local endpoint gadget. We cannot specify 59 labelled original values passing every S060 original q matching, every actual (E(U\setminus I)), every mixed (g) and SAME-c Fano tuple while exhibiting a first proper non-q original zero. No true fully S060-gated hostile NONMINIMAL (G_{59}) was constructed; no genuine minimal (G_{59}), no zero-sumfree (G_{58}), and no universal theorem was obtained. These are strict distinctions.

## 6. Hostile review and next real mathematical bridge

- SELF-CONTAINED: projection-packing lemma, internal elementary (D(C_5^3)=13) group algebra argument, exclusion of (r=3) in (U_{22}), and exact ORIGINAL endpoint-swap stabiliser/equality12 necessary condition.
- SOURCE-CONDITIONAL: exclusion of (r=2) in (U_{22}) imports the exact (D_2(C_5^3)=20) value reported in SRC-0029's abstract; *not* an independently rerun or certified computation. Historical SRC-0015 (D_3=25) remains SOURCE_STATED. Original SRC-0008/0015/0023 not upgraded.
- NOT PROVED: any forced end-swap order2 directions in a canonical S060-feasible U; any actual weighted triple-XOR zero; exclusion of FULL8 or ≥13; all-q-matchings and full original four Fano constraints universally incompatible; alternative quotient profiles; Davenport n20 equality or an n20 counterexample.

**S067 primary target:** rather than repeat the IMPOSSIBLE old (r=3) complete-pair instruction, attack the genuine FULL8 and 12/13+ original-index witness supports via their (E(U\setminus I))/Fano constraints and the NEW endpoint-swap stabilisers; either force an actual proper q-only original zero with explicit full (G) intersections and proof for all masks, or produce a completely labelled S060-compatible nonminimal total-zero (G_{59}) with its FIRST true non-q original zero/complement. Independently verify any desired use of (D_2(C_5^3)=20); refrain from converting a SOURCE_STATED abstract into programme proof. NO numerical mathematical search in this symbolic line.
