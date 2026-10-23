import numpy as np

def cumsum(a):
    n = len(a)
    i = np.arange(n)
    L = (i[:, None] >= i[None, :]).astype(a.dtype)
    return L @ a