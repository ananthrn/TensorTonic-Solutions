import numpy as np
import collections

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    counts = collections.Counter(y)
    values = [v for v in counts.values()]
    # total_count = sum(counts.values())
    # print(counts)
    # print(counts.values())
    counts_array = np.asarray(values)
    # print("counts_array: ", counts_array)
    probs = counts_array/np.sum(counts_array)
    # print("probs:", probs)
    log_probs = np.log2(probs)
    # print("log_probs:", probs)
    entropy = - np.sum(probs * log_probs)
    # print(entropy)
    return entropy.item()