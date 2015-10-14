"""
Chapter 5
"""
from __future__ import division
from collections import Counter

def mean(x):
    return sum(x) / len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        #odd
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) // 2

def quantile(x,p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """ most common value(s) """
    counts = Counter(x)
    max_count = max(counts.values())
    return [ x_i for x_i, count in counts.iteritems() if count == max_count ]

## ----- TESTS

print(quantile([1,2,2,56], 0.5))
print(mode([1,2,2,56]))
