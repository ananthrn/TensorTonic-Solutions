import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    extracted_probs = y_pred[np.arange(len(y_true)), y_true]
    print(extracted_probs)
    return -np.sum(np.log(extracted_probs))/len(y_true)