import numpy as np

def vector_sum(a):
    ones_vector = np.arange(len(a)) * 0.0 + 1.0
    return np.dot(a, ones_vector)
