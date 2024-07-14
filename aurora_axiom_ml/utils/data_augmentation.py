import pandas as pd
import numpy as np

def augment_data(data, augmentation_factor):
    augmented_data = pd.DataFrame()
    for i in range(augmentation_factor):
        augmented_data = pd.concat([augmented_data, data + np.random.normal(0, 0.1, size=data.shape)])
    return augmented_data
