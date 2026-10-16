# S096 — a physical axial 59-index partial model separates Fano/mixed gates from the invariant q-matching obstruction

16 October 2026. **INTERNAL SAME_EXECUTOR HAND PROOF.** This is a genuine completely indexed total-zero `G=(Z/20)^3` *nonminimal* 59-original-position construction used only as a countermodel to an unjustified local-to-global inference. It is **not** a passing S060 59-model, not a minimally zero-sum 59-atom, not a 58-zero-free example, and not a proof of `D(C20^3)=58`. No solver, numerical search, lifted-orbit enumeration, CAS, SAT, ILP, campaign, Lean, Palomar or outside certification. The physical source/frontier objects 29/30 remain frozen.

Entry authoritative main `cb9b86cb3293adfbc1b0578b6a4149fec8e94d67`, authentic Git root tree `b1befeb1a44ed82e41e800396bc7ed2b6f5288b2`; S095 ordinary two-parent merge, prompt S096 blob `e0caa269ff4a90ab81a0cd2dddeff31dff9aab04`. Claim CLM-0336 is precisely the *separation* stated here; all stronger universal implications remain open.

## 1. A single coherent 59-index assignment, with carries never suppressed

Use standard integer representatives 0..19, componentwise arithmetic modulo20. Put `q=(0,0,1)` (parity quotient) and `t=(1,1,0)` (the only parity of all 22 original pairs), so `P_q=empty`. Distinct **indices** may carry identical values. Declare all original pair indices as follows:

| Actual pair labels | Count | a_i in G20 | b_i in G20 | (a_i+b_i)/2 in H10 |
|---|---:|---|---|---|
| i=1,...,8 | 8 | (1,1,0) | (1,19,0) | e1 |
| i=9,...,16 | 8 | (1,1,0) | (19,1,0) | e2 |
| i=17,...,22 | 6 | (19,1,0) | (1,19,2) | e3 |

The displayed division is the uniquely defined `iota^{-1}:2G -> H`, not an illicit group decomposition. In every row both endpoints have exactly actual quotient parity `t`. Hence `U*=e1^8 e2^8 e3^6`. Its indexed subset sums cannot vanish nontrivially in H: their coordinate counts lie in `[0,8]x[0,8]x[0,6]`, each strictly below10.

Choose the **seven distinct original singleton labels**:

| Original index | G20 value |
|---|---|
| X1=s_(100) | (1,0,0) |
| Y1=s_(101) | (1,0,1) |
| X2=s_(010) | (0,1,0) |
| Y2=s_(011) | (0,1,1) |
| X3=s_(110) | (1,1,0) |
| Y3=s_(111) | (1,1,1) |
| S=s_q | (0,0,1) |

Here the binary subscript records quotient parity in coordinate order (e1,e2,e3); `r3=r1+r2` in Q. Their three actual paired group totals are `V1=(2,0,1)`, `V2=(0,2,1)`, `V3=(2,2,1)`, all of parity q. Set seven of the eight **distinct indexed** `g_1,...,g_7=(0,0,1)` and the eighth `g_8=(0,0,17)`; all have parity q.

There are exactly `2*22+8+7=59` original indices. The **full original G20 sum**, not merely projected parity, is
`2 sum U* + V1+V2+V3+S+sum g = (16,16,12)+(4,4,3)+(0,0,1)+(0,0,24)=(20,20,40)=0 mod20`.
Every coordinate, carry and full/proper exception has been exhibited explicitly.

## 2. Four SAME physical Fano values and exact S060 C/Delta

The only even Fano triples, all true *disjoint original singleton* selections, are
`L0={X1,X2,X3}`, `L12={Y1,Y2,X3}`, `L13={Y1,X2,Y3}`, `L23={X1,Y2,Y3}`.
Their legitimate H half-sums are
`x0=(1,1,0)`, `x12=x13=x23=(1,1,1)`.
They are NOT four independently fabricated abstract E-extension values.

The original S060 sum constraint is checked exactly:
`x0+x12+x13+x23=(4,4,3)=overline(V1+V2+V3)` in H.
For all three switched pairs `ij=12,13,23`,
`rho(xij-x0)=(0,0,1)=Delta_ij`.
In fact `iota^{-1}(V1+V2)=(1,1,1)`, `iota^{-1}(V1+V3)=(2,1,1)`, `iota^{-1}(V2+V3)=(1,2,1)`; adding the prescribed `r_i+r_j` mod2 produces exactly (0,0,1) in every case. This proves the real C/Delta equations, including all original G20 carries.

The axial **negative indexed full-pair box** is
`B(U*)={(-k1,-k2,-k3):0<=k1<=8, 0<=k2<=8, 0<=k3<=6}`.
Therefore `E(U*)=H\B(U*)` contains *every* H value whose first or second coordinate is exactly1.

Every S060 `I=empty` Fano shift chooses `delta in {0,1}` and an actual labelled `J subset [8]` with `delta+|J|` even. Its full G sum `delta S+sum_J g_j` has zero horizontal coordinates and even third coordinate, hence its true H half-sum is `(0,0,k)` for some k mod10. Thus for each of the FOUR actual x values, *all 256 genuinely indexed even q-shifts* `x+(0,0,k)` lie in `E(U*)`: the first and second coordinates remain1. This proves **4*256=1024 labelled Fano extension tests** in the exact `F_0=F_*` family (`P_q=empty`), without inspecting 1024 cases or claiming independence.

## 3. Both ACTUAL endpoints of all 22 non-q pairs: every even q-shift mixed test passes

The only original non-q singleton parity class is `t=110`, so its genuine singleton is `s_t=X3=(1,1,0)`. The only even Fano triples omitting THIS physical original index are `L13` and `L23`; their common half-sum is `x=(1,1,1)`. For each pair i, write `sigma_alpha=(alpha_i+s_t)/2` via the legitimate G20 even-subgroup inverse, and `h_alpha=x+sigma_alpha`. Directly from the **actual** endpoint values:

| i class | h_a | h_b | Fixed H coordinate that guarantees membership in E(U*\\i) |
|---|---|---|---|
| e1, 8 genuine pairs | (2,2,1) | (2,1,1) | first coordinate 2 is allowed after deleting e1: A_(i,1)={1,2} |
| e2, 8 genuine pairs | (2,2,1) | (1,2,1) | second coordinate 2 is allowed after deleting e2: A_(i,2)={1,2} |
| e3, 6 genuine pairs | (1,2,1) | (2,1,2) | first coordinate1 for a, second coordinate1 for b after deleting e3 |

For the e3 deletion the remaining axial pair box has bounds `(8,8,5)`, so both first and second slab sets are `{1}`. For e1/e2 deletions the relevant bound7 gives the corresponding `{1,2}` slab. These are **true E(U*\\i)**, not the weaker `E(U*)` substitution.

Appending ANY subset of `g_1,...,g_8,S` with **even cardinality** preserves even G parity of each five-index mixed support and changes its half-sum only in the third H coordinate. The tabulated horizontal escape coordinate never changes. Consequently both actual endpoints of each of 22 actual pairs pass BOTH omitted Fano-line E(U*\\i) tests with ALL 256 labelled even q-outsider selections. This is `22*2*2*256=22528` genuine mixed-index extension tests proved by one common coordinate argument; they are not a claim that 22528 different mathematical constraints are independent. Every support is nonempty proper (it contains the split endpoint but omits its true mate).

For clarity: this verifies one-split mixed Fano + q-only-shift gates. It does NOT verify arbitrary multi-splits, masks with other singleton choices, all 2048 outsiders, or all matching atoms.

## 4. NONE of the three S095 trigger hypotheses holds anywhere in this fixed 512-fibre

**CLM-0333:** For an actual **even-parity outsider-only** index subset R, let p_l be the parity of its number of singleton labels from physical coset l. Horizontal parity vanishes iff `p1+p3=p2+p3=0` in F2. Thus either `p=000` or `p=111`. In the latter case R selects exactly ONE of X_l/Y_l from each coset. The true horizontal integer sum is then precisely (2,2), independent of the selected Y variants and of all vertical q outsiders; its real half-sum has horizontal components **(1,1) modulo5**. The CLM-0333 required residues `h1,h2 !=1 mod5` are absent. Adding any physical singleton 10d lift changes half-sums by5 and cannot alter these residues. Hence no nonzero-p outsider R in this physical fibre can trigger CLM-0333.

**CLM-0334:** It requires one genuine non-q pair parity index in each of THREE singleton cosets. All 22 actual pair parities are t=110 in the THIRD coset; the first two have no such index. Therefore the antecedent is impossible for this entire 512-fibre regardless of corner values.

**CLM-0335:** In the actual e1,e2,e3 pair classes the fixed legitimate endpoint half-differences `(b_i-a_i)/2` in H are respectively `(0,9,0)`, `(9,0,0)`, and `(1,9,1)`. No coordinate of ANY of these vectors equals5 mod10, so CLM-0335's necessary five-separated coordinate equality is impossible. Singleton 10d shifts do not change endpoint differences. Therefore that trigger is absent in the entire fibre.

This excludes exactly the THREE *stated sufficient trigger hypotheses*, not every possible axial obstruction. It remains consistent with additional obstructions (indeed the next section exhibits one).

## 5. A fatal **p=000 q-group matching** zero, entirely independent of all physical singleton lifts

The **four distinct original outsider indices**
`R0={S,g_8,g_1,g_2}` have G20 sum
`(0,0,1)+(0,0,17)+(0,0,1)+(0,0,1)=(0,0,20)=0`.
This is a legitimate nonempty **PROPER four-original-index zero** in the 59-index dataset. It selects none of X_l/Y_l, so its original p mask is `000`. It remains zero under **every** singleton 10d physical lift, because none of its four physical indices changes.

It also specifically defeats the demanded **all q-supervertex perfect-matchings**: among the twelve actual q groups, match (S,g8), producing H block (0,0,9), and (g1,g2), producing H block (0,0,1); pair the remaining eight q group labels arbitrarily. These TWO real blocks sum zero in H, and the resulting 28-block H sequence has a nonempty proper zero subcollection, despite U* itself being zero-sumfree. This is a genuine q matching failure, not a synthetic edge transplanted across matchings. The offending grouped q subset belongs to the S060 pair-respecting proper outsider family, **not** the 2048 Fano-transversal residual class.

A false move would be to invoke one of CLM-0333–0335 automatically because the full 512-fibre is dead. Those hypotheses are demonstrably absent. Instead the invariant p=000 q gate (which S094 correctly kept separate from seven gauge channels) catches the zero directly.

## 6. CLM-0336 and honest proof boundary

**CLM-0336 (physical local-gate separation; PROGRAMME_PROVED, INTERNAL).** There exists a completely specified total-zero 59-original-index S060-profile axial `G20^3` physical assignment with (i) actual `U*=e1^8 e2^8 e3^6` zero-sumfree, (ii) exact four same-six-index Fano x values satisfying full C and all three Delta, (iii) all 1024 labelled Fano F0 tests, (iv) all 22528 genuine both-endpoint omitted-Fano non-q one-split + even q-shift E(U*\\i) tests, and (v) no CLM-0333/0334/0335 trigger anywhere in its 512 physical singleton-lift fibre; nevertheless it contains the explicit invariant **p=000** proper original four-index zero R0 above, violating a demanded actual q matching atom.

Proof is the complete original label assignment, coordinatewise calculations, E slab arguments and support R0 in sections1–5. The asserted extension-test counts follow solely from counts of labelled subsets; **no mathematical search or enumeration of lifts** occurred.

**What this really disproves:** the implication `U* zero-free + SAME x/C/Delta + full F0 + all omitted-Fano one-non-q-split even q shifts => some S095 trigger` is FALSE, even for genuinely coherent original G20 positions and total0. None of those local tests alone can replace the physically indexed p=000 q-matchings. Likewise it exposes why q gate constraints must be incorporated BEFORE attempting a trigger-forcing theorem. The example is not a counterexample to an implication whose antecedent additionally contains the complete all-q-matching and 2048-outsider gates: it deliberately FAILS the former.

**Unproved after S096:** Whether the *full* original twelve-q all-matchings + 2048 outsiders + same four Fano C/Delta + q multi-splits + all signed non-q splits force one of CLM-0333–0335, or some DIFFERENT original zero, remains OPEN. No such universally q-gated physical model was constructed. Full8/exact12/13+, 26 hubs, alternative P26, arbitrary U22 and unrestricted G59 are unaddressed. No zero-sumfree G58, no `D(C20^3)=58`, no source promotion, no Phase1 PASS.

## 7. Gate coverage matrix and failure analysis

| Required issue | Actual S096 verification | Boundary |
|---|---|---|
| 59 indices, true quotient t/q, G20 sum/carries | Fully explicit 22 pairs, eight g, seven s, total (20,20,40) | Model is nonminimal |
| Same six X/Y; four x, C and Delta | All verified from genuine physical values | Does not imply H28 atom |
| U* zero-sumfree and E(U*\\i) | Proven indexed axis-box escape | Restricted axial family |
| Actual 256 shifts for each of 4 Fano lines | All 1024 F0 tests pass | P_q=empty, so no nontrivial q split I |
| Non-q one-split both endpoints and both omitted Fano lines | All 22528 even-q-shift mixed tests pass | Multi-splits, other singleton masks OPEN |
| CLM-0333–0335 trigger antecedents | All absent throughout 512 physical lifts | Other obstructions possible |
| Twelve real q groups, all matchings | Explicit FAILED matching on real (S,g8),(g1,g2) | Cannot be called globally gated |
| 2048 ungrouped outsiders / multi-splits | Not checked completely | OPEN, no false PASS |
| Proper/full mask, torsion invariant p000 | Explicit R0 length4 remains proper under all singleton lifts | Shows missing input essential |
| 26 hubs, FULL8/12/13+, U22/P26/unrestricted G59 | None solved | OPEN |
| G58 zero-sumfree, D(C20^3)=58 | None | NOT CLAIMED |

**Hostile audit:** literal singleton names vs values are distinguished, V_i are true pair sums, q matching uses disjoint original groups, all displayed halves have even full G parity, H reduction mod10 is correct, original q-only subset R0 is proper, E(U\\i) boxes use deletion, the 512 fibre is not scanned, and no conditional S095 theorem is contradicted. The entry main was unmodified during this proof. INTERNAL SAME_EXECUTOR only.
