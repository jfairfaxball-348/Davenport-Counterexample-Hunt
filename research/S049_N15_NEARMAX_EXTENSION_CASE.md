# S049 — exact eleven-term C5³ extension geometry (CLM-0191)
13 October 2026. Exact symbolic example, NOT the universal near-maximal inverse required to close CLM-0185.

Let H=F5³ with independent e1,e2,e3. Put
P=e1³ e2³ e3³ (e1+e2)(e1+e3), an eleven-term ORIGINAL-position multiset. It is H-zero-sumfree: the first coordinate of a subset is an integer between0 and5. If it is 0, no e1, e1+e2 or e1+e3 is selected, after which e2/e3 coefficients <=3 forbid nonempty zero. If it is 5, both mixed elements and all three e1 are selected, whence the e2 coordinate lies 1..4 and cannot be0. Hence no nonempty subset has all coordinates0.

Write B={0,1,2,3}³⊂F5³, u=(1,1,0), v=(1,0,1). Then the inclusive subset sumset Σ(P) (empty allowed) is exactly B∪(B+u)∪(B+v)∪(B+u+v). Inspect by first coordinate, using explicit 4×4 rectangles in the last two coordinates:
x=0: B and B+u+v, with yz rectangles [0..3]² and [1..4]², missing (y,z)=(4,0),(0,4).
x=1: B, B+u and B+v, with yz rectangles [0..3]², [1..4]×[0..3], [0..3]×[1..4], missing only(4,4).
x=2 or3: all four rectangles appear and cover F5².
x=4: B+u, B+v and B+u+v, leaving only(y,z)=(0,0).
Thus H\Σ(P)={(0,4,0),(0,0,4),(1,4,4),(4,0,0)} exactly, and
E(P)=H\(-Σ(P))={(0,1,0),(0,0,1),(4,1,1),(1,0,0)}.
Every extender lies in the nonzero affine-character plane ℓ(x,y,z)=x+y+z=1 mod5; E has only FOUR points, not the whole 25-point plane. This directly rebuts the tempting replacement of 'E subset a plane' by 'E equals a whole plane'. It is not a non-affine counterexample, nor does it prove all zero-free length11 sequences have an affine E(P). Coupling all six-cap residual supports, re-strippings and possible supports>=7 remains open; CLM-0185 stays strictly conditional.
