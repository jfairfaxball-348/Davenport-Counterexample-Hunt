# S082 — axial three-vector cross obstruction and universal nine-fibre original-index exclusion

15 October 2026. Owner instruction "Run next session" executes S082 only on merged S081 main `c55614a875640a75387d5999d7459273c8200bed`, true Git root tree `02f6bd76efadebf7ff632568d32325c22132207f`. Source-conditional **canonical** 22 full same-nonzero-parity pairs + eight same-q originals + seven parity-singleton originals; self-contained INTERNAL SAME_EXECUTOR symbolic proofs. No numerical mathematical search, CAS, SAT, ILP, code-generated candidate, historical author execution, Lean/Palomar, certification, publication or source upgrade. This document does NOT prove D(C20^3)=58, disprove it, or produce a 58-term zero-sumfree sequence.

## 1. Original-index and exact axial extension convention

Let G=C20^3, H=C10^3, ι(h)=2h, Q=G/2G=C2^3. **Never** identify G with Q⊕H. Fix H-zero-sumfree indexed 22-block sequence U*=e1^8 e2^8 e3^6. Its full indexed subset sums are Σ(U*)=[0,8]×[0,8]×[0,6] mod10, and

    E=H\(-Σ(U*))={h in H: h1=1 OR h2=1 OR h3 in {1,2,3}}.
    E5=π5(E)={x in P=C5^3: x1=1 OR x2=1 OR x3 in {1,2,3}}.
    c=-sum(U*)=(2,2,4) in H;  c5=(2,2,4) in P.

As in S060/S081 the twelve genuine mutually disjoint original q-supervertex groups z_1,...,z_12 in G are the EIGHT individually labelled g_j, the labelled singleton s_q, and the THREE groups V_i=X_i+Y_i of genuinely disjoint singleton original pairs. ALL z_j have parity q≠0, while the other six singleton originals are the true X_i/Y_i, not invented atoms. The total 59-original-index G sum is0; hence sum_j z_j=ι(c). For each j define the half-projection y_j=(1/2)π5(z_j) in P, where 1/2 is the inverse of2 in C5. This definition uses ONLY π5, never illicit G division. For EVEN I⊆[12], the genuine H value h(I)=ι^-1(sum_{j in I} z_j) is well-defined and satisfies π5(h(I))=sum_{j in I} y_j. Their full projected sum is c5, whose THIRD coordinate is 4.

**Exact original support completion.** For EVERY proper nonempty EVEN I, if sum_{j in I} y_j lies outside E5, then h(I) lies outside E, so -h(I) is an ACTUAL indexed subset sum of U*. Choose B⊆[22] of full original pairs with sum_{i in B}u_i=-h(I). The union of ALL original member indices of the q-supervertex groups in I and BOTH original endpoints of each indexed pair in B sums0 in G. It is nonempty and proper because at least one other original q-supervertex is omitted. This is a literal indexed G-zero, not a synthetic projected contradiction. The full I=[12] is EXEMPT, since c5=(2,2,4)∉E5, and its zero completion is the entire T59.

## 2. CLM-0286 — analytic all-125 projected single-fibre 2k capacity sieve

Suppose m≥2 original q-supervertices have the identical P half-projection y=(y1,y2,y3). Any selected 2k of these groups, with 2k<12, has projected H sum 2k y. If 2k y∉E5, the above completion produces a proper original G zero. Therefore an original q-only-compatible T59 must satisfy

    m(y)≤2κ(y)-1,  where  κ(y)=min{k in {1,2,3,4,5}: 2k y NOT in E5}.

Here κ always exists because 10y=0∉E5. This is an upper bound on m≤2κ-1 for up to 9 repeats; for m≥10 a ten-group support is already proper, so the same formula is unqualified on twelve groups. No torsion lift choice can evade it: the obstruction is in the genuine π5 image of E.

For k=1,2,3,4 the exact four tests are respectively

    k=1: (y1=3 OR y2=3 OR y3 in {1,3,4});
    k=2: (y1=4 OR y2=4 OR y3 in {2,3,4});
    k=3: (y1=1 OR y2=1 OR y3 in {1,2,3});
    k=4: (y1=2 OR y2=2 OR y3 in {1,2,4}).

A parenthesised test is exactly the condition 2k y∈E5, not a numerical orbit enumeration. Consequences: if y3=0, then κ(y)≤3 because the three distinct horizontal requirements y_i=3,4,1 cannot all be met by only two horizontal coordinates, so m(y)≤5. If y=(1,3,1) as in S081, the k=2 test FAILS, giving m(y)≤3 immediately (not merely S081's four-colour cap4). If y=(1,0,0), even k=1 fails, so m(y)≤1. For every y, m(y)≤9 by the proper ten-group projection0 test; the next theorem uniformly improves this to EIGHT for the axial c5-total.

This is a genuinely mod5-*slab* sieve, substantially stronger than merely forbidding even zero in P; the latter admits S081's nine-a/three-b parity shadow.

## 3. CLM-0287 — three-vector affine cross lemma, complete symbolic proof

**Lemma.** For any three vectors w1,w2,w3 in C5^2, there exists a NONEMPTY subset J⊆{1,2,3} whose sum w_J=(x,y) satisfies x≠1 AND y≠1. Equivalently, no three-vector indexed sequence has all seven nonempty subset sums contained in C={(x,y):x=1 OR y=1}.

**Proof.** Assume all nonempty subset sums are in C. In particular each w_i is in C. By pigeonhole, two of the three, say w1,w2, are on the same one of the two affine coordinate lines; by switching coordinates arrange w1=(1,a), w2=(1,b). Since their sum (2,a+b) must be in C, a+b=1 modulo5.

If w3=(1,d), the sums w1+w3 and w2+w3 force a+d=b+d=1, hence a=b and 2a=1. In C5 this means a=b=d=3, whereas the three-vector sum is (3,9)=(3,4), outside C, contradiction.

Otherwise w3=(t,1) with t≠1. If t≠0, each of w1+w3 and w2+w3 has first coordinate 1+t≠1 and therefore must have second coordinate1, forcing a=b=0, contrary to a+b=1. If t=0, the total sum is (2,a+b+1)=(2,2), again outside C. Exhaustive algebraic case split, no computation. QED.

## 4. CLM-0288 — universal original nine-equal-q-projection exclusion

**Theorem (S082 central).** For the axial U* and the canonical real TOTAL-ZERO original T59, passing the true S060 m=0 q-only original gate forces EVERY fibre of the map j↦y_j=(1/2)π5(z_j)∈C5^3 to contain AT MOST EIGHT of the twelve genuine labelled q-supervertices. This holds for **arbitrary** values of the three other projected q groups and for ALL original 10-torsion lifts (no equality of their real G values is assumed). Thus a nine-a/three-*arbitrary*-outsider projected family cannot pass even the original q-only gate, not just S081's one 9a+3b model.

**Proof.** Suppose nine labelled q-supervertices have the same projected y; call the other three individually labelled projected vectors b1,b2,b3. If y3=0, §2 gives an even r∈{2,4,6} or at latest r=6 with r y∉E5, so a selected proper even r among the nine has an actual original zero by §1. [Indeed these three distinct nonzero r residues require three different horizontal coordinate values equal1, impossible with two coordinates.] Hence y3≠0.

Define in P the three vectors with third coordinate0:

    w_i=b_i-(b_{i,3}/y3)y, i=1,2,3.

For EACH NONEMPTY subset J⊆{1,2,3}, let k=|J|. Among the integers r between0 and9 with r≡k (mod2) there are EXACTLY FIVE representatives, one of each C5 residue: {0,2,4,6,8} if k even, {1,3,5,7,9} if k odd. Therefore choose r_J in this set with

    r_J y3 + sum_{i in J} b_{i,3}=0 in C5.

Choose r_J of the NINE genuinely distinct ORIGINAL q groups in the y fibre, and ALL original members of the k distinct outsider q-supervertex groups in J. The selected set has even total number of q groups (r_J+k even), so its literal G sum has an H preimage. Its projection is

    r_J y + sum_{i in J}b_i
      = sum_{i in J}(b_i-(b_{i,3}/y3)y)
      = sum_{i in J}w_i,

with THIRD coordinate0. By CLM-0287 there is a nonempty J whose latter FIRST TWO coordinates are both different from1. For that J the full projected H sum is outside E5.

This selected q-supervertex support cannot be the forbidden FULL twelve: that would require J={1,2,3} and r_J=9, whose projected H sum would be the FULL c5 with third coordinate4, whereas the constructed projected H sum has third coordinate0. Thus it is PROPER (and nonempty as J≠empty). Apply the exact original-index completion from §1 to obtain a proper zero of ACTUAL ORIGINAL G indices, contradicting the true q-only gate. QED.

**Strength.** Unlike S081's four-label (t2,t3) fibre cap for a=(1,3,1), this argument controls ANY y and ANY independent, repeated or unrelated projected outsider triple, and does not need rank2, a synthetic matching, 10-torsion assignment, SAT, or a search. It uses three outsider groups' *actual labelled* existence and the axial full-total c5, including the full-set exception; it does NOT show every arrangement with 12 q groups must have a ninefold fibre.

## 5. CLM-0289 — sharpened FIRST explicit original failure in the S081 total-zero model

Recall the fully original-labelled partial S081 model: nine q groups A=(2,6,7) (eight g plus s_q), and V1=B,V2=B,V3=B' with B=(2,0,5), B'=(2,10,15) in C20^3; U*=e1^8e2^8e3^6 consists of 22 complete original pairs; the six singleton originals are X_i,Y_i with V_i=X_i+Y_i. In the previously reported 32-original-index zero, g1+g2 and fifteen complete pairs vanish. There is an even SMALLER directly named failure:

    V1+V2 = 2B=(4,0,10) in G,
    8 complete ORIGINAL e1 pairs contribute (16,0,0) in G,
    5 complete ORIGINAL e3 pairs contribute (0,0,10) in G,
    TOTAL=(20,0,20)=0 in G.

Select ALL FOUR genuinely distinct singleton original indices X1,Y1,X2,Y2 making V1 and V2, plus BOTH endpoints of eight distinct e1-pairs and five distinct e3-pairs. This is exactly 4+2(8+5)=30 ORIGINAL positions, proper and nonempty. Equivalently the even H sum ι^-1(V1+V2)=(2,0,5)∉E, and its mod5 projection 2b=(2,0,0)∉E5. Another explicit size30 alternative is V1+V3 plus 8 e1 and 5 e2 pairs. The earlier rank-two 'zero-free' assertion was only a C2×C5^2 ZERO-AVOIDANCE assertion, not a π5(E)-SLAB assertion; this precisely corrects the tempting false upgrade. No claim that 30 is the *global minimal* zero-subset cardinality of the 59-labelled model.

## 6. Attacked further bridges; first honest missing implication

The new theorem kills the complete NINE-EQUAL-FIBRE class among any 12 original q-supervertices, irrespective of rank2/3 and torsion. It does NOT prove axial full m0 q-only impossibility. The actual bottleneck is the remaining **max-fibre≤8** projected configurations: show that 12 vectors y_j summing c5=(2,2,4), with EVERY nonempty proper even subset in the exact E5, are impossible, OR write down their actual mod20 original lifts and apply TRUE H E, all FOUR coupled Fano x, ALL 2048 outsider cuts, q split I/α with E(U\I), and then mixed signed non-q K. Neither construction nor global contradiction was proved here. A max-fibre≤8 restriction does not itself force any particular Fano line or any non-q sign/torsion carry.

No attempted false upgrade: (i) C5^3 projected zero-free is far WEAKER than all even sums in E5; (ii) E5 membership is still only NECESSARY for actual H E; (iii) twelve q groups are grouped originals but the full 12 support MUST be exempt; (iv) four Fano triple values belong to the SAME six singleton original positions; (v) rank≥2 projected distributions remain genuinely open, as do q split actual endpoint selections, all 26 q-hubs, non-q signed w_i/τ_ε, FULL8/exact12/13/14/≥15, original overlap/majority and P26 (0,4),(0,6),(1,7). Arbitrary H-zero-free U22 remains open. G58 and D(C20^3)=58 remain UNPROVED, source29/frontier30 unchanged, Phase1 IN_PROGRESS/CAM-0001 BLOCKED/CI ABSENT_NOT_PASS.
