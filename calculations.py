import numpy as np
from statistics import mean, variance
from sklearn.linear_model import LinearRegression
import matplotlib
import matplotlib.pyplot as plt

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
def calcUniqueValues(data):
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

# calculates the number of samples for each value
def calcBreakDown(data):
    sent = "You have "
    (unique, counts) = np.unique(data, return_counts=True)
    freq = np.asarray((unique, counts))

    freq = freq.T.astype(int)
    count = 0
    for i in freq:
        sent += str(i[1]) + " samples labelled as " + str(i[0])
        if count != len(freq) - 1:
            count += 1
            sent = sent + " and "
        else:
            sent = sent + "."

    return sent

# displays a histogram for a feature
def calcHistogram(data, category):
    title = category + " Histogram"
    file_name = title + '.png'
    num_bin = 0
    num_unique_val = calcUniqueValues(data)
    if num_unique_val < 10:
        num_bin = num_unique_val
    else:
        num_bin = 10
    matplotlib.use('agg')
    plt.hist(data, bins=num_bin)
    plt.title(title)
    plt.xlabel(category)
    plt.ylabel("Count")
    plt.savefig(file_name)
    plt.close()

    return file_name