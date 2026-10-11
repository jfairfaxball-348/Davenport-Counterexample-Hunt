# S003 — Frontier re-audit of C_n^3, n=1..30 (2026-10-11)

The lower bound \(D^*=3n-2\) is independently proved in research/FOUNDATIONS.md. **SETTLED** below means exact by *primary SOURCE_STATED* Olson p-group theorem, not programme formalisation. **SANDWICHED** means an independently written deduction of a lower/upper *interval*, conditional on primary SOURCE_STATED multiwise input where used, not an exact value. No composite case is certified or claimed settled; no 'UNKNOWN' label implies an external mathematical open problem.

**S002 correction:** the 2007 Bhowmik–Schlage-Puchta Proposition 1 reads \(D_k(C_3^3)=3k+6\) for \(k\ge3\), giving \(D_3=15,D_4=18\), not the inherited 14/17. The old tripling \(+5\) upper estimate cannot be derived; valid sourced tripling estimate is \(+6\). The source-reported Grinsztajn universal \(4n-P(n)-2\) bound is a supplemental theorem claim with conditional Lean axioms, not used to sharpen the table.

| n | D* | Classification | Audited D interval | Upper-bound reason |
|---:|---:|---|---|---|
| 1 | 1 | SETTLED | 1 | trivial |
| 2 | 4 | SETTLED | 4 | Olson p-group, SRC-0003 |
| 3 | 7 | SETTLED | 7 | Olson p-group, SRC-0003 |
| 4 | 10 | SETTLED | 10 | Olson p-group, SRC-0003 |
| 5 | 13 | SETTLED | 13 | Olson p-group, SRC-0003 |
| 6 | 16 | SANDWICHED | 16..17 | 2D(C3^3)+3 = 17; source-stated Olson 7 and programme-proved C2 multiwise |
| 7 | 19 | SETTLED | 19 | Olson p-group, SRC-0003 |
| 8 | 22 | SETTLED | 22 | Olson p-group, SRC-0003 |
| 9 | 25 | SETTLED | 25 | Olson p-group, SRC-0003 |
| 10 | 28 | SANDWICHED | 28..29 | 2D(C5^3)+3 = 29 |
| 11 | 31 | SETTLED | 31 | Olson p-group, SRC-0003 |
| 12 | 34 | SANDWICHED | 34..36 | 3D(C4^3)+6 = 36; NOT 35 |
| 13 | 37 | SETTLED | 37 | Olson p-group, SRC-0003 |
| 14 | 40 | SANDWICHED | 40..41 | 2D(C7^3)+3 = 41 |
| 15 | 43 | SANDWICHED | 43..45 | 3D(C5^3)+6 = 45; NOT 44 |
| 16 | 46 | SETTLED | 46 | Olson p-group, SRC-0003 |
| 17 | 49 | SETTLED | 49 | Olson p-group, SRC-0003 |
| 18 | 52 | SANDWICHED | 52..53 | 2D(C9^3)+3 = 53 |
| 19 | 55 | SETTLED | 55 | Olson p-group, SRC-0003 |
| 20 | 58 | SANDWICHED | 58..61 | 2D(C10^3)+3 <= 61 |
| 21 | 61 | SANDWICHED | 61..63 | 3D(C7^3)+6 = 63; NOT 62 |
| 22 | 64 | SANDWICHED | 64..65 | 2D(C11^3)+3 = 65 |
| 23 | 67 | SETTLED | 67 | Olson p-group, SRC-0003 |
| 24 | 70 | SANDWICHED | 70..72 | 3D(C8^3)+6 = 72; NOT 71 |
| 25 | 73 | SETTLED | 73 | Olson p-group, SRC-0003 |
| 26 | 76 | SANDWICHED | 76..77 | 2D(C13^3)+3 = 77 |
| 27 | 79 | SETTLED | 79 | Olson p-group, SRC-0003 |
| 28 | 82 | SANDWICHED | 82..85 | 2D(C14^3)+3 <= 85 |
| 29 | 85 | SETTLED | 85 | Olson p-group, SRC-0003 |
| 30 | 88 | SANDWICHED | 88..93 | min(2D(C15^3)+3,3D(C10^3)+6) <= 93 |

## Phase-2 entry target: n=6 (PROPOSED only)

At n=6, 16≤D(C6^3)≤17, independently deduced in [S002_INDUCTIVE_PROOFS](../research/S002_INDUCTIVE_PROOFS.md). The existence or absence of a 16-term zero-sumfree sequence is not established. An n=6 skeleton must admit at most three disjoint mod-3 zero sums, but the inherited 5553 orbit count is unverified and the previously assumed multiwise thresholds were wrong. Any enumeration/orbit reduction requires independent proof **after Phase-1 PASS and Phase-2 authorization**. No campaigns or searches executed here.

For n=10, Yiu's 2026 abstract reports D4(C5^3)=30, ruling out the inherited antecedent D4=28. Our upper 29 comes instead from the proved binary multiwise deduction and Olson D(C5^3)=13. The new primary Grinsztajn statement is not a pointwise resolution.

### S003 gate annotation
Every n=1..30 interval remains the S002 source-conditional deduction. The binary multiwise recurrence is standalone PROGRAMME_PROVED; ternary recurrence depends on published BSP theorem whose proof is not fully independently reconstructed. Original Grinsztajn PDF body inaccessible; universal author bound NOT used to sharpen these rows. n=6 still 16..17; CAM-0001 only PROPOSED. Details in research/S003_SOURCE_PROOF_AUDIT.md.
