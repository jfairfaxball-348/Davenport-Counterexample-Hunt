# S085 — Sevenfold axial q half-fibre: torsion rigidity and five-outsider analytic cuts

15 October 2026. **INTERNAL SAME_EXECUTOR, SOURCE-CONDITIONAL.** Entry live main `ea404fd2971a213ffb6398eb5fa8ad68abfaafce`; TRUE root Git tree `7d7415d81b4c2bc3a57aa06b7627f5b68399b47b`. The S084 ordinary merge has parents `4bc7b957ff3cedc979388debcb8ac97c4549e224` and `a4b209e2478e9bccd7868400d13a324e04e9f279`. The actual S084 eightfold obstruction gives maximum projected multiplicity seven, not a twelve-q no-go. New results below CLM-0296–0299 are symbolic deductions in the axial model, not a global Davenport result. No numerical mathematical search, generated orbit, CAS, SAT/ILP, Lean/Palomar, independent proof certification, or publication.

## 1. Actual original labels and the unique permissible completion

As before let `G=(Z/20)^3`, `H=(Z/10)^3`, `iota(h)=2h`, and `q=(0,0,1) mod2`. The 59 **ORIGINAL positions** consist of 22 indexed original pairs `(a_i,b_i)` whose complete pair sums have H values `U*=e1^8 e2^8 e3^6`; eight individually indexed `g_j`, the singleton `s_q`, and six distinct original singleton positions `X_i,Y_i` (`i=1,2,3`) with genuine group values `V_i=X_i+Y_i`. The twelve pairwise disjoint genuine q groups `z_j` are precisely the eight `g_j`, `s_q`, and the three `V_i`; in the last three cases the whole group means BOTH of its actual singleton original positions. Their total sum is `iota(c)`, `c=(2,2,4)` in H, because the full original total is zero.

For any even group-label support `I`, `h(I)=iota^{-1}(sum_{j in I}z_j)` exists in H and its mod5 value equals `sum_{j in I} y_j`, where `y_j=(1/2)pi5(z_j)` in `P=F5^3`. The indexed U subset-sum box is `[0,8]x[0,8]x[0,6]` modulo10; its extension set and projection are

```
E   = {h in H: h1=1 or h2=1 or h3 in {1,2,3}};
E5  = {x in P: x1=1 or x2=1 or x3 in {1,2,3}};
C   = {(v1,v2) in F5^2: v1=1 or v2=1}.
```

**Literal original witness algorithm, not a search.** If `I` is nonempty, proper, even, and `sum_I y_j notin E5`, then `h(I) notin E`. Write `k_1=(-h_1 mod10) in [0,8]`, `k_2=(-h_2 mod10) in [0,8]`, `k_3=(-h_3 mod10) in [0,6]`. Select the FIRST `k_l` genuinely indexed `e_l`-value U pairs, BOTH ORIGINAL endpoints of each, together with ALL ORIGINAL members of q groups indexed by `I`. Their G sum is `iota(h(I)+sum_l k_l e_l)=0`. It is proper because at least one genuine q group is not selected, and nonempty because `I` is. The all-twelve support is exempt throughout; its P sum is `c5=(2,2,4)` and cannot be a projected-third-zero witness.

## 2. CLM-0296 — exact seven-repeat parity-matched outsider escape calculus

Suppose seven distinct labelled true q groups share `y=(a,b,t)` and the other five groups have projected values `b_i=(b_i1,b_i2,d_i)`. If `t=0`, the three proper even **pure** repeat selections of sizes2,4,6 have third sum0, so each would require `2(a,b),4(a,b),6(a,b) in C`. These three requirements demand the three distinct horizontal values 3,4,1 to appear among only two coordinates `a,b`, impossible. Thus **t !=0**.

For `t !=0`, set `e_i=d_i/t` in F5 and `w_i=(b_i1,b_i2)-e_i(a,b)` in F5^2. For each nonempty outsider label subset `J`, its residual is `w_J=sum_{i in J}w_i` and normalised third sum `e_J=sum_{i in J}e_i`. Selecting `r` of the **seven separate original q groups** gives an even original union exactly when `r ≡ |J| mod2`.

* For outsider support `|J|` even (2 or4), available repeat counts `r=0,2,4,6` represent F5 residues `0,2,4,1`, missing only residue 3. If `w_J notin C` and `e_J !=2`, there is a REAL available repeat count `r=-e_J mod5`, yielding projected sum `(w_J,0) notin E5` and hence the literal proper original zero above. Therefore **`w_J notin C => e_J=2`**.
* For outsider support `|J|` odd (1,3 or5), available repeat counts `r=1,3,5,7` represent `1,3,0,2`, missing residue 4. Therefore **`w_J notin C => e_J=1`**, or a real proper original zero follows.

Every chosen third-zero support is automatically proper: even for `J` of size5 and `r=7`, that would be all twelve groups, whose actual total third projection is 4, not0. For empty outsider support the pure-repeat tests above apply, rather than the nonempty-J rules. The actual total gives
```
sum_{i=1}^5 d_i = 4 - 7t = 4-2t,
sum_{i=1}^5 e_i = 4/t - 2   (in F5).
```
In particular when `t=3` the five-outsider normalised third sum is **1**. The all-five-outsider set then AUTOMATICALLY has the odd-case missing-residue escape, regardless of `w_1+...+w_5`. Thus **do not infer W in C** for the surviving sevenfold case. These escape implications are NECESSARY projected conditions only, not a full actual H/Fano/S060 lift.

## 3. CLM-0297 — sevenfold third-coordinate class and actual modulo20 torsion rigidity

**Theorem.** Under the same TRUE original q-only avoidance, seven groups with the same half-projection necessarily satisfy **`t=3`**, and all seven have the SAME actual third coordinate in G, either all `1 mod20` or all `11 mod20`. Their first two coordinates and original label roles need not be equal.

**Proof.** Each true q group has first two G coordinates even and third coordinate odd. For a fixed `y`, the given parity and mod5 half-projection uniquely prescribe the G coordinates modulo10; the only remaining independent choices are the three binary 10-torsion bits `alpha_{j,1},alpha_{j,2},alpha_{j,3}` in `z_j=z0+10alpha_j`. For even `r=2k` repetitions, the actual H completion is `k z0+5 sum_j alpha_j` mod10, with the sum of the selected binary bits interpreted modulo2.

**Case `t=1`.** Any four repeats have projected third coordinate `4`, hence to lie in E their true H first or second coordinate must be exactly1. For a horizontal coordinate with `y_l=4`, the original `z0_l=8` and the four-group H coordinate equals `6+5 xor(alpha_{j,l})` in C10; it is1 precisely when the selected four bits XOR to1. If NEITHER horizontal `y_l=4`, the four-group projected sum is already outside E5. Otherwise encode the one or two coordinates for which `y_l=4` as binary one- or two-bit colours on the seven original groups. Any seven labelled binary colours of dimension at most two contain FOUR distinct labels whose colour XOR is ZERO: in dimension1 at least four of seven are equal; in dimension2 either some colour appears four times, or two different colours each appear twice, since avoiding both bounds the total at `3+1+1+1=6`. That four-group original support has H horizontal value6 in every potentially qualifying coordinate and projected third4, so it is outside E. By §1 it gives a literal original G zero. Contradiction.

**Case `t=2`.** Every pair of repeats has projected third4, so an actual H pair can lie in E only through a horizontal coordinate with `y_l=3`. In that coordinate `z0_l=6` and the pair H coordinate is `6+5 xor(alpha_{i,l},alpha_{j,l})`, equal to1 only when the two binary bits DIFFER. Thus each pair of the seven original groups must have distinct colours restricted to at most two such qualifying horizontal binary coordinates. There are at most four colours; seven pairwise different labels cannot fit. (With no qualifying coordinate, even a pair fails.) Contradiction.

**Case `t=4`.** The six-group projected third is4. At least one horizontal coordinate must have `y_l=1` because `6y_l=1` in F5 exactly when `y_l=1`. If EXACTLY ONE horizontal coordinate `y_l=1`, then `z0_l=2` and every one of the seven six-element original subgroups has H coordinate `6+5 xor(alpha_{j,l}:j in I)`; to be1, the XOR of the six chosen torsion bits must equal1. Comparing the seven sextuples (each omits one label) forces ALL seven bits equal; then each six-fold XOR is0, contradiction. If BOTH horizontal coordinates equal1, every pair has projected horizontal coordinates2 and third3, so the only way to belong to E is third H equal3. Here `z0_3=3`; pair third equals `3+5 xor(alpha_{i,3},alpha_{j,3})`, so all seven third torsion bits must be the same. Now choose ANY four: its actual H third equals `2*3+5 xor(four identical bits)=6`, while both projected horizontal coordinates are4 (so neither actual H horizontal coordinate can be1). Its H value lies outside E. Contradiction.

Only `t=3` remains. For this value `z0_3=1`. In size `r=2,4,6` pure repeated supports, third H equals respectively `1,2,3 + 5 xor(selected third torsion bits)`; it is admissible via its third coordinate exactly when that XOR is0. The only way for a horizontal coordinate to rescue the `r`-support is that `y_l=3,4,1`, respectively. Three DISTINCT qualifying horizontal values are needed to rescue all three sizes, but there are only TWO horizontal coordinates. Thus for at least ONE size `r in {2,4,6}`, NEITHER horizontal coordinate can rescue; EVERY r-element original group selection then has XOR of its third torsion bits zero. Compare two such r-element supports exchanging labels i and j while keeping r-1 of the remaining five labels fixed (possible for each r≤6): their XOR equation forces `alpha_{i,3}=alpha_{j,3}`. So ALL seven third torsion bits are equal. Since the fixed mod10 third residue is1, all seven original G third coordinates are identical, either1 or11. QED.

Crucially this is a TRUE H-mod10 torsion argument, stronger than the `E5` projection alone. It checks only pure repeated supports; it does not certify any sevenfold outsider arrangement or any original Fano cut.

## 4. CLM-0298 — four of the five outsider residuals cannot coincide

**Theorem.** In a sevenfold hypothetical q-only-compatible configuration with `t !=0`, four of the five outsider residual horizontal vectors `w_i` cannot be identical (regardless of their distinct projected third values). Hence any surviving sevenfold pattern has residual outsider multiplicity at most THREE.

**Proof.** Name four true outsider labels with residual `u` and normalised third values `e_1,e_2,e_3,e_4`, and the remaining fifth label with residual `v` and normalised third `f`. All genuine outsider-only supports of sizes1 to5 obey CLM-0296.

If `u in C` and `2u in C`, then up to swapping horizontal coordinates `u=(1,3)`, so `3u=(3,4)` and `4u=(4,2)` lie outside C. ALL four triples chosen from the four u labels must have normalised third sum1; comparing triples forces all four e_i equal, and `3e_i=1` implies `e_i=2`. But the genuine four-u outsider support then has third sum `4*2=3 !=2` and residual `4u notin C`, violating the EVEN escape condition.

If `u in C` but `2u notin C`, then all six pairs of four u labels must have normalised third sum2, so all `e_i=1`. Every three-u support therefore has normalised third3, different from the ODD escape value1, forcing `3u in C`. Since u itself is in C and 2u is not, up to coordinate swap `u=(1,2)`; but `4u=(4,3) notin C` and the actual four-u third sum4 differs from the EVEN escape value2. Contradiction.

Finally suppose `u notin C`. The four true outsider singletons force `e_i=1`. Because three-u and four-u selected supports have third sums3 and4 instead of their requisite 1 and2, respectively, `3u,4u in C` must both hold. Their coordinate requirements force (up to swapping axes) `u=(2,4)`: one coordinate must be2 to make 3u hit1, and the other4 to make 4u hit1. Both coordinates are nonzero. For each `k in {0,1,2,3,4}`, the actual outsider subset of k of these four u labels plus the FIFTH label has residual `v+k u` and normalised third `f+k`. Its size `k+1` alternates parity; CLM-0296 yields:
```
k             0    1    2    3    4
required f    1    1    4    4    2
whenever v+k u lies OUTSIDE C.
```
For any fixed `f`, at least THREE of these five residual values MUST therefore belong to C. Yet the five points `v+k(2,4)` (`k in F5`) hit the affine line `x=1` at exactly one k and `y=1` at exactly one k; hence **at most TWO** lie in their union C. Contradiction. No numerical orbit, SAT or search is involved. By §1, every failed required escape entails a *proper literal original indexed G zero*. QED.

This excludes outsider residual multiplicity partitions containing 4 or5, not patterns with maximum three. It is not a sevenfold no-go and gives no lift satisfying the full original gates.

## 5. CLM-0299 — analytic six-repeat parity sieve, no sixfold exclusion

For six projected equal q groups with `y=(a,b,t)`, six labelled outsiders, `t=0` is ruled out by the same 2/4/6 pure-fibre requirement `y_h` simultaneously containing 3,4,1. If `t !=0`, put `e_i=d_i/t` and `w_i=b_{i,h}-e_i y_h` for the SIX real outsider groups. For any nonempty even outsider J (size2,4 or6), r among `0,2,4,6` is available and omits only residue3 in F5, so `w_J notin C => e_J=2`. For any odd outsider J (size1,3 or5), available r are `1,3,5`, omitting residues2 and4, hence `w_J notin C => e_J in {1,3}`. The actual total gives `sum e_i = 4/t-6 = 4/t-1`. Any other violation chooses an actual parity-correct r and yields an original zero by §1. For J all six outsiders and r=6 the selected support would be all twelve, but its total third4 prevents it being the third-zero support; exemption checked explicitly. This is only a sharpened NECESSARY sieve for future sixfold work, not a classification, not a failed or surviving original sequence.

## 6. Hostile boundaries and remaining S060 bridge

No full sevenfold projected-spectrum exclusion was obtained; only `t=3`, shared actual third torsion, and outsider residual max-three were proved. Sixfold retains multiple odd missing residues and remains unresolved, as do spectra with max-fibre<=5. The original full 59-label problem still additionally requires true H `E(U*)` for EVERY proper even q support, four coupled modulo20 Fano original line values from the SAME six original X/Y positions obeying S060 sum and Delta identities, all 2048 partial-singleton transversals, ALL q-pair split masks I/alpha tested against the ACTUAL `E(U*\\I)`, all 26 q hubs, all non-q signed original-pair masks and FULL8/exact12/13/14/>=15 overlap carries, and other U22/profiles. Projection/torsion necessary conditions are NOT sufficient; no fully indexed original T59 compatible model was constructed. Nothing establishes an original 58-zero-sumfree sequence, `D(C20^3)=58`, or general rank-three Davenport equality. Source29 and original frontier30 remain untouched, Phase1 IN_PROGRESS and CAM-0001 BLOCKED.
