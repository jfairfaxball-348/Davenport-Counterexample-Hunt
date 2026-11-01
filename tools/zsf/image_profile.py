"""S114 exact squarefree CRT image representatives and coefficient-box checker.

No target search CLI: validation is in sessions/S114/validate.py.
RREF enumerates full-rank labelled image maps modulo independent left GL actions.
No permutation reduction, rank-deficient omission without CLM-0384, or n20 support.
"""
from itertools import combinations, product
from math import prod, gcd


def gaussian(k, r, p):
    return prod(p**k-p**j for j in range(r)) // prod(p**r-p**j for j in range(r))


def rref_images(p, k, r=3):
    if p < 2 or any(p % a == 0 for a in range(2, int(p**0.5)+1)):
        raise ValueError('prime component required')
    if not 0 <= r <= k:
        raise ValueError('rank outside column range')
    for pivots in combinations(range(k), r):
        free = [(i, j) for i in range(r) for j in range(pivots[i]+1, k) if j not in pivots]
        for entries in product(range(p), repeat=len(free)):
            m = [[int(j == pivots[i]) for j in range(k)] for i in range(r)]
            for (i, j), x in zip(free, entries):
                m[i][j] = x
            yield tuple(tuple(m[i][j] for i in range(r)) for j in range(k))


def crt_images(primes, components):
    n = prod(primes)
    if len(set(primes)) != len(primes) or len(primes) != len(components):
        raise ValueError('distinct prime factors required')
    weights = [(n//p)*pow(n//p, -1, p) for p in primes]
    k, r = len(components[0]), len(components[0][0])
    return tuple(tuple(sum(w*c[j][i] for w, c in zip(weights, components)) % n
                       for i in range(r)) for j in range(k))


def order(g, n):
    return n // gcd(n, *g)


def box_zero(values, alpha, n):
    """Return a nonzero bounded coefficient vector summing to zero, or None.

    Meet in the middle over support coefficients, not indexed subset propagation.
    Retain a nonzero left representative if zero and nonzero share a sum.
    """
    if len(values) != len(alpha) or any(a < 0 for a in alpha):
        raise ValueError('invalid profile')
    k = len(alpha)
    split = min(range(k+1), key=lambda j: max(prod(a+1 for a in alpha[:j]), prod(a+1 for a in alpha[j:])))
    r = len(values[0])

    def sums(vs, bounds):
        for x in product(*(range(a+1) for a in bounds)):
            yield tuple(sum(t*g[j] for t, g in zip(x, vs)) % n for j in range(r)), x

    left = {}
    for s, x in sums(values[:split], alpha[:split]):
        if s not in left or any(x):
            left[s] = x
    for s, y in sums(values[split:], alpha[split:]):
        x = left.get(tuple(-a % n for a in s))
        if x is not None and (any(x) or any(y)):
            return x+y
    return None


def local_pure_zero(values, alpha, n, p):
    """Necessary rejection only: coefficients multiples of n/p (squarefree n)."""
    scale = n//p
    if n % p or gcd(scale, p) != 1:
        raise ValueError('coprime component required')
    projected = [tuple(scale*x % p for x in g) for g in values]
    return box_zero(projected, [a//scale for a in alpha], p)
