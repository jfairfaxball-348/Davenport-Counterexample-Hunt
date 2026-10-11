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

| S004 | Major frontier omission | Schmid2011 Thm4.1 gives D(C6³)=16; original 1969 families settle eight composite rows | Withdraw n6 tooling recommendation; retain old valid nonsharp inequalities as history. CAM-0001 PROPOSED / NOT RUNNING, activation blocked |
| S004 | Definitive draft reconciliation | Publisher offprint removes editorial note, renumbers lemma and includes p≥7 | Use SRC-0021 as definitive version; access obstacle resolved, proof completeness separate |
| S004 | Published coefficient discrepancy | Short-block statement (3p−1)/2 differs by one from split-proof text and Lem2.3 coefficient 3(p−1)/2 | Exact axiom unclosed; S004 supplies weaker sufficient conditional route, not theorem disproof |
| S004 | p7 eta case gap | Published Lem5.2 brief cases and absent (1,6) used in a stated zero sum | No exhaustive case closure or numerical replacement; retain SOURCE_STATED |
| S004 | Small-prime source dependencies | GHST eta5 theorem rests on computational Prop5.6; BSP2007 diagrammatic cases incomplete here | No code execution, programme exact computation or source-proof upgrade |
| S004 | Thesis scope | Full Chapter4 remains HTTP403; indexed p41 exactly-three counterexample has a two-term zero sum | Specific remark does not refute earlier at-most-three-free hypothesis; full review still outstanding |
| S004 | Yiu ancillary discrepancy | Both downloaded source archives contain only five TeX/bibliography files | Do not claim advertised computations independently verified or globally absent; locate records in future source-only session |
| S004 | Absence of CI | Public REST workflows0, runs0, check-runs0; combined status pending with total_count0 | No CI PASS. Administrative validation is distinct from Actions and mathematical certification |

**Negative-results scope through S004:** no exhaustive negative mathematical result has been produced; no search space was executed. Inherited 43/699/5553 remain quarantined. Source-access failures and proof gaps are not UNSAT certificates or counterexamples.

| S005 | Published BSP2012 Lemma5.2 p7 alleged zero sum | 2(6,1)+(1,6)+(1,0)=(0,1) in C7², not zero | New local **proof defect** CLM-0073; no false claim that Lemma5.2 fails; entire p7 case not certified |
| S005 | Rank-two prime dependency | Reiher 2010 p27 identifies Property B⇒Property C via Gao–Geroldinger, but original proof chain not fully reconstructed | SRC-0025/CLM-0074; no universal bound upgraded |
| S005 | GHST2007 computational record | Published original Prop5.6 p17 gives C53.html complete-code/output pointer; record not accessible/read | Provenance gap recorded; no source execution/COMP_EXACT |
| S005 | Access and frontier | Full Sheikh Chapter4 remains inaccessible, Yiu code/logs remain unlocated, five intervals persist after targeted review | Keep explicit incomplete proof/access gaps; no present-day openness claims |

**S005 negative scope:** no exhaustive mathematical negative, SAT certificate, orbit count, search, sequence generation or candidate. Historic inherited 14/17, +5, 43/699/5553 stay quarantined.

| S006 | Published p7 alleged zero sum | False printed (1,6) expression can be replaced in that same assumed case by 2(6,1)+(2,4)+(0,1)=0 | Valid conditional CLM-0075 only; do not claim full case exhaustion or eta7 proof |
| S006 | Stronger BSP coefficient and source dependencies | Short block split gives (3p−1)/2, not claimed 3(p−1)/2; GG/Reiher and BSP diagram proofs incomplete | CLM-0068 only a conditional replacement; Phase1 remains IN_PROGRESS |
| S006 | Computation and interval provenance | GHST C53 actual original code uninspected, Yiu M1 final predicate distinct from generated counts, no new exact primary n15/20/21/28/30 | Never label code certified, UNSAT, or a currently open row based on absence |

| S007 | BSP p7 reduction | First x,2x WLOG can be proved by replacement but later subgroup/classification reduction not verified | CLM-0076 limited PROGRAMME_PROVED, no eta7 upgrade |
| S007 | Original Sheikh dissertation | Direct university 137p PDF located/indexed but full-file HTTP403 | Full Chapter4 not read; no exactly-three/at-most-three conflation |
| S007 | GHST/Yiu provenance | GHST C53 code inaccessible, Yiu M1 generator repetitions do not repeat final predicate; M2/M3 distinct | No computed certificate or external code run |
| S007 | Hosted CI/protection | No runs/jobs/checks/status contexts, protection read 403 | No CI PASS or branch-unprotected claim |

| S008 | p7 mixed-line normalization | Under no short zero sum, distinct values on an occupied line have ratio 3 or 5 once x,2x eliminated; two such lines admit a conditional GL2 normalization, not the assertion that at most one exists | CLM-0077 scope limited; full p7 proof and eta7 not closed |
| S008 | p7 final t cases | If preceding multiplicity setup actually holds, t=0,3,5,6 yield explicit forbidden short sums; t1/2/4 and setup are not proved | CLM-0078 partial hand check only |
| S008 | Source coefficient / access | Printed 3p split still one term too weak, Sheikh PDF current fetch error after historical 403, C53 unavailable, Yiu archived artifacts not independently located | Phase1 held; source-stated results not demoted, no code run |
| S008 | Hosted GitHub verification | Actual workflows0, runs0, jobs0, check-runs0, statuses0; rulesets [] but protection not independently readable | ADMIN validation is NOT CI PASS; no unsafe inference |

**S008 negative scope:** no mathematical exhaustive negative, zero-sumfree candidate, campaign, SAT/ILP, code execution, numerical enumeration or formal certificate. Historical 14/17, +5, 43/699/5553 quarantined.
