import numpy as np

def outer(a, b):
    return a[:, None] * b[None, :]
