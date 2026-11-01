"""Actual-image bounded meet-in-the-middle; independent of pair_b."""
from itertools import product
from math import gcd
import numpy as np


def decode(key, p, k):
    key = int(key)
    if key < 0 or key >= p ** (3*k):
        raise ValueError('key outside format')
    out = np.empty((3, k), dtype=np.int64)
    for r in range(3):
        for c in range(k):
            out[r,c] = key % p
            key //= p
    return out


def actual(key_p, key_q, p, q, k):
    if p not in (2,3,5) or q not in (2,3,5) or p == q:
        raise ValueError('distinct supported primes required')
    a, b = decode(key_p,p,k), decode(key_q,q,k)
    return (a + p * (((b-a)*pow(p,-1,q)) % q)) % (p*q)


def admissible(m, n):
    cols = [tuple(int(x) for x in m[:,j]) for j in range(m.shape[1])]
    return len(set(cols)) == len(cols) and all(gcd(n,gcd(v[0],gcd(v[1],v[2]))) == 1 for v in cols)


def grids(alpha):
    split = len(alpha)//2
    left = np.array(list(product(*(range(a+1) for a in alpha[:split]))), dtype=np.int64)
    right = np.array(list(product(*(range(a+1) for a in alpha[split:]))), dtype=np.int64)
    return left, right


def scan(m, n, left, right):
    """Complete work, including zeros wholly within either half."""
    split = left.shape[1]
    ls = (left @ m[:,:split].T) % n
    rs = (-right @ m[:,split:].T) % n
    weights = np.array([1,n,n*n],dtype=np.int64)
    lk, rk = ls @ weights, rs @ weights
    order = np.argsort(lk,kind='stable')
    sorted_keys = lk[order]
    lo = np.searchsorted(sorted_keys,rk,side='left')
    hi = np.searchsorted(sorted_keys,rk,side='right')
    # Grid row 0 is the all-zero tuple in each half. Prefer a nonempty match.
    if lo[0] < hi[0] and order[lo[0]] == 0:
        lo[0] += 1
    hits = np.flatnonzero(lo < hi)
    if not len(hits):
        return None
    j = int(hits[0]); i = int(order[lo[j]])
    return tuple(int(v) for v in np.concatenate((left[i],right[j])))


def classify(key_p, key_q, p, q, alpha):
    n=p*q
    if len(alpha)<2 or len(alpha)>6 or any(type(a) is not int or a<0 or a>=n for a in alpha):
        raise ValueError('coefficient domain')
    m=actual(key_p,key_q,p,q,len(alpha))
    if not admissible(m,n):
        return {'kind':'INVALID'}
    w=scan(m,n,*grids(alpha))
    if w is None:
        return {'kind':'ZSF'}
    if not any(w) or not all(0<=x<=a for x,a in zip(w,alpha)) or np.any((m@np.array(w))%n):
        raise AssertionError('bad A witness')
    return {'kind':'ZERO','witness':list(w)}


def traverse(keys_p,keys_q,start,stop,p,q,alpha):
    if not 0 <= start <= stop <= len(keys_p)*len(keys_q):
        raise ValueError('interval')
    for ordinal in range(start,stop):
        i,j=divmod(ordinal,len(keys_q))
        yield ordinal,classify(keys_p[i],keys_q[j],p,q,alpha)
