# S102 — exceptional five-flat q-group colour rigidity closes all >=3-colour leaves

16 October 2026. **CLM-0344: INTERNAL SAME_EXECUTOR conditional hand proof, not independent/formal certification.** Entry real main `a245cc861996e7d07042113614985bd614e8c22b`, directly fetched Git root tree `862b9ab7ec50e46ffeac994db8e9a0ea3ac9f779`. Prior S101 PR #104 is a genuine two-parent merge (parents `7da04f8dc90d3653a45b79eeeaced4c67fbaa735`, `68f513f7571f107eb58bb3d43a2438a30ab6839c`), with exactly one authored S101 commit `68f513f7571f107eb58bb3d43a2438a30ab6839c`. No enumeration, numerical mathematical search, CAS/SAT/ILP, generated lifts, Lean/Palomar, campaign, source promotion, contact or publication.

## 1. Twelve physically disjoint grouped q objects, never fictitious Fano shifts

Use the **same** source-conditional original 59-index total-zero `G=C20^3` setup from S060/S097/S098: 22 genuine original **pairs** `(a_i,b_i)` with sum half-multiset `U*=e1^8 e2^8 e3^6` in `H=C10^3`; eight distinct-original-index `g_j`; one `S=s_q`; and three mutually disjoint genuine two-original groups `V_i=X_i+Y_i`, `i=1,2,3`. The twelve `q=(0,0,1)` parity groups `S,g_1,...,g_8,V_1,V_2,V_3` partition the fifteen original outsider positions, and have true G20 total `(4,4,8)`. The `V_i` are groups of two physical original positions: **they may be among the flats or exteriors**, but may NEVER be attached to a Fano line containing one of their own original positions. This proof never selects a Fano line and avoids that overlap entirely.

For every even nonempty proper subset `J` of these twelve disjoint q GROUP labels, the sum of their original G values is even. Its legitimate half `h(J)=sum_G(J)/2 in H` must belong to
`E(U*)={h in H: h1=1 OR h2=1 OR h3 in {1,2,3}}`.
Otherwise the original support consisting of **all** original indices in the groups `J`, together with both real endpoints of `k_1=(-h_1 mod10)` of the eight e1-pairs, `k_2=(-h_2 mod10)` of the eight e2-pairs, and `k_3=(-h_3 mod10)` of the six e3-pairs is a genuine nonempty proper original G20 zero. Properness holds because at least one disjoint q group outside `J` remains unselected; there are exactly 2046 such proper even grouped q tests, distinct from the 2048 ungrouped Fano residuals. The original full12 support is never tested as proper.

Assume exactly **five** actual q GROUPS are horizontal G20 flats (both horizontal components 0 or 10), in the S098 exceptional vertical pattern: four ordinary labels `f_1,...,f_4` have third value `z` and an exceptional label `e` has third `z+2`, where **`z=1 or 11 mod20`**. Write their horizontal F2² colours as the original 0/10 halves. The seven other real q groups are `v_1,...,v_7`, each with even G20 horizontals and odd third. We prove that if the ordinary leaves occupy **at least three** different colours, a proper original zero is forced, with no assumption that flats are individual S/g singletons.

**Elementary colour-rescue lemma.** For `x=(x1,x2) in C10²`, define
`H_x={c in F2²: x1+5c1=1 OR x2+5c2=1 mod10}`.
It never has four elements. If it contains the three colours `F2²\{m}`, then it is exactly these three, and both coordinates satisfy `x_j=6-5m_j mod10`. Indeed a coordinate can rescue only a single binary bit, and both independent rescuing bit-lines must have their unique intersection and their missing point exactly as stated. This is exact modulo10 horizontal arithmetic induced by actual 0/10 G20 flat values.

## 2. Four distinct ordinary colours — all flat V overlaps also excluded

Suppose the four ordinary colours exhaust `F2²`. For any one of the **seven original** exterior q groups `v`, let `x_v=(v_1/2,v_2/2) in C10²` (legal since the *individual group total* has even horizontals), and `d=(v_3+z)/2 mod10` (legal since both thirds are odd).

* The four **proper two-q-group** supports `{v,f}`, one for each ordinary f, have third half `d` and horizontal shifts `x_v+5c(f)` covering ALL four binary colours. Hence the vertical gate must rescue them: `d in {1,2,3}`.
* The four **proper four-q-group** supports `{v}` plus any three of the four ordinary leaves have third half `d+z=d+1 mod10`. Since the XOR of all four distinct ordinary colours is 00, these four triple colour XORs also cover ALL four binary colours. Hence `d+1 in {1,2,3}` and therefore **`d in {1,2}`**.
* Since `2z=2 mod20`, `d=1` means `v_3=z` and `d=2` means `v_3=z+2`, in TRUE G20, not only mod5.

Let `k` of the seven exteriors have `d=2`. From the actual full q total third `8`, the five flat third total `5z+2`, and seven exterior third total `7z+2k`, we get
`8=(12z+2+2k)=(14+2k) mod20`.
Since `0<=k<=7`, **`k=7`**: EVERY exterior has third `z+2`.

For each exterior `v`, now select the **proper four-q-group** supports `{v,e,f_i,f_j}` with two distinct ordinary leaves. Their legitimate third half is `d+z+1=4 mod10`, NOT in {1,2,3}. The six pairwise XOR colours of four distinct ordinary leaf colours are exactly `F2²\{00}`, so these supports have horizontal binary shifts `D+(F2²\{00})=F2²\{D}`, where `D` is the true exceptional flat colour. By the rescue lemma,
`x_{v,h}=6-5D_h mod10` for BOTH horizontal coordinates, for each of all seven true v labels.

Choose **any four distinct** exterior q GROUPS. This is a proper original grouped support even if some are two-original V groups. Its genuine half sum has horizontals `4(6-5D_h)=4 mod10` for each h, and third `4(z+2)/2=2z+4=6 mod10`. Thus `h(J)=(4,4,6)\notin E(U*)`. The literal original zero adds both endpoints of **six** e1 pairs, **six** e2 pairs and **four** e3 pairs to all original positions in the four selected q groups: `(4,4,6)+(6,6,4)=(10,10,10)=0 in H`. This support contains at most `8+2(6+6+4)=40<59` original positions, is nonempty and proper, and sums to zero in actual G20. This excludes EVERY four-distinct exceptional five-flat q-GROUP assignment, including any V-overlapping flat arrangement; it strengthens S099 without appending V to a Fano transversal.

## 3. Repeated 2+1+1 ordinary colours — C3=1 and C3=3 both excluded

Suppose instead the ordinary colour multiset is `A,A,B,C` with `A,B,C` three distinct elements of F2². Put `M=A+B+C`, the FOURTH colour not among A,B,C. Again fix ANY exterior `v`, with true horizontal `x_v=v_h/2` and `d=(v_3+z)/2`.

* The six true **proper four-q-group** cuts `{v,e,f_i,f_j}` have third half `d+2`, and the two-ordinary pair XORs `A+A=00`, `A+B`, `A+C`, `B+C` exhaust F2². Translating by D changes no coverage. Hence **`d+2 in {1,2,3}`**, so `d in {9,0,1}`.
* If `d=9`, the true **two-group** cuts `{v,f_i}` have third9 and horizontal colour set `{A,B,C}`, while the **four-group** cuts `{v}` plus any three ordinary leaves have third `d+1=0` and horizontal colour set `{B,C,M}` (the twice-repeated A gives triples `M,M,B,C`). Their union is all F2². Both vertical residues fail, so `H_{x_v}` would have to contain all four colours — impossible. Therefore **`d in {0,1}`** for each of the seven external q groups. These are exact G20 third alternatives `v_3=-z` or `v_3=z`.
* At `d=0`, all `{v,f_i}` cuts have vertical half0 and must be horizontally rescued for the **three** colours `A,B,C=F2²\{M}`. By the rescue lemma `x_{v,h}=6-5M_h` in BOTH H10 horizontal coordinates.

Let `k` of seven exteriors have `d=0`, equivalently true G20 third `-z`. Using all original q group totals gives
`8=(5z+2)+(7-k)z-kz=(12-2k)z+2=(14-2k) mod20`,
since `z=1 or11` gives `12z=12` and `2z=2` modulo20. Thus **`k=3`**. In particular two distinct actual exterior q groups `v,w` have third `-z` and each has horizontal half `(6-5M_1,6-5M_2)`. Their genuine original two-q-group support has half sum
`h({v,w})=(2,2,9)` in H: `2(6-5M_h)=2 mod10` in each horizontal coordinate and `(-z-z)/2=-z=9 mod10`. This is OUTSIDE `E(U*)`.

Take all original indices making up these **two disjoint** q groups, and BOTH actual endpoints of **all eight** indexed e1 pairs, **all eight** indexed e2 pairs and **one** indexed e3 pair. The exact original G20 half-sum is `(2,2,9)+(8,8,1)=(10,10,10)=0 in H`. The physical support has at most `4+2(8+8+1)=38<59` original indices, is nonempty, proper and zero-sum. Thus **every** exceptional five-flat `A,A,B,C` instance is impossible, independent of `D`, `C3=1/3`, S101 `eta` escapes, and whether a flat q group is itself a two-original `V_i`. This strictly strengthens CLM-0342/0343 and solves the named S102 survivor/overlap obligation via actual disjoint q-group positions rather than illegal Fano overlaps.

## 4. Hostile audit, exact limitation and remaining targets

1. All five flats and seven exteriors are twelve physically disjoint q GROUPS. If a group is `V_i`, BOTH of its genuine original X_i/Y_i positions are selected together, once. No Fano triple is selected or combined with V; there is no V/Fano overlap.
2. Each tested group J has size2 or4, so is a proper even group support within twelve. The full12 exception is never used. All G20 halves are applied ONLY to an even total: vertical odd+odd or four odd groups, horizontal individual q-group even. Integer carries `z=11` are retained (`2z=2 mod20`), not silently projected away.
3. Four-distinct case: singleton ordinary shift and triple ordinary shift each cover four colours; `d=1/2` exact. Full total forces seven d2, so four-exterior h=(4,4,6); the **actual** U* full-pair completion uses k=(6,6,4).
4. Repeated 2+1+1: exceptional+two ordinary pairs cover four colours, the d9 one/triple ordinary union covers four, d0 ordinary shifts cover precisely three missing M. Full total forces three d0, and two distinct such exterior groups give h=(2,2,9) with full-pair completion k=(8,8,1).
5. Neither case assumes any particular actual X/Y lift or S060 C/Delta, nor q P_q/I/alpha splits; this is a stronger q-only NECESSARY contradiction. It does not pretend the other 2046 grouped masks or separate 2048 Fano masks have been checked. S101's local Fano conclusions remain valid historically but their entire named repeated-five-flat survivor class is eliminated here, even for V overlaps.
6. No result for ordinary leaf-colour patterns `2+2`, `3+1`, `4` (one colour), for uniform `z^5`, <=4 flats, other U22, P26, 26 hubs, signed non-q split gates, FULL8/exact12/13+, or unrestricted G59. No zero-sumfree G58 constructed and **no `D(C20^3)=58` claim**. Prior source29 and ordered frontier30 frozen. Claim is a **conditional no-go theorem for a genuine original-index axial subclass**, internally audited, with Phase1 HOLD and CI ABSENT_NOT_PASS.
