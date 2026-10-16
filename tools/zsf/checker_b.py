"""Checker B: pure-Python exact subset COUNTING DP over a flat list.

Algorithmically distinct from checker_a.py: no numpy, no prefix criterion, no
boolean sets.  We compute, for every group element x, the exact number c[x] of
index subsets I of {1..L} (including the empty one) with sum_{i in I} g_i = x,
using arbitrary-precision Python integers and hand-written mixed-radix index
arithmetic.  S is zero-sumfree iff c[0] == 1 (only the empty subset).

Also returns, when S is not zero-sumfree, an explicit nonempty index subset
summing to zero (recovered by backward reconstruction over the stored count
tables), which callers re-verify by direct summation.
"""


def _encode(x, mods):
    idx = 0
    for xi, m in zip(x, mods):
        idx = idx * m + (xi % m)
    return idx


def _decode(idx, mods):
    out = []
    for m in reversed(mods):
        out.append(idx % m)
        idx //= m
    return tuple(reversed(out))


def _add_table(mods):
    """add[a][b] would be too big; instead precompute per-element shift maps lazily."""
    size = 1
    for m in mods:
        size *= m
    return size


def _shift_map(g, mods, size):
    # perm[x] = index of (decode(x) + g)
    return [_encode(tuple(a + b for a, b in zip(_decode(x, mods), g)), mods) for x in range(size)]


def subset_counts(seq, mods, keep_tables=False):
    mods = tuple(mods)
    size = _add_table(mods)
    c = [0] * size
    c[0] = 1
    tables = [c[:]] if keep_tables else None
    for g in seq:
        g = tuple(int(v) % m for v, m in zip(g, mods))
        perm = _shift_map(g, mods, size)
        new = c[:]
        for x in range(size):
            if c[x]:
                new[perm[x]] += c[x]
        c = new
        if keep_tables:
            tables.append(c[:])
    return c, tables


def is_zero_sumfree(seq, mods):
    c, _ = subset_counts(seq, mods)
    return c[0] == 1


def zero_sum_witness(seq, mods):
    """Return a sorted list of 0-based indices of a nonempty zero-sum subsequence,
    or None if the sequence is zero-sumfree."""
    mods = tuple(mods)
    c, tables = subset_counts(seq, mods, keep_tables=True)
    if c[0] == 1:
        return None
    size = len(c)
    # Need a NONEMPTY subset with sum 0.  Choose the largest k such that some subset
    # of g_1..g_k containing index k sums to 0, i.e. tables[k][0] > tables[k-1][0].
    k = max(j for j in range(1, len(tables)) if tables[j][0] > tables[j - 1][0])
    chosen = [k - 1]
    target = _encode(tuple(-v for v in seq[k - 1]), mods)
    j = k - 1
    while target != 0:
        # subsets of g_1..g_j summing to target exist: tables[j][target] > 0
        while tables[j - 1][target] > 0:
            j -= 1  # can avoid g_j
        # must use g_j
        chosen.append(j - 1)
        g = seq[j - 1]
        target = _encode(tuple(a - b for a, b in zip(_decode(target, mods), g)), mods)
        j -= 1
    # target == 0 reached using empty remainder
    return sorted(chosen)


def verify_witness(seq, mods, idxs):
    if not idxs or len(set(idxs)) != len(idxs):
        return False
    tot = [0] * len(mods)
    for i in idxs:
        for a in range(len(mods)):
            tot[a] += seq[i][a]
    return all(t % m == 0 for t, m in zip(tot, mods))
