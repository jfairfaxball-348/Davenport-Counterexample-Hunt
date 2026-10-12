# S029 separate adversarial reconstruction

This is a separate logical review pass by the session executor, not an external reviewer or formal certification. No delegation was requested.

1. **Degree and support:** delete ONE original index; n=3p-1 strictly exceeds 3(p-1). Only three group polynomials are used, not the four-polynomial length-divisibility system. Indicator proof has total degree at most 3(p-1)^2<n(p-1), making each monomial sum vanish. Identically zero coordinate polynomials cause no problem.
2. **Signs:** each indexed support contributes (p-1)^k=(-1)^k mod p. The empty support contributes +1; full Z cannot survive deletion. Proper zero sums have sizes b/b+1 because their complements are also nonempty zero sums. Thus Q_i=1+s(m-r_i)-sr_i. Multiplication by s gives 2r_i=m+s, not m-s.
3. **Complement direction:** a b+1 zero-sum subset avoids i exactly when its complementary b subset contains i. Repeated vector values do not identify index subsets.
4. **Double count:** exact sum_i r_i=mb. Summing the per-index congruence over 3p positions yields 2mb=0 mod p; since 2b=-1 mod p, m=0 mod p. The case m=0 is forbidden by Q_i=1. No assumption m<p was smuggled into this step.
5. **Exclude m=p:** r_i in [0,p] with nonzero residue t has exactly one lift t. Hence 3t=b, whereas b=1 mod3. Contradiction. Therefore m>=2p, not merely m>=p. The arithmetic is integer after the modular step.
6. **m=2p:** only two degree lifts t,t+p; exact incidence total gives H=3p-1-3t. At p7 degrees 4/11 with counts13/8 give140. At p5 degrees2/7 with counts7/8 give70. These are necessary censuses, not realizations or searches.
7. **Scope attack:** S028 proves four WHOLE-CELL b blocks only. A no-short vector lift may have additional partial-cell b blocks and b+1 complements. Replacing complete m by4 for an arbitrary lift would be a fatal gap. The valid corollary excludes exactly-four indexed families, independently of signature count; an arbitrary six-cell lift requires >=2p-4 extra partial-cell b blocks, and is not excluded.
8. **Dependencies:** local theorem is self-contained through elementary field-power sums; no Olson D1 import is needed. Only application to a longer S uses prior p-or-3p extraction. No source statement or D1/Dk value is promoted, no novelty or current-openness claim.

Conclusion: CLM-0125/0126 hand proof passes this logical reconstruction. First essential open case is arbitrary indexed families m>=2p, including m=2p with the forced degree census. Stop Route A. Route B not activated; D2 target and strong extraction remain unproved. Administrative validation and absent hosted checks do not certify mathematics.
