"""
Chapter 4
"""

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
    # correction from the book, n must be a float
    c = 1/float(n)
    return scalar_multiply(c, vector_sum(vectors))

def dot(v, w):
    """
    The dot product of two vectors is the sum of their
    componentwise products.
    """
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

print( dot( [1,1], [1,1]) )
