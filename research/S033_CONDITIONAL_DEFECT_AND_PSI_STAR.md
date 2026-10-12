# S033 — Pair-cover defect, high–low incidence and critical Psi star moments

Date 2026-10-12. Exactly ONE newly owner-invoked Phase-1 symbolic mathematics/provenance session, Route A only. Entry observed LIVE main `a63089f7d121960e0b1dd4a9b1a1f560435b8348`, tree `9618f15f25e7cbdaffab6c3cabbdb5a5ac4f8b82`. S032 atomic research commit `926ac9f8b675c2c9b834b64dc842895f421894f4`, sole parent `a8d268c9dd6aa98781e08982d8a448b67c72f693`, same tree; PR #32 non-force true two-parent merge to entry main. Zero competing S033 branches/PRs, 32 previously merged PRs, no open PRs. No numerical mathematical search, CAS, SAT/ILP, candidate/orbit generation, author code execution, Lean, Palomar, campaign, publication, contact or Phase 2/3.

## Hypotheses and precise scope

Fix prime p>=7, N=3p, a=3(p-1)/2, b=(3p-1)/2, s=(-1)^b, t=(p+s)/2. Let Z be an indexed zero-sum N-sequence in F_p^3 with no nonempty zero-sum subsequence of size <=a. Let F be the COMPLETE family of b-subsets summing to zero, m=|F|, with r_i blocks through i, pair codegrees lambda_ij and triple codegrees tau_ijk. By S029 m=kp, k>=2; S030 proves that for ALL distinct i,j at least one b-block contains both or neither, and hence lambda_ij>=1, since the alternative 'neither' alone does not yield positive lambda. **Important repair:** the S030 pair-cover as stated is OR, not AND. Positivity lambda_ij>=1 is NOT established by S030 alone. For the theorem below we must use an independent positive-pair-containment derivation, or withdraw the sharpening. See explicitly assessed gate below.

## Critical scope check: S030 pair-cover gives OR, so positivity is unproved

The S030 local Lemma 1 says exactly: for every pair i,j, there is a b-block containing BOTH **or** containing NEITHER. The implication lambda_ij>=1 is FALSE as a logical inference from this disjunction. The S026 older source-stated Olson pair-cover also uses the same alternative. Therefore a tempting purported refined deficiency e_i>=ceil((b+1)t/(t-1)) would be UNPROVED absent an additional lemma forcing lambda_ij>=1. This session does NOT register it as PROGRAMME_PROVED. A formally conditional result is recorded next, preserving mathematical integrity.

## CLM-0135 — a rigorously conditional improvement and the exact missing incidence premise

**Theorem (conditional).** Add the explicit hypothesis **P**: for every two distinct indices i,j, lambda_ij>=1. If m=2p, set H=(3p-2-3s)/2 and L=(3p+2+3s)/2, and e=ceil((b+1)t/(t-1)). Then:
1. Each low index i (r_i=t) has at least e other indices j with lambda_ij != t modulo p.
2. If s=+1 (equivalently p congruent 3 mod 4), each high index i (r_i=p+t) has at least THREE low j with lambda_ij<t.
3. The number of nonzero three-deletion coefficients Psi_ijk is at least ceil((Le+3H)/6) if s=+1, or ceil(Le/6) if s=-1. At p=7 this conditional lower bound is 37 (compared with S031's unconditional 24).

**Proof.** Under m=2p the exact census is r_i=t for L low indices and r_i=t+p for H high indices. For low i, 1<=lambda_ij<=t. Count all b-block incidences through i:
sum_{j!=i}lambda_ij=(b-1)t.
Hence sum_{j!=i}(t-lambda_ij)=(N-b)t=(b+1)t.
Each exceptional j contributes a positive integer at most t-1 by hypothesis P. Thus at least e distinct exceptional partners exist; nonexception is exactly lambda_ij=t (not merely congruent) because 0<=lambda_ij<=t<p.

For high i put T=p+t and delta_ij=T-lambda_ij. Then sum_{j!=i}delta_ij=(b+1)T. For high j, inclusion-exclusion among the m=2p blocks gives lambda_ij>=2T-2p=2t, and thus delta_ij<=p-t. For low j, lambda_ij<=t and delta_ij=p+(t-lambda_ij). Consequently
sum_{j low}(t-lambda_ij) >= (b+1)(p+t)-pL-(H-1)(p-t)
=3(1+s)(p-1)/4.
For s=+1 this is 3(p-1)/2; with 1<=lambda_ij<=t each positive deficit is at most t-1=(p-1)/2, forcing at least THREE distinct exceptional high–low pairs per high i. For s=-1, the inequality yields zero and no positive mandatory high–low count.

Let E_LL, E_LH, E_HH count exceptional unordered low-low, low-high and high-high pairs. Low-first-index counting gives 2E_LL+E_LH>=Le. When s=+1 high-first-index counting gives E_LH>=3H. Therefore E_LL+E_LH+E_HH >=(Le+3H)/2 (respectively >=Le/2 for s=-1). The S031 exact pair moment sum_{k!=i,j}Psi_ijk=s(lambda_ij-t) says every exceptional pair is contained in at least one NONZERO Psi triple; any triple contains only three unordered pairs. Dividing by three and rounding proves the claimed conditional bound.

Exact symbolic p=7: b=10,s=+1,t=4,H=8,L=13,e=ceil(11*4/3)=15; exceptional unordered pairs >=ceil((13*15+3*8)/2)=110; nonzero Psi triples >=ceil(110/3)=37. This cannot defeat S032 U>=111 even **under** additional hypothesis P, and P itself is UNPROVED. No mathematical instance search occurred. QED conditional theorem.

**FIRST indispensable failure**: S030 pair-cover DOES NOT imply P. The case of a pair lying in no b-block but avoided by at least one b-block is compatible with the established disjunctive statement. An attempted unconditional presentation of the above 37 bound is therefore rejected, not silently promoted. It is an explicit CONDITIONAL theorem, not an unconditional improvement to CLM-0130.

## CLM-0136 — unconditional uniform critical-coefficient star moment

**Theorem (no P required).** For every original index i, under just the original no-short hypotheses,
  sum_{unordered {j,k} subset I\{i}} Psi_ijk = -1/8 in F_p.
In particular every i belongs to at least one triple with Psi_ijk !=0. Moreover the global sum over all distinct unordered triples is 0 in F_p.

**Complete proof.** From S031 for every j!=i,
 sum_{k distinct i,j} Psi_ijk = s(lambda_ij-t).
Sum over j!=i. Each unordered pair {j,k} contributes twice. Since b-blocks through i supply b-1 other positions each,
 2 sum_{j<k; j,k!=i} Psi_ijk
 =s( (b-1)r_i-(N-1)t).
S029 gives r_i=t modulo p (since m=kp). Thus the right side is s((b-N)t)=-s(b+1)t. In F_p, b+1=(3p+1)/2=1/2 and st=s(p+s)/2=1/2. Hence twice the star sum is -1/4; divide by 2 (p>=7) to obtain -1/8. This is nonzero because p>=7. Summing the star identity over i counts each unordered deletion triple three times, giving 3 sum_{|D|=3}Psi_D = N(-1/8)=0, and 3 is invertible. At p=7, -1/8=-1 modulo 7 = 6, so each star sum is nonzero and the global sum vanishes. QED.

This star theorem is GL3-invariant by S031 and introduces actual value constraints; it does NOT imply arbitrary triple vanishing, a nonzero summand converse, cancellation control, or exclusion of m=2p/m>=3p.

## Independent adversarial reconstruction and mandatory STOP

SECOND INTERNAL same-executor pass: checked complement orientations, exact S030 pair-cover disjunction, invalid inference to P, high-high lower codegree 2t conditional on m2p, high-low maximum t, the 3(1+s)(p-1)/4 sign, double counting low-low vs low-high, three pairs per Psi witness, the s=+1 <=> p=3 mod4 parity, and p7 arithmetic. Independently rederived CLM-0136 star moment by summing S031 pair identity, checking b-N=-(b+1), st=1/2 and projective Psi orientation. Reviewer is NOT external, Lean or hosted CI.

STOP after unconditional star theorem and honest discovery of crucial unproved positivity premise P for the stronger conditional support estimate. The geometric zero-fibre raw union U and all true overlap/cancellation effects remain uncontrolled; S032's no-go still applies. No theorem excludes m=2p or m>=3p, proves p>=7 strong extraction, D2(Cp³)<=6p-6, rank-three Davenport equality or counterexample. A future S034 must first prove or refute P (or use a defect bound valid with lambda=0), then pursue projective overlap/cancellation; no S034 execution here. Optional Route B not activated.

## Read-only original provenance and immutable frontier

Fresh SRC-0021 original publisher author-offprint PDF (Contemporary Mathematics 579, 2012) pp22–23 including visual printed p23 inspected: original Lemma2.1 states weaker <=(3p-1)/2; later rank-three split prints <=3(p-1)/2 without the necessary supplied implication; printed Lemma2.3 omits rank-three proof. None of CLM-0135/0136 is attributed to the authors. Sheikh2017 full Chapter4 remains unread; GHST original C53 code plus output unread and NEVER RUN; Yiu2026 terminal independent M1 three-disjoint verification unauthenticated, M2/M3 distinct. Historical n15/20/21/28/30 exact-source intervals unchanged; non-discovery cannot establish present-day openness.

All 30 original rank-three JSON frontier row OBJECTS and all 30 Markdown group/D*/bounds/status/FULL ORDERED evidence table rows conserved; historic25, intervals n15 43..45,n20 58..59,n21 61..63,n28 82..83,n30 88..90. Schmid n6=16, van Emde Boas/Yiu SOURCE_STATED. No source enum promotion, classic rank-three D1/Dk update or campaign. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; CAM-0001 PROPOSED/NOT_RUNNING/BLOCKED n6=16. Zero hosted CI checks is NOT PASS.
