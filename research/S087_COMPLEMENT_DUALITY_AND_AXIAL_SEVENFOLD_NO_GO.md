# S087 — five-outsider complement duality and complete sevenfold horizontal-axis exclusion

16 October 2026. **INTERNAL SAME_EXECUTOR hand proof; conditional on the true S060 canonical 59-ORIGINAL-index axial U*=e1^8 e2^8 e3^6 setup, not a global Davenport theorem.** Entry genuinely merged S086 main `fdc5cef563fe05fdadbe20d7dda123cb8026909f`; entry Git root tree `f5bf1ac016fa4897e7a3cc0a8f23ecab94391256`. No mathematical combinatorial enumeration, generated orbits, CAS, SAT/ILP, author code, Lean, Palomar or external independent verification.

## 1. Reconstruct the literal original-index zero witness

Write G=(Z/20)^3, H=(Z/10)^3, iota(h)=2h, P=F5^3. The actual T has **22 separately indexed complete original pairs** with H sums U*=e1^8 e2^8 e3^6, eight separately indexed g positions, one actual s_q singleton and the SAME six separately indexed X_i,Y_i singletons. Grouping the last six as three genuine disjoint V_i=X_i+Y_i produces twelve true q-supervertices. The true q groups each have parity (0,0,1); any even selection I has actual H half-sum h(I) and projected y(I) in P. The sum of all 12 projected half-values is (2,2,4).

The true indexed U*-extension set is E={h:h1=1 or h2=1 or h3 in {1,2,3}} in H, and E5={x:x1=1 or x2=1 or x3 in {1,2,3}} in P. For a **proper nonempty even q-label support** I with projected y(I) outside E5, its actual h(I) is outside E. Let k_l=(-h(I)_l mod 10), so 0<=k1,k2<=8 and 0<=k3<=6. Select ALL named ORIGINAL positions of the q groups I and BOTH original endpoints of the first k_l differently labelled U* pairs of each type e_l. Their literal G sum is 2(h(I)+sum_l k_l e_l)=0. Nonempty: I nonempty. Proper: at least one q group omitted. This is the only zero-witness promotion used; a projected survivor is NOT an original survivor.

S085/S086 already imply that if seven of the 12 projected q half-values coincide, their common third is t=3, their seven actual mod20 third coordinates are all exactly 1 or all 11, and their five projected outsiders have horizontal residual multiplicity at most three. Write the common horizontal value v=(a,b); for each outsider, let e_i be its projected third divided by 3 and w_i its projected horizontal vector minus e_i v. Then in F5, **sum e_i=1** and **W=sum w_i=(2,2)-3v**. Put C={u:u1=1 or u2=1}.

For every nonempty outsider J of size at most four, with e_J and w_J additive, S086 CLM-0300 gives:

| parity of J | zero-third necessary | fourth-third necessary |
|---|---|---|
| odd (1,3) | e_J != 1 => w_J in C | e_J != 4 => w_J+3v in C |
| even (2,4) | e_J != 2 => w_J in C | e_J != 0 => w_J+3v in C |

Each failed AVAILABLE clause gives the genuine indexed G zero above. The five-outsider J=ALL support must NOT be tested, since the only physically available fourth-third count would select all twelve q groups.

## 2. CLM-0304 — exact singleton/pair-to-quartet/triple complement duality

**Proposition.** With the genuine outsider totals e_all=1 and W=(2,2)-3v, all S086 size-3 and size-4 conditions follow EXACTLY from, respectively, the size-2 and size-1 conditions, including their distinct exceptional e-values. Conversely, each pair/triple and singleton/quartet complement has equivalent tests. Thus, inside this projected **necessary** two-layer sieve, checking all five genuine singletons and ten genuine pairs is equivalent to checking all nonempty proper outsider subsets of sizes1..4.

**Proof.** For the outsider complement J^c inside the five, e_{J^c}=1-e_J and w_{J^c}=W-w_J=(2,2)-3v-w_J. The horizontal cross satisfies the exact reflection identity u in C iff (2,2)-u in C. Hence
`w_{J^c} in C <=> w_J+3v in C`
and
`w_{J^c}+3v in C <=> w_J in C`.
A parity change occurs because five is odd. For odd J, its zero-layer trigger e_J!=1 is equivalent to the complement even fourth-layer trigger 1-e_J!=0, and its fourth trigger e_J!=4 is equivalent to the complement even zero-layer trigger 1-e_J!=2. For even J the same equivalences reverse: e_J!=2 iff 1-e_J!=4; e_J!=0 iff 1-e_J!=1. Thus singletons and complementary quartets, and pairs and complementary triples, have IDENTICAL obligations. Both sides are proper outsider supports (sizes1..4); neither derives a false all-twelve zero. QED.

This is a simplification, **not** two extra independent sources of contradictions. In particular S086's triple used in the v=0 proof can be replaced by the complementary pair, using genuine total W.

## 3. CLM-0305 — no sevenfold common horizontal value on EITHER coordinate axis

**Theorem.** Under the S060/S085/S086 true-original-index necessary q-zero avoidance, a sevenfold projected q half-value (a,b,3) must have **a!=0 AND b!=0**. Consequently the 25 possible horizontal v in F5² reduce first to the S086 24 (origin removed) and now to **exactly sixteen not-yet-excluded values**. This does NOT assert that any of the sixteen is feasible.

**Proof.** S086 removes v=(0,0). By exchanging e1 and e2 it suffices to contradict v=(0,b), b!=0. Put c=1-3b, so c!=1. Write w_i=(x_i,y_i). The two crosses are C0={x=1 or y=1} and C4={x=1 or y=c}. Their intersection is the exact vertical line x=1.

Call an outsider **strong** when its e_i is one of {0,2,3}. For a singleton both third layers are required precisely for these values, hence every strong outsider has x_i=1. For any pair (i,j) with e_i+e_j in {1,3,4}, BOTH layers are required and x_i+x_j=1. If both i,j are strong, x_i+x_j=2 and therefore their e sum must lie in {0,2}; the only compatible unordered strong pairs are (0,0), (0,2), (2,3).

**At most two strong labels.** Any triple of strong labels whose three pairs are compatible has e multiset (0,0,0) or (0,0,2). Its e sum is 0 or2, so the ODD triple must satisfy BOTH layers. But its x sum is 3, not1: contradiction. A set of at least three strong labels contains such a triple or an already forbidden pair.

Write k for the number of strong labels, necessarily 0,1,2. The total sum e_all=1 and the remaining e values in {1,4} give the following exhaustive small **symbolic congruence** table; entries show the complete five-label multiset (up to permutation):
  
| k | possible e multisets |
|---|---|
| 0 | (1,1,1,4,4) |
| 1 | (0,4,4,4,4); (2,1,1,1,1); (3,1,4,4,4) |
| 2 | (0,0,1,1,4); (0,2,1,4,4); (2,3,1,1,4) |

Indeed if p of 5-k weak values are 1 and the remaining are 4=-1, and the strong values sum S, then 1=S+2p-(5-k) modulo5; with 0<=p<=5-k this yields exactly this table (the permitted strong pairs already determined). We now rule out EVERY row using only five singleton/pair clauses and W_x=2, W_y=2-3b=c+1.

* k=1, e=(0,4,4,4,4): the e0 strong label has x=1. Every e4 label paired with it has e sum4, requiring both layers and hence x=0. But any e4+e4 pair has e sum3, requiring x_pair=1, whereas its x_pair=0. Contradiction.
* k=1, e=(2,1,1,1,1): strong e2 has x=1; every e1 label paired with it has e sum3 and thus x=0. Their full x total is then1, contradicting W_x=2.
* k=1, e=(3,1,4,4,4): strong e3 x=1, the one e1 label x=0. Every pair of the three e4 labels has sum3, hence x_i+x_j=1. Subtraction yields all three x=3 (since 2x=1). Full x total 1+0+3*3=0 modulo5, not2.
* k=2, e=(0,2,1,4,4): both strong x=1; all weak x=0 because their pair e sums with at least one of the strong labels trigger both crosses. The two e4 weak labels have e sum3 and x_pair=0, contradicting the both-layer x_pair=1 requirement.
* k=2, e=(0,0,1,1,4): both strong x=1, all three weak x=0. Each e1 singleton must then have y=c; each e4 singleton y=1. The pair of e1 labels (e sum2) has only C4 required, so 2c=c, forcing c=0 and b=2. The pair of two strong e0 labels (e sum0) has C0 required, and its x sum2 requires y_strong_pair=1. Thus the full y sum is 1+0+0+1=2, but W_y=c+1=1. Contradiction.
* k=2, e=(2,3,1,1,4): again strong x=1 and all weak x=0. Two e1 singleton y values are c and the pair e sum2 forces 2c=c, so c=0. The e4 singleton y=1. The (e2,e3) strong pair has e sum0 and x sum2, forcing its y sum1 via C0. Total y=2 but W_y=c+1=1. Contradiction.

It remains k=0: three e1 labels A_1,A_2,A_3 and two e4 labels B,B'. Their two e4 pair has e sum3 (both crosses), so x_B+x_B'=1. Hence x_{A1}+x_{A2}+x_{A3}=W_x-1=1. Let c=1-3b as above. Each e1 singleton and each e1+e1 pair must lie in **C4** (because their e sums are1 and2, respectively). We first show **c=0**. If none of the three x_A is1, the three singleton clauses force all three y_A=c; at least one x_A!=0 since their sum1, and its complementary pair of A labels has x_pair!=1, forcing 2c=c. If exactly one x_A is1, the other two sum0 and both have x!=1, hence y=c; their pair has x=0!=1 and again forces 2c=c. If exactly two x_A are1, the third x_A=4 and y_A=c; each pair of an x=1 A with this x=4 A has x sum0, forcing each such y_A=0; their remaining x=1+x=1 pair forces 0=c. Three x_A=1 cannot sum to1. Thus c=0, so b=2 and W_y=1.

With c=0 the three A singles/pairs furthermore imply: every A with x!=1 has y=0, and **if any A has y!=0, its x must equal1 and the other two A x must both equal0** (otherwise the pair with a nonzero other x forces y_A=0; if both have x1, the remaining x4 and its pair clauses force both y=0).

Write x_B=u, x_B'=1-u. If u is neither0 nor1, both e4 singleton clauses force y_B=y_B'=1. If some A had y_A!=0, its x_A=1 and its mixed e1+e4 pair with either B has x sum !=1, requiring y_A+1=1, a contradiction. Hence all three y_A=0 and the total y is2, not W_y=1.

If u is 0 or1, relabel so x_B=1 and x_B'=0; the e4 singleton B' has y_B'=1. Every A with x_A!=0 has mixed e1+e4 pair with B with x sum !=1 and therefore y_A+y_B=1. If all A y are zero, at least one x_A!=0, giving y_B=1 and total y=2. If an A has nonzero y, it is the **unique** nonzero-x A (x=1, other two x=0), so y_A+y_B=1 and once again full y=y_A+y_B+y_B'=2. Contradiction.

We have excluded all seven possible e multisets; so v=(0,b!=0) cannot occur. Symmetry excludes v=(a!=0,0). Every contradiction is a failed physically available singleton or pair third-layer clause. By §1 and CLM-0304 it gives a literal nonempty proper original G index zero completed by REAL original q members and BOTH endpoints of allowed indexed U* full pairs. QED.

**Scope:** This eliminates the eight nonzero horizontal-axis v values, in addition to S086's origin; the remaining sixteen ab!=0 are neither proven possible nor eliminated here.

## 4. CLM-0306 — two-point sum rigidity when ab!=0 (further necessary restriction, not no-go)

Suppose a,b!=0. By S086, each strong outsider (e_i in {0,2,3}) has w_i among the two points A=(1,1-3b) and B=(1-3a,1). If a strong pair has e_i+e_j in {1,3,4}, it also needs **w_i+w_j in {A,B}**. Direct coordinate equality gives:

* A+B lies in neither {A,B} (indeed A+B=A would mean B=0, impossible because B_2=1, and similarly for B).
* 2A belongs to {A,B} only if (a,b)=(3,1), in which case 2A=B.
* 2B belongs to {A,B} only if (a,b)=(1,3), in which case 2B=A.

Thus away from (3,1),(1,3), **every pair of strong outsiders must have e sum in {0,2}**. If there are three or more strong outsiders there, compatible strong pair types force any strong triple to have e multiset (0,0,0) or (0,0,2); the triple must also satisfy both layers. Its sum of A/B can be one of {A,B} only at one of three exceptional horizontal parameter values: (3,1),(1,3),(4,4). For completeness, 3A=B iff (a,b)=(1,3), 3B=A iff (a,b)=(3,1), and 2A+B=A or A+2B=B iff A+B=0 iff (a,b)=(4,4); no other three-term A/B sum equals A or B. Therefore at **every** ab!=0 outside those three exceptions, **at most TWO strong outsiders** are possible. This is only a finite-geometry NECESSARY restriction; it is not a contradiction for all weak e distributions and not an original lift.

## 5. Sixfold check and remaining original-index bridge

For six repeated q projections the S086 physical r-even/odd sets are unchanged. At v=0 all proper even outsider pairs and quartets are forced into C (their two missing e-values never coincide because beta=4/t !=0). For t=2, odd e_J=3 may escape both layers; for t=3, odd e_J=1 may do so. These exceptions prevent the universal singleton/pair/triple cross argument. No new sixfold categorical exclusion is asserted. All outsider groups here are true individually labelled original groups; this is not an independent sixfold construction.

The **unproved bridge** remains: finish the sixteen sevenfold ab!=0 cases or produce a hand-specified projected survivor passing every proper even q-support E5 gate; then check TRUE H modulo10 torsion for all actual groups, four coupled SAME-six-original Fano transversal values and C/Delta, all 2048 original outsider masks, q-split I/alpha against E(U*\\I), non-q signed pair choices, all 26 hubs and FULL8/12/13/14/>=15 mixed carries; deal with sixfold and smaller spectra and arbitrary U22/P26. Neither this proof nor S081–S086 establishes a fully S060-gated original 59-index zero-free-up-to-total sequence, an explicit G58 zero-sumfree counterexample, D(C20³)=58, or the rank-three Davenport conjecture. Original 29 source entries/30 frontier rows frozen; Phase1 IN_PROGRESS, CAM-0001 BLOCKED; INTERNAL SAME_EXECUTOR, hosted CI ABSENT_NOT_PASS.
