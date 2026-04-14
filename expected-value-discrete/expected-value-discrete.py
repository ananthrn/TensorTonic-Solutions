import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x_arr = np.array(x)
    p_arr = np.array(p)

    if np.abs(np.sum(p_arr) - 1.0) > 1e-6:
        raise ValueError

    return np.sum(x_arr * p_arr)
