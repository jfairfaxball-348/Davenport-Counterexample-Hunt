"""Reference checker C (tests only): explicit enumeration of all 2^L - 1 nonempty
index subsets via itertools.combinations.  Exponential; used for L <= 16."""
from itertools import combinations


def is_zero_sumfree(seq, mods):
    L = len(seq)
    for r in range(1, L + 1):
        for comb in combinations(range(L), r):
            if all(sum(seq[i][a] for i in comb) % m == 0 for a, m in enumerate(mods)):
                return False
    return True
