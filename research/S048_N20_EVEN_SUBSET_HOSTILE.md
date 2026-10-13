# S048 — 763 matching tests collapse to 127 even-subset tests; distinct-point hostile family (CLM-0186/0187)
13 October 2026. Original-index symbolic proof under S047 n20 six-odd conditional setup; no full S58 or parity-profile elimination.

## Exact collapse (CLM-0186)
Take EIGHT ORIGINAL C20^3 points g1,...,g8 of one identical mod2 class, retain the other22 original disjoint parity-pair H=C10^3 decorations U22, and write iota(h)=2h. Every sum of an EVEN number of the gi belongs to 2G, so for each nonempty EVEN index subset I define v_I=iota^{-1}(Σ_{i∈I}g_i).

If a nonempty partial matching M has vertex set I, Σ_{edge {i,j}∈M} iota^{-1}(g_i+g_j) = v_I. Thus EVERY matching of a fixed even index subset has EXACTLY THE SAME H sum (not merely all 105 perfect matchings). Conversely every nonempty even subset admits a matching. The 763 labelled matching tests of CLM-0183 are therefore EXACTLY equivalent to v_I∈E(U22) for all
 C(8,2)+C(8,4)+C(8,6)+C(8,8)=28+70+28+1=127
nonempty EVEN index subsets. These are labelled subset expressions, NOT 127 distinct H values or independent restrictions. For fixed I the degeneracy is respectively 1,3,15,105 matchings of its 2,4,6,8 vertices. Totals 28+210+420+105=763. The proof uses the genuine non-split iota, not a fictional C2⊕C10 splitting.

The equivalence extends to any even number 2r of original points of one parity class, giving 2^(2r-1)-1 nonempty even index-subset tests against a fixed external zero-free paired core U. It does not test zero subsets with odd counts in several parity classes whose combined mod2 XOR vanishes.

## Fully symbolic eight-distinct-original-point hostile family (CLM-0187)
Take H=C10^3 basis f1,f2,f3 and set U22=f1^9 f2^9 f3^4. This is H-zero-sumfree. Its negative subset sums have arbitrary first/two coordinates and third coordinate in {0,6,7,8,9}; therefore E(U22) is precisely all vectors whose f3-coordinate lies in {1,2,3,4,5}.

Choose eight pairwise distinct d_i from span(f1,f2), for example 0,f1,2f1,3f1,f2,f1+f2,2f2,2f1+f2, and ORIGINAL points g_i=G_f3+2d_i in G=C20^3, where G_f3 is the standard order20 third basis element and H coordinates d_i are lifted by 2. All eight original g_i are distinct and share the SAME nonzero f3 parity class. For every even I of size 2j, 1<=j<=4,
v_I=j f3+Σ_{i∈I}d_i,
whose third coordinate is j∈{1,2,3,4}. Hence ALL 127 even-subset tests (and all 763 matched labelled tests) hold simultaneously. Pair-swap differences d_i-d_j can be genuinely nonzero and two-dimensional, so this is NOT the all-equal-point degeneration.

Each of the 22 external H pair decorations can be realised by TWO C20 original positions sharing any chosen nonzero parity class r: use r and 2h-r for a desired H decoration h. For example distribute 22 pairs among the OTHER six nonzero parity classes in counts 4,4,4,4,3,3, and add six odd-class singleton original positions, one in each of those six classes. Together with the eight selected points this gives a 58-position original multiset matching the six-odd-class parity census; z=-ΣS restores augmented total zero and has parity f3. This only realises the parity/paired-core bookkeeping. It is NOT shown G-zero-sumfree and is NOT asserted to pass Fano hub grids, all alternative pairings of all 58 points, the three remaining P26 profile tests, or full minimum-zero conditions.

## Verdict
The full single-U22 same-class matching inverse, even with eight DISTINCT indices and nonzero two-dimensional transfer differences, cannot by itself imply a contradiction. A decisive n20 route needs cross-parity Fano codewords, globally coordinated external U cores, or a genuinely new restriction not true of this hostile family. Historical D(C10³)=28 remains SOURCE_STATED.