import numpy as np

def triu_ones(n: int) -> np.ndarray:
    i = np.arange(n)
    return (i[:, None] <= i[None, :]).astype(float)