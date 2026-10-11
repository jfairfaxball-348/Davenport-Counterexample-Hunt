# Failures, discrepancies, lessons

| Session | Topic | Observation | Disposition |
|---|---|---|---|
| S001 | n=10 inherited shortcut | Seed says D4(C5^3)=28 might settle n=10, but Yiu 2026 abstract asserts 30 | Keep conditional seed quarantined; n=10 not newly settled |
| S001 | Open-status inference | Historical literature saying rank-three remains open does not decide any single n today | Cases lacking inspected proof remain UNKNOWN/provisional |
| S001 | 2019 primary HTML erratum hazard | Zakarczemny HTML Lemma 3.4 appears to state rank-two D=n1+n2-2 while D*=n1+n2-1 | Avoid using that line; verify with primary survey or original |
| S001 | Computation provenance | 43/699/5553 and Dk values are inherited without local scripts/hash | Regression targets only; no exact certificate |
| S001 | Empty initial repo | A one-file initialization commit is prerequisite to a normal S001 parented atomic commit | Keep initial .gitignore and record initialization SHA |

| S002 | Primary source contradicts inherited D3/D4(C3^3) | BSP Proposition 1 D_k=3k+6 k>=3: D3=15, D4=18; inherited 14/17 wrong | New CLM-0050; inherited claims quarantined |
| S002 | Off-by-one tripling failure | Published ternary multiwise formula yields 3D(Cm^3)+6, not +5 | Wider bounds at 12,15,21,24; no global falsehood claim for +5 |
| S002 | Misleading Grinsztajn formalisation reading | Author README admits Lean axiomatizes zero-sum inputs; PDF proof not yet independently audited | SOURCE_STATED; S003 proof challenge |
| S002 | n=6 orbit-count provenance | 5553 count inherited without scripts and uses wrong D4 threshold | Proposed only; no exhaustive claims |
| S002 | Primary thesis qualification | Sheikh 2017 thesis explicitly reconstructs potential proof gaps in BSP 2007 | Independent literature proof inspection remains |

| S003 | Original Grinsztajn PDF inaccessible | Author GitHub PDF blob exists, binary-only connector and disabled web raw/HTML routes prevent reading written proof | Source-level 4n−P(n)−2 theorem remains unverified |
| S003 | BSP large-exponent exact imported axioms | Primary author PDF has visible editorial notes including 'Forgot the second claim'; p>7/7 cutoffs differ | Do not upgrade universal bound without definitive source reconciliation |
| S003 | Sheikh Chapter 4 incomplete | Indexed thesis intro flags gcd(d,6) issues and incorrect Remark 4.3.11; full PDF 403 | Avoid declaring 2007 auxiliary cases independently closed |
| S003 | D³ vs D₃ collision | Original superscript at-most-three D³=17, multiwise D₃=15 and D₄=18 | Inherited 14/17, +5 and 5553 remain invalid/unverified |
| S003 | Freeze–Schmid original DOI correction | S002 listed wrong 2009.07.002 | Primary PDF p.9 and correct 2010.07.028 now recorded |
| S003 | Exact C6³ theorem diligence | Targeted search did not authenticate newer individual proof | No inference of openness from absence of a hit |
