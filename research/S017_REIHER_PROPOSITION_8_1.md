# S017 — original Reiher Proposition 8.1

2026-10-12. ONE bounded Phase-1 original-primary-source symbolic hand-proof/provenance pass. SRC-0025: original 29-page Rostock PDF, printed pp17–18, PDF zero-based pages16–17. Fresh lawful download: 289379 bytes, SHA256 `7d94931bcbf8fb4ce77c0ed94206659df74e8cb5543e1615e7dde23e86b994d8`, freshly measured in S017 and equal to the historical S013 hash. Original page17 display checked visually against extracted text. The PDF is not committed. No mathematical numerical/computational search, CAS, author code, solver, enumeration, Lean, campaign, candidate, manuscript or contact.

## CLM-0103 — Proposition 8.1, exact hypotheses and geometric reduction

Claim: a cloudy sequence over Fp² containing FOUR DISTINCT original points which either are vertices of a parallelogram or have one point equal to the sum of the other three is simple. Cloudy means an indexed length-(2p−1) zero-sum sequence with no nonempty proper zero-sum index subset. Simple means the normal form defined in the original introduction, as used in CLM-0094/0100. No general four-point classification is assumed.

For p=2 or3 simplicity is already independently established by S014: Obs2.6 for p2, and five nonzero terms in four vector directions, Cor2.5 and Obs2.6 for p3. For the remaining proof assume p≥5, INCLUDING p5. In the sum configuration relabel the original four points so D=A+B+C and set η=1. In the parallelogram configuration label opposite vertices A,C and B,D, so A+C=B+D, hence D=A−B+C and η=−1. Thus both hypotheses yield precisely D=A+ηB+C with η²=1. In an odd field these are the two roots of (η−1)(η+1)=0. Degenerate affine parallelograms with three distinct collinear vertices are already covered by Prop5.1; the algebra below needs only the stated relation and distinctness, so no extra nondegeneracy assumption is imported.

Choose one indexed occurrence of each of A,B,C,D, leaving the ORIGINAL residual positions P1,...,P_(2p−5). By cloudy Cor2.5 each distinct pair of original points is linearly independent with the origin. In particular k=[A B]≠0 and C=xA+yB has unique coordinates; D=(x+1)A+(y+η)B. The full six-pair determinant audit is

| Original pair | Determinant |
|---|---|
| A,B | k |
| A,C | yk |
| B,C | −xk |
| A,D | (y+η)k |
| B,D | −(x+1)k |
| C,D | (ηx−y)k |

All six are nonzero by Cor2.5. Thus x,y,x+1,y+η,ηx−y are nonzero, though we do NOT divide by any of these expressions. No affine translation is applied to the sequence (which could invalidate cloudy zero-sum hypotheses). No extra general-position condition, exclusion of trapezoids, or assumption on a conic is needed.

## Four genuine conditional equations

Define T(U,V,W)=µ(U,V,W,P1,...,P_(2p−5)), symmetric and trilinear by the independently proved coefficient definition. Exactly 3+(2p−5)=2p−2 indexed arguments occur. Write u=T(A,A,A), v=T(A,A,B), w=T(A,B,B), z=T(B,B,B), and h=x(x+1), b=2xy+ηx+y, c=y(y+η). Deleting each of the four chosen original indices gives a suspicious sequence with µ=1, CLM-0094. These are FOUR actual deletion equations, not zero-coefficient assumptions on a changed sequence:

E1 (omit A): T(B,C,D)=hv+bw+cz=1.

E2 (omit B): T(A,C,D)=hu+bv+cw=1.

E3 (omit C): T(A,B,D)=(x+1)v+(y+η)w=1.

E4 (omit D): T(A,B,C)=xv+yw=1.

For E1 and E2 expand the two linear slots C=xA+yB, D=(x+1)A+(y+η)B: their AA coefficient is x(x+1), AB coefficient is x(y+η)+y(x+1)=b, BB coefficient is y(y+η). E3/E4 follow by one-slot multilinearity. Residual repeats cause no ambiguity: ONLY the designated indexed occurrence is omitted each time.

## Exact strategic equation

Omit the original D occurrence and accentuate A,B,C in the remaining suspicious sequence. CLM-0095 (original Prop4.1, p≥5) applies with the SAME residual positions and SAME T. Its determinants are [BC]=−xk, [CA]=−yk, [AB]=k, with sum k(1−x−y). Trilinearity gives T(C,C,C)=x³u+3x²yv+3xy²w+y³z and T(A,B,C)=xv+yw. Divide the strategic identity ONLY by k≠0 to obtain

E5: (x³−x)u+3x(x−1)(y−1)v+3(x−1)y(y−1)w+(y³−y)z=0.

The v coefficient is 3x²y+3x(1−x−y)=3x(x−1)(y−1); the w coefficient is 3xy²+3y(1−x−y)=3(x−1)y(y−1). This equation comes from the suspicious original deletion; there is no strategic identity asserted for a non-suspicious auxiliary sequence.

## Printed multipliers and explicit hand cancellation

Multiply (E1,E2,E3,E4), in their PRINTED ORDER, by

α=y−η, β=x−1, γ=ηx+y, δ=(3+η)(1−x)−4y.

The u coefficient in the weighted sum is βh=(x−1)x(x+1)=x³−x. The z coefficient is αc=(y−η)y(y+η)=y³−η²y=y³−y. For v the coefficient αh+βb+γ(x+1)+δx expands term by term as

 (x²y+xy−ηx²−ηx)
 +(2x²y−2xy+ηx²−ηx+xy−y)
 +(ηx²+ηx+xy+y)
 +((3+η)x−(3+η)x²−4xy)
 =3x²y−3xy−3x²+3x=3x(x−1)(y−1).

For w the coefficient αb+βc+γ(y+η)+δy expands as

 (2xy²+ηxy+y²−2ηxy−η²x−ηy)
 +(xy²−y²+ηxy−ηy)
 +(ηxy+η²x+y²+ηy)
 +((3+η)y−(3+η)xy−4y²)
 =3xy²−3xy−3y²+3y=3(x−1)y(y−1).

Every η-dependent term cancels in these two sums; the only η² simplification needed for the pure coefficients was η²=1. Hence the weighted LEFT side of E1–E4 is EXACTLY the left side of E5. The weighted RIGHT side is

 α+β+γ+δ
 =y−η+x−1+ηx+y+(3+η)(1−x)−4y
 =2−2x−2y=2(1−x−y).

Subtract E5 to conclude 2(1−x−y)=0. The only additional divisor is 2≠0 since p≥5. Thus x+y=1. This is precisely the printed cancellation; it uses no division by a possibly zero multiplier or by x−1,y−1,1−x−y. All formulas and divisions remain valid at p5.

## Apply Prop5.1 to original points and STOP

Now C=xA+(1−x)B, so C is on the affine line through A and B. Equivalently [B−A,C−A]=k(1−x−y)=0. A and B are distinct original points, so this is a genuine line; [AB]≠0 also shows it avoids the origin. C was chosen as a THIRD DISTINCT original point, not an inserted auxiliary value. In fact C=A orB would force x=1 or0 and violate distinctness, but these endpoint exclusions are not needed as divisors. Thus the exact premise of independently proved Prop5.1 (CLM-0100) holds for the ORIGINAL cloudy sequence, proving simplicity. QED for both configurations and every prime, including p5.

Dependencies actually used: CLM-0094 (conditional µ=1, Cor2.5 and p2/3 simplicity), CLM-0095 (Prop4.1) and CLM-0100 (Prop5.1). CLM-0101/0102 Section6 are preserved, not re-proved and not needed as additional assumptions here. No unclosed prerequisite entered the proof. STOP mathematical expansion after Proposition8.1. Example8.2, Section9, Lem9.2/9.6, Proposition10.1, full Property B, unconditional Property C, eta(C7³)≤116 and the rank-three conjecture are NOT proved in S017.

## S017 read-only provenance and frontier

Fresh S017 official Sheikh137p original thesis PDF request through web retrieval returns HTTP403 Forbidden, separately from S016/S015/S014/S013 attempts. Full Chapter4/Remark4.3.11 not obtained. A lawful original-location search finds the same official PDF and thesis record, not a newly accessible complete original. Original GHST C53.html request resolves to HTTPS and is inaccessible via the web tool; neither full code nor output authenticated. Yiu original v1 HTML/abstract read-only and ancillary locator inspected; no independently authenticated final M1 three-disjoint implementation/log/certificate acquired. Historical S013 16680-byte source bundle hash `99dc658b3381038fe0c7b2f89145c52a9687e185883cf2a6fdcc0cb8860b1e21` NOT freshly rehashed in S017. Repeated 98622-generator/230983-extension stages do not establish independent final M1 checking; M2 s≤6=24 and M3 s≤7=19 are distinct predicates. Nothing executed; retrieval failure is not global absence.

Complete inherited source/claim fields preserved. GG1999 B⇒C stays conditional on Property B, historical CLM-0082 SOURCE_STATED; BSP2012 stronger 3(p−1)/2 coefficient unproved, original split only R=(3p−1)/2; BSP2007 full diagrams/classification upper induction unproved, restricted k−3 count insufficient; subscript D3(C3³)=15,D4=18 distinct from superscript at-most-three threshold17. S012 corrected doubled triple and actual terminal t-sum trichotomy unchanged.

All n1..30 audited against BOTH full numerical mirrors: n1 trivial, prime powers source-exact, historical composite exact rows n6,10,12,14,18,22,24,26 retain source evidence; intervals n15 43..45,n20 58..59,n21 61..63,n28 82..83,n30 88..90 unchanged. Every numeric/status/evidence row preserved. Schmid n6=16 and original van Emde Boas II/III exact rank-three 2p^a/3·2^a families SOURCE_STATED without whole-source independent proofs. Bounded targeted searches with both search services authenticate no new exact original update for those five intervals; NON-DISCOVERY IS NOT CURRENT OPENNESS. Inherited14/17,+5,orbit43/699/5553 quarantined. Rank-two progress does not upgrade rank-three evidence. Phase1 IN_PROGRESS, Phases2/3 NOT_STARTED; CAM-0001 PROPOSED / NOT RUNNING activation BLOCKED by published n6=16. No replacement target or search.
