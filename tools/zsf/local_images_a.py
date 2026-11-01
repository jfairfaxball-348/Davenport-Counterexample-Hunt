"""S115 engine A: image RREF, bounded free-variable zero solving.
Independent of local_kernels_b; numpy and standard library only.
"""
import itertools
import numpy as np


def strata(k=6, r=3):
    return list(itertools.combinations(range(k), r))


def size(p, piv, k=6):
    return p**sum(j > i and j not in piv for i in piv for j in range(k))


def matrices(p, piv, start, stop, k=6):
    m = np.zeros((stop-start, len(piv), k), dtype=np.int16)
    for row,col in enumerate(piv):
        m[:,row,col] = 1
    digits = np.arange(start,stop,dtype=np.int64)
    # Least-significant first; IDs are deterministic but not S114 itertools order.
    for row,col in [(i,j) for i,t in enumerate(piv) for j in range(t+1,k) if j not in piv]:
        m[:,row,col] = digits % p
        digits //= p
    return m


def survivors(m, p, piv, bounds):
    free = [j for j in range(m.shape[2]) if j not in piv]
    answers = []
    full_order = np.all(np.any(m != 0,axis=1),axis=1)
    for beta in bounds:
        ok = full_order.copy()
        for y in itertools.product(*(range(beta[j]+1) for j in free)):
            if not any(y):
                continue
            ids = np.flatnonzero(ok)
            if not len(ids):
                break
            x = -np.sum(m[ids][:,:,free]*np.array(y,dtype=np.int16),axis=2) % p
            bad = np.all(x <= np.array([beta[j] for j in piv]),axis=1)
            ok[ids[bad]] = False
        answers.append(ok)
    return np.asarray(answers)


def keys(m,p):
    flat = m.reshape(len(m),-1).astype(np.uint64)
    weights = np.array([p**i for i in range(flat.shape[1])],dtype=np.uint64)
    return flat @ weights
