# S048 — seven-circuit affine inverse exclusion on n=15 (CLM-0185)
13 October 2026. Original-index symbolic Phase1 hand proof; no full C15^3 equality or counterexample.

## Exact conditional setting
Use the SIX quotient values A,B,C,D,E,U of S046 CLM-0176, with relations A+B=E, U+C=A, U+D=B in Q=C3^3. The three values A,B,U form a basis of Q. Take the indexed residual R=A^2 B^2 C^2 D^2 E^2 U (eleven ORIGINAL positions), total_Q(R)=0. Fix eleven disjoint monochromatic quotient-zero triples outside R, with their H=C5^3 sums P=(p_1,...,p_11), whose H sum is -h(R) in a hypothetical minimally zero augmented T44. Let E(P)=H\(-Σ(P)) with Σ(P) containing the empty subset.

Assume there exists a nonzero homomorphism ℓ:H→F5 and a scalar λ∈F5\{0} with E(P) contained in the affine hyperplane {v:ℓ(v)=λ}. This is a condition on the H extension set, NOT a universal assertion about all zero-sumfree P of length11.

## Seven genuine circuit families
For every choice of indexed copies compatible with the following count vectors, each W is a proper nonempty quotient-zero part of R and its complementary R\W is likewise nonempty quotient-zero. Each part has size >=4; total R size11. Relations A+B=E, C=A-U, D=B-U verify all Qzero conditions by coefficients a+c+e=b+d+e=u-c-d=0 mod3.

W1 = A+B+2E (length4)
W4 = 2A+2B+E (length5)
W2 = 2A+C+U (length4)
W3 = 2B+D+U (length4)
W7 = 2C+2D+E+U (length6)
W5 = 2A+B+C+2D (length6)
W6 = A+2B+2C+D (length6).

In hypothetical G-minimal T44, P plus the two decorated pieces W,R\W is a 13-term minimal H-zero sequence for every such cut (the partition uses ALL 44 original indexed positions). Hence h(W) ∈ E(P), so ℓ(h(W))=λ for each of these seven families and EVERY index choice.

Vary the A and B singleton in W1 to force ℓ(h(A_1))=ℓ(h(A_2))=:a and similarly b. Vary the E singleton in W4 to force common e. Vary the C singleton in W2 and D singleton in W3 to force common c and d. Write u=ℓ(h(U)). These are equalities of projected H labels only, NOT assumptions that original H decorations coincide.

The seven λ-equations include
(1) a+b+2e=λ (W1),
(2) 2a+2b+e=λ (W4),
(3) 2a+c+u=λ (W2),
(4) 2b+d+u=λ (W3),
(5) 2c+2d+e+u=λ (W7),
(6) 2a+b+c+2d=λ (W5),
(7) a+2b+2c+d=λ (W6).

Put s=a+b and t=c+d. (1),(2) give s=e=2λ over F5. Adding (3),(4) gives t+2u=3λ. From (5) get 2t+u=4λ. Solving yields u=4λ and t=0. But adding (6),(7) gives 3(s+t)=2λ. Substitution gives 6λ=2λ, i.e. λ=0 in F5, contrary to the chosen λ≠0. **No original-index H decoration of R satisfies all seven split circuit conditions under this affine E(P) hypothesis.**

## Immediate hostile kill
S046's partial witness used P=f1^4 f2^4 f3^3. Here E(P) is EXACTLY {v: third coordinate=1}, since the negative subset sums cover all first/two coordinates and third coordinates 0,2,3,4. Therefore the whole eleven-triple P configuration is excluded for this fixed R, regardless of the remaining eleven H labels; this is stronger than excluding S046's displayed three-cut decoration. In the particular displayed S046 assignment h(A/B/C/D)=0, h(E_1)=h(E_2)=(0,0,3), h(U)=(1,1,1), W4=2A+2B+E_1 has H sum (0,0,3). Together with TWO of the f3 decorated monochromatic quotient-zero triples it gives a proper nonempty genuine G=C15^3 zero-sum subset of the augmented T44. Thus that partial hostile model cannot be a minimal-zero T44.

## Correct limitations
Only the specified S046 six-value cap and residual shape R are analysed, not every six-support cap or every permissible stripping. No proof says E(P) lies in a nonzero affine hyperplane for all zero-sumfree 11-term P⊂C5^3. That missing inverse theorem would be strong and may itself be false. The proof eliminates a substantial all-index local inverse subfamily and proves neither D(C15^3)=43 nor existence of a length43 zero-sumfree G counterexample. Same-executor INTERNAL proof review only; no source-priority claim.