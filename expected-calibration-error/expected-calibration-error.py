import collections
import math
def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here

    bins = collections.defaultdict(
        lambda: collections.defaultdict(float)
    )
    n = len(y_true)
    for p_true, p_pred in zip(y_true, y_pred):
        
        bin_index = math.floor(p_pred * n_bins) if p_pred < 1 else n_bins - 1
        bins[bin_index][
            "num_acc"
        ] += 1
        bins[bin_index][
            "acc"
        ] += p_true
        bins[bin_index][
            "pred"
        ] += p_pred

    # for p in sorted(y_pred):
    #     bin_index = math.floor(p * n_bins)
    #     bins[bin_index][
    #         "pred"
    #     ] += p 

    total_ece = 0.0
    for bin_index, bin in bins.items():
        print("bin_index: ", bin_index)
        print("num_acc: ", bin["num_acc"])
        print("bin[acc]: ", bin["acc"])
        print("bin[pred]: ", bin["pred"])
        

        # acc = 1.0/bin["num_acc"] * bin["acc"]
        # conf = 1.0/bin["num_acc"] * bin["pred"]
        acc = bin["acc"]
        conf = bin["pred"]
        print("acc: ", acc)
        print("conf: ", conf)
        abs_diff = abs(acc - conf)

        print("abs_diff: ", abs_diff)
        total_ece += abs_diff
        print("total_ece: ", total_ece)
        print()
            

    
    
    return total_ece/n