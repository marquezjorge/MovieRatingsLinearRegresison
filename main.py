
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as mplt


# https://numpy.org/doc/stable/reference/routines.linalg.html?highlight=linear%20algebra
# https://online.stat.psu.edu/stat462/node/132/
# https://www.youtube.com/watch?v=K_EH2abOp00
# https://www.geeksforgeeks.org/introduction-to-3d-plotting-with-matplotlib/
# https://aegis4048.github.io/mutiple_linear_regression_and_visualization_in_python


def getData() -> list:
    f = open("data.txt", "r")
    data = f.readlines()
    return data


def getBeta(X: np.array, Y: np.array) -> np.array:
    xTranspose = np.transpose(X)
    result1 = la.inv(np.dot(xTranspose, X))
    result2 = np.dot(xTranspose, Y)
    return np.dot(result1, result2)


def getErrorVector(bMatrix: np.array, X: np.array, Y: np.array) -> list:
    e = []
    for i in range(0, len(X)):
        e.append(Y[i] - bMatrix[0] + bMatrix[1]*X[i][1] + bMatrix[2]*X[i][2])
    return e


def getSumOfSquaresError(e: list) -> float:
    return float(np.dot(np.transpose(e), e))


def getMeanSquareError(sse: float, X: np.array):
    mse = float(sse / len(X) - 3)
    return mse


def getStandardErrors(mse: float, X: np.array) -> list:
    alpha = np.sqrt(mse)
    temp = la.inv(np.dot(np.transpose(X), X))
    return [temp[0][0] * alpha, temp[1][1] * alpha, temp[2][2] * alpha]


def getCoefficientsOfCorrelation(X: np.array, Y: np.array) -> list:
    x1y = 0
    x2y = 0
    x1Mean = 0
    x2Mean = 0
    yMean = 0
    x1SquaredSum = 0
    x2SquaredSum = 0
    ySquaredSum = 0

    for i in range(0, len(X)):
        x1Mean += X[i][1]
        x2Mean += X[i][2]
        yMean += Y[i]
        x1y += X[i][1]*Y[i]
        x2y += X[i][2]*Y[i]
        x1SquaredSum += np.square(X[i][1])
        x2SquaredSum += np.square(X[i][2])
        ySquaredSum += np.square(Y[i])

    x1Mean = x1Mean / len(X)
    x2Mean = x2Mean / len(X)
    yMean = yMean / len(Y)

    R1 = x1y - len(X)*x1Mean*yMean
    R1 = R1 / (np.sqrt(x1SquaredSum - len(X)*np.square(x1Mean))*np.sqrt(ySquaredSum - len(Y)*np.square(yMean)))
    R2 = x2y - len(X)*x2Mean*yMean
    R2 = R2 / (np.sqrt(x2SquaredSum - len(X)*np.square(x2Mean))*np.sqrt(ySquaredSum - len(Y)*np.square(yMean)))

    return [R1, R2]


def graph(X, Y, bMatrix):

    x1 = []
    x2 =[]
    x1Input = np.linspace(50, 200, 150)
    x2Input = np.linspace(150000000, 400000000, 150)
    yHat = bMatrix[0] + bMatrix[1]*x1Input + bMatrix[2]*x2Input

    for i in range(0, len(X)):
        x1.append(X[i][1])
        x2.append(X[i][2])

    fig = mplt.figure()
    ax = mplt.axes(projection='3d')
    ax.scatter(x1, x2, Y, c=Y, cmap='cividis')
    ax.set_xlabel('Runtime')
    ax.set_ylabel('Budget')
    ax.set_zlabel('Rating')
    ax.plot(x1Input, x2Input, yHat, label='Y = B0 + B1(X1) + B2(X2)')
    ax.legend()
    fig.tight_layout()
    mplt.show()


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
    bVector = getBeta(X, Y)
    SSE = getSumOfSquaresError(getErrorVector(bVector, X, Y))
    MSE = getMeanSquareError(SSE, X)
    standardErrors = getStandardErrors(MSE, X)
    coefficientsOfCorrelation = getCoefficientsOfCorrelation(X, Y)
    print("B0:", bVector[0],
          "\nB1:", bVector[1],
          "\nB2", bVector[2])
    print("SSE:", SSE)
    print("MSE:", MSE)
    print("S.E. B0: ", standardErrors[0],
          "\nS.E. B1: ", standardErrors[1],
          "\nS.E. B2: ", standardErrors[2])
    print("R1:", coefficientsOfCorrelation[0],
          "\nR2:", coefficientsOfCorrelation[1])
    graph(X, Y, bVector)


if __name__ == '__main__':
    main()


