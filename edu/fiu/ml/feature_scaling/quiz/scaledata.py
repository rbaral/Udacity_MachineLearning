__author__ = 'rbaral'
""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    import numpy as np
    arr = np.array(arr)
    scaledArr = np.zeros_like(arr)
    scaledArr = (arr - float(min(arr)))/(max(arr) - min(arr))
    return scaledArr

def featureScalingSklearn(arr):
    from sklearn.preprocessing import MinMaxScaler
    import numpy as np
    scaler = MinMaxScaler()
    arr = np.array(arr, dtype=float) # floating type is required for sklearn
    scaledArr = scaler.fit_transform(arr)
    return scaledArr

# tests of your feature scaler--line below is input data
data = [[115], [140], [175]]
print featureScaling(data)
print featureScalingSklearn(data)