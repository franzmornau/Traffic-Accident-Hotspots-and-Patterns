def roc_curve(probs, labels):
    sorting    = np.argsort(probs)
    thresholds = probs[sorting]
    TPRs = []
    FPRs = []
    
    real_pos_cases = sum(labels)
    real_neg_cases = len(labels) - real_pos_cases
    
    for i in range(len(labels)):
        class_pos = labels[sorting][i:] 
        lab_pos = len(class_pos)
        tr_pos= sum(class_pos)
        f_pos = lab_pos - tr_pos
        TPRs.append( tr_pos / real_pos_cases )
        FPRs.append( f_pos / real_neg_cases )
    return TPRs, FPRs, thresholds

import numpy as np