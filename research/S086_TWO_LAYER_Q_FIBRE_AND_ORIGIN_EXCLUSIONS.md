# S086 — two forbidden-third layers and strict zero-horizontal-fibre exclusions

15 October 2026. **INTERNAL SAME_EXECUTOR symbolic proof; source-conditional canonical original setting only.** Entry authentic S085 ordinary two-parent merge 257e2bc0eb2e996925ed8a47441734d28f1a8489; actual Git root tree 88c84e07a936b7b0ce7fcfb2949fa466db6317ba; S085 authored 203edfe2e38e2bd4c71de7383c97ea634e5f59f1. No mathematical numerical search, generated orbit, CAS/SAT/ILP, Lean, Palomar, independent certificate, source upgrade or publication.

## 1. Original indices and exact cancellation (used in every theorem)

G=(Z/20)^3, H=(Z/10)^3, iota(h)=2h. A total-zero canonical original T has 59 **distinct original indices**: 22 individually indexed complete pairs U*=e1^8e2^8e3^6 in H; eight genuine g indices; the original q singleton s_q; and the SAME six original singleton positions X_i,Y_i (i=1,2,3), grouped into three actual V_i=X_i+Y_i. These constitute twelve pairwise disjoint genuine q-parity supervertices z_1,...,z_12, each of which has third-coordinate ODD and first two coordinates EVEN. A selected V_i contributes both named ORIGINAL X_i and Y_i positions, never a synthetic position. The projected half-values y_j=(1/2)pi5(z_j) in F5^3 obey sum_j y_j=(2,2,4).

For any proper nonempty EVEN group-label selection I, the actual sum z(I) is even in G and h(I)=iota^{-1}(z(I)) exists in H; pi5(h(I))=sum_{j in I}y_j. The exact full-pair extension E=H\(-Sigma(U*)) equals {h:h1=1 or h2=1 or h3 in {1,2,3}}; its projection E5={x:x1=1 or x2=1 or x3 in{1,2,3}}. If sum_I y_j is outside E5, h(I) is outside E. Explicitly let k_ell=(-h(I)_ell mod10); then k1∈[0,8], k2∈[0,8], k3∈[0,6]. Select the FIRST k_ell separately labelled actual U* pairs of the corresponding type e_ell, **BOTH original endpoints of each**, and all true original positions in the selected q groups. Their sum in actual G is 2(h(I)+sum k_ell e_ell)=0. The index set is nonempty because I is nonempty and PROPER because at least one genuine q group is omitted. No statement uses the full twelve-q set as a proper witness. This is an index-selection construction, not a numerically specified counterexample or an independently certified zero.

## 2. CLM-0300 — exact zero-THIRD AND fourth-THIRD simultaneous cross gates for seven repeats

Assume seven different q group labels have **equal** y=(a,b,t) with t!=0 and five individually labelled outsiders b_i=(b_{i,h},d_i), i=1,...,5. Write v=(a,b), e_i=d_i/t in F5 and w_i=b_{i,h}-e_i v in F5². For outsider support J let m=|J|, e_J=sum_{i in J}e_i, w_J=sum_{i in J}w_i, and C={(x1,x2): x1=1 or x2=1}. The actual total has sum_i e_i=4/t-2. If no proper q-only original zero exists then, for EVERY nonempty outsider J of sizes 1 through 4, the following TWO implications BOTH hold:

* J even (m=2,4): **e_J !=2 implies w_J∈C**; **e_J !=(4/t-3) implies w_J+(4/t)v∈C**.
* J odd (m=1,3): **e_J !=1 implies w_J∈C**; **e_J !=(4/t-4) implies w_J+(4/t)v∈C**.

In particular at the already S085-necessary sevenfold value t=3, write beta=4/3=3 in F5:

| m parity | third layer 0 requires | third layer 4 requires |
|---|---|---|
| even (2,4) | e_J !=2 => w_J∈C | e_J !=0 => w_J+3v∈C |
| odd (1,3) | e_J !=1 => w_J∈C | e_J !=4 => w_J+3v∈C |

For J of size five, odd repeated counts r=1,3,5,7 are physically permitted but r=7 selects all twelve groups. At t=3 the real total e_{all5}=1, so third layer0 would require missing r=4 modulo5, while third layer4 requires r=7: **exactly the EXEMPT full twelve-group selection. Neither cross condition is imposed on J=all five.** For all proper J the maximal r=7 gives at most ten of the twelve actual q groups (m<=3), and r=6 plus even m<=4 gives at most ten. Thus no illicit all-twelve witness occurs.

**Proof.** For fixed outsider J, choose a physically available number r of the seven *different original* repeated q group labels, with r+m even. Its P third component is t(r+e_J), its horizontal component is w_J+(r+e_J)v. When third component0, r≡-e_J mod5 and the horizontal component is w_J. When third component4, r≡4/t-e_J mod5 and the horizontal component is w_J+(4/t)v. For EVEN m the allowed counts r=0,2,4,6 have mod5 residues {0,2,4,1}, omitting exactly3. Hence the 0 cancellation is available unless e_J=2, and the 4-layer cancellation is available unless e_J=4/t-3. For ODD m=1,3 the allowed counts r=1,3,5,7 have residues {1,3,0,2}, omitting exactly4. Thus 0 is available unless e_J=1, and 4 unless e_J=4/t-4. If an available layer has horizontal coordinate outside C, the projected H sum is outside E5, and the literal indexed original completion of section1 gives a **proper nonempty original G zero**. The r bound proves propriety for m<=4. The all-five special case is expressly exempted as stated. QED.

For t=3, every nonempty J of m<=4 has at least one forced cross membership: even missing e choices 2 and0 are distinct; odd missing e choices 1 and4 are distinct. Importantly, this DOES NOT force either named membership separately in every case. This strengthens S085 CLM-0296 without implying projected sufficiency or the all12 crossing.

## 3. CLM-0301 — sevenfold horizontal origin v=(0,0) is impossible

**Theorem.** Under the actual canonical original q-only-zero-avoiding hypotheses, seven equal projected q group values cannot have y=(0,0,3).

**Proof.** Suppose v=(0,0). In CLM-0300 the two mandatory horizontal tests w_J and w_J+3v coincide. The missing values for the two tests are disjoint, for BOTH parities. Consequently **EVERY nonempty outsider J of size at most four** has w_J∈C. In particular the five individually labelled singleton outsiders have w_i∈C; and every pair and every triple of outsider labels has sum in C.

Colour each of these five original outsider labels by a coordinate on which its w_i equals1, choosing either one if both equal1. At least THREE labels receive the same coordinate colour. After swapping horizontal axes, label them i,j,k with w_i=(1,u), w_j=(1,v), w_k=(1,s). Their three actual outsider PAIRS have first coordinate2, which is not1 modulo5. Since each pair sum belongs to C, u+v=u+s=v+s=1 in F5. Subtraction forces u=v=s, and 2u=1 gives u=3. The actual outsider TRIPLE {i,j,k} consequently has w_i+w_j+w_k=(3,9)=(3,4), which is OUTSIDE C: contradiction to its forced proper third0-or4 membership. All labels i,j,k denote genuine original q groups, not new elements. At least one of the singleton/pair/triple gates fails, so choose its true repeated count r from section2 and complete by the explicit genuine original U* pair endpoints of section1. Its q support has at most 7+3=10 groups and is proper. QED.

The proof uses neither the five-outsider total cross (which is NOT valid at t=3) nor a fictitious fourth Fano line. This removes one of the 25 projected horizontal values for the last S085 sevenfold t=3 fibre. It does **not** prove the other 24 values incompatible; it does not produce a complete 59-index survivor.

## 4. CLM-0302 — sixfold two-layer formula and origin t=1,4 exclusion

Let SIX distinct original q groups share y=(v,t), t!=0; write the SIX outsider projections b_i=(e_i v+w_i,t e_i), beta=4/t in F5. For any nonempty outsider support J of size up to FIVE, a parity-correct repeated count r is available from r_even={0,2,4,6}, residues {0,2,4,1}, or r_odd={1,3,5}, residues {1,3,0}. The 0-third and 4-third gates therefore impose:

* EVEN outsider J (m=2,4): e_J!=2 => w_J∈C; e_J!=beta-3 => w_J+beta v∈C.
* ODD outsider J (m=1,3,5): e_J∉{1,3} => w_J∈C; e_J∉{beta-2,beta-4} => w_J+beta v∈C.

Again any violating available support has genuine q label total ≤11 and the literal original U* complete-pair zero. J of all SIX is not used in these implications; the all12 full-set exception is therefore bypassed.

**Consequent strict exclusion.** If v=(0,0) and t=1 (beta=4), the odd 0-layer missing e set {1,3} and odd 4-layer missing set {0,2} are DISJOINT. If v=(0,0) and t=4 (beta=1), they are {1,3} versus {4,2}, again DISJOINT. EVEN outsider J never escapes both layers for any beta!=0 because its two missing e values 2 and beta-3 coincide only at beta=0. Thus at t=1 or4 every outsider J with 1<=|J|<=5 has w_J∈C. Six singleton labels include three coloured on the same cross coordinate; as above, all three pair sums in C force those three second coordinates to equal3, while their triple residual is (3,4) outside C. Contradiction; the corresponding real selected q groups and complete genuine U pairs produce a proper original G zero. Therefore **a sixfold repeated half-value with v=0 has t∉{1,4}**, supplementing S085's t!=0.

At t=2 (beta=2) an ODD outsider set with e_J=3 can evade BOTH zero/fourth layers; at t=3 (beta=3) an ODD outsider set with e_J=1 can evade BOTH. Even-support exclusions remain, but the all-subsets-in-C conclusion cannot be drawn. These t=2,3 cases and v!=0 remain OPEN. No categorical sixfold elimination is claimed.

## 5. CLM-0303 — exact double-cross intersection geometry (conditional only)

For the sevenfold t=3 case define C_0={w:w1=1 or w2=1}, C_4={w:w1=1-3a or w2=1-3b}, where y_h=(a,b). Whenever a proper outsider subset J has a normalised third value requiring BOTH layers under section2, it must have w_J∈C_0∩C_4. This intersection is explicit:

* If a and b are both nonzero in F5, C_0∩C_4 consists of precisely the TWO points (1,1-3b), (1-3a,1).
* If a=0 and b!=0, C_0∩C_4 is the vertical line w1=1.
* If a!=0 and b=0, it is the horizontal line w2=1.
* If a=b=0, it equals C_0 (used in CLM-0301).

For an individual outsider e_i∈{0,2,3}, BOTH layers are required, so its residual belongs to this exact intersection. If a=0,b!=0 and two such outsiders i,j exist, each has (w_i)1=(w_j)1=1, hence (w_i+w_j)1=2; their pair cannot satisfy BOTH cross tests. Therefore the pair e_i+e_j must be one of the two even-support missing values 0 or2. The analogous conclusion holds when b=0,a!=0. These are conditional necessary original-index constraints, **not** a no-go for all remaining horizontal y_h. If a,b both nonzero, the two-point residual restriction is exact but not enough to exclude all five outsiders.

## 6. Hostile boundary and next smallest obligations

All new claims are ONLY source-conditional canonical U*=8/8/6 original-index necessary conditions. **No complete sevenfold no-go**: the S085 survivor y=(a,b,3), a,b not both0, with seven actual group thirds common 1 or11, outsider residual max3, remains. **No sixfold no-go**: generic y_h and t2/t3 zero-horizontal cases remain. The 0/4 layer argument is mod5-necessary only; actual H torsion could rule out more than it rules in. All genuine S060 SAME-six X/Y four coupled transversals, 2048 outsider original selections, q pair splitting I/alpha with E(U*\I), all 26 hubs, non-q signed split original indices, FULL8/exact12/13/14/>=15 overlaps, other U22 and P26 profiles are still unverified.

Suggested S087 attack: prove whether the **two-layer constraints for the full five-outsider proper-size1..4 subset hypergraph** are inconsistent for ALL horizontal (a,b)≠(0,0), with exact total e_i=1 and W=(2,2)-3(a,b), residual multiplicity≤3; include true H third torsion and seven common original G-third 1/11 if two-layer alone does not close. Do not impose the erroneous all-five full12 fourth layer. If an algebraic sevenfold spectrum survives, test literal actual mod20 q original lifts and THEN real coupled S060/Fano/mixed gates; otherwise isolate exact remaining fibre or actual zero. Continue t2/t3 sixfold zero-horizontal exceptional odd-sum strata. Phase1 stays IN_PROGRESS, CAM-0001 BLOCKED. NOT G58, NOT D(C20³)=58.