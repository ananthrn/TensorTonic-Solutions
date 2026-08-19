import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x_arr = np.array(x)
    n = x_arr.shape[0]
    
    x_hat = np.mean(x_arr)
    s = np.std(x, ddof=1)
    t = (x_hat - mu0)/(s/np.sqrt(n))

    return t