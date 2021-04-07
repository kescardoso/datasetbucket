import numpy as np
from statistics import mean, variance
from sklearn.linear_model import LinearRegression

# calculate the mean of an array of data
def calcMean(data):
    if data is None: return None
    else: return mean( np.array(data) )

# calculate the variance of an array of data
def calcVariance(data):
    if data is None: return None
    else: return variance( np.array(data) )

# >! not using yet !< #
# calculate the linear Regression of an array of data
def calcLinearReg(npArray):
    if npArray is None: return None
    X = npArray
    # y = 1 * x_0 + 2 * x_1 + 3
    # TODO need to figure out exactly what this y calc does
    y = np.dot(X, np.array([1, 2])) + 3
    
    reg = LinearRegression().fit(X, y)
    reg.score(X, y)
    reg.coef_
    reg.intercept_
    
    # TODO need to figure out what parameters to predict >>:>> (np.array([])) array-like or sparse matrix, shape (n_samples, n_features)
    return reg.predict(np.array([[3, 5]]))
    # returns prdicted values: array, shape(n_samples)

# calculates how many unique values are in an array
# TODO: make it work for a dict too
def calcUniquieValues(data):
    if data is None:
        return
    array = np.array(data)
    count = 0
    temparray = []
    for d in array:
        if d not in temparray:
            temparray.append(d)
            count += 1
    return count
