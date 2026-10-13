# S050 — one-parameter nontrivial C5³ eleven-term inverse family (CLM-0193)
13 October 2026; direct hand rectangles, INTERNAL only. This is **positive supporting evidence**, not a universal inverse theorem.

Let H=F5³, basis e1,e2,e3 and t∈F5×. Define the eleven ORIGINAL-index terms
P_t=e1³ e2³ e3³ (e1+e2)(e1+t e3).
The first coordinate of any subset is represented by an integer 0..5. To vanish it must be 0 or5. At 0 all e1 and mixed terms are omitted and only ≤3 copies each of e2,e3 remain; there is no nonempty zero subset. At 5 both mixed terms and all three e1 are selected; the second coordinate is 1..4 because there are at most three e2, so it cannot vanish. Thus P_t is zero-sumfree for **all four nonzero t**, without needing the third coordinate.

Put B={0,1,2,3}³ and u=(1,1,0), v=(1,0,t). The inclusive subset sumset is Σ(P_t)=B∪(B+u)∪(B+v)∪(B+u+v). In any 4-by-4 yz layer, the z-shift {t,t+1,t+2,t+3} equals F5\{t−1}, whereas {0,1,2,3}=F5\{4}. List the missing yz-pairs at each first coordinate x, directly by the four possible inclusion states of the two mixed terms:
- x=0: (y,z)=(4,t−1),(0,4);
- x=1: (4,4);
- x=2 or3: no missing pairs;
- x=4: (0,t−1).
The x=0 case uses B and B+u+v; x=1 uses B,B+u,B+v; x=2,3 have all four; x=4 has B+u,B+v,B+u+v. All row/column coverage claims follow from the displayed two four-element shifted intervals, including the t=1 boundary.

Negate the four omitted sums to obtain exactly
E(P_t)={(0,1,1−t),(0,0,1),(4,1,1),(1,0,1−t)}.
All four extenders satisfy x+y+t^-1 z=t^-1, a NONZERO affine fibre; the point set is much smaller than the full 25-element plane. For t=1 this recovers S049 CLM-0191; for t=2,3,4 this provides three additional original-index examples with distinct second mixed decorations. No universal all-P11 assertion: affine E may fail outside this family, and the six-cap seven-circuit and re-stripping problems are unresolved. E empty, λ=0, support≥7 cases remain open.
