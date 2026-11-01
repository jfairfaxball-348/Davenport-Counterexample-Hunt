"""Relation kernels and coordinatewise CRT box intersection; no A imports."""
from itertools import product
import numpy as np


def unpack(code, prime, width):
    number=int(code)
    if not 0 <= number < prime**(3*width):
        raise ValueError('malformed image key')
    return [[(number//prime**(row*width+col))%prime for col in range(width)] for row in range(3)]


def kernel_vectors(matrix, prime):
    a=[list(row) for row in matrix]
    width=len(a[0]); piv=[]; row=0
    for col in range(width):
        eligible=[i for i in range(row,3) if a[i][col]%prime]
        if not eligible:
            continue
        i=eligible[-1]; a[row],a[i]=a[i],a[row]
        inv=pow(a[row][col],prime-2,prime)
        a[row]=[(x*inv)%prime for x in a[row]]
        for i in range(3):
            if i!=row:
                factor=a[i][col]
                a[i]=[(x-factor*y)%prime for x,y in zip(a[i],a[row])]
        piv.append(col);row+=1
        if row==3:break
    free=[i for i in range(width) if i not in piv]
    basis=[]
    for col in free:
        v=[0]*width;v[col]=1
        for i,pivot in enumerate(piv):v[pivot]=-a[i][col]%prime
        basis.append(v)
    out=[]
    for digits in product(range(prime),repeat=len(free)):
        out.append([sum(d*v[c] for d,v in zip(digits,basis))%prime for c in range(width)])
    return np.asarray(out,dtype=np.int64)


def intersection(u,v,p,q,bounds):
    # Construct CRT table by enumeration, independently of A's inverse formula.
    table=np.empty((p,q),dtype=np.int64)
    for t in range(p*q):table[t%p,t%q]=t
    values=table[u[:,None,:],v[None,:,:]]
    good=np.all(values<=np.asarray(bounds),axis=2) & np.any(values!=0,axis=2)
    pairs=np.argwhere(good)
    if not len(pairs):return None
    i,j=pairs[0]
    return [int(x) for x in values[i,j]]


def classify(code1,code2,p,q,bounds):
    if p not in [2,3,5] or q not in [2,3,5] or p==q:
        raise ValueError('unsupported factors')
    k=len(bounds)
    if k<2 or k>6 or any(type(t) is not int or t<0 or t>=p*q for t in bounds):
        raise ValueError('unsupported box')
    a,b=unpack(code1,p,k),unpack(code2,q,k)
    for j in range(k):
        if all(a[i][j]==0 for i in range(3)) or all(b[i][j]==0 for i in range(3)):
            return {'kind':'INVALID'}
        for h in range(j):
            if all(a[i][j]==a[i][h] and b[i][j]==b[i][h] for i in range(3)):
                return {'kind':'INVALID'}
    w=intersection(kernel_vectors(a,p),kernel_vectors(b,q),p,q,bounds)
    if w is None:return {'kind':'ZSF'}
    if not any(w) or not all(0<=x<=t for x,t in zip(w,bounds)):
        raise AssertionError('bad B bounds')
    for field,m in [(p,a),(q,b)]:
        if any(sum(x*y for x,y in zip(row,w))%field for row in m):
            raise AssertionError('bad B relation')
    return {'kind':'ZERO','witness':w}


def traverse(first,second,begin,end,p,q,bounds):
    width=len(second)
    if begin<0 or begin>end or end>len(first)*width:raise ValueError('bad shard')
    for row in range(len(first)):
        offset=row*width
        if offset>=end:break
        if offset+width<=begin:continue
        for col in range(max(0,begin-offset),min(width,end-offset)):
            yield offset+col,classify(first[row],second[col],p,q,bounds)
