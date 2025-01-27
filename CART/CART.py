from numpy import *
import matplotlib.pyplot as plt
from numpy import linalg


# Leaf model for classification
def regLeaf(dataSet):
    return mean(dataSet[:, -1])


# Error model for classification
def regErr(dataSet):
    return var(dataSet[:, -1]) * shape(dataSet)[0]


# Solve the matrix, to get coefficients
def linearSolve(dataset):
    m, n = shape(dataset)
    X = full((m, n), 1.0)
    X[:, 1:n] = dataset[:, 0:n-1]
    Y = dataset[:, -1]
    xTx = matmul(transpose(X), X)
    if linalg.det(xTx) == 0.0:
        raise NameError('Cannot do inverse matrix')
    ws = matmul(linalg.inv(xTx), matmul(transpose(X), Y))
    return ws, X, Y


# Leaf model for linear approximation
def modelLeaf(dataset):
    ws, X, Y = linearSolve(dataset)
    return ws


# Error model for linear approximation
def modelErr(dataset):
    ws, X, Y = linearSolve(dataset)
    yHat = matmul(X, ws)
    return sum(power(Y-yHat, 2))


def isTree(obj):
    return type(obj).__name__ == 'dict'


def loadDataSet(fileName):
    # read csv and return it as an array
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(',')
        fltLine = list(map(float, curLine))
        dataMat.append(fltLine)
    return array(dataMat)


def binSplitDataSet(dataSet, feature, value):
    # Divide into 2 parts
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0], :]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :]
    return mat0, mat1


def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1, 4)):
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
    if feat is None:
        return val
    # build tree recursively, splitting dataset into smaller segments
    retTree = {'spInd': feat, 'spVal': val}
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree


def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1, 4)):
    tolS = ops[0]   # tolerance in err. reduction
    tolN = ops[1]   # min. data instances to include in a split
    # Check if all target values are the same
    if len(set(dataSet[:, -1].tolist())) == 1:
        return None, leafType(dataSet)
    m, n = shape(dataSet)
    S = errType(dataSet)
    bestS = inf
    bestIndex = 0
    bestValue = 0
    # iterate over all features and values to find split with the lowest error
    for featIndex in range(n - 1):
        for splitVal in set(dataSet[:, featIndex]):
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
            if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
                continue
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    # exit if low error reduction
    if (S - bestS) < tolS:
        return None, leafType(dataSet)
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    # exit if dataset created in split is too small
    if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
        return None, leafType(dataSet)
    return bestIndex, bestValue


def plot_tree(tree, x_range):
    if isTree(tree):
        # Recursively search through the tree to find the leaf nodes
        split = tree['spVal']
        plot_tree(tree['right'], (x_range[0], split))
        plot_tree(tree['left'], (split, x_range[1]))
    else:
        # Plot the linear segment
        slope, intercept = tree
        x_vals = linspace(x_range[0], x_range[1], 100)
        y_vals = slope + intercept * x_vals
        plt.plot(x_vals, y_vals)


# Load the dataset
myData = loadDataSet('polynomial.txt')
myMatrix = array(myData)

# Linear approx: modelLeaf & modelErr
# Classification: regLeaf & regErr
leafType = modelLeaf
errType = modelErr

# Create the tree
myTree = createTree(myMatrix, leafType, errType, ops=(1, 10))

print(myTree)

# Plot results

# Plot the tree
plt.figure(figsize=(10, 6))

plt.scatter(myMatrix[:, 0], myMatrix[:, 1], c="blue", label="Data Points", s=4)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Data Points")
plt.legend()
plt.grid()
if leafType == modelLeaf:
    plot_tree(myTree, (min(myMatrix[:, 0]), max(myMatrix[:, 0])))
    plt.title("Data Points with Linear Fit")

# Show the plot
plt.show()
