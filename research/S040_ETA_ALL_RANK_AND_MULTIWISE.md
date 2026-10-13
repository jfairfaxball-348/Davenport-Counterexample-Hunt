# S040 — Line-pigeonhole eta proof and the composite multiwise obstruction

2026-10-13. One Phase-1 symbolic mathematics session. Entry main `ef982dd532cd5f275d24bdddcddf538b05e04447`. Complete proofs below are INTERNAL reconstructions, not novelty determinations, external review, Lean or Palomar. No mathematical instance enumeration, numerical search, CAS, SAT/ILP, author code or candidate generation.

## CLM-0148 — An elementary all-rank eta theorem with no exceptional p=7 lemma

**Theorem.** For every prime p>=7 and integer d>=3, writing
R = 1+p+...+p^(d-2) = (p^(d-1)-1)/(p-1),
we have

eta(C_p^d) <= (3p-7)R+4.

Here eta is the length that forces a NONEMPTY zero-sum block of length at most p. Rank-two inputs are **already independently programme-proved**: eta(C_p^2)<=3p-2 (CLM-0091), and Property C(p) (CLM-0111): a short-free indexed sequence of length 3p-3 in a plane consists of p-1 copies each of three vector values.

**Proof (all d, including p=7).** Suppose an indexed sequence A of N=(3p-7)R+4 vectors of C_p^d has no nonempty zero-sum subset of size <=p. Zero values cannot occur. Every one-dimensional linear subgroup L has at most p-1 A-positions: any p positions of that cyclic subgroup contain a nonempty zero sum of length <=p by the elementary cyclic Davenport bound D(C_p)=p. There are exactly (p^d-1)/(p-1)=pR+1 such subgroups, and they partition all nonzero vector VALUES, hence all indexed A-positions. Furthermore

N - 2(pR+1) = (p-7)R+2 > 0.

Thus some line contains at least three indexed positions; choose a line L with maximum occupancy m, giving 3<=m<=p-1. Exactly R=(p^(d-1)-1)/(p-1) two-dimensional linear subgroups U contain L; their off-L parts partition the positions of A outside L (each vector outside L spans a unique plane together with L). Therefore some U contains at least

m + ceil((N-m)/R)
 = 3p-7+m+ceil((4-m)/R)

indexed A-positions. Since d>=3, R>=p+1, and m<=p-1, hence -R<4-m<R. Three exhaustive cases remain.

- m>=5: ceil((4-m)/R)=0, so |A in U|>=3p-7+m>=3p-2. Programme-proved rank-two eta supplies a short zero sum, contradiction.
- m=4: the ceiling is zero and |A in U|>=3p-3. Choose any 3p-3 positions. Their short-freeness and Property C(p) force p-1 identical vector values, hence p-1 positions on their common cyclic subgroup. But p-1>=6>m=4, contradiction.
- m=3: the ceiling is one and |A in U|>=3p-3. The same Property C argument gives p-1>=6>m=3, contradiction.

All possibilities for maximal line occupancy m have been excluded. The theorem follows. QED.

**Independent boundary check:** For p=7,d=3, R=8, N=116, number of lines=57, so N>2*57. At m=3,4,5,6 the forced plane occupancies are respectively 18,18,19,20. The first two contradict Property C(7) (six repeated points on a line), the last two eta(C7^2)<=19. For p=13,d=3, R=14, N=452, m3/4 force 36, m5 forces 37, and eta(C13^2)<=37. For d=4,p=7, R=57,N=802, line count400 and N>800; exactly the same m cases apply. These are hand arithmetic, not a mathematical search.

**Novel dependency improvement:** The original BSP2012 Theorem1.2(3) all-rank eta numerical inequality can therefore be independently reconstructed using the already proven rank-two Property C and rank-two eta, WITHOUT the separately intricate BSP2012 Lemma5.2 15-term p7 classification. S022 CLM-0112's existing independent p7 proof remains historically valid, but is no longer needed for this route. This does not give a smaller eta numerical upper or authenticate the separate source's omitted multiwise coefficient. The publisher original SRC-0021 pp28-30 was compared against the later author-associated arXiv copy 1702.03403 pp9-10, whose displayed plane reduction is corroborative, not a newly authenticated separate source object.

## CLM-0149 — Unconditional reconstructed rank-three large-k comparison

For every prime p>=7 and integer k>=2p-4,

D_k(C_p^3) <= p*k + p^2 - 3.

Proof: S039 CLM-0142-0144 independently established D_(2p-4)(C_p^3) <= 3p^2-5p <= M=3p^2-4p-3. CLM-0148 here proves eta(C_p^3)<=M, so the following standard extraction is valid. For a sequence with M+p(k-j) positions, j=2p-4, repeatedly remove k-j disjoint nonempty zero-sum blocks of length <=p, leaving at least M positions after the removals and therefore satisfying eta at each preceding stage. The remaining sequence has j disjoint nonempty zero sums by the S039 bound. This gives D_k<=M+p(k-j)=pk+p^2-3. At k=j the identity is an inequality of bounds, not a claim of exact D_j. No strong (3p-3)/2 split, triple Psi exclusion, or omitted BSP2012 Lemma2.3 is imported.

For k>=3p-2 this proves the local estimate used in the Grinsztajn global source argument, with a three-position improvement over pk+p^2. At p7, j=10,M=116: D10<=112<=116, then Dk<=7k+46. At p13, j=22,M=452: D22<=442<=452, then Dk<=13k+166. The fact that D_j has slack p-3 does NOT automatically lower M: eta must hold at the actual extraction threshold.

The global inequality D(C_n^3)<=4n-P(n)-2 (P the largest **full prime-power component** of n) has a written source induction that was already reconstructed in S004, but the inputs for small prime powers, p3/p5 generalized multiwise statements, and some published computational/source chains remain at the evidence statuses recorded there. This session strengthens the p>=7 component; it does not promote the entire original arbitrary prime-power argument to PROGRAMME_PROVED or assert full composite equality.

