# S056 — exact eight-outsider edge potentials and all one-split parity fibres (CLM-0210)
14 October 2026. One original-index Phase1 symbolic session; all statements are conditional on the S053/S054 hypothetical T59 arrangement, not on existence of such a minimal zero-sum T. No computation, search, candidate generation or inverse conjecture promotion.

## Definitions and exact lift
Let G=C20³, H=C10³, iota(h)=2h in G, and π:G→Q=G/2G=C2³. Let g_1,...,g_8 be EIGHT distinct ORIGINAL INDEXED positions satisfying π(g_j)=q≠0 (their G-values may coincide). Set
  w = g_1 mod 10 ∈H, d_1=0, d_j=iota⁻¹(g_j−g_1) ∈H (2≤j≤8).
The d_j exist uniquely because equal parities imply g_j−g_1∈2G; this is NOT a splitting G≅Q⊕H. Thus g_j=g_1+iota(d_j) in G and π_H(w)=q.

For every distinct pair of ORIGINAL indices j,k define h_jk=iota⁻¹(g_j+g_k)∈H. Then
  **h_jk=w+d_j+d_k.**                                           (1)
Indeed g_j+g_k=2g_1+2d_j+2d_k in G, and iota is an isomorphism H→2G. In particular h_jk=h_1j+h_1k−w when j,k≠1. Every matching among the 8 original indices yields a 4-tuple whose sum is
  **Σ_{edges {j,k} in M} h_jk = 4w+Σ_{j=1}^8 d_j**,             (2)
independent of the matching. Every four-cycle switch satisfies
  **h_ij+h_kl=h_ik+h_jl=h_il+h_jk**                             (3)
for four distinct indices. This is equality of H **values**, not just of parities or cardinalities. It collapses 28 superficially separate pair-block labels to the eight parameters w,d_2,...,d_8, with a necessary parity π_H(w)=q. It does not assert those parameters determine s_r or U.

## Exact value normal form for the 4096 one-sided split obligations
Retain ORIGINAL pairs (a_i,b_i), their H sums u_i, U=(u_i)_1^22, and seven original s_r with π(s_r)=r∈Q\{0}. Let S_C=Σ_{r∈C}s_r for a subset of their SEVEN original positions, and let p(C)=Σ_{r∈C}r. For a fixed i, π(a_i)=t_i≠0. For ε∈{0,1}, C with p(C)=t_i+εq define the *genuinely even* G sum
  B_i(C,ε)=a_i+S_C+ε g_1,
  β_i(C,ε)=iota⁻¹(B_i(C,ε))∈H.
For any subset J⊆{1,...,8} of ORIGINAL g positions with |J|≡ε (mod 2), the corresponding one-split H value is
  **z_a(C,J)=β_i(C,ε)+ ((|J|−ε)/2)w+Σ_{j∈J}d_j.**            (4)
Proof: a_i+S_C+Σ_{j∈J}g_j = B_i(C,ε)+ (|J|−ε)g_1+iota(Σ_J d_j). Since |J|−ε is even, the last two terms lie in 2G and pulling back by iota proves (4). Conversely every parity-matched original outsider A is uniquely C∪J with p(C)=t_i+εq. Thus the **entire** one-sided S055 CLM-0209 gate is equivalent to imposing
  β_i(C,ε)+ ((|J|−ε)/2)w+Σ_{j∈J}d_j ∈ E(U\{i})
for ALL ε,C,J as above, with original labels retained. For each ε there are 16 C subsets because the seven Fano singleton parities span Q, and exactly 128 J subsets of given parity; 16·128·2=4096 tests per i. The 16/128 counts refer to INDEXED subsets, never independent values. Equation (4) simultaneously incorporates all 2,048 mixed odd-J tests omitted by the earlier Fano-only approach. It admits both member choices by S055 complement reflection, but does NOT imply the conditions are consistent.

## Hostile reverse audit
- (3) is necessary but not by itself sufficient for the FULL original G lift: a common anchor w with π_H(w)=q and coherent β_i(C,ε), original s_r, U and all multi-splits remain needed.
- A four-cycle switch preserves the total (2); therefore no contradiction follows from total equality or from maximality of each 28-atom alone. Any proof must find a forbidden partial ORIGINAL subset or an independently established inverse restriction on length28 C10³ atoms.
- The unselected b_i and all |I|≥2 split-pair extensions remain essential. Never infer a full T59 or a zero-free G58 witness from (1)-(4).
- The algebra works for duplicate g VALUES but distinct original labels. Dividing g_j individually by 2 is INVALID; only even sums or differences are pulled through iota.
- No numerical/computational mathematical search, CAS/SAT/ILP, orbit enumeration, candidate, Lean, Palomar or source-promotion took place.
