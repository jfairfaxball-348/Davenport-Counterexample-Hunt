"""Checker A: numpy boolean-array subset-sum DP with the prefix criterion.

Group G = Z/m1 x ... x Z/mr (default rank 3, m_i = n).  Sigma(S) is the set of
sums of ALL subsets of S *including the empty subset* (so 0 is always in it).

Prefix criterion (CLM-0345): S = (g_1..g_L) is zero-sumfree iff for every k,
-g_k is NOT in Sigma(g_1..g_{k-1}).  Update: Sigma(S+[g]) = Sigma(S) | (g + Sigma(S)),
translation implemented exactly with np.roll along every axis (modular wrap).

This module is deliberately independent of checker_b.py (different data
structure, different criterion).  It also provides the incremental Oracle with
an explicit rollback stack, used by search engines.
"""
import numpy as np


def _norm(g, mods):
    if len(g) != len(mods):
        raise ValueError("element rank mismatch")
    return tuple(int(x) % m for x, m in zip(g, mods))


def translate(sig, g):
    """Return g + sig (exact cyclic translation on each axis)."""
    return np.roll(sig, shift=g, axis=tuple(range(sig.ndim)))


def empty_sigma(mods):
    sig = np.zeros(mods, dtype=bool)
    sig[(0,) * len(mods)] = True
    return sig


def neg(g, mods):
    return tuple((-x) % m for x, m in zip(g, mods))


def is_zero_sumfree(seq, mods):
    """Return (bool, k) where k is the first index (0-based) whose -g_k lies in the
    prefix subset sums, or None if zero-sumfree."""
    mods = tuple(mods)
    sig = empty_sigma(mods)
    for k, g in enumerate(seq):
        g = _norm(g, mods)
        if sig[neg(g, mods)]:
            return False, k
        sig |= translate(sig, g)
    return True, None


def subset_sums(seq, mods):
    mods = tuple(mods)
    sig = empty_sigma(mods)
    for g in seq:
        sig |= translate(sig, _norm(g, mods))
    return sig


class Oracle:
    """Incremental exact zero-sumfree oracle with rollback.

    push(g) appends g only if legal (-g not in Sigma) and returns True; else
    returns False and leaves the state unchanged.  pop() restores the exact
    previous Sigma (stored copy, no recomputation)."""

    def __init__(self, mods):
        self.mods = tuple(mods)
        self.sig = empty_sigma(self.mods)
        self.seq = []
        self._stack = []

    def legal(self, g):
        return not self.sig[neg(_norm(g, self.mods), self.mods)]

    def legal_mask(self):
        """Boolean array L with L[g] True iff g may be appended: -g not in Sigma."""
        # -g in Sigma  <=>  g in -Sigma ; -Sigma via index reversal mod m.
        negsig = self.sig
        for ax in range(negsig.ndim):
            negsig = np.roll(np.flip(negsig, axis=ax), 1, axis=ax)
        return ~negsig

    def push(self, g):
        g = _norm(g, self.mods)
        if not self.legal(g):
            return False
        self._stack.append(self.sig)
        self.sig = self.sig | translate(self.sig, g)
        self.seq.append(g)
        return True

    def pop(self):
        self.sig = self._stack.pop()
        return self.seq.pop()

    def coverage(self):
        return int(self.sig.sum())
