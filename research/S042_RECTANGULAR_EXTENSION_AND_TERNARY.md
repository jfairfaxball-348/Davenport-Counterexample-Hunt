# S042 — A 17-plane rectangular extension theorem and the ternary antipodal gate

13 October 2026. One internal symbolic proof session; no numerical mathematical search, source status promotion, external verification or novelty finding.

## CLM-0162: exact extensions of a 17-in-plane rectangular family

Let H=C10^3 with basis e1,e2,e3. Let
 A=e1^9 e2^8
and B consist of nine indexed terms a_j e1+beta_j e2+e3, j=1,...,9, where a_j,beta_j in C10. Put P=A*B, |P|=26. This is a genuinely 17-position direct-summand plane configuration: A is supported in K=<e1,e2>, B has common generator e3 in the cyclic H/K.

Since every nonempty B-subcollection has e3-coordinate between1 and9, P is zero-sumfree. The subset sums of A are EXACTLY all a e1+b e2 with a arbitrary modulo10 and b in {0,...,8}. Therefore a nonempty subcollection Z of B*x with zero e3-coordinate can be completed using A to a nonempty zero sum exactly when its e2-coordinate is NOT 1 modulo10. This gives an exact reduction to nine decorated cyclic positions, and an exact E(P) computation.

Write T=sum_j beta_j and let x=a e1+b e2+r e3, r in {0,...,9}. To extend P without a zero sum, every nonempty zero-e3 subcollection of B*x must have second coordinate 1.

If r=0, the only such subcollection is {x}; hence b=1.
If r=1,...,9, every such subcollection consists of x and exactly 10-r of the nine B indices, so the condition is
 b + sum_{j in J} beta_j = 1 (mod10) for ALL J of size 10-r.
When r=1 this is the unique all-nine choice, giving b=1-T. For 2<=r<=9, the subset size is between1 and8. All fixed-size subset sums can be equal only if all beta_j are equal, by swapping one indexed j for another.

Accordingly the extension set is EXACTLY:
* If beta_j are not all equal: E(P) consists of ALL a e1+e2, and ALL a e1+(1-T)e2+e3, a arbitrary in C10. Every x in E obeys the nonzero character equation chi(x)=b+T*r=1.
* If all beta_j=beta: E(P) consists of ALL a e1+(1+r*beta)e2+r e3, a,r arbitrary in C10. Every x obeys chi(x)=b-beta*r=1.

Thus 4E(P) and3E(P) are DISJOINT: any four-extension sum has chi=4 and any three-extension sum has chi=3 in C10. Such a P cannot arise as the Fano-pair sequence of a hypothetical n20 counterexample. The result is NOT a universal character confinement theorem for arbitrary 26-term zero-sumfree P.

Hostile examples: with one beta_j=1 and the other eight0, the extension image has two different e3-levels and character chi=b+r=1, while P can avoid the already excluded 18-term saturated plane. With all beta=0, the extension set has every e3-level but all have b=1. A claim that all extensions have the same CYCLIC QUOTIENT would be false even in this family; the surviving invariant is an affine character, not one fixed quotient value.

**General 17-plane decorated reduction without generator-repetition:** Retain A=e1^9e2^8 but allow B nine arbitrary elements of H, with e2/e3 coordinates (beta_j,r_j). For any x, P*x is zero-sumfree if and only if EVERY nonempty indexed subcollection Z of B*x whose sum r is0 has sum beta equal1 modulo10. The e1 coordinates are irrelevant because the e1^9 subset sums cover all first coordinates. This is an EXACT 3D-to-decorated-cyclic inverse reduction, with the sole difficult case now the possibly non-generator-repeated nine-term projected sequence. The preceding character theorem cannot be applied there without additional proof.

## CLM-0163: n15 ternary antipodal-support gate

Condition on the historical/source-stated D_11(C3^3)=39 and the known D(C5^3)=13 required in the S041 n15 source framework. A hypothetical zero-sumfree S43 in C15^3 projects to U43 in C3^3.

No quotient position is zero: deleting it leaves 42=D_12(C3^3) positions, admitting 12 more disjoint quotient-zero blocks, hence 13 decorations in C5^3 and an actual zero sum. Nor can U have TWO index-disjoint pairs with opposite nonzero quotient values: deleting four positions leaves 39=D_11(C3^3), forcing 11 more quotient blocks, again 13 total. These are the precise S041 forbidden-block statements.

There are (3^3-1)/2=13 opposite-value pairs {v,-v} in C3^3, i.e. projective lines. If two DIFFERENT projective classes both occur with both orientations, they give disjoint opposite pairs. If a single class has multiplicity >=2 on EACH side, it also gives two disjoint opposite pairs. Therefore among the 13 unoriented classes at most one uses both orientations, and in that class the minority orientation occurs exactly once. Consequently U uses AT MOST 14 distinct nonzero values (one orientation in each of 13 classes, plus at most one exceptional opposite). This shrinks the inverse-support problem from 26 possible nonzero vector values to 14. Some quotient value necessarily occurs at least four times because 43>3*14.

The source-stated BSP2007 Prop8 inverse diagram and exact ternary 44-term extremiser classification have NOT been reconstructed here. The 14-value support bound does NOT classify the multiplicities, prohibit the appended 44-term minimal zero sum, or solve D(C15^3)=43. All 43 original indices and their arbitrary C5^3 CRT components matter.
