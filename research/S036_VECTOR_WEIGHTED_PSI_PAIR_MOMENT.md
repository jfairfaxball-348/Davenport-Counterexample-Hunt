# S036 — Vector-weighted critical Psi pair moment: two-witness rigidity

2026-10-12. ONE independently owner-invoked Phase1 original-primary-source SYMBOLIC Route A session. Remote entry main af4a4a41b26c8ecb45bad431253976cc1cb7303b, tree c0e8262028003f6de43dbbeccb99cba299d3013c; S035 sole branch commit b1a6784213f87c273637535f38e36d3235e6d4e7 parent b6d6883d182815098fc9b7625635d7c1698fb054, tree identical, PR35 ordinary non-force two-parent merge equals observed entry main. No competing S036 PR/branch/record. Route A1 preregistered first: combine Psi pair sums with indexed vector zero-sums to find actual-Z-dependent cancellation/overlap. STOP at first substantial new scoped theorem. Alternatives A2 high-high identical neighborhoods and A3 m>=3p census unexecuted; optional Route B D2 saving unactivated.

## Definitions and fixed evidence

Odd prime p>=7, N=3p=2b+1, b=(3p-1)/2, a=b-1, s=(-1)^b, t=(p+s)/2. Hypothetical indexed zero-sum Z=(z_i) of size N in F_p^3 with no nonempty zero-sum of at most a positions. Every z_i is nonzero. Let F be the COMPLETE indexed b-zero-sum block family of size m=kp>=2p, r_i=number of blocks through index i, lambda_ij pair codegrees and tau_ijk triple codegrees. S029 gives r_i=t modulo p for every i; S030 gives for pairwise distinct i,j,k:

  Psi_ijk = -1/2 +s(lambda_ij+lambda_ik+lambda_jk-2tau_ijk) in F_p.

S031 gives scalar pair moment sum_(k distinct from i,j) Psi_ijk=s(lambda_ij-t). S033 gives star moment -1/8 for every i and total triple sum zero. S032 represents Psi_ijk as a projective sum whose nonzero terms may CANCEL; never silently reverse support implication.

## CLM-0139 (PROGRAMME_PROVED): exact vector-weighted pair moment and doubled support

**Theorem.** For ANY complete m=kp family (every k>=2, both signs), and every distinct original indices i,j,

  sum_(k distinct from i,j) Psi_ijk z_k = 0 in F_p^3.             (V)

If lambda_ij is not congruent to t modulo p, there are at least TWO distinct third indices k for which Psi_ijk !=0. If exactly two, their associated nonzero z_k lie in the same one-dimensional projective direction; if exactly three, the three z_k are linearly dependent. If E is the number of unordered exceptional pairs lambda_ij !=t (mod p) and W is the number of unordered nonzero-Psi deletion triples, then

  2E <= 3W, hence W >= ceil(2E/3).                               (D)

This is a conditional necessary property of the ACTUAL hypothetical indexed Z, not an abstract family contradiction.

**Complete vector hand proof.** All sums run over k distinct from i,j. Using the global Z zero sum, and for each indexed B in F the exact block zero sum, double-count:

  sum_k z_k = -(z_i+z_j);
  sum_k lambda_ij z_k = -lambda_ij(z_i+z_j);
  sum_k lambda_ik z_k = -r_i z_i - lambda_ij z_j;
  sum_k lambda_jk z_k = -r_j z_j - lambda_ij z_i;
  sum_k tau_ijk z_k = -lambda_ij(z_i+z_j).

For example sum_k lambda_ik z_k = sum_(B through i) sum_(k in B excluding i,j) z_k. Every B through i contributes -z_i, and each B also through j contributes an additional -z_j. This gives precisely -r_i z_i-lambda_ij z_j. The triple count similarly sums over every B containing BOTH i,j. Distinct indices remain distinct even if some z-values coincide.

Multiply the exact Psi expression by z_k and sum over k. The constant -1/2 contributes +(z_i+z_j)/2. The four incidence terms contribute -s(r_i z_i+r_j z_j): all lambda_ij z_i/z_j terms cancel with coefficient -1-1+2=0. Thus

  sum_k z_k Psi_ijk = (1/2-s r_i) z_i+(1/2-s r_j) z_j = 0,

because r_i=r_j=t (mod p) and st=1/2 (mod p). No source-stated Olson input, pair positivity P, omitted BSP proof or projective noncancellation lemma was imported.

For an exceptional pair, scalar sum_k Psi_ijk=s(lambda_ij-t) is NONZERO. If just one Psi_ijk were nonzero then the vector-weighted sum would equal Psi_ijk z_k !=0, since z_k !=0, contradicting (V). So at least two k are needed. If there are precisely two nonzero Psi values, (V) gives Psi_ijk z_k = -Psi_ijl z_l, forcing parallel z_k,z_l, not necessarily identical indices. If exactly three, (V) is a nontrivial linear dependence among the three vectors. Count incidences between exceptional unordered pairs and their nonzero Psi triple witnesses: every exceptional pair requires >=2, while each nonzero triple contains <=3 unordered exceptional pairs. Hence 2E<=3W.

**m=2p corollaries, all ceilings as integers.**
- s=+1, p=3 mod4: S034 proves E>=ceil([L(b+1)t+3H(t+1)]/(2t)), where L=(3p+2+3s)/2, H=(3p-2-3s)/2. Thus W>=ceil(2E/3) with the quoted lower E. At p=7: b10,a9,s+1,t4,L13,H8; 8E>=13*11*4+3*8*5=692, so E>=87 and **W>=ceil(174/3)=58** (previous S034 >=29). Mixed lambda>=1 used only in S034 for this sign, not assumed universally.
- s=-1, p=1 mod4: S035 proves E>=b(b+1)+3 using mixed/high-high transfer without any P premise. Hence W>=ceil(2[b(b+1)+3]/3). At p=13: b19,a18,t6,L19,H20, E>=19*20+3=383 and **W>=ceil(766/3)=256** (previous S035 >=128). Mixed zero codegrees remain allowed.

## Independent adversarial reconstruction / STOP

Separate INTERNAL same-executor reconstruction independently recovered every z_k-weighted block-sum coefficient and the residue st=1/2; checked scalar moment and nonzero z_k implication; checked the >=2 incidence count and exact-two parallel conclusion; rechecked p7 and p13 hand arithmetic, both signs, complements b versus b+1, multiplicity as indexed POSITIONS, projective GL3 covariance, -1/8 star and global zero. No all-pairs P, forbidden blanket three-deletion Chevalley–Warning vanishing, projective summand noncancellation or ≥3 witness conclusion is valid. In particular S032 raw U>=p²+10p-8 is a LOWER bound on an upper-capacity NUMBER, not a small actual-Z upper bound: p7 U>=111 vs W>=58, p13 U>=291 vs W>=256 DOES NOT produce contradiction. While (V) holds for m>=3p, the high/low E lower bounds only apply to m=2p. No exclusion for any m established.

**First indispensable open extension:** exploit geometry of exactly-two parallel witnesses or cancellation/overlap of actual projective zero fibres to derive a true incompatible UPPER support constraint, or attack all m>=3p degree levels. STOP at first substantial CLM-0139. No strong p>=7 short extraction, D2(Cp^3)<=6p-6, classic D1/Dk result, candidate, mathematical numerical/computational search, solver, author code, Lean, Palomar, publication, external review or priority assertion.

Fresh ORIGINAL primary SRC-0021 Bhowmik–Schlage-Puchta 2012 definitive publisher-offprint printed pp22–24 read and printed p23 visually inspected. Its Lem2.1 gives weaker <=(3p-1)/2 than a later stronger <=3(p-1)/2 step; omitted original rank3 Lem2.3 proof unproved. CLM-0139 INTERNAL only, NOT an author-attributed claim. Sheikh full Chapter4 / GHST original C53 code/output UNREAD (code NEVER RUN); Yiu independently complete final M1 predicate unauthenticated. All original30 frontier row objects/MD ordered rows and 28 source records/enums untouched; Phase1 IN_PROGRESS, Phase2/3 NOT_STARTED, CAM-0001 BLOCKED n6=16, absent CI not PASS. S037 FUTURE ONLY.
