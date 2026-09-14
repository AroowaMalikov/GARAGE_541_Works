import numpy as np

def construct_matrix(arr1, arr2) -> np.ndarray:
    return np.hstack([arr1.reshape(len(arr1), 1), arr2.reshape(len(arr2), 1)])