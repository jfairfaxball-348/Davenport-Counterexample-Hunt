# S013 — original rank-two extraction, eta and conditional B⇒C

2026-10-11. One preregistered Phase-1 original-primary-source hand-proof/provenance pass. Entry main `e22e1f369606c848d94b71bce737d74301a00954`. All sequences below have indexed positions. A short zero sum is NONEMPTY and has length AT MOST p. No mathematical numerical/computational search, enumeration, author code, solver, candidate, Lean or campaign was used. Proofs are symbolic hand arguments; source reading/OCR and administrative scripts are not mathematical searches.

## 1. Original source identity and prerequisite boundary

The coauthor publications list https://geroldinger.github.io/publications.html independently authenticates item38's original GG1999 scan at https://geroldinger-0836a9.gitlab.io/38.long-minimal-zero-sequences.pdf . Fresh download has the same 1,147,605 bytes and SHA256 a60f6192235fa25ac9161dbb689032de1c67d0d8684e3c703cb469f8681ee42f as S012. Original printed p185, pp203–208 and bibliography pp209–210 inspected, with rendered scan checked against read-only OCR. This is SRC-0026, not the GG2006 survey.

Original p185 Lem4.3(1),(2) cites [Ol2;Lemma1.1], John E. Olson, *A combinatorial problem on finite Abelian groups II*, JNT1(1969),195–199, DOI10.1016/0022-314X(69)90037-7. Publisher metadata was inspected; the attempted full-PDF endpoint returned HTTP200 but only a 195-byte Site Unavailable HTML body. The original Olson proof was NOT acquired/read; metadata and an HTTP200 are not PDF access. New SRC-0027 is METADATA_ONLY. The precise required rank-two statements are independently proved below, so this access limitation does not leave those mathematical premises as axioms.

[Ga4] in the actual GG bibliography is W. Gao, *On a combinatorial problem connected with factorizations*, Colloquium Math72(1997),251–268. Original publisher-hosted archive https://matwbn.icm.edu.pl/ksiazki/cm/cm72/cm7225.pdf authenticated against the journal volume listing/DOI10.4064/cm-72-2-251-268, newly SRC-0028. Lemmas5–7 printed pp253–255 read. Lem7 assumes H=C_n1⊕…⊕C_nl, n_l|n, n≥D(H), and D(H⊕C_n²)=2(n−1)+D(H); for a ZERO-SUM S in H⊕C_n with |S|≥n+D(H), it supplies a proper zero block T with |S|−n≤|T|<|S|, so its complement has length1..n. At H=C_p,n=p this imports D(C_p)=p and D(C_p³)=3p−2. Its whole general proof is not certified here. Section3 instead proves the exact required rank-two consequence without importing the rank-three p-group theorem.

The complete S012 CLM-0087 p7 Lem5.2 proof is preserved, never reopened. No specific defect was demonstrated in this pass. Earlier CLM-0075–0079,0081,0083 and CLM-0088 retain their original narrow scopes. Printed 2(6,1)+(1,6)+(1,0) remains nonzero; the available different sum in S012 remains valid.

## 2. CLM-0089 — self-contained finite-field counting and p/2p extraction

First prove the needed counting principle. For polynomials f_j over F_p in N variables with sum_j deg(f_j)<N, the number of common zeros is divisible by p. The function Q=product_j(1−f_j^(p−1)) is the indicator of their common zero set. Fermat's identity for a≠0 follows by multiplying all nonzero field elements after the permutation u↦au, and cancelling their nonzero product. Every monomial of Q has total degree <N(p−1), so some variable has exponent d<p−1. If d=0, its sum over F_p is p=0 in the field. If 0<d<p−1, the polynomial X^d−1 has at most d roots, hence some nonzero a has a^d≠1. Multiplication by a permutes F_p and gives sum_u u^d=a^d sum_u u^d, forcing that sum to vanish. Thus the sum of EVERY monomial over F_p^N is zero. The indicator sum is therefore zero modulo p. The elementary root bound used here follows by successive division by X−a for each distinct root. No Chevalley–Warning input remains unproved in this argument.

For indexed g_i=(a_i,b_i), i=1,…,3p−2, use the THREE equations

    sum X_i^(p−1)=0,
    sum a_i X_i^(p−1)=0,
    sum b_i X_i^(p−1)=0.

Their total degrees are at most3(p−1)<3p−2. A solution's support is a zero-sum index subset with size divisible by p. Only sizes0,p,2p fit. If N_r counts zero-sum subsets of size r, the solution count is

    1+(p−1)^p N_p+(p−1)^(2p) N_2p ≡ 1−N_p+N_2p ≡0 (mod p).

For p=2 the signs agree modulo2. If both N_p and N_2p were zero the congruence would say1=0. Hence EVERY length3p−2 sequence in C_p² has a p- or2p-term zero sum. This is the exact original Lem4.3(2) prerequisite, independently hand-proved for every prime.

## 3. CLM-0090/0091 — exact D, eta and the long-zero short block

**Exact D(C_p²)=2p−1, CLM-0090.** In the group algebra F_p[C_p²], let u,v be the basis generators. It is F_p[u,v]/(u^p−1,v^p−1), or, with X=u−1,Y=v−1, F_p[X,Y]/(X^p,Y^p). These identifications follow from the p² basis monomials u^a v^b, 0≤a,b<p, and the invertible substitution u=1+X,v=1+Y in characteristic p. Each 1−u^a v^b belongs to the ideal (X,Y). Every product of2p−1 such factors vanishes: any monomial of total degree≥2p−1 has X exponent≥p or Y exponent≥p. For a hypothetically zero-sumfree indexed sequence g_1,…,g_(2p−1), expand product_i(1−g_i) in the group basis. Its coefficient at the identity equals1: only the EMPTY index subset has sum0. This contradicts the zero product. The sequence e1^(p−1)e2^(p−1) is zero-sumfree by coordinate counts0..p−1, giving equality. This proof does not certify the general p-group theorem or change older SOURCE_STATED frontier evidence classes.

**Short block inside a2p-term zero sequence.** Exact D supplies a nonempty zero block of length≤2p−1, hence a proper block; its complement is nonempty and zero. The shorter of the two has length≤p.

**Eta(C_p²)≤3p−2, CLM-0091.** Apply CLM-0089. A p-term zero is short; a2p-term zero contains a short zero by the preceding split.

**Every zero-sum sequence S of length N≥2p contains a short zero, also CLM-0091.** N=2p was just proved; N≥3p−2 follows from eta by restriction. For2p<N<3p−2 append k=3p−2−N zero positions, where1≤k≤p−3. Apply CLM-0089. A p-term block has between p−k and p original terms, nonempty and short. A2p-term block yields an original zero block T of length2p−j, 0≤j≤k. Its complement IN S is zero, has positive length because N>2p, and length N−2p+j≤p−2. Thus it is short. This supplies original Lem4.3(3) with all indexed availability checked. The middle interval is empty for small primes; no hidden small-prime exception is needed. In particular a short-free sequence has no2p-term zero block.

## 4. Cyclic and quotient tools, with no imported inverse theorem

For C_p, p+1 partial sums including the empty one give D(C_p)≤p by pigeonhole; p−1 copies of a nonzero generator give equality. For any zero-free lengthp−1 cyclic sequence, its p−1 nonempty partial sums in EVERY ordering are distinct and exhaust F_p\{0}. Swapping adjacent terms changes only one partial sum. All other p−2 values are fixed, so the changed value must equal its predecessor; the swapped terms are equal. Any pair can be made adjacent. Thus all terms equal the same nonzero element. Removing one position from a minimal cyclic zero sequence of lengthp proves all its p terms coincide too (the last is fixed by total0).

If a minimal rank-two zero sequence of length2p−1 contains p−1 copies of nonzero e1, its other p positions project to a MINIMAL quotient zero sequence in C_p²/<e1>. Otherwise a proper nonempty quotient-zero block of at mostp−1 positions lifts to an actual zero using k∈{0,…,p−1} available e1 copies, of length at most2p−2, contradicting minimality. All p quotient terms therefore equal a nonzero quotient generator. Choose a lift e2 to obtain e1^(p−1) product_i(a_i e1+e2), with sum a_i=1 modp. Conversely quotient sums force any zero block to use none or all p other positions, and in the latter case the coordinate sum forces all p−1 e1 positions too. This completely proves the SPECIFIC rank-two Cor10.5(2) used here; Cor10.5(1),(3) and its higher-rank Proposition10.4 are not claimed.

**Translation/padding tool.** Let short-free S have length3p−3 and p−1 copies of b. It has no p- or2p-term zero sum by CLM-0091. Translating all terms by−b preserves absence at THESE lengths, since the sum changes by−pb or−2pb. The translated sequence consists of p−1 zero positions and2p−2 remaining positions R. Any nonempty zero block in R of length r could be padded to length p or2p with k∈{0,…,p−1} of those zero positions. Thus R is all-length zero-sumfree. Append c=−sum R; the resulting length2p−1 zero sequence is minimal: a proper zero block excluding c contradicts zero-freeness of R; one including c has a nonempty zero complement contained in R. It is maximal by CLM-0090. This is a justified translation at p/2p lengths, not arbitrary affine preservation of short-freeness.

## 5. CLM-0092 — complete original Lemma10.6, conditional on Property B

Let p be odd and assume Property B: every minimal zero sequence in C_p² of length D=2p−1 contains p−1 equal terms. Suppose S=a^(p−1)b^(p−1) product_(i=1)^(p−1)c_i is short-free. The vectors a,b are nonzero and independent. If dependent, at least2p−2≥p positions are in the same C_p line, contradicting its D=p. Set e1=a,e2=b. No c_i can lie on either axis: c_i=k e1, k∈{1,…,p−1}, together with p−k available e1 copies is a short zero, and similarly for e2. Hence c_i=x_i e1+y_i e2 with integer representatives1≤x_i,y_i≤p−1.

Translate by−e2 and apply the tool: R=(e1−e2)^(p−1) product_i[x_i(e1−e2)+(x_i+y_i−1)e2] is zero-free. Its p−1 quotient terms (x_i+y_i−1)e2 are zero-free in C_p: any quotient-zero block lifts using0..p−1 available e1−e2 copies, giving a forbidden zero in R. The cyclic tool makes all these quotient coefficients equal and nonzero. For each original c_i, the AVAILABLE zero block e1^(p−x_i)e2^(p−y_i)c_i has length2p+1−x_i−y_i. Short-freeness forces x_i+y_i≤p. Thus all positive integer sums are the SAME m∈{2,…,p}.

m=2 gives all x_i=y_i=1, so all c_i equal. For m=p, any nonempty zero block among the p−1 cyclic x_i also has y-sum0, hence gives a short original c-block. Thus the x_i sequence is zero-free and all its terms equal by the cyclic tool; so the c_i coincide.

For3≤m≤p−1 let t be the positive inverse of m−1 modp. Since m−1 is neither1 nor−1, 2≤t≤p−2; tm≡t+1. For EVERY t-index subset I write A=|sum_I x_i|_p and B=|sum_I y_i|_p in {1,…,p}. The zero block

    e1^(p−A)e2^(p−B) product_(i∈I)c_i

is available. A+B is either t+1 or p+t+1 (other multiples cannot lie in2..2p). Its length is accordingly2p−1 or p−1. The latter is short and impossible. The former is minimal: any proper zero block has a nonempty zero complement and one of the two has length≤p−1. Property B applies with the exact D supplied above. None of the c_i equals an axis term, and there are only t≤p−2 of them; hence the repeated p−1 term must be e1 or e2. Thus A=1 or B=1. If e1 has p−1 copies, Cor10.5(2) makes all selected y_i=1; if e2 has p−1 copies, it makes all selected x_i=1. In either case all c_i in that subset coincide, because x_i+y_i=m. Every pair of indices extends to a t-subset (t≤p−2<p−1), so EVERY c_i coincides. This completes original Lem10.6 with its actual hypothesis and full term availability; Property B remains an explicit input.

## 6. CLM-0093 — complete conditional implication B⇒C, including the real setup

Assume odd-prime Property B and short-free |S|=3p−3. Append one zero and use CLM-0089. Removing it if selected leaves a zero block of length p−1,p,2p−1 or2p. Short-freeness and CLM-0091 eliminate all but2p−1. That block is minimal, since a proper zero block and its nonempty complement sum to length2p−1 and one is short. By CLM-0090 and Property B, S contains b^(p−1).

Use the translation/padding tool on S−b, forming zero-free R of length2p−2 and minimal T=R·c, c=−sum R. If R itself contains g^(p−1), then S contains both b^(p−1) and (g+b)^(p−1); Lem10.6 finishes the required three blocks, each repeatedp−1. The two values are distinct because g≠0, and availability means these are disjoint positions.

Otherwise Property B on T can only select its newly appended value c, so R contains exactly p−2 copies of c. Write a=c+b. Then S=a^(p−2)b^(p−1) product_(i=1)^p w_i. The vectors a,b are independent: if on the same line, their2p−3≥p positions already violate D(C_p)=p. The appended term c=a−b, so the translated minimal sequence is

    (a−b)^(p−1) product_(i=1)^p [x_i(a−b)+(x_i+y_i−1)b].

Here w_i=x_i a+y_i b. Cor10.5(2) proves all x_i+y_i−1 are the same NONZERO quotient value. This supplies the actual constant-coordinate-sum setup rather than assuming it.

No w_i lies in <b>, since b has p−1 copies. If w_i=k a with2≤k≤p−1, the p−k available a copies and w_i give a short zero (p−k≤p−2). If w_i=a, S now has p−1 copies of both a and b, and Lem10.6 finishes. Excluding this completed branch, all coordinates have representatives1..p−1. If x_i+y_i≥p+1, then x_i≥2, and the zero block a^(p−x_i)b^(p−y_i)w_i is AVAILABLE and short. Hence every sum is≤p and≥2. Equality modulo p from the quotient therefore yields exact integer x_i+y_i=m∈{2,…,p}. m=2 gives the zero p-block (a+b)^p. m=p gives a nonempty zero subset of the p x_i in C_p, also zero in the y-coordinate, hence a short w-block. Thus3≤m≤p−1. (For p=3 this range is empty, already a contradiction.)

Choose t as in Section5. For a t-subset I with sum_I x_i≠1, its positive representative A lies in2..p and p−A≤p−2; hence the a exponent of the same zero block used in Section5 is available even though S has only p−2 copies. The b exponent is≤p−1. Again length is2p−1 or p−1; the latter is impossible, and the former is minimal. Property B and Cor10.5(2) imply all selected x_i=1 or all selected y_i=1 (indeed the limited a multiplicity permits only the former repeated-axis choice). With constant sum m, the source's REAL trichotomy follows for EVERY t-subset:

    sum_I x_i=1 OR all x_i=1 OR all x_i=m−1.

No replacement by universal sum1 has occurred. A constant all-1 subset has sumt, not1. S012 CLM-0088 applies and proves at least p−1 FULL w_i coincide, say z. S therefore contains disjoint b^(p−1) and z^(p−1) blocks; Lem10.6 makes its remaining p−1 positions equal. This is exactly Property C. The p=2 case is elementary: a short-free length3 sequence over C2² has the three distinct nonzero values (zeros or repetitions give short sums).

Thus the conditional theorem and Lem10.6 have no remaining internal GG proof prerequisite. This does NOT prove Property B itself. In compliance with the incoming handoff, historical CLM-0082 stays SOURCE_STATED; its old session observation is not retrospectively edited. New CLM-0093 records precisely the independently proved implication under the explicit Property B hypothesis, while full unconditional GG/Reiher closure remains incomplete.

## 7. First unresolved prerequisite and preserved rank-three limits

Original Reiher SRC-0025 fresh PDF has289,379 bytes, SHA2567d94931bcbf8fb4ce77c0ed94206659df74e8cb5543e1615e7dde23e86b994d8. Thm10.2 printed p26 routes support≤3 through Lem7.2; for four points Lem9.2 classifies seven cases, with cloudiness/Cor2.5 excluding(a),(b), Props5.1/6.2/8.1 treating(c)–(f), and Lem9.6/Prop10.1 treating(g). Lem7.2's actual proof imports Cor2.5, Obs7.1, Obs2.6 and the STRATEGIC EQUATION (Prop4.1). Prop4.1 pp10–13 in turn uses coefficient identities/Nullstellensatz and a three-case polynomial argument; the later general-position branch also needs the quartic/conic chain in Section9. These are read/dependency-inspected, not independently rebuilt.

**FIRST incomplete prerequisite in the unconditional continuation is Property B, specifically the Lem7.2 route's unrebuilt Prop4.1 strategic-equation package (with Cor2.5/Obs7.1 prerequisites).** This is a programme-proof boundary, not a demonstrated defect in Reiher. Preregistered proof expansion stops here. The other listed nodes receive inspection only; no partial statement-reading is promoted to unconditional Property B certification.

BSP2012 SRC-0021 definitive pp22–23 and29–30 inspected. S012 section7's rank-three plane proof now has independently proved rank-two eta and CONDITIONAL Property C via Section6. For N=3p²−4p−3 and maximal line multiplicity m≤p−1, some plane through that line has m+ceil((N−m)/(p+1)) terms. Eta excludes m≥5; m=3,4 yields a3p−3 subsequence and Property C would supply p−1 repeated terms, contradicting m≤4 forp≥7. Thus m≤2; plane occupancy≥3p−6 contradicts capacity2(p+1) forp≥11, and atp7 contradicts preserved CLM-0087. Therefore eta(C7³)≤116 and the corresponding p≥11 bound remain CONDITIONAL on Property B. No unconditional eta upgrade.

Splitting3p terms still gives ONLY R=(3p−1)/2, not3(p−1)/2; exact Lem2.3 coefficient remains unproved. CLM-0068 retains eta plus its recorded classical assumptions; its historical scope is not silently changed. BSP ref[10] is the distinct 2003 Gao–Geroldinger article, not1999.

## 8. Other source-only checks and all thirty frontier rows

BSP2007 SRC-0008/0019 Prop1 p3, diagrams pp6–10 and Prop8 pp10–11 inspected. Restricted multiplicity2+3κ permits κ monochromatic triples, total k−3. It does not close the diagram classification or whole upper induction. Subscript D3(C3³)=15,D4=18 remains distinct from superscript at-most-three threshold17. Original diagrams were visually inspected as source illustrations, without enumerating cases computationally.

Fresh S013 official Sheikh137-page full-PDF request returned HTTP403,6274-byte HTML body. Chapter4/Remark4.3.11 full context remains unread. This is separately S013403, S012403,S011403,S010403, and S009 internal error. Exactly-three-free does not imply at-most-three-free; the known indexed example's zero pair prevents that substitution.

GHST2007 SRC-0024 original Prop5.6 pp16–17 and C53.html pointer reread; fresh HTTPS code/output retrieval timed out. No authentic original code AND output read; no author program executed. Yiu originalv1 abstract and freshly downloaded16680-byte source archive inspected read-only: SHA25699dc658b3381038fe0c7b2f89145c52a9687e185883cf2a6fdcc0cb8860b1e21, same five README/TeX/bibliography members, none an implementation/log/certificate. M1 repeats98,622 generators and230,983 extensions, NOT the final three-disjoint-zero-sum predicate. M2s≤6=24 andM3s≤7=19 have different predicates. Advertising ancillary files and reading the manuscript do not authenticate them. Non-discovery is limited to the retrieved locations, not global absence.

Every n1..30 numeric mirror remains unchanged. n1 trivial; source-stated Olson prime powers n2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29; original II Cor4.3 exact2p^a family n6,10,14,18,22,26; original III Cor1.5VIII exact3·2^a family n6,12,24; original Schmid2011 Thm4.1(2) independently n6=16. Current original source statements and all applications were checked; full historic proofs remain scoped. New rank-two proofs do not change the rank-three p-group frontier evidence classes.

The five conditional intervals are n15:43..45=3·13+6 upper; n20:58..59=2·28+3; n21:61..63=3·19+6; n28:82..83=2·40+3; n30:88..90=3·28+6. Lower bounds3n−2 in each case. Bounded targeted queries returned no newly authenticated individual exact primary theorem; some literal group-notation queries returned irrelevant records. This limited retrieval is NOT evidence of present-day openness and is not comprehensive literature coverage. No published exact value is demoted.

## 9. Gate and stop

New CLM-0089–0093 close rank-two extraction, exact D, eta/long-zero short block, original Lem10.6 and full B⇒C implication with Property B explicit. Complete p7 lemma preserved. The FIRST unconditional prerequisite is unrebuilt Reiher Property B; stronger coefficient, BSP2007 full diagrams, Sheikh/GHST/Yiu and historical provenance obligations persist. Phase1 IN_PROGRESS/PASS withheld; Phases2/3 NOT_STARTED; CAM-0001 PROPOSED / NOT RUNNING, activation BLOCKED by published n6=16. No replacement campaign, candidate or certificate. Inherited14/17,+5,43/699/5553 quarantined. Zero hosted workflows/runs/jobs/checks/status contexts, NOT CI PASS. Administrative validation only. Stop after S013; S014 is strictly FUTURE UNEXECUTED.
