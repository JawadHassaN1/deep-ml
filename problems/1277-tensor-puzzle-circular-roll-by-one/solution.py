import numpy as np

def roll(a):
    n = len(a)
    indices = (np.arange(n) + 1) % n
    return a[indices]