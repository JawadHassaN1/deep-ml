import numpy as np

def diag(A):
    i = np.arange(A.shape[0])
    return A[i, i]
    