def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    return np.log(1 + np.asarray(values))