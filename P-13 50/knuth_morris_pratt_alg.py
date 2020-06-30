# Knuth-Morris-Pratt Algorithm (KMP): O(n+m)

def find_kmp(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)"""
    n, m = len(T), len(P)           # introduce convenient notations
    if m == 0: return 0             # trivial search for empty string
    fail = compute_kmp_fail(P)      # rely on utility to precompute
    j = 0                           # index into T
    k = 0                           # index into P
    while j < n:
        if T[j] == P[k]:            # P[0:1+k] matched thus far
            if k == m-1:            # match is complete
                return j - m + 1
            j += 1                  # try to extend match
            k += 1
        elif k > 0:
            k = fail[k-1]           # reuse suffix of P[0:k}
        else:
            j += 1
    return -1                       # reached end without match

def compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m                  # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    """checks for all characters after the first one (P[1:m-1]) if they are equal to k;
    at the same time if there is a match, k is counted up and it is checked whether 
    that sequence of characters is to be repeated inside P"""
    # O(m)
    while j < m:                    # compute f(j) during this parr, if nonzero
        if P[j] == P[k]:            # k + 1 characters match thus far (there is another character in P that matches k)
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:                 # k follows a matching prefix
            k = fail[k-1]
        else:                       # no match found starting at j -> check for all characters in P (while j < m)
            j += 1
    return fail
