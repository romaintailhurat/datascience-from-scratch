"""
Chapter 5

Notes :
- correlation is linear correlation, a correlation of 0 doesn't imply
there is no relation, it can exist a non linear one
- in addition, correlation tells you nothing about how large the relationship is
    x = [1 2 3 4]
    y = [101 102 103 104]
- Simpson's paradox
"""

from __future__ import division
from collections import Counter
from random import randint
import linear_algebra as lin
import math

DATA = [ randint(0,100) for x in range(1000) ]
DATA_2 = [ randint(0,100) for x in range(1000) ]

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

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return lin.sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    """ more robust than standard deviation """
    return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x, y):
    n = len(x)
    return lin.dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 #if no variation, correlation is zero

## ----- TESTS
print('Mean : %d' %mean(DATA))
print('Variance : %d' %variance(DATA))
print('Standard Deviation : %d' %standard_deviation(DATA))
print('Interquartile : %d' %interquartile_range(DATA))
print('Covariance DATA / DATA_2 : {}'.format(covariance(DATA, DATA_2)))
print('correlation DATA / DATA_2 : {}'.format(correlation(DATA, DATA_2)))
