# S038 — Mixed low–high neighbourhood containment forces critical Psi witnesses

Date 2026-10-13. One independently owner-authorised bounded Phase-1 ORIGINAL-primary-source SYMBOLIC Route A session; **CLM-0141 PROGRAMME_PROVED within its conditional hypotheses**, not a classical rank-three Davenport theorem. Entry main \`50cd0b277aeadaf85ec653c6d0742c367473ce79\` is the ordinary two-parent S037 PR #37 merge (parents \`6168aa6578836dc0a8b95cf0dded8cb797d949ba\` and \`6496a8a3840cadfc16f483d6145a976f484fcd1a\`, S037 single head parent the first and tree \`d98f8cfa2a97cd365b4c082866aa5bb1443f0848\`). S038 unused at entry, Phase 1 IN_PROGRESS, zero open PRs / competing S038 branches. Route A1 opposing projective cancellation upper remains unproved; Route A2 indexed block-neighbourhood analysis succeeded, FIRST substantial theorem STOP. A3 and Route B not executed.

## Standing indexed hypotheses

Let p>=7 be an odd prime; N=3p=2b+1, b=(3p-1)/2, a=b-1, s=(-1)^b, t=(p+s)/2. Suppose Z=(z_v:v in I) is a length-N ZERO-SUM sequence in F_p^3 with **no nonempty zero-sum subsequence of length <=a**. Let F be the COMPLETE family of indexed b-subsets summing to zero. S029 gives m=|F|=kp>=2p, each r_i=t (mod p); S030 gives the critical coefficient

  Psi_ijk=-1/2+s(lambda_ij+lambda_ik+lambda_jk-2 tau_ijk) (mod p).

S031: sum_(k not i,j) Psi_ijk=s(lambda_ij-t). S036: sum_(k not i,j) z_k Psi_ijk=0. S037: any nonempty pair Psi-support has >=3 distinct projective z_k directions, since parallel-fibre weighted Psi*z contributions are equal and 1<=c_d<=p-1. NO pair positivity premise is imported; pair-cover is BOTH OR NEITHER, NOT BOTH.

For this session **add m=2p**. Then r_i=t at L=(3p+2+3s)/2 LOW indices and r_j=T=t+p at H=(3p-2-3s)/2 HIGH indices. Both degree levels are exact integer counts. For each indexed i define F_i={B in F:i in B}.

## CLM-0141 — every low–high pair has critical Psi support

**Theorem.** For EVERY low i and high j, at least three distinct indices k outside {i,j} satisfy Psi_ijk !=0. Write F=# {(i,j):i low,j high, lambda_ij=t}, and h(p)=min{h>=0: binom(h,floor(h/2))>=p}. More sharply, each of these F *nonexceptional* mixed pairs has at least h(p) distinct active third indices, where h(p)>=5 for every p>=7 (h(7)=5; h(13)=6). Each of the LH-F other mixed pairs has at least three active third indices. Consequently, with W=# unordered deletion triples with Psi!=0,

  2W >= 3(LH-F)+h(p)F = 3LH+(h(p)-3)F,
  W >= ceil((3LH+(h(p)-3)F)/2) >= ceil(3LH/2).       (NEW)

At p=7: s=+1,b=10,t=4,L=13,H=8,LH=104, so **W>=156** (previous unconditional S037 W>=87). In fact W>=156+F since h(7)=5.
At p=13: s=-1,b=19,t=6,L=19,H=20,LH=380, so **W>=570** (previous unconditional S037 W>=383). In fact W>=570+ceil(3F/2) since h(13)=6.
Here "unconditional" refers to not assuming universal pair positivity P **inside the hypothetical Z,m=2p**. No existence of Z and no contradiction are claimed.

**Proof, case 1: mixed pair exceptional.** Since r_i=t as an exact integer, 0<=lambda_ij<=t<p. If lambda_ij<t, the S031 scalar moment s(lambda_ij-t) is a nonzero element of F_p, so pair support is nonempty. S037's exact projective-fibre theorem yields at least THREE distinct active third-index projective directions, hence at least THREE eligible indexed k.

**Proof, case 2: mixed pair has zero scalar moment.** If lambda_ij=t, then ALL t blocks containing low i also contain high j, i.e. F_i subset F_j. There are **exactly p additional DISTINCT indexed b-blocks** A=F_j\F_i (because |F_j|=t+p). Every B in A contains j and avoids i; write its incidence row on I\{i,j}, a binary word of length N-2 and weight exactly b-1. For eligible k define mu_k=# {B in A:k in B} (integer 0..p). Since F_i subset F_j, lambda_ik=tau_ijk and lambda_jk=lambda_ik+mu_k. Substitution into the ACTUAL critical coefficient yields

  Psi_ijk=-1/2+s(t+mu_k)=s mu_k in F_p

because st=1/2. Therefore **Psi_ijk!=0 iff 1<=mu_k<=p-1**; columns of the p-by-(N-2) A-incidence matrix are precisely active when they are NOT constant across all p rows. Let h count these variable columns. Every other column is identically 0 or 1. The p DISTINCT equal-weight incidence rows differ only on the h variable columns and have the SAME Hamming weight among those h columns; therefore there are at most binom(h,w) <= binom(h,floor(h/2)) possible distinct rows, for some integer w. Since there are exactly p distinct rows, p<=binom(h,floor(h/2)), hence h>=h(p). Since binom(4,2)=6<p for every p>=7, h(p)>=5. For p=7, binom(5,2)=10>=7, yielding h(7)=5. For p=13, binom(5,2)=10<13<=binom(6,3)=20, yielding h(13)=6. All h active indices are outside i,j. S037 independently ensures they occupy at least three projective directions. **This uses no polynomial coefficient vanishing assumption** and no numeric search.

**Counting.** There are exactly LH unordered mixed pairs, each with either >=3 witnesses or, in the F containment case, >=h(p). Count (mixed pair, nonzero-Psi triple containing it) incidences. An unordered triple of vertices in a LOW/HIGH bipartition has either 0 (all one type) or exactly 2 mixed constituent pairs (two one type, one the other). Thus each nonzero triple contributes at most **TWO**, not three, to this incidence count, giving the inequality as stated. This is a necessary **lower** support bound, not an actual-Z upper.

## Additional exact neighbourhood identity, useful for future orientation work

If any pair i,j (any degree type) has **identical** block neighbourhoods F_i=F_j, then lambda_ij=r_i=r_j and for every eligible k, lambda_ik=lambda_jk=tau_ijk. Therefore Psi_ijk=-1/2+s r_i=0 for EVERY third k (r_i=t modp). In particular at m=2p low–low nonexceptional pairs with lambda=t are full twins and have zero pair Psi-support; at s=-1 high–high nonexceptional lambda=T are full twins and have zero pair Psi-support. This is NOT true of low–high lambda=t: strict containment leaves exactly p extra high-only blocks and necessarily forces multiple nonzero witnesses. The distinction is the core reason S031's scalar moment cannot simply classify supported pairs.

## Adversarial checks, first STOP, and provenance

Independent SAME-EXECUTOR internal reconstruction: (i) containment F_i subset F_j iff lambda=t for LOW i; (ii) exactly p distinct A blocks, all contain j, avoid i, have b-1 OTHER positions; (iii) mu_k integer 0..p and reduction modp is zero at BOTH 0,p, nonzero at 1..p-1; (iv) Psi=s mu sign for BOTH s=+1 and s=-1; (v) variable columns all have common row weight and central-binomial ceiling, with p7 h5/p13 h6; (vi) mixed-edge capacity of any indexed triple is 2; (vii) p7 L13 H8 W>=156 and p13 L19 H20 W>=570; (viii) S037 three projective directions, S036 vector, S033 star -1/8 and global 0, indexed multiplicities, pair-cover BOTH/NEITHER, GL3, complement of b block has b+1, finite-field cancellations all compatible. No inference of forbidden 0/1 zero-sum from collinearity or from nonzero Psi. The sum of all Psi over each mixed containment pair is 0 modp, consistent with sum mu_k=p(b-1); nonzero individual coefficients can sum to zero. Twin-pair pointwise vanishing is consistent with zero scalar and vector moments. The coarse S032 U>=p²+10p-8 is a LOWER bound on raw upper-capacity U and cannot contradict W>=156 or W>=570.

STOP at this first substantial scoped original-programme theorem CLM-0141. A1 genuine actual-Z-dependent upper and cancellation/overlap remain unproved, A3 m>=3p not attempted, B D2(Cp³)<=6p-6 not activated. NO m=2p exclusion, p>=7 strong <=a extraction, omitted BSP rank-three Lem2.3 proof, classical D1/Dk result, candidate, search, solver, Lean, Palomar, source-status upgrade, campaign, external review, manuscript, contact or publication.

Read-only direct original-primary SRC-0021: Bhowmik–Schlage-Puchta (2012) definitive author-hosted publisher offprint, printed pp22–24 and printed p23 image (PDF page 3 / zero-based 2), URL https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf . Its printed Lem2.1 states <=(3p−1)/2; the p23 passage uses <=3(p−1)/2 without supplying an independently verified proof; printed rank3 Lem2.3 proof is omitted. THIS CLM-0141 is programme-internal algebra, not attributed to authors. Sheikh full Chapter4 UNREAD, GHST original C53 complete code/output UNREAD and NEVER RUN, original complete independent Yiu M1 final verification unauthenticated (M2/M3 separate). No upgrades to historical source access.

Original30 frontier JSON row objects and exact full ordered Markdown table rows, 28 original source records/access enums, five intervals and n6=16 unchanged; Phase1 IN_PROGRESS; Phase2/3 NOT_STARTED; CAM-0001 PROPOSED / NOT RUNNING / BLOCKED. Hosted workflows/checks absent NOT PASS, protection 403 UNKNOWN. S039 FUTURE ONLY.