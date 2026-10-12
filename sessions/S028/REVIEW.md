# S028 — adversarial independent logical review (hand proof, not Lean/CI)

**Notation/dimension:** six FORMAL cells A..F, six occupied distinct 4-cube strings and only 5 equations (one for total, four for selected b blocks). Every coefficient is nonzero mod p>=7; the sum 1-1+1+3-2-2=0. ell parity ensures d integer and positive b>=10. Sum sizes 4d+6ell-1=3p. p7 boundary (4,6,5,4,1,1) totals21; b10.

**Independent all-subset check:** any whole-cell union has coefficient alpha-beta+gamma+3delta-2epsilon-2phi in [-5,5], so mod p zero iff integer zero. Splitting by delta∈{0,1} and epsilon+phi∈{0,1,2} exhausts ALL 2^6 whole-cell inclusion choices by 6 symbolic cases, not numerical enumeration. Exactly 10 whole-cell zero sums: empty, full, four b unions AB,ACE,ACF,ADEF, and their four b+1 complements CDEF,BDF,BDE,BC. All are genuinely distinct. No proper zero whole-cell union shorter than b or longer than b+1.

**Sizes check:** put b=2d+3ell-1. AB, ACE, ACF, ADEF each have b. The four complements have b+1. Nonzero u∈F_p³ arbitrary.

**Pair/triple check:** A1111 B1000 C0110 D0001 E0101 F0011 none has bitwise opposite in the occupied set; hence indexed pair-cover at cell level. For each omitted j use (A,B),(B,F),(B,E),(B,C); each agrees bit j and differs the other three, witnessing triple separation. Four edges form a star/tree on five vertices, D the sixth.

**Fatal overclaim prevented:** cells specify TOTAL sums only; they do NOT specify any individual z_i. The 3p-index no-short hypothesis quantifies over all possible partial-cell index subsets. None is checked or established by the aggregate argument. This is a genuine symbolic consistency countermodel to a TOO-WEAK lemma, not a counterexample to strong short extraction or D(C_n³)=3n−2. No classification of all possible six-cell systems, or seven/eight-cell systems, or five+ b blocks was completed. Exact B route D2<=6p−6 is UNPROVED; p5 Yiu remains SOURCE_STATED. Original source access enums unchanged, no hosted CI PASS.
