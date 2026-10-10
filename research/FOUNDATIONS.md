# S001 elementary foundation (programme proof)

**Lemma.** For every integer $n\ge 2$, $D(C_n^3)\ge3n-2$.

**Proof.** Let $e_1,e_2,e_3$ be the three standard basis elements of $(\mathbb Z/n\mathbb Z)^3$. Form a sequence $S$ with exactly $n-1$ copies of each $e_i$. A subsequence chooses integers $0\le a_i\le n-1$. Its sum is $(a_1,a_2,a_3)$ modulo $n$. If this sum vanishes, $n\mid a_i$ for each $i$, so every $a_i=0$; hence the subsequence is empty. Thus $S$ is zero-sumfree of length $3(n-1)$, so the shortest universal zero-sum length is at least $3(n-1)+1=3n-2$. QED.

**Counterexample equivalence (from definitions).** If a zero-sumfree sequence of length $3n-2$ exists, then $D(C_n^3)\ge3n-1$. Conversely, if $D(C_n^3)>3n-2$, by the definition of the least universal length there is a zero-sumfree sequence of length $3n-2$. This equivalence needs no computation; it does not assert existence.

**Prime powers (source stated, not programme proved).** Olson's p-group theorem gives $D(C_{p^a}^3)=3p^a-2$. Direct full primary proof not inspected in S001; catalogued as a classical literature result, not a new theorem.

**Inductive upper bound (primary source stated, not yet programme proved).** Zakarczemny 2019 Lemma 3.3 (SRC-0006) states $D(G)\le D_{D(H)}(G/H)$. Derivation and exploitation scheduled S002.

**Important:** The inherited no-short-zero-sum cap reduction, the D_k values, the off-by-one sandwiches and 5553 orbits remain INHERITED_UNVERIFIED. They must not be promoted by this document.
