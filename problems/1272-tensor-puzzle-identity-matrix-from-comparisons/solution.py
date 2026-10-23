
import numpy as np

def eye(n: int) -> np.ndarray:
    i = np.arange(n)
    return (i[:, None] == i[None, :]).astype(np.float64)

