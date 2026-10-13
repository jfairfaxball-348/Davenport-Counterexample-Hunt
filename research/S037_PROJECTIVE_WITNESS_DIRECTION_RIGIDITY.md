# S037 — Projective parallel-fibre rigidity of critical Psi witnesses

Date 2026-10-13. ONE new owner-authorised Phase-1 ORIGINAL-primary-source SYMBOLIC Route A1 session. Independently observed entry main `6168aa6578836dc0a8b95cf0dded8cb797d949ba`, tree `7ccfd574b32127708287aa0a7fe2e11381c74e2c`. S036 atomic branch `4c2940f05a716edf6b4fd07d4394d97373d0ab85`, parent `af4a4a41b26c8ecb45bad431253976cc1cb7303b`, tree `7ccfd574b32127708287aa0a7fe2e11381c74e2c`; PR #36 ordinary two-parent non-force merge to entry main. Zero open PRs, competing S037 branches or session records. No mathematical numerical/computational search, CAS, SAT/ILP, orbit/candidate generation, historical author code, Lean, Palomar, campaigns, publication or outside contact.

## Hypotheses and exact identities

Fix p>=7 prime, N=3p=2b+1, b=(3p−1)/2, a=b−1, s=(−1)^b, t=(p+s)/2. Hypothetical indexed zero-sum Z=(z_v:v in I) in F_p^3, |I|=N, has NO nonempty zero sum of length <=a, so all z_v≠0. Let F be its COMPLETE family of indexed b-zero-sum subsets, m=kp>=2p, r_i=t+p j_i, pair codegree lambda_ij and triple codegree tau_ijk. For pairwise distinct i,j,k, exact three-deletion critical coefficient:

    Psi_ijk = [X_1^(p−1) X_2^(p−1) X_3^(p−1)] product_(v not in {i,j,k}) <X,z_v>
            = −1/2+s(lambda_ij+lambda_ik+lambda_jk−2tau_ijk)  (in F_p).

S031 scalar pair moment: Σ_(k≠i,j) Psi_ijk=s(lambda_ij−t).
S036 vector pair moment: Σ_(k≠i,j) Psi_ijk z_k=0.
S033 star at each index: −1/8; global Psi sum 0.
No assumption all critical Psi vanish; degree 3(p−1) is the boundary where standard strict Chevalley–Warning does not apply. Indexed pair-cover means BOTH or NEITHER, not 'both'.

## CLM-0140 — exact parallel-fibre exchange and THREE-direction support

**Theorem (PROGRAMME_PROVED, scoped).** Fix original distinct indices i,j. If k,l are distinct and outside {i,j}, and z_l=c z_k for c∈F_p^*, then

    Psi_ijk=c Psi_ijl,      Psi_ijk z_k=Psi_ijl z_l.       (P)

All eligible third-index positions in one projective vector direction therefore have either ALL nonzero or ALL zero Psi values, and every nonzero weighted term Psi_ijk z_k in that direction is the SAME vector. Every nonempty pair-support set {k:Psi_ijk≠0} occupies AT LEAST THREE DISTINCT projective vector directions. If exactly three indexed witnesses exist, their directions are distinct and the three projective points collinear. For an exceptional pair lambda_ij≢t (mod p), the scalar pair moment makes support nonempty. If E is the number of unordered exceptional pairs and W the number of distinct nonzero-Psi unordered deletion triples,

    3E<=3W, hence W>=E.                                    (D3)

At hypothetical m=2p: p7 s=+1,b10,t4,L13,H8,S034 E>=87 => W>=87 (previous S036 58); p13 s=−1,b19,t6,L19,H20,S035 E>=383 => W>=383 (previous S036 256). This is a necessary LOWER-support condition; neither m=2p nor m>=3p is excluded.

**Exact hand proof.** Write L_v(X)=<X,z_v>. For k,l eligible and parallel, define R(X)=product_(v in I\{i,j,k,l}) L_v(X), homogeneous degree N−4=3p−4. Removing k leaves the factor L_l=cL_k while removing l leaves L_k. Thus EXACT coefficient linearity yields

    Psi_ijk=[central]R L_l=c[central]R L_k=c Psi_ijl.

Multiplying by z_k, with z_l=c z_k, proves (P). No projective field-sum noncancellation, positivity premise P, or SOURCE_STATED rank-three Davenport theorem was used. It also proves zero/nonzero equivalence within every eligible projective direction including repeated identical values and arbitrary nonzero scalars.

For each active projective direction d among eligible k, write K_d={k outside {i,j}:[z_k]=d}, n_d=|K_d|, V_d=Psi_ijk z_k for any one k in K_d. (P) makes V_d well-defined, nonzero and parallel to d. The no-short condition gives TOTAL multiplicity of each direction among I at most p−1: p nonzero vectors on one direction give p nonzero scalars in cyclic C_p, which by elementary partial sums (D(C_p)=p) have a nonempty zero-sum of size at most p; and p<=a for p>=3. Thus 1<=n_d<=p−1, so n_d is nonzero mod p. S036 vector moment becomes

    0=Σ_(active d) n_d V_d.                                (M)

One active d would make n_d V_d≠0. Two active distinct d,e have nonparallel, hence linearly independent, nonzero V_d,V_e, so n_dV_d+n_eV_e≠0. Therefore THREE or more distinct active directions are necessary. With exactly three indexed witnesses the coefficients Psi are nonzero, the directions must all be distinct, and (M) is a nontrivial relation: rank is two (not one), so their three projective points are collinear. Every exceptional unordered pair has nonzero scalar sum and >=3 witness triples; each nonzero unordered triple witnesses at most its three unordered constituent pairs. Counting gives 3E<=3W (NOT 3E<=W). QED.

## Adversarial boundary and STOP

S036 allowed exactly-two parallel cancellation in an ABSTRACT vector moment; (P) rules it out for ACTUAL critical Psi: if two parallel eligible witnesses are active their weighted products are EQUAL, so sum is 2V_d≠0, p>=7. Crucially the factor is +c, not −c: if c=−1, both Psi and z change sign and their product remains equal. With three active directions projective collinearity is permitted and DOES NOT imply a forbidden 0/1 zero-sum. Complement of a b-block has b+1 positions, not b. For m>=3p, direction theorem survives but m2p sign-specific binary E bounds do NOT transfer. Star −1/8, global Psi 0, GL3 covariance, indexed multiplicities and finite-field cancellation remain compatible.

At p7, W>=87 while S032 coarse U>=111; no contradiction. At p13 W>=383, U>=291, BUT U>=291 is a **LOWER bound on a raw projective union capacity U** (which itself only supplies a loose upper bound on W), NOT an actual upper U<383. Inferring a contradiction by reversing the inequality is invalid. No actual Z-dependent small projective UPPER or support obstruction has been proved.

Route A1 preregistered; STOP on first substantial scoped theorem CLM-0140. A2 high-high equal block neighborhoods, A3 m>=3p degree levels and optional independently preregistered Route B D2(C_p³)<=6p−6 were NOT executed. Direct read-only original primary SRC-0021 Bhowmik–Schlage-Puchta 2012 offprint printed pp22–24 and printed p23 image: Lem2.1 only gives <=(3p−1)/2, a stronger <=3(p−1)/2 appears on p23 without a fully independently supplied proof, rank3 Lem2.3 proof omitted. CLM-0140 is entirely PROGRAMME-INTERNAL, not authors' claim. Sheikh full Chapter4 UNREAD; GHST C53 code/output UNREAD/NEVER RUN; Yiu complete independent M1 final predicate unauthenticated (M2/M3 distinct). Original 30 historical frontier row objects/full ordered Markdown evidence table and 28 source records/access remain unchanged; Phase1 IN_PROGRESS, Phase2/3 NOT_STARTED, CAM-0001 PROPOSED/NOT_RUNNING/BLOCKED n6=16. No D1/Dk theorem, D2 saving, strong p>=7 extraction, candidate, certification, external review or hosted CI PASS. S038 strictly FUTURE.
