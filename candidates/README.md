# Quarantine protocol

Every discovered putative counterexample is only CANDIDATE. Store a canonical sorted list of triples in `candidates/<id>/sequence.json` with modulus, length and SHA-256 over documented UTF-8 canonical JSON. Never claim uniqueness or correctness from one computation.

CERTIFIED only after (1) canonical explicit sequence/hash; (2) two independent different algorithms (reachable-sums DP and meet-in-middle or full subsets); (3) kernel-checked Lean 4 proof; (4) cold recheck in later session. A Palomar registration requires explicit owner authorization. Negative results require independently checked LRAT/DRAT or independent exhaustive algorithms **and** a completeness/symmetry proof. S001: no candidates.
