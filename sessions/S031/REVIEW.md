# S031 separate INTERNAL adversarial reconstruction

Reviewer: the session executor, separate mathematical pass; NOT independent external reviewer, Lean/Palomar, or hosted CI.

1. Pair-sum calculation independently re-derived: (N-2)lambda_ij + [(b-1)r_i-lambda_ij]+[(b-1)r_j-lambda_ij]-2(b-2)lambda_ij = (b-1)(r_i+r_j)+(N-2b)lambda_ij. N-2b=+1. Constant -(N-2)/2+(b-1)=-1/2 modulo p.
2. Signs: s=(-1)^b and t=(p+s)/2 satisfy st=1/2 mod p; thus pair-sum equals s(lambda_ij-t), NOT s(lambda_ij+t).
3. For each low r_i=t>=1, choose any b-block B_i; N-b=b+1 indices j outside it have lambda_ij<=t-1. Pair-sum nonzero implies SOME nonzero Psi_ijk. Directed-pair overcount <=2, unordered-triple capacity <=3, yielding ceil(L(b+1)/6). No distinct-witness requirement.
4. p7: b10, s+, t4, H8, L13, >=ceil(13*11/6)=24 nonzero triples. This arithmetic is an analytic substitution, not mathematical numerical search.
5. Projective sum signs -sum_Fp3=+sum_P2; total degree exactly 3(p-1). Blocking argument requires p+1 distinct directions in a common TWO-dimensional subspace (or a genuine blocking set), not merely p+1 equal vectors.
6. In the quartet identity U has 3p-4 linear factors; its c_h coefficient degrees sum exactly 3p-4 and Psi(U union q)=c(U) dot z_q. Any linear dependence among the four z_q yields a corresponding Psi relation. No m2p contradiction has been smuggled into the identity.
7. Rejected invalid stronger inference: every deletion triple contains a projective blocking set, so Psi=0. Such a covering premise is NOT derived, and would conflict with CLM-0130 for m2p. Three deletion degrees equal the CW threshold; no automatic vanishing.
8. Route B D2<=6p-6 not proved or activated. No novel priority, new D1/Dk theorem, indexed lift or universal stronger extraction.

**FIRST essential unproved lemma:** force sufficiently many retained triple sets to be projectively blocked (or otherwise force too few nonzero Psi) from the actual indexed zero-sum hypotheses, beyond the S031 lower support bound. Killing m2p would still leave m>=3p. Evidence status INTERNAL HAND PROOF, not external/formal certification.
