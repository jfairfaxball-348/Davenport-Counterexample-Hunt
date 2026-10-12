# S029 — Indexed Chevalley–Warning block multiplicity obstruction

2026-10-12. One bounded Phase-1 symbolic mathematics/provenance session. Entry main `5fa1f4c645f4d9454341e17eb3ba104f75b44487`, tree `a6ceb8dc68e4e94b8d8b9f563a86b548e07a9c72`. S028 atomic commit `45297dd7c4b174b8128d0d430112f60affc9e87d`, sole parent `64e7cdee9b6acf97aafec51536042d67607a67a6`, same tree, PR28 ordinary two-parent merge to entry main. No mathematical computation/search or author code execution.

## Local statement, independent of Olson's theorem

Let p>=7 be prime, a=3(p-1)/2, b=(3p-1)/2=a+1, and let Z be an **indexed** zero-sum sequence over F_p^3 of length 3p=2b+1 with no nonempty zero-sum subsequence of length <=a. Write F for the COMPLETE family of indexed b-position zero-sum subsets, m=|F|, and r_i=|{B in F:i in B}| for each original position i. Put s=(-1)^b and t=(p+s)/2, an integer strictly between 0 and p.

**CLM-0125 (PROGRAMME_PROVED):**

1. For every i, 2r_i = m+s (mod p).
2. m is a positive multiple of p, and in fact m>=2p. Consequently r_i=t (mod p).
3. If m=2p, every r_i is either t or t+p. Exactly H=(3p-2-3s)/2 positions have r_i=t+p, and the other 3p-H have r_i=t.

This is a conditional necessary-condition theorem about an actual indexed Z. It does NOT assert existence of Z or a no-short lift, a D1/D2 bound, or a novelty claim. The LOCAL proof below uses only elementary finite-field polynomial summation, and does NOT use SOURCE_STATED Olson D1. Application to a hypothetical length 6p-3 sequence uses the already reconstructed p-or-3p existence part of CLM-0120.

## Complete indexed proof

Because sigma(Z)=0, a proper nonempty zero sum W has a proper nonempty zero-sum complement. Both lengths are >=b, so W has size b or b+1. Complementation is a bijection between the b-block family F and all b+1 zero-sum blocks. This refers to distinct INDEX SUBSETS even if vector values repeat.

Fix position i and delete it. In T=Z\\{i}, there are n=3p-1 variables X_j, one per remaining index. For each group coordinate h=1,2,3, let

P_h(X)=sum_{j in T} z_{jh} X_j^(p-1).

There is NO cardinality polynomial here: all zero-sum support sizes are counted. Each degree is at most p-1; n=3p-1>3(p-1). Chevalley–Warning therefore makes the number Q_i of simultaneous zeros divisible by p.

For completeness, the divisibility used here has an elementary direct proof. The indicator for a simultaneous zero over F_p is product_{h=1}^3 (1-P_h(X)^(p-1)). Its total degree is at most 3(p-1)^2<n(p-1). Sum its monomials over F_p^n. For a variable exponent e, sum_{x in F_p} x^e is zero when e=0 (the sum is p), zero for positive e not divisible by p-1, and -1 for positive e divisible by p-1. A monomial could have a nonzero total sum only if EVERY variable had a positive exponent divisible by p-1; that would require total degree at least n(p-1), impossible. Thus the sum of the indicator is 0 in F_p, proving p divides Q_i. This also handles a coordinate polynomial that vanishes identically.

Every support J of a simultaneous zero is a zero-sum index subset. Conversely each such J has exactly (p-1)^|J| variable assignments with that support, contributing (-1)^|J| modulo p. There is one empty support. T has no full-Z support, and its only nonempty zero-sum supports have size b or b+1. Exactly m-r_i b-blocks avoid i. A b+1 block avoids i if and only if its complementary b-block CONTAINS i, so precisely r_i b+1 blocks avoid i. It follows that

0 = Q_i = 1+(-1)^b(m-r_i)+(-1)^(b+1)r_i
  = 1+s(m-2r_i) (mod p).

Multiplying by s (s^2=1) gives 2r_i=m+s (mod p), proving part 1. In particular m cannot be zero: otherwise every r_i=0 and the displayed Q_i congruence would read 1=0.

Now count incidences EXACTLY over the integers: sum_i r_i=mb because all m members of F have b indices. Summing part 1 over the 3p positions gives

2mb = sum_i 2r_i = 3p(m+s) = 0 (mod p).

But 2b=3p-1=-1 (mod p), so the left side is -m modulo p. Hence p divides m. Therefore m is at least p. Also 2r_i=s (mod p), whose unique residue in {0,...,p-1} is t=(p+s)/2.

Suppose m=p. The integer bounds 0<=r_i<=p, together with 1<=t<=p-1, force r_i=t for EVERY position. Then the exact incidence equality gives 3p t=p b, hence 3t=b. This is impossible: 2b=3p-1 implies b=1 (mod 3). Thus m!=p, and m>=2p. This proves part 2 without a bound on the number of incidence cells.

Finally suppose m=2p. Since 0<=r_i<=2p, the only integers with residue t are t and t+p. If H positions have the larger value, then

3p t+pH=sum_i r_i=2pb=p(3p-1),

so H=3p-1-3t=(3p-2-3s)/2. This is an integer: if s=1 it is (3p-5)/2=b-2; if s=-1 it is (3p+1)/2=b+1. The remaining count 3p-H is positive. This proves part 3. QED.

## CLM-0126 — exactly four is impossible; the six-cell lift is still not excluded

**Corollary (PROGRAMME_PROVED, conditional):** No actual indexed balanced-only Z satisfying the local hypotheses can have EXACTLY FOUR b-zero-sum subsets, regardless of the number or arrangement of membership-signature cells. This follows immediately from m>=2p>=14. It eliminates the entire exactly-four indexed case left by S026/S027, rather than only a six-cell support.

For a putative no-short indexed assignment of the S028 six cells with their specified cardinalities and aggregate sums, AB, ACE, ACF and ADEF are FOUR DISTINCT indexed b-zero-sum subsets. CLM-0124 proves that these are the ONLY size-b WHOLE-CELL zero-sum unions. By CLM-0125, such an assignment must have at least 2p total b-zero-sum subsets. Thus it must introduce **at least 2p-4 additional b-zero-sum subsets**, each using a proper nonempty portion of at least one cell. The same number of additional b+1 complements also occurs. This is a necessary consequence for ANY no-short lift, not a construction or a nonexistence proof for all lifts.

At p=7: b=10, s=1, t=4. Any balanced-only Z must have m a multiple of 7 and m>=14. In the minimal m=14 case, exactly 8 positions occur in 11 b-blocks and 13 positions occur in 4 b-blocks. Their incidence total is 8*11+13*4=140=14*10 (hand arithmetic). In the four S028 whole-cell blocks, the positions in A,B,C,D,E,F occur respectively 4,1,2,1,2,2 times; these are NOT the degrees for the complete family if an indexed lift exists. At least TEN additional b=10 partial-cell blocks are required. No list of vectors was generated or tested.

The local proof applies to p=5 as well (if such a local Z existed): b=7, s=-1, t=2, m>=10; at m=10 there would be 8 positions of degree 7 and 7 of degree 2, giving 70=10*7. This consistency check does not prove or contradict the externally SOURCE_STATED p5 short-threshold result for longer sequences. At the target primes, s=1 for p=3 mod 4 and s=-1 for p=1 mod 4.

## First essential gap and mandatory STOP

It would be INVALID to identify the complete indexed family F with the four WHOLE-CELL unions in S028. Additional partial-cell b/b+1 zero sums are permitted by the no-short hypothesis. The new congruences force many such blocks but do not yet force a zero sum of length <=a. Therefore **no theorem rules out EVERY vector assignment to the specified six cells**, and there is no symbolic no-short lift either. General families with m>=2p (including m=2p and the forced degree census) remain the first essential unclosed indexed case. The full strong extraction statement for p>=7 remains unproved, as do the independent D2<=6p-6 target and BSP's omitted rank-three multiwise estimate.

Route A stops after this closed theorem and its sharp scope review, as preregistered. Optional Route B was NOT activated. The known safe recurrence still gives D_{2p-4}<=M+2, M=3p^2-4p-3; a separately proved D2<=6p-6 would suffice to reach M. At p5 this unproved generic target is 24, b7, k6, M52; p7 target36, b10, k10, M116. No new D2 or D1 bound is claimed.

## Source and frontier conservation

SRC-0021 definitive publisher offprint, printed pp22–24, was re-read including original p23 page image: three group polynomials here adapt its finite-field support method, but CLM-0125/0126 are INTERNAL deductions, not assertions attributed to that publication. Its weak stated split, stronger unaccounted split in the proof, and omitted rank-three Lem2.3 remain distinct. Classical Olson SRC-0003 remains SOURCE_STATED and is not needed for the local new proof. No source priority claim is made.

Fresh original Royal Holloway Sheikh full-thesis PDF request and original GHST C53 code/output request returned tool internal fetch errors; full Chapter4/Remark4.3.11 and full code/output were not inspected or executed. Earlier HTTP403 observations are historical, not assigned to this attempt. Original Yiu v1 HTML Section2.3 was rechecked: repeated generator counts 98622/230983 do not authenticate the final M1 three-disjoint predicate; M2/M3 differ and independent terminal M1 implementation/log/certificates remain unauthenticated. Access enums unchanged. Bounded exact-original-source queries for n15/20/21/28/30 yielded empty or irrelevant results, not new authenticated exact theorems and not evidence of current openness.

All original 30 JSON row objects and all 30 Markdown table rows (group,D*,bounds,status,complete ordered evidence) are preserved. Historical 25 exact/trivial rows and intervals n15 43..45,n20 58..59,n21 61..63,n28 82..83,n30 88..90 remain unchanged. Schmid n6=16, van Emde Boas exact families and Yiu retain SOURCE_STATED distinctions; inherited14/17,+5,43/699/5553 quarantined. Phase1 IN_PROGRESS; Phases2/3 NOT_STARTED; CAM-0001 PROPOSED/NOT_RUNNING/BLOCKED n6=16. Zero hosted checks are NOT CI PASS. No candidate, solver, mathematical search, Lean, Palomar, manuscript, publication or outreach. S030 remains strictly future, unexecuted.
