import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A_arr = np.asarray(A)
    A_t = np.zeros((A_arr.shape[1],A_arr.shape[0]))

    for r in range(A_arr.shape[0]):
        for c in range(A_arr.shape[1]):
            A_t[c, r] = A_arr[r, c]


    return A_t
