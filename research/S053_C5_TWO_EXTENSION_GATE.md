# S053 — two-extender and midpoint obstruction for arbitrary C5³ P11 (CLM-0204)
14 October 2026. SOURCE-DEPENDENT use of historical p-group identity D(C5³)=13, retained SOURCE_STATED, no new original-primary-source proof and no D(C15³)=43 conclusion.

Let H=F5³ and let P be ANY indexed eleven-term zero-sumfree sequence. Write σ=ΣP, c=−σ, and E=H\(−Σ(P)), the set of x such that P*x remains zero-sumfree. Complement symmetry gives E=c−E. Let d=c/2 (division by2 is LEGITIMATE in F5³, unlike dividing original odd C20 elements), and F=E−d, hence F=−F.

**Pair-sum exclusion theorem (conditional on SOURCE_STATED D(H)=13).** For EVERY x,y∈E, including two separately indexed copies with the same H value, P*x*y has 13 terms and hence has a nonempty zero-sum submultiset by D(H)=13. Since P, P*x and P*y are each zero-free, the zero-sum must contain BOTH new indexed x,y, so −x−y∈Σ(P). Equivalently x+y∉E. Thus
  (E+E)∩E=∅.   (The empty E case is vacuous.)
In translated symmetrical coordinates this is exactly
  d∉F+F+F,
because E+E meets E iff d=f3−f1−f2 with f_i∈F, and F=−F. Also 0∉E by the empty P subset, hence −d∉F and d∉F. These are genuine restrictions valid for ALL supports ≥7 and ALL indexed repetitions, not just the S051/S052 six-support examples. They still do not force d∉span_F5(F), the specific inverse condition of S053.

**Midpoint minimal-zero-sum equivalence.** Since 2d=c, the length13 indexed sequence P*d*d has total zero. It is minimally zero-sum iff d∈E. Indeed P and P*d contain no zero-subset iff d∈E. If a proper P-subset B plus both copies d summed to0, then ΣB=−2d=σ, giving a nonempty zero-sum complement P\B, contradicting P zero-free. No other proper zero subset exists. This is an exact structural equivalence, NOT an assertion that every P has midpoint in E.

**Hostile abstract no-go to avoid overclaim:** take F={±e1,±e2,±e3} in F5³ and d=(2,2,2). Then F=−F, spans all three dimensions, yet d∉3F because attaining 2 in each of three coordinates takes at least six ±basis summands, more than three. Also −d∉F. E=d+F therefore has FULL affine span, excludes0 and satisfies (E+E)∩E=∅ and E=2d−E. This is an abstract EXTENDER-SET countermodel to inferring the proposed universal inverse from only complement symmetry plus pair-sum exclusion; it is NOT asserted to equal E(P) for any actual eleven-term zero-free P.

The remaining challenge is to use actual indexed subset-sum structure of P11 (including support≥7, six-cap re-strippings and empty E), beyond these general additive set axioms. No computational mathematical search was performed.
