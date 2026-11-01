"""S115 engine B: relation subspaces, full-vector box intersection.
Independent enumeration, elimination, key construction and zero predicate.
Does not import engine A or S114 mathematical helper functions.
"""
from itertools import combinations, product
import numpy as np


def strata(k=6,r=3):
    return tuple(combinations(range(k),k-r))


def size(p, piv, k=6):
    dimension = 0
    for col in range(k):
        if col not in piv:
            dimension += sum(t < col for t in piv)
    return p**dimension


def matrices(p,piv,start,stop,k=6):
    # Kernel generators: column-major free-digit traversal, opposite radix order.
    cells = [(i,j) for j in range(k) if j not in piv for i,t in enumerate(piv) if t < j]
    out = np.zeros((stop-start,len(piv),k),dtype=np.int16)
    for i,j in enumerate(piv):
        out[:,i,j] = 1
    for pos,(i,j) in enumerate(cells):
        out[:,i,j] = (np.arange(start,stop,dtype=np.int64)//p**(len(cells)-pos-1)) % p
    return out


def image(kernel,p,piv):
    free = [c for c in range(kernel.shape[2]) if c not in piv]
    a = np.zeros((len(kernel),len(free),kernel.shape[2]),dtype=np.int16)
    for i,q in enumerate(free):
        a[:,i,q] = 1
        for j,t in enumerate(piv):
            a[:,i,t] = -kernel[:,j,q] % p
    # Batched independent Gaussian elimination to unique image RREF.
    nextrow = np.zeros(len(a),dtype=np.int16)
    inverse = np.array([0]+[pow(x,-1,p) for x in range(1,p)],dtype=np.int16)
    for col in range(a.shape[2]):
        eligible = (np.arange(a.shape[1])[None,:] >= nextrow[:,None]) & (a[:,:,col] != 0)
        ids = np.flatnonzero(np.any(eligible,axis=1))
        if not len(ids):
            continue
        selected = eligible[ids].argmax(axis=1)
        row = nextrow[ids]
        tmp = a[ids,row].copy()
        a[ids,row] = a[ids,selected]
        a[ids,selected] = tmp
        a[ids,row] = a[ids,row]*inverse[a[ids,row,col]][:,None] % p
        for j in range(a.shape[1]):
            other = ids[row != j]
            rr = nextrow[other]
            a[other,j] = (a[other,j]-a[other,j,col,None]*a[other,rr]) % p
        nextrow[ids] += 1
    assert np.all(nextrow == len(free))
    return a


def survivors(kernel,p,piv,bounds):
    # All nonzero kernel vectors, regardless of box. A uses bounded free-variable solving.
    coefficients = np.array(list(product(range(p),repeat=len(piv)))[1:],dtype=np.int16)
    vectors = np.einsum('ur,brc->buc',coefficients,kernel,optimize=False) % p
    # A zero image column is exactly a unit vector in the relation space.
    nonzero_image_columns = ~np.any(np.count_nonzero(vectors,axis=2) == 1,axis=1)
    return np.array([nonzero_image_columns & ~np.any(np.all(vectors <= np.array(beta),axis=2),axis=1)
                     for beta in bounds])


def keys(a,p):
    code = np.zeros(len(a),dtype=np.uint64)
    for i in reversed(range(a.shape[1])):
        for j in reversed(range(a.shape[2])):
            code = code*np.uint64(p)+a[:,i,j].astype(np.uint64)
    return code
