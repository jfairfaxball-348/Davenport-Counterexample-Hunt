# S051 — six-support eleven-term C5³ zero-free example with nine extenders (CLM-0196)
13 October 2026; direct original-index symbolic boxes, internal proof only; NOT the universal P11 inverse.

In F5³ with basis e1,e2,e3, put
 P = e1³ e2³ e3² (e1+e3)(e2+e3)(e1+e2+4e3).
There are exactly 3+3+2+1+1+1=11 indexed terms, of six distinct support types.

## Direct zero-freeness, no enumeration
For a subset let i,j∈{0,1,2,3}, k∈{0,1,2} be numbers of selected basis terms, and a,b,c∈{0,1} indicate the three mixed terms in displayed order. Its vector is
 (i+a+c, j+b+c, k+a+b+4c) mod5.
The first integer belongs to [0,5]. If it equals0, i=a=c=0; then the second integer j+b∈[0,4] must equal0, so j=b=0; then k=0, yielding only the EMPTY subset. If the first equals5, i=3,a=c=1; the second is j+b+1∈[1,5], so zero modulo5 forces j=3,b=1; the third is k+1+1+4=k+6, i.e. 1,2,3 modulo5 for k=0,1,2, NEVER zero. Therefore P has no nonempty zero-sum subset.

## Exact subset-sum complement
For given a,b,c, attainable x=i+a+c and y=j+b+c each range over four consecutive residues (i,j=0,1,2,3), and z ranges over the THREE residues a+b+4c+{0,1,2}. The complete allowed choices and z-intervals are
 c=0: (a,b)=(0,0)→{0,1,2}, (1,0)/(0,1)→{1,2,3}, (1,1)→{2,3,4};
 c=1: (a,b)=(0,0)→{4,0,1}, (1,0)/(0,1)→{0,1,2}, (1,1)→{1,2,3}.
For x=0, the only (a,c) are (0,0),(1,1); for x=1 they are (0,0),(1,0),(0,1); for x=2 or3 all four (a,c) are possible; for x=4 they are (1,0),(0,1),(1,1). The identical rule holds for (b,c) against y. Combining the above intervals (NOT independent choices of c) yields the hand coverage table; an entry is the set of missing z residues:
                    y=0      y=1      y=2      y=3      y=4
 x=0                {4}      {4}      {4}      {4}      {4}
 x=1                {4}       ∅        ∅        ∅        ∅
 x=2                {4}       ∅        ∅        ∅        ∅
 x=3                {4}       ∅        ∅        ∅        ∅
 x=4                {4}       ∅        ∅        ∅        ∅
For instance x=0 permits only the c0 a0 and c1 a1 alternatives, with z in {0,1,2,3} at EVERY y; y=0 is symmetric. For x,y≠0, in interior x,y∈{1,2,3} the c0 four a/b choices supply intervals covering 0..4; each boundary x=4 and/or y=4 is completed by the c1 options, e.g. x=y=4: c0(a=b=1) supplies {2,3,4} and c1(a=b=0) supplies {4,0,1}. This accounts for the entire 25-cell table.

Consequently Σ(P)=F5³ \ {(x,y,4): x=0 OR y=0}. In particular |Σ(P)|=116 and
 E(P)=F5³\(-Σ(P)) = {(x,y,1): x=0 OR y=0}.
There are exactly 5+5−1=9 extenders, lying in the NONZERO affine fibre z=1; the set is a union of two perpendicular affine lines, not an entire affine plane. Independent symmetry check: σ(P)=(0,0,3) and E(P)=-σ(P)-E(P), visible as (x,y,1)→(-x,-y,1).

## Status and impact
This substantially varies the earlier four-point S049/S050 P_t families: six support classes and NINE exact extenders, still affine. It neither proves nor refutes the assertion every arbitrary zero-free P11 has E(P) contained in a nonzero character fibre; E empty, λ=0/nonaffine cases, support≥7, all 28-block re-strippings and seven six-cap circuits remain OPEN. No complete C15³ case or numeric Davenport theorem follows. All 5×5 coverage entries were hand-derived from the interval list; no computational/orbit search or CAS used.
