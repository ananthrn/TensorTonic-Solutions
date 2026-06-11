import numpy as np
import math
import scipy.special as special

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x_arr = np.asarray(x)

    return 0.5 * x_arr * (1.0 + special.erf(x_arr/np.sqrt(2)))
    
