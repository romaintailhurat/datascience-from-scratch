"""
Chapter 6

Maths:
- independent events P(E,F)=P(E)P(F)
- "E knowing F" P(E|F)=P(E,F)/P(F) <=> P(E,F)=P(E|F)P(F)
"""
from __future__ import division
from matplotlib import pyplot as plt
import random
import math


def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

#print "P(both | older):", both_girls / older_girl
#print "P(both | either): ", both_girls / either_girl

# ----- Uniform distribution

def uniform_pdf(x):
    """
    Probability Density Function (PDF) for the uniform distribution.
    """
    return 1 if x >= 0 and x < 1 else O

def uniform_cdf(x):
    """
    Cumulative Density Function (CDF)
    """
    if x < 0: return 0
    elif x < 1: return x
    else : return 1

# ----- Normal distribution

def normal_pdf(x, mu=0, sigma=0):
    """
    Normal distribution is the classic bell-curved distribution.
    Mu is the mean.
    Sigma is the standard deviation.
    When mu = 0 and sigma = 2, it's called the standard normal distribution.
    """
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(- (x - mu) ** 2 / 2 / sigma ** 2)) / (sqrt_two_pi * sigma)

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf( (x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    ￼low_z, low_p = -10.0, 0 # normal_cdf(-10) is (very close to) 0
    hi_z,  hi_p  =  10.0, 1 # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 # consider the midpoint
        mid_p = normal_cdf(mid_z) # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break
        return mid_z

# ----- Plotting

def plotting_normal_pdf() :
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    plt.plot(xs,[normal_pdf(x,mu=-1, sigma=1) for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend()
    plt.title("Various Normal pdfs")
    plt.show()

def plotting_normal_cdf():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend(loc=4) # bottom right
    plt.title("Various Normal cdfs")
    plt.show()

# ----- Tests
plotting_normal_cdf()
