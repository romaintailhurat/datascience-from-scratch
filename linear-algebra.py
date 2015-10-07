"""
Chapter 4

Various notes:
- python list not to be used in production, they're slow, use NumPy instead
- matrices will be used for
  > representing data made of multiple vectors
  > n x k matrices used to represent a linear function from n-dimensional vectors
  to k-dimensional vectors
  > representing binary relationship, such as a link between two persons
"""
from __future__ import division # to avoid the float hack in division !
import math

# ----- VECTORS

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def vector_sum_enhanced(vectors):
    # me enhancing :)
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    # use that if you dot not use __future__ division !
    c = 1/float(n)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """
    The dot product of two vectors is the sum of their
    componentwise products.
    """
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

# ----- MATRICES

A = [[1,2],
     [3,4],
     [5,6]]

B = [[1,2,3],
     [4,5,6]]

def shape(mat):
    num_rows = len(mat)
    num_cols = len(mat[0]) if mat else 0
    return num_rows, num_cols

def get_row(mat, i):
    return mat[i]

def get_column(mat, j):
    return [mat_i for mat_i in mat]

def make_matrix(n, m, entry_fn):
    return [[entry_fn(i, j) for j in range (m)] for i in range(n)]

def is_diagonal(i, j):
    return 1 if i == j else 0

def print_matrix(mat):
    # helper printer =)
    for i in mat:
        print(i)

## ----- TESTS
print( vector_mean([ [2,2,3],[9,9,9] ]) )
