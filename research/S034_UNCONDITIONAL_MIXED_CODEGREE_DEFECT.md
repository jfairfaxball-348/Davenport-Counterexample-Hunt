# S034 — An unconditional high–low defect bound for critical Psi support

Date: 2026-10-12. Exactly ONE separately owner-invoked Phase-1 original-primary-source SYMBOLIC mathematics/provenance session (Route A). LIVE entry main `95d5cf1f17539394387a309840eefcbfdd1005e4`, parent merge tree `123e00c2282ac8a32c585c2116cc71b3e2abd8c7`. Prior S033 branch `21080be3fabbe81ee00578a75eeb080d3f04f3ce` parent `a63089f7d121960e0b1dd4a9b1a1f560435b8348`, tree `123e00c2282ac8a32c585c2116cc71b3e2abd8c7`; PR #33 genuinely merged by ordinary two-parent non-force commit `95d5cf1f17539394387a309840eefcbfdd1005e4`. No competing S034 records or open PRs at entry.

## Standing hypotheses and established identities

Let p>=7 be prime, N=3p, a=3(p-1)/2, b=(3p-1)/2, s=(-1)^b and t=(p+s)/2. Let Z=(z_i) be a **hypothetical indexed zero-sum sequence** in F_p^3, length N, with no nonempty zero-sum subsequence of length <=a. Let F be its COMPLETE family of b-element zero-sum indexed blocks, m=|F|. For i!=j let r_i be the block-degree and lambda_ij the pair codegree. Let Psi_ijk be the exact three-deletion coefficient of S030. S029–S031 give, all modulo p when appropriate,

* m=kp with k>=2 and r_i=t (mod p).
* For distinct i,j, sum_{k !=i,j} Psi_ijk=s(lambda_ij-t).
* At m=2p, low degrees are r_i=t at L=(3p+2+3s)/2 indices; high degrees are r_i=T=p+t at H=(3p-2-3s)/2 indices.
* For any i, sum_{j!=i}lambda_ij=(b-1)r_i, so sum_{j!=i}(r_i-lambda_ij)=(b+1)r_i.
* S033's universal pair-positivity P is NOT established. The S030 pair-cover is the disjunction BOTH or NEITHER, NOT both.

## CLM-0137 — unconditional sign-positive mixed-codegree defect theorem (PROGRAMME_PROVED, scoped)

**Theorem.** Suppose **in addition** m=2p and s=+1, equivalently p congruent 3 mod 4. (Thus t=(p+1)/2.) For unordered exceptional pairs involving at least one low-degree index define E_LL as the number of low–low pairs with lambda_ij<t and E_LH as the number of low–high pairs with lambda_ij<t. Then

(1) Every high–low pair has lambda_ij>=1, but NO universal positivity of low–low pairs is asserted.

(2) Every high index has >=3 exceptional low partners, and hence E_LH>=3H.

(3) The total E=E_LL+E_LH satisfies
    2t E >= L(b+1)t + 3H(t+1).
Consequently the number W of unordered triples {i,j,k} having Psi_ijk !=0 in F_p satisfies
    W >= ceil( [L(b+1)t + 3H(t+1)]/(6t) ).

This conclusion requires **NO unproved all-pairs-positive premise P**. It is a necessary consequence of an ACTUAL hypothetical indexed Z with m=2p; it does not assert such Z exists.

**Proof of (1):** For two sets of blocks F_i,F_j in the complete m=2p family, inclusion–exclusion gives lambda_ij=|F_i intersect F_j| >= r_i+r_j-m. For a high i and low j the right side is (p+t)+t-2p=2t-p=s=1. Thus 1<=lambda_ij<=t for every mixed pair. The analogous bound for two low indices is 2t-2p<0, so no positive low–low codegree is inferred. For two high indices, the same elementary inequality yields lambda_ij >= 2(p+t)-2p=2t.

**Proof of (2):** Fix high i and put T=p+t. The exact degree-incidence identity gives
  (b+1)T = sum_{j low}(T-lambda_ij) + sum_{j high, j!=i}(T-lambda_ij).
For high j, lambda_ij>=2t, so 0<=T-lambda_ij<=p-t. For low j, T-lambda_ij = p+(t-lambda_ij). Hence
  sum_{j low}(t-lambda_ij) >= (b+1)(p+t)-Lp-(H-1)(p-t)
                           = 3(p-1)/2
when s=+1. For each low j, 1<=lambda_ij<=t by (1), so a positive defect t-lambda_ij is at most t-1=(p-1)/2, and a nonexception contributes zero. The displayed positive total needs at least THREE distinct low partners with lambda_ij<t. Distinct high indices identify distinct mixed unordered pairs, giving E_LH>=3H.

**Proof of (3):** Fix low i. Since r_i=t and b-blocks have size b,
  sum_{j!=i}(t-lambda_ij)=(b+1)t
as an exact integer identity, with 0<=lambda_ij<=t. Sum over all L low i:
  L(b+1)t = 2 sum_{{i,j} low-low}(t-lambda_ij)
               +sum_{{i,j} low-high}(t-lambda_ij).
A positive low–low defect is <=t (zero codegree allowed!), and a positive low–high defect is <=t-1 by (1). Therefore
  L(b+1)t <= 2t E_LL + (t-1)E_LH
           = 2t(E_LL+E_LH) - (t+1)E_LH
           <= 2t E - 3H(t+1).
Rearrange for (3). Any exceptional low-containing pair has 0<=lambda_ij<t<p, so lambda_ij is NOT congruent to t mod p. The exact S031 pair-sum identity then forces SOME k distinct from i,j with Psi_ijk !=0. Each nonzero three-element deletion set can witness at most three distinct unordered exceptional pairs (its three edges); thus 3W>=E, proving the stated ceil bound. QED.

**p=7 complete symbolic boundary test:** b=10, N=21, s=+1, t=4, T=11, m=14, L=13, H=8. Mixed codegree >=11+4-14=1. Each high index has low-defect total >=3(7-1)/2=9, each exceptional mixed partner contributes <=3, giving >=3 partners and E_LH>=24. Low summed defect is 13*11*4=572. Therefore
  8 E >= 572+5*24=692,
  E>=87, W>=ceil(87/3)=29.
Prior unconditional S031 W>=24; conditional S033 W>=37 assumes unproved P and is NOT thereby upgraded. Star moment sum Psi=-1/8=6 mod7 remains consistent. S032's coarse raw upper capacity has U>=111 at p7, so 29<111 DOES NOT yield a contradiction.

**Other sign test:** For p congruent 1 mod4, s=-1, t=(p-1)/2, mixed inclusion-exclusion only gives lambda_ij>=-1, which reduces to the trivial >=0. Therefore neither the mixed maximum defect t-1 nor the high-index three-exception conclusion is licensed. For s=-1 retain S031's unconditional W>=ceil(L(b+1)/6) and S033's merely conditional P result. No cross-sign extrapolation.

## Scope and mandatory first essential STOP

This **genuinely strengthens the unconditional support bound for s=+1**, avoiding the S033 OR/AND mistake. However, W>=29 for p7 is a LOWER bound on nonzero coefficients. Neither the S032 raw projective support budget nor the star/exchange identities provide a conflicting actual-Z-dependent UPPER bound. The first indispensable gap remains distinct light-projective-fibre overlaps/cancellation or new zero-sum-geometric correlations strong enough to EXCLUDE m=2p; even such exclusion would leave every m>=3p open. No universal P proof/refutation, actual vector counterexample, stronger p>=7 short-extraction lemma, D2(Cp^3)<=6p-6, classic rank-three D1/Dk result, novelty or priority is claimed. **STOP at CLM-0137; no S035 executed.** Optional Route B not activated.

## Original primary-source provenance (read-only)

Freshly opened original 2012 BSP publisher-author offprint SRC-0021, `https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf`, extracted printed pp22–24 and visually inspected printed p23 (PDF page index 2). Printed Lemma2.1's weak <=(3p-1)/2 differs from later stronger <=3(p-1)/2 without the extra step; printed Lemma2.3 states that the rank-three proof is omitted. CLM-0137 is an INTERNAL deduction from previously proved indexed identities, not an author-attributed assertion. Sheikh2017 original Chapter4 and original GHST C53 full code/output still UNREAD, historical author code NEVER RUN. Yiu final M1 independent complete three-disjoint verifier/log/certificate unauthenticated (98622/230983 are generator counts, not M1 final test); M2/M3 distinct. All historical exact source intervals unchanged, non-discovery never proves current openness.

All thirty original JSON frontier ROW OBJECTS and thirty Markdown numerical/status/FULL ORDERED evidence rows remain bytewise unchanged; 25 historical settled/trivial, intervals n15 43..45, n20 58..59, n21 61..63, n28 82..83, n30 88..90. Schmid n6=16 and van Emde Boas/Yiu remain SOURCE_STATED. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED/NOT_RUNNING/BLOCKED by n6=16. No hosted CI checks means ABSENT_NOT_PASS; inaccessible branch protection UNKNOWN. Separate INTERNAL same-executor adversarial reconstruction is recorded; no EXTERNAL independent review.
