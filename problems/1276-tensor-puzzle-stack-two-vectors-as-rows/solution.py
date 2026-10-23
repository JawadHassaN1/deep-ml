import numpy as np

def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    row = np.arange(2)[:, None]
    return (row == 0) * a + (row == 1) * b
