# S052 — another six-support C5³ eleven-term E with EXACT four points (CLM-0199)
13 October 2026, symbolic boxes; internally checked, not universal inverse or D(C15³)=43.

Let Q=F5³ with basis e1,e2,e3. Put
 P=e1³ e2³ e3² (e1+e3)(e2+e3)(e1+e2).
It has eleven distinct original indexed positions, six distinct support types. This differs from S051 CLM-0196 in the LAST support type: S051 used e1+e2+4e3.

## Zero-freeness
For selected basis counts i,j∈{0,1,2,3}, k∈{0,1,2} and selected mixed indicators a,b,c∈{0,1} (respectively e1+e3,e2+e3,e1+e2), an indexed subset sum is
 (i+a+c, j+b+c, k+a+b) modulo5.
The first INTEGER lies in [0,5]. If first 0, i=a=c=0, then second is j+b≤4 and zero forces j=b=0, and third k=0 gives the empty subset. If first5, i=3,a=c=1. Then second=j+b+1∈[1,5], so zero requires j=3,b=1; third k+2∈{2,3,4} is never zero modulo5. Thus NO nonempty zero-sum subset.

## Exact all-25 xy-cell inclusion table (hand interval proof)
For fixed (a,b,c), attainable x and y range through four consecutive residues starting at a+c and b+c. For each x, the possible (a,c) are:
 x=0: (0,0),(1,1);
 x=1: (0,0),(1,0),(0,1);
 x=2 or3: all four pairs;
 x=4: (1,0),(0,1),(1,1).
The same table applies to (b,c) given y. Crucially the c choice must be SHARED by x and y, not chosen independently. The attainable third residues are I_(a+b), where
 I0={0,1,2}, I1={1,2,3}, I2={2,3,4}.
Take, for each (x,y), the union of I_(a+b) over admissible (a,b,c) with shared c. The COMPLETE missing-z table is
             y=0   y=1   y=2   y=3   y=4
 x=0          ∅     {4}     ∅     ∅     {0}
 x=1         {4}     ∅      ∅     ∅      ∅
 x=2          ∅      ∅      ∅     ∅      ∅
 x=3          ∅      ∅      ∅     ∅      ∅
 x=4         {0}     ∅      ∅     ∅      ∅
For reproducible hand spot-checks: at (0,1), c=0 gives I0∪I1 and c=1 gives I1, hence missing4; at (0,4), c=0 gives I1 and c=1 gives I1∪I2, hence missing0; at (0,0), c0 gives I0 and c1 gives I2, all five; if both x,y∈{1,2,3}, c=0 admits a,b=0,1 and provides I0∪I1∪I2; other boundary cells are obtained by the same displayed admissible pairs. Thus
 Σ(P)=Q\{(0,1,4),(1,0,4),(0,4,0),(4,0,0)}.
By definition E(P)=Q\(-Σ(P)) is EXACTLY
 **E(P)={(0,4,1),(4,0,1),(0,1,0),(1,0,0)}**.
All four satisfy x+y+2z=1 mod5, a nonzero affine character fibre. The total σ(P)=(0,0,4), so c0=-σ(P)=(0,0,1) and the complement involution x→c0-x exchanges the pairs (0,4,1)↔(0,1,0) and (4,0,1)↔(1,0,0). No claim that the four points exhaust the affine plane.

## Universal inverse reduction and non-resolution
For any zero-free eleven-term P in F5³, E(P)=c-E(P) where c=-ΣP≠0; writing t=c/2 (well defined over F5), R=span_F5{e-t:e∈E(P)} when E nonempty, E is contained in SOME nonzero affine character fibre if and only if c∉R. Indeed a nonzero functional annihilating R but not c exists exactly when c∉R, and its common level on E is φ(t)=φ(c)/2≠0. If E empty, containment is vacuous. This is an elementary equivalent reformulation, NOT a proof of c∉R for all P11. The example here has c∉R. The support≥7, E empty, zero-fibre-only, full-affine-dimension and all six-cap re-strippings remain unresolved. No computer search, CAS or orbit generation used.
