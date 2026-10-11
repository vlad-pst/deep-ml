import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    fro = False
    if arr.ndim == 2: 
        arr = arr.reshape(-1) 
        fro = True

    if "l1" in norm_type:
        norm = float(sum(abs(arr)))
    elif "l2" in norm_type:
        norm = np.sqrt(sum(arr**2))
    elif "linf" in norm_type:
        norm = float(max(abs(arr)))
    elif "fro" and fro:
        norm = np.sqrt(sum(arr**2))
    else:
        raise ValueError
    return norm
