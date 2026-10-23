import numpy as np

def diff(a):
    out = a.copy()
    out[1:] = a[1:] - a[:-1]
    return out
