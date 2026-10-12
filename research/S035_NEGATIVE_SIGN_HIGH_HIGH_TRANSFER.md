# S035 — The negative-sign high–high complement incidence theorem

Date: 2026-10-12. Exactly one owner-invoked Phase-1 **symbolic** primary-source/provenance session, Route A. Entry LIVE remote main `b6d6883d182815098fc9b7625635d7c1698fb054`, tree `3c5bfda6c527b5bfe0900f0b5a9f89064da1ad3a`; prior S034 sole branch commit `f9ff25b9167691b6a07a38c8296623b3caba5f1f`, its parent `95d5cf1f17539394387a309840eefcbfdd1005e4`, tree `3c5bfda6c527b5bfe0900f0b5a9f89064da1ad3a`, PR #34 merged by normal two-parent commit `b6d6883d182815098fc9b7625635d7c1698fb054` with precisely those parents. No open PR or competing S035 branch observed at entry. One theorem and STOP. No numerical mathematical search, CAS, SAT/ILP, candidate/orbit enumeration, original author code execution, Lean, Palomar, campaign, manuscript, contact, outreach or publication.

## Standing hypotheses and definition of a genuinely exceptional pair

Fix a prime p>=7, N=3p=2b+1, b=(3p-1)/2, a=b-1, s=(-1)^b, t=(p+s)/2. Suppose an indexed **zero-sum** Z=(z_i) of length N in F_p^3 has no nonempty zero-sum of size <=a. Let F be its COMPLETE family of indexed b-subsets summing to zero, m=|F|. Write r_i=|F_i|, lambda_ij=|F_i intersect F_j| for distinct indices, and Psi_ijk for the genuine three-index deletion polynomial coefficient. S029–S031 give m=kp (k>=2), exact sum of codegrees through i equal to (b-1)r_i, and the field identity
    sum_{k distinct i,j} Psi_ijk = s(lambda_ij-t) (mod p).
The local CW pair-cover says BOTH OR NEITHER, not both. Every pair with lambda_ij not congruent to t modulo p is an **exceptional pair**; each is an edge of at least one actual nonzero Psi triple. Thus if E counts such edges and W counts triples with Psi_ijk !=0, then E<=3W (NOT a vanishing inference, NOT a converse).

Under the additional hypothesis m=2p, every r_i is exactly t (low) or T=p+t (high). The number of low indices is L=(3p+2+3s)/2, of high indices H=(3p-2-3s)/2.

## CLM-0138 — unconditional negative-sign high–high transfer and nonzero Psi support (PROGRAMME_PROVED, scoped)

**Theorem.** In the stated hypothetical indexed setting with m=2p and s=-1 (equivalently p=1 mod4), let
    t=(p-1)/2, q=p-t=t+1, b=3t+1, L=b, H=b+1, T=p+t=b.
Let E_LL,E_LH,E_HH count exceptional unordered pairs of the indicated low/high types, let
    D = sum_{i low,j high} (t-lambda_ij)
as an exact nonnegative **integer**, and let E=E_LL+E_LH+E_HH. Then:

(1) D>=2tL. For each high i, writing nu_ij=lambda_ij-2t for other high j, one has the EXACT integer identity
    sum_{j low}(t-lambda_ij) = sum_{j high, j!=i} nu_ij.
In particular 0<=nu_ij<=q, and D=2 sum_{unordered high-high pairs} nu_ij.

(2) EVERY high-high pair has lambda_ij in [2t,T], so its pair moment vanishes only when lambda_ij=T, or equivalently nu_ij=q. Consequently
    E_HH >= C(H,2)-D/(2q).
Also
    E_LL+E_LH >= L(b+1)/2 + D/(2t).

(3) Combining these inequalities yields
    E >= b(b+1)+D/(2tq)
      >= b(b+1)+b/q
      = b(b+1)+3-2/q.
As E is an integer and q>=2, this gives the clean UNCONDITIONAL necessary lower bound
    E >= b(b+1)+3,
    W >= ceil((b(b+1)+3)/3).
Here 'unconditional' means **no additional universal pair-positivity P beyond the standing hypothetical Z and m=2p**. It is NOT an unconditional statement of existence or rank-three Davenport resolution.

**Proof.** The exact low degree is t. Thus 0<=lambda_ij<=t whenever i is low. The exact block incidence sum through a low i is
    sum_{j!=i}(t-lambda_ij)=(N-b)t=(b+1)t.
For s=-1, there are L-1=b-1 *other lows*. Each of their deficits is <=t, so the sum of the deficits to high partners is at least ((b+1)-(b-1))t=2t. Summing low rows gives D>=2tL. No low-low or low-high positivity was silently assumed.

For two highs, elementary set inclusion–exclusion among m=2p DISTINCT b-blocks gives
    lambda_ij >= r_i+r_j-m = 2(p+t)-2p=2t,
and lambda_ij<=r_i=T=p+t. Hence 0<=nu_ij=lambda_ij-2t<=T-2t=p-t=q. For any high i, decompose the EXACT block-degree incidence sum (b-1)T by low and high neighbors:
    (b-1)T = sum_{j low}(t-(t-lambda_ij)) + sum_{j high,j!=i}(2t+nu_ij)
            = Lt+(H-1)2t - D_i + sum_high nu_ij.
For s=-1, L=b,H-1=b,T=b and b-1=3t, so (b-1)T=3tb=bt+b(2t), proving D_i=sum_high nu_ij. Sum over high i to count each high-high nu twice: D=2 sum_HH nu.

For any low-containing pair, since 0<=lambda<=t<p, exceptional is exactly t-lambda>0. Each exceptional LL contributes at most t to the defect counted twice; each exceptional LH at most t counted once. Consequently
    Lt(b+1) = 2 sum_LL(t-lambda)+D <= 2t E_LL + D,
and E_LH>=D/t. Add to obtain E_LL+E_LH >= L(b+1)/2 + D/(2t). No assumption that zero codegrees are forbidden occurs here.

For any high-high pair, 2t=p-1 and T=p+t. Since [2t,T] lies below 2p and above t, the ONLY integer in this interval congruent to t mod p is T itself. A high-high pair is thus nonexceptional only when nu=q. The total nu mass is D/2, so there are at most D/(2q) such nonexceptional high-high pairs, yielding E_HH >= C(H,2)-D/(2q).

Combining,
    E >= L(b+1)/2 + C(H,2) + D(1/t-1/q)/2.
Since q=t+1, the coefficient equals 1/(2tq)>0, and D>=2tL. With L=b,H=b+1, the first two terms each equal b(b+1)/2; hence E>=b(b+1)+b/q. Finally b=3t+1=3q-2, so b/q=3-2/q, which strictly lies between 2 and 3 for q>2 (indeed q=(p+1)/2>=7 for p>=13 in this residue class). The integer E is therefore at least b(b+1)+3. The S031 pair moment makes every exceptional pair belong to some nonzero Psi triple; a triple has exactly three unordered edges, yielding E<=3W. QED.

## Boundary arithmetic, sign/complement tests, and robustness

**p=13 first admissible s=-1 boundary:** N=39, m=26, a=18,b=19, t=6,q=7,T=19,L=19,H=20. Every low row has total defect (b+1)t=120; the 18 other lows can contribute at most 108, so mixed defect >=12 per low and D>=228. There are C(20,2)=190 HH pairs. Using D>=228 only in the monotone COMBINED inequality gives E>=19*20+19/7>382, so integer E>=383 and W>=ceil(383/3)=128. The separate raw bounds at the minimal hypothetical D are E_LH>=38, E_LL>=171, E_HH>=ceil(190-228/14)=174; these are **illustrative evaluations at D=228**, not separately universal minima when D can be larger. S031 unconditional previously forced W>=ceil(19*20/6)=64; it is doubled to 128. No actual sequence was generated. The S032 coarse projective capacity has universal U>=p²+10p-8=291 (not an upper bound <128), so this does NOT contradict m=2p.

**p=7 opposite sign boundary:** s=+1,b=10,t=4,T=11,L=13,H=8,m=14. The s=-1 identity D_i=sum nu DOES NOT hold: its baseline is 3(p-1)/2=9 for each high. Here mixed lambda>=1 by rL+rH-m=1, S034 W>=29; do not apply the 128 formula. The exact star moment -1/8=6 in F7 remains consistent. p13 star moment -1/8 remains nonzero (no cancellation-to-zero assumption), and global Psi sum 0 mod p is compatible with many nonzero coefficients.

**Complement and multiplicity scope:** all B are distinct indexed b-subsets. The b+1 proper zero sums are exactly their complements in I (N=2b+1), so lambda counts blocks through both, not blocks avoiding both; a mixed pair may have lambda=0 for s=-1 and the argument permits it. At m>=3p, low/high degree levels and the key exact H=b+1 census change; do NOT extrapolate. Four-index exchange and GL3 invariance continue to hold but provide no independent upper bound. A projective zero-index-fibre term can be nonzero yet cancel in the Fp sum: no reverse implication is used.

## First indispensable STOP

The new theorem strengthens the **s=-1** previously untouched side and uses actual-Z-implied block incidence, but proves only a lower bound on critical nonzero Psi support. There is no genuinely opposing *actual-Z-dependent* projective overlap/cancellation upper bound. The no-short Z with m=2p is not excluded; m>=3p remains untouched. The strong p>=7 <=3(p-1)/2 extraction is NOT proved. Optional Route B independent D2(Cp³)<=6p-6 was not activated, no omitted original BSP rank-three Lem2.3 proof imported. No rank-three D1/Dk endpoint, numerical/computational search, candidate, negative certificate, source-status upgrade, novelty or publication. STOP after this first substantial scoped theorem; S036 is FUTURE ONLY.

## Original primary-source provenance and external limits

Freshly inspected original definitive Bhowmik–Schlage-Puchta Contemporary Mathematics 579 (2012), SRC-0021, author-hosted publisher offprint https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/large_exponent.pdf, printed pp22–24 including visually inspecting printed p23 (PDF page index 2). On printed p22 Lemma2.1 promises <=(3p-1)/2; printed p23 then uses <=3(p-1)/2 without independently establishing that stronger step, and says the rank3 Lemma2.3 proof is omitted. This INTERNAL CLM-0138 is NOT attributed to the paper. Sheikh Chapter4 full text UNREAD; GHST C53 original code/output UNREAD and NEVER RUN; Yiu M1 independent complete final predicate unauthenticated and M2/M3 separate. The five historical source intervals n15 43..45,n20 58..59,n21 61..63,n28 82..83,n30 88..90 are retained; absence of newly inspected original evidence is not proof of current openness.

All original thirty JSON rank-three frontier row objects and full ordered Markdown table rows left unchanged. Historical 25 settled/trivial rows, Schmid n6=16 and van Emde Boas/Yiu SOURCE_STATED, original 28 sources and access enums preserved. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED, CAM-0001 PROPOSED/NOT_RUNNING/BLOCKED. Separate INTERNAL adversarial symbolic review only (not independent external verification, Lean or hosted CI); no checks is NOT PASS.
