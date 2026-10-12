# S035 adversarial reconstruction — separate INTERNAL same-executor pass

No independent external reviewer, formal certificate, numerical mathematical search, solver, author code or hosted CI is claimed.

1. Verify low/high degrees at m=2p. Negative sign means p≡1 mod4, p>=13, t=(p-1)/2, b=3t+1, N=6t+3, m=4t+2, L=b,H=b+1,T=b,q=t+1. Count **indices**, not distinct vectors; every b-block is a distinct indexed subset. Recheck S029 r_i exact census.
2. Exact low row sum: Σ_{j≠i}(t-λ_ij)=(b+1)t. It has b-1 other low indices, each λ∈[0,t], so mixed defect D_i>=2t. This uses NO unproved all-pair P. Nonzero mixed pair must have δ>0, even λ=0 is allowed.
3. Exact high row: (b-1)T=Lt+(H-1)2t-D_i+ΣHHν; s=-1 gives (b-1)b=bt+b2t, hence D_i=ΣHHν, not D_i=-ΣHHν or plus a residual. Inclusion-exclusion HH λ>=2t; ≤T implies ν∈[0,q]. Summing over all high i yields D=2Σ_HHν (each unordered pair twice). Counts are ordinary integers, not congruences.
4. Check special HH congruence: 2t=p-1, T=p+t<2p, t<p. The ONLY λ in [2t,T] with λ≡t(mod p) is exactly T (ν=q). Every other HH is exceptional by CLM-0129. #nonexception HH≤D/(2q); hence E_HH≥C(H,2)-D/(2q). No mistaken inference that every HH ν>0 or that pair-cover OR supplies positivity.
5. Low pair defects: L(b+1)t=2ΣLLδ+D; E_LL≥(L(b+1)t-D)/(2t) and E_LH≥D/t, yielding E_LL+E_LH≥L(b+1)/2+D/(2t). Add HH bound and simplify using q-t=1, C(H,2)=b(b+1)/2. **Monotonicity:** E≥b(b+1)+D/(2tq) INCREASES with D; substitute MINIMUM D=2tL only at this point. Substituting D=228 individually into an HH inequality as if it were a uniform bound would be invalid; proof avoids that.
6. Since b/q=3-2/q, q>=7 at p13, and E integer, E>=b(b+1)+3. Each pair λ≢t implies sum_k Psi≠0 and so is covered by some nonzero triple; 3W≥E. NO reverse implication from zero-fibre products or assumption all Psi vanish.
7. p13 hand arithmetic: low defect 120; other 18 lows at most108; mixed defect ≥12 per low so D≥228. Base two E terms 190+190; 228/(2*6*7)=19/7; E≥382+5/7→383, W≥128. Prior S031 B=ceil(19*20/6)=64; S032 U≥291 cannot contradict. Low-high λ=0 is allowed, no invented sequence.
8. p7 other sign: b10,t4,L13,H8, inclusion-exclusion mixed λ≥1, high row has residual9; CLM-0137 W≥29 retained. Wrong-sign transplant of s=-1 formula invalid. Star moment -1/8 is nonzero at p7 and p13, global sum 0; no conflict with many nonzero terms, consistent with GL3-invariant projective identity and possible cancellation.
9. For m>=3p the binary high/low census fails, and no statement follows. Complement of b-zero sum has b+1 positions, avoid-both versus include-both may differ; not silently swapped. Original SRC-0021 p23 printed stronger proof step is still unproved; full Sheikh/GHST/Yiu independent evidence absent. Internal review is not external validation.

**STOP:** a genuine actual-Z-dependent projective *UPPER* support bound is still missing; m2p and m>=3p open. No D1/Dk, D2 saving, search/candidate, frontier/source/phase/campaign promotion.
