# S032 — Projective light-hyperplane support, incidence moments and a precise coarse-bound no-go

Date 2026-10-12. One owner-invoked Phase-1 ORIGINAL-primary-source symbolic mathematics/provenance session, Route A only; no candidate, CAS, numerical mathematical search, solver, orbit enumeration, Lean, Palomar, campaign or publication. Entry LIVE main a8d268c9dd6aa98781e08982d8a448b67c72f693, tree 9aaf5ae3a6e461aefd5349ee04cc86a77cb8cc75. S031 single branch commit 02638aa12c38bd75fd6eb287feaafad20e26105f has sole parent eed11ce4a6e05515198e48a32ba8cc8165bc375c and tree 9aaf5ae3a6e461aefd5349ee04cc86a77cb8cc75; PR31 genuine non-force two-parent merge has parents [eed11ce4a6e05515198e48a32ba8cc8165bc375c,02638aa12c38bd75fd6eb287feaafad20e26105f] and equals LIVE main. No competing S032 PR/branch existed at entry.

## Hypothesis and previous bounds

Fix an odd prime p>=7, N=3p, b=(3p-1)/2, a=b-1, s=(-1)^b, t=(p+s)/2. Let indexed Z=(z_i:i in I) be zero-sum in F_p^3, |I|=N, without nonempty zero-sum on <=a positions. Each z_i is nonzero. The COMPLETE indexed family F of b-zero-sum subsets has m=kp >=2p, degrees r_i=t+p j_i. At m=2p, there are L=(3p+2+3s)/2 low-degree indices and S031 CLM-0130 forces at least B=ceil(L(b+1)/6) *NONZERO* coefficients Psi_D, D an unordered deletion triple. Psi_D was precisely defined and field-sum-proved in S030; S031 proved the projective representation
 Psi_D = sum_[X in P^2(F_p)] prod_(i not in D) <X,z_i>.
Every product is projectively well-defined because 3p-3=3(p-1). Strict Chevalley–Warning does NOT apply after three deletions.

## CLM-0132 (PROGRAMME_PROVED): exact sparse projective support decomposition

For each projective functional [X] define the indexed ZERO FIBRE H_X={i in I:<X,z_i>=0}, h_X=|H_X|. This is unchanged by scaling X, and may contain repeated vector directions at *distinct* positions. For each |D|=3 we have the EXACT identity
 Psi_D = sum_([X]:H_X subseteq D) prod_(i not in D) <X,z_i> in F_p.
Indeed every summand in the S031 projective formula is zero unless all of its zero factors lie among the three deleted original positions. Conversely whenever H_X is contained in D the product consists of nonzero scalars. Such summands may still cancel in F_p; the identity must NOT be turned into a nonvanishing equivalence.

Let Q_j=# {[X]:h_X=j}, q=p^2+p+1. Then
 # {D:|D|=3, Psi_D !=0} <= min( C(N,3), U ),
 U=C(N,3)Q_0+C(N-1,2)Q_1+(N-2)Q_2+Q_3.
Proof: a fixed X with h_X<=3 can occur for exactly C(N-h_X,3-h_X) deletion triples. With h_X>=4 it can occur for none. The union bound covers every nonzero coefficient, with potential overlap and cancellation only reducing support. This is an *upper bound*, not an equality or a claim that the coefficient vanishes without a light hyperplane.

For a PAIR {i,j}, S031 pair-sum proves lambda_ij !=t (mod p) implies at least one nonzero Psi_{ijk}. Such a triple must contain H_X for some [X]. Counting the pairs that can be extended to a triple containing H_X yields the further necessary condition
 #{ {i,j}:lambda_ij != t (mod p) } <= C(N,2)(Q_0+Q_1)+(2N-3)Q_2+3Q_3.
For h=0 or1 ANY pair can be extended; for h=2 the pair must contain at least one of the two H_X positions, giving C(N,2)-C(N-2,2)=2N-3; for h=3 both pair indices must be among its three zero positions, giving 3. Pair counts can overlap, and no independent witness for each pair is asserted. Under m=2p S031 gives at least ceil(L(b+1)/2) pairs with lambda_ij !=t, since L(b+1) low-first-index directed pairs have at most two orientations per unordered pair. Thus both inequalities must hold for any ACTUAL indexed Z.

## CLM-0133 (PROGRAMME_PROVED): exact projective line-incidence deficit and factorial second moment

A nonzero vector z specifies one point of the *primal* P^2 and lies in exactly p+1 projective functional kernels: one projective line in the dual plane. Consequently, for N=3p,
 sum_[X] h_X=N(p+1)=3p(p+1)=3(q-1);
 hence **sum_[X] (3-h_X)=3**, exactly as an INTEGER.
In Q-counts this is 3Q_0+2Q_1+Q_2 - sum_{j>=4}(j-3)Q_j=3. In particular some functional has h_X<=2, but this does NOT force a Psi coefficient nonzero.

There is also an exact second factorial moment. Let c_d denote indexed multiplicity of each distinct ONE-DIMENSIONAL projective vector direction d (sum_d c_d=N), and E_par=sum_d C(c_d,2). Every pair of NONPARALLEL vectors is annihilated by exactly one projective functional; every pair of PARALLEL vectors is annihilated by p+1 distinct projective functionals. Double-counting indexed pairs therefore gives
 sum_[X] C(h_X,2)=C(N,2)+p E_par.
The directions here are distinct lines through zero, not distinct vector VALUES, and h_X counts indexed occurrences. This is a robust exact rank-three geometric incidence identity, not an exclusion of any configuration.

An additional elementary no-short prerequisite is c_d<=p-1. If p indexed nonzero vectors lie in the same 1-dimensional F_p-subspace, write them as nonzero scalar multiples of its generator; the p-term scalar sequence has a nonempty zero-sum among at most p terms by partial-sum pigeonhole, and p<=3(p-1)/2 for p>=3. This contradicts no-short. In particular at least four distinct projective directions occur when N=3p and p>=7, but NOT p+1 directions in some single plane.

## CLM-0134 (PROGRAMME_PROVED scoped NO-GO): raw light-hyperplane union capacity cannot by itself contradict S031

The raw cover budget U above is universally *too large* to oppose the S031 lower bound B using only the first projective incidence identity. In fact for EVERY nonzero indexed Z of length N=3p and p>=7,
 U >= q+3N-9 = p^2+10p-8.
Proof without numerical search: set H=sum_{j>=4}Q_j and E=sum_{j>=4}(j-3)Q_j >=H. From the exact deficit identity Q_2=3-3Q_0-2Q_1+E; also Q_3=q-Q_0-Q_1-Q_2-H. Substitution gives, EXACTLY,
 U=q+3(N-3)
  +[C(N,3)-1-3(N-3)]Q_0
  +[C(N-1,2)-1-2(N-3)]Q_1
  +(N-3)E-H.
For N>=21 the two bracket coefficients are nonnegative and (N-3)E-H >=(N-4)H>=0, proving the inequality. Since L<=(3p+5)/2 and b+1=(3p+1)/2,
 B <= ceil((3p+5)(3p+1)/24) < p^2+10p-8 <=U
for p>=7 (direct multiplication shows margin (15p^2+222p-197)/24>1). Also C(N,3)>=B. Thus EVEN the capped upper bound min(C(N,3),U) is always >=B. **A contradiction cannot be derived by comparing these two raw numeric bounds alone.** This does NOT prove no other upper bound or refined overlap/cancellation argument exists; such improvements may be decisive.

Exact p=7 parity/hand arithmetic: b=10, a=9, s=+1, t=4, N=21, q=57, L=13, B=ceil(13*11/6)=24 and low-pair bound ceil(143/2)=72. U>=57+63-9=111. If Q0=Q1=0 then Q2=3+sum_{j>=4}(j-3)Q_j>=3, so the simplistic idea that there is at most one light h=2 point is INCONSISTENT with the incidence deficit. The rough pair capacity with Q0=Q1=0 is (39 Q2+3Q3); it is not forced below 72. These are purely symbolic substitutions, no instance search.

## Independent adversarial reconstruction, hard STOP

A separate SAME-EXECUTOR internal pass (not external review, formal verification, or hosted CI) redid the zero-fibre subset direction, q and (p+1) line count, parallel/nonparallel pair multiplicities, pair-coverage capacities for h=0/1/2/3, E>=H and every sign/coefficient in U. It checked that h=0 or1 creates large capacity, h>=4 contributes NOTHING to a triple, and **raw union cover** can overcount dramatically through shared deletion triples and F_p cancellations. For p=7 confirmed U>=111 versus B=24 and 72 forced exceptional pairs. A superficially tempting inference that all projective points satisfy h>=4 is IMPOSSIBLE by sum (3-h)=3; another tempting inference that the union-capacity comparison excludes m=2p is disproved by the universal inequality just proved. p+1 *distinct projective directions* on a line is not equivalent to p+1 repeated copies of one direction. No m2p contradiction is claimed, and m>=3p is untouched.

FIRST essential unclosed extension: obtain an actual Z-dependent sharpened upper bound on the UNION size, on cancellation patterns, or on geometry of light hyperplanes/zero fibres paired with b-block incidence which falls below B, or independently establish strong p>=7 extraction. First moments and unrefined witness capacities provably cannot do so. Route B D2<=6p-6 was NOT separately activated. No D1/Dk endpoint, sequence, full rank-three Davenport counterexample, novelty/priority claim, paper or campaign.

## Primary provenance and immutable frontier

Original definitive Bhowmik–Schlage-Puchta publisher offprint, Contemporary Mathematics 579 (2012), pp22-24, https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf, inspected freshly at its printed p23 image and pp22-23 text. The stated Lemma2.1 threshold <=(3p-1)/2 differs from the unsupported stronger <=3(p-1)/2 passage on p23; original rank3 Lemma2.3 proof explicitly omitted. CLM-0132/0133/0134 are PROGRAMME-INTERNAL deductions using S031 projective identity, NOT authors' claims. Original Sheikh2017 full Chapter4 and GHST C53 full original author code/output UNREAD; no author code executed. Yiu 2026 final independent M1 disjointness implementation/log/certificates unauthenticated; 98622/230983 are generator counts, NOT final verification. n15/20/21/28/30 primary exact source statuses unchanged; no new direct source authentication or present-day openness inference.

Thirty original frontier JSON row objects and all 30 Markdown n/group/D*/bounds/status/full ordered-evidence table rows unchanged; historical25 and intervals n15:43..45,n20:58..59,n21:61..63,n28:82..83,n30:88..90 preserved. Schmid n6=16, van Emde Boas/Yiu SOURCE_STATED, inherited 14/17,+5,43/699/5553 quarantined. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED/NOT_RUNNING/BLOCKED n6=16. No hosted checks is NOT CI PASS. S033 FUTURE ONLY.