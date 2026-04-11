import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if len(seqs) == 0:
        return np.ndarray()

    if max_len is None:
        max_len = max([len(seq) for seq in seqs], default=0)
    new_seqs = []
    for seq in seqs:
        if len(seq) < max_len:
            new_seq = seq + [pad_value] * (max_len - len(seq))
            new_seqs.append(
                new_seq
    
            )
        else:
            new_seqs.append(
                seq[:max_len]
            )
    # array = np.ndarray(new_seqs, dtype=np.int32)
    print(new_seqs)
    # array = 
    return new_seqs

    