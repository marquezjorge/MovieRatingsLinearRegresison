
import numpy as np
import numpy.linalg as la


# https://numpy.org/doc/stable/reference/routines.linalg.html?highlight=linear%20algebra
# https://online.stat.psu.edu/stat462/node/132/
# https://www.youtube.com/watch?v=K_EH2abOp00


def getData() -> list:
    f = open("data.txt", "r")
    data = f.readlines()
    return data


# xTranspose is the transpose of matrix X
# result1 is the inverse of the dot product between the xTranspose and X
# result2 is the dot product between xTranspose and Y
# dot product between 
def getBeta(X: np.array, Y: np.array) -> np.array:
    xTranspose = np.transpose(X)
    result1 = la.inv(np.dot(xTranspose, X))
    result2 = np.dot(xTranspose, Y)
    return np.dot(result1, result2)


# yHat == B0 + B1*X1 + B2*X2
# e == Y - yHat == e' * e
def getSumOfSquaresError(bMatrix: np.array, X: np.array, Y: np.array) -> float:
    e = []
    for i in range(0, len(X)):
        e.append(Y[i] - bMatrix[0] + bMatrix[1]*X[i][1] + bMatrix[2]*X[i][2])
    return float(np.dot(np.transpose(e), e))


def getMeanSquareError(sse: float, X: np.array):
    mse = float(sse / len(X) - 3)
    return mse


def getStandardErrors(mse: float, X: np.array) -> list:
    temp = la.inv(np.dot(np.transpose(X), X))
    return [temp[0][0], temp[1][1], temp[2][2]]


def getCoefficientOfCorrelation():
    pass


def main():
    data = getData()
    tempRows = []
    Y = []

    for i in range(0, len(data)):
        temp = data[i].split()
        Y.append(float(temp[2]))
        tempList = [1.0, float(temp[0]), float(temp[1])]
        tempRows.append(tempList)

    X = np.array(tempRows)
    Y = np.array(Y)
    bMatrix = getBeta(X, Y)
    SSE = getSumOfSquaresError(bMatrix, X, Y)
    MSE = getMeanSquareError(SSE, X)
    standardErrors = getStandardErrors(MSE, X)

    print("B0:", bMatrix[0],
          "B1:", bMatrix[1],
          "B2", bMatrix[2])
    print("SSE:", SSE)
    print("MSE:", MSE)
    print("S.E. B0: ", standardErrors[0],
          "S.E. B1: ", standardErrors[1],
          "S.E. B2: ", standardErrors[2])


if __name__ == '__main__':
    main()


