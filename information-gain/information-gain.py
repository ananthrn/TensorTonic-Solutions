import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    y = np.asarray(y)
    if y.size == 0:
        return 0.0

    n_left = len(split_mask[split_mask == True])
    n_right = len(split_mask[split_mask == False])

    # print(
    #     "n_left:", n_left
    # )
    # print("n_right: ", n_right)

    y_left = y[split_mask]
    y_right = y[~split_mask]

    print(
        "y_left: ", y_left
    )
    print(
        "y_right: ", y_right
    )
    n_left, n_right = len(y_left), len(y_right)
    print(
        "n_left:", n_left
    )
    print("n_right: ", n_right)
    originalEntropy = _entropy(y)
    leftEntropy = _entropy(y_left)
    rightEntropy = _entropy(y_right)
    
    newEntropy = 1.0/(n_left + n_right) * (n_left * leftEntropy + n_right * rightEntropy)
    return originalEntropy - newEntropy
