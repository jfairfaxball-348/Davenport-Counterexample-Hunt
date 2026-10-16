# S092 — complete proper-original axial sixfold projected-fibre no-go

16 October 2026. INTERNAL SAME_EXECUTOR hand algebra, SOURCE-CONDITIONAL, not external or formal verification. Entry main b389976e3c49f49f1d3feb627506b4141d9e09ce. Entry Git tree 6d4cebfd1eea45145357959702bc5dc637758a4b reconstructed from prior independently recorded true tree a270f3b82bca0543288e04ecfec7c48c2297f395 plus all 19 S091 changed paths/blob hashes, not directly fetched via a commit-object API. S091 authored 254647b11780a689b7c72fb08dc69c5df8611480 and genuine merged PR #93; GitHub comparison from S090 merge to current main reports two commits. No numerical mathematical search, generation, CAS, SAT, ILP, Lean, Palomar, external certification or source promotion.

## 1. Exact original-index scope, and the only gates used

Use the true conditional S060/S081–S091 individually indexed 59-original G=(Z/20)^3 total-zero setup, the 22 actual COMPLETE original pairs U*=e1^8 e2^8 e3^6, eight actual g positions, s_q and the SAME six X_i/Y_i originals grouped into genuine disjoint paired V_i. The 12 physical q groups are distinct, carry a total projected half-sum (2,2,4) in F5^3, and six of them have identical projected half-value (v,3). S089 excluded t other than 3 and horizontal v=0; put v=(a,b) nonzero. Label the six OUTSIDERS by e_i in F5 and w_i in F5^2 with actual projected values (e_i v+w_i, 3e_i). Their physical total is
   sum e_i=2,  sum w_i=W=(2,2)-3v.
Write c=1-3a, d=1-3b, C0={(x,y):x=1 OR y=1}, C4={(x,y):x=c OR y=d}, P=C0 intersect C4.

For every nonempty PROPER set J of outsider labels, |J|<=5, physical original q supports provide these necessary gates:
* even |J|: e_J != 2 -> w_J in C0; e_J != 0 -> w_J in C4;
* odd |J|: e_J not in {1,3} -> w_J in C0; e_J not in {1,4} -> w_J in C4.
In particular each even pair has AT LEAST ONE gate. A pair of e-sum 1,3,4 lies in P; of e-sum 0 lies C0; of e-sum 2 lies C4. Each e0/e2 singleton lies P; e4 singleton lies C0. For all proofs below only |J|<=3 is used. NEVER treat all six outsiders as a proper support: FULL12 is exempt.

Every failed proper projected gate gives a literal nonempty proper original G zero: use the exact labelled q groups realising that permitted layer (not fictional independently chosen projections), and add BOTH ORIGINAL endpoints of k_l=(-h_l mod10) of the genuine U* full pairs for l=1,2,3 (k1<=8,k2<=8,k3<=6). Selected and omitted q groups both exist; therefore the support is PROPER. Passing projected gates is merely NECESSARY, not original H/Fano/split sufficiency.

When ab !=0, P consists of TWO DISTINCT points
 A=(1,d), B=(c,1), D=B-A=(c-1,1-d),
and W=A+B. Both coordinates of D are nonzero. On axis a=0,b!=0 the gate P is the entire x=1 line; on b=0,a!=0 it is y=1.

## 2. CLM-0323: off-exception P-fork obstruction closes six spectra

**Fork lemma.** Suppose a true strong outsider s has w_s in P, and two different outsider labels i,j satisfy both s+i and s+j pair gates in P, as well as i+j in P. On a nonzero horizontal axis this is impossible: if the prescribed P coordinate of s is 1, both i,j have that coordinate 0, hence their pair has coordinate 0, not 1.

Off-axis, if w_s=A, the pair gates require w_i,w_j in {0,D}; if w_s=B, they are in {0,-D}. Their pair must belong to {0,D,2D} or {0,-D,-2D}, respectively. Here 0 is never P. The membership of any +/-D or +/-2D in {A,B} is possible ONLY when
  B=2A, or A=2B, or B=-A,
respectively v=(3,1),(1,3),(4,4). For clarity D=A gives B=2A; -D=B gives A=2B; 2D=A gives B=4A=-A; analogous signed/mirrored equalities cover all choices. Thus the fork is impossible for ALL generic nonzero v, axes included, with no reliance on e3/4 singleton or all-six selection.

The following **six** of S091's eight generic spectra all contain a physically proper fork. We list the strong label s and the two labels i,j:
| e-multiset | s | i,j | P-pair reasons |
|---|---|---|---|
| 0 3^3 4^2 | e0 | two e3 | 0+3=3, 3+3=1 |
| 0 1^2 3^2 4 | e0 | two e3 | 0+3=3, 3+3=1 |
| 2 1 3^2 4^2 | e2 | two e4 | 2+4=1, 4+4=3 |
| 0^2 1 3 4^2 | e0 | two e4 | 0+4=4, 4+4=3 |
| 0 2 1 3^3 | e0 | two e3 | 0+3=3, 3+3=1 |
| 0 2 1^2 4^2 | e2 | two e4 | 2+4=1, 4+4=3 |

Each row produces a genuine original-index proper q gate failure on one of the indicated PAIRS, and hence a literal proper 59-original zero by section 1. No 62-clause numerical scan is asserted.

## 3. CLM-0324(a): two e0 and one e4 cannot coexist, any generic v

This covers e-multiset 0^2 1^3 4 and supplies a second independent obstruction for 0^2 1 3 4^2. Let s,t be two actual e0 outsider residuals and u an actual e4 residual. Both s,t belong to P, each s+u and t+u belongs P (e=4 pair), s+t belongs C0 (e=0 pair), u belongs C0 (e4 singleton), and s+t+u belongs C0 (e=4 odd triple). ALL are proper selected outsider supports of sizes one, two or three.

On axis P prescribed coordinate=1: s,t each coordinate1, u coordinate0; u in C0 forces its other coordinate=1; s+t in C0 (prescribed coordinate2) forces their other-coordinate sum1; s+t+u now has prescribed coordinate2 and other coordinate2, so is OUTSIDE C0. Contradiction.

Off-axis, if s,t are opposite A and B, intersections (P-A) intersect (P-B)={0}, so u=0 contradicts u in C0. If s=t=A, then s+t=2A=(2,2d) in C0 forces d=3; u from P-A={0,D} and C0 forces u=D. The triple s+t+u=A+B=W=(1+c,1+d) in C0 forces c=0 or d=0, hence c=0. Now D=(4,3) is outside C0, contradiction. The s=t=B case is coordinate-swapped: pair forces c=3, triple forces d=0, and u=-D=(3,4) lies outside C0. The proof works even at three exceptional v, but is needed here only off-exception.

## 4. CLM-0324(b): the final generic spectrum 2 1^3 3 4 fails proper gates

Let s be the e2 strong outsider, t the e4 outsider, z1,z2,z3 the e1 outsiders, and u the e3 outsider. This is precisely S091's eighth spectrum. All support tests below use at most TWO outsider labels and the physical total W.

On nonzero axis, interchange horizontal coordinates to take P: x=1, c=1. Then s_x=1; e2+e1 and e2+e4 pairs have ratios 3 and 1, so all z_i,x and t_x vanish. The e4 singleton C0 forces t_y=1. Every e1+e4 pair has ratio 0 and lies C0, hence all z_i,y=0. Every e1+e1 pair has ratio2 and lies C4, so d=0. The e1+e3 pair has ratio4 and lies P, forcing u_x=1. The e2+e3 pair ratio0 must lie C0; its x coordinate is2 so s_y+u_y=1. But the actual residual total has y-coordinate W_y=1+d=1, whereas s_y+u_y+t_y+sum z_i,y=2. Contradiction. Other axis symmetric.

Off-axis, exchange A and B if needed so s=A. Pair gates e2+e4 and e2+e1 give t,z_i in {0,D}. Since an e4 singleton has to lie in C0 and 0 not in C0, necessarily t=D.

* If the three z_i mix 0 and D: their actual e1+e1 pair with unlike residuals has ratio2 and forces D in C4, while an e1=0 plus e4=D pair has ratio0 and forces D in C0. Thus D in P, impossible outside the three exceptions by the fork arithmetic.
* If all three z_i=D: the e1+e1 pair forces 2D in C4, while the e1+e4 pair forces 2D in C0. Hence 2D in P, again impossible generically.
* If all three z_i=0: total W=A+B forces u=W-A-D=A (IMPORTANT: u=A, NOT zero). The e1+e1 pair forces 0 in C4, i.e. c=0 OR d=0. The e4 singleton t=D lies C0, i.e. c=2 OR d=0. Together imply d=0. But the real e2+e3 ratio0 pair has residual s+u=2A=(2,2d) and must lie C0, forcing d=3. Contradiction.

With s=B, interchange horizontal coordinates, use t=-D, obtain the symmetric contradiction c=0 versus c=3 in the all-zero case. Thus every generic spectrum is eliminated by literal properly available q gates.

## 5. CLM-0325: the THREE exceptional parameters, including arbitrary strong counts

Let v=(3,1),(1,3), or (4,4). Now P lies on a one-dimensional line L through 0. More precisely choose its generator h so that
- v=(3,1) or (1,3): P={h,2h}, W=3h (choose h=A for first, h=B for second);
- v=(4,4): P={h,-h}, W=0 (choose h=A).
In EACH case C0 intersect L=C4 intersect L=P. This equality is directly verified from h=(1,3),(3,1), or (1,4) and from c,d=(2,3),(3,2), or (4,4).

S091 CLM-0321 rules out an all-weak sixfold ratio multiset. Hence at least one ACTUAL strong e0 or e2 is present, with w in P subset L. We first show ALL six residuals w_i lie L, without assuming any extra strong-count cap at these exceptional v.

If an e0 occurs, every e1, e3, and e4 is connected to it by a P pair (sums1,3,4), and every e2 already lies P; thus all w in L. If no e0 but some e1 occurs, at least one e2 must be strong; e1 and e4 each connect to that e2 by P pairs (sums3,1), and every e3 connects to an e1 by a P pair (sum4). Thus all w in L.

It remains no e0 and no e1. Write n_i for the six outsider e multiplicities. Then n2>=1 and n3<=3,n4<=2 from S091; the exact e-total gives n3+2n4=0 (mod5), with 0<=n3+2n4<=7. Thus only (n3,n4)=(0,0),(3,1),(1,2) can occur. In (0,0) all six are e2 strong, already in P. In (3,1), the three e3 have ALL pair sums in P (3+3=1): modulo L their transverse images x_i satisfy x_i+x_j=0 on each of the triangle's three edges, so x_i=0 since characteristic5 is odd. All e2 and the e4 lie L (the latter connects to e2). In (1,2), all e2/e4 lie L and the single e3 does as well because the total W lies L. This establishes w_i in L in EVERY exceptional case, without a third-torsion uniformity assumption.

Write w_i=lambda_i h. Because EVERY pair carries a nonempty proper gate, and C0 intersect L=C4 intersect L=P, for each i!=j the scalar sum lambda_i+lambda_j lies in {1,2} in the first two cases, or {1,-1} in the last.

Fix one index. Among its other FIVE scalars only two values are permitted, so at least THREE of those five are equal to lambda. Their pair gives 2lambda in the two-element allowed set. For P={h,2h}, lambda is 1 or3. With lambda=1 all other scalars are 1 except at most one 0 (two zeros would sum0 outside P). With lambda=3 all other scalars are 3 except at most one 4 (two fours sum3 outside P). Since six labels exist, their total scalar sum is respectively 1 or0, or 3 or4 (mod5). The required W=3h therefore forces ALL SIX scalars to equal3. But the existing strong outsider residual must be h or2h, contradiction.

For P={h,-h}, lambda is2 or3. With lambda=2 every other scalar equals2 except at most one4; with lambda=3 every other scalar equals3 except at most one1. The possible sixfold scalar totals are 2,4,3,1 respectively, NEVER 0=W/h. Contradiction.

All three exceptions are eliminated. The values (3,4),(4,3), for which equality of the original repeated q third-torsion bits is unproved, lie outside this exceptional list and are handled by sections2–4: NO torsion-bit uniformity was assumed anywhere.

## 6. Exact consequence and hard boundary

S082–S084 forbid eightfold or higher, S085–S088 forbid sevenfold, S089 forces sixfold t3 and excludes horizontal origin, S090–S091 leave eight generic spectra and three special v, and sections2–5 of THIS proof exclude each remaining case. Therefore, under the same **source-conditional fixed ACTUAL indexed axial U*=e1^8 e2^8 e3^6 total-zero 59-position and no-proper-original-zero assumptions**, every projected half-value occurs among the twelve genuine q groups at most FIVE times. All exclusions use indexed proper supports |J|<=3; no FULL12 misuse. This is a NECESSARY projected q obstruction and yields NO actual zero-free 59-sequence.

This does NOT prove the twelve q groups as a whole impossible: six/more repeats are gone, but patterns whose every projected multiplicity is <=5 remain. It does not address full H=(Z/10)^3 actual proper E(U*) selection, the four SAME-six-original X_i/Y_i Fano x_eps coupled through C/Delta, 2048 actual outsider masks, all q split I/alpha with E(U*\\I), signed non-q original splits, 26 hubs, FULL8/exact12/13/14/>=15 carries, arbitrary U22, P26, G58 zero-sumfreeness, D(C20^3)=58, or the global rank-three conjecture. Keep source29/frontier30 original snapshots fixed, Phase1 IN_PROGRESS/HOLD, CAM-0001 PROPOSED NOT_RUNNING BLOCKED and CI ABSENT_NOT_PASS. Internal same-executor review, NOT independent verification.