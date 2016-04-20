# -*- coding:utf-8 -*-
from numpy import *


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('c:\\mldata\\testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])  # 注意这块，X0=1
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


# 梯度上升
def gradAscent(dataMatIn, classLabels):
    # mat()将矩阵转换成numpy类型的矩阵，可以用来转置等操作
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()  # transpose()为矩阵的转置
    m, n = shape(dataMatrix)  # m表示行，n表示列
    alpha = 0.001  # 目标移动的步长
    maxCycles = 500  # 迭代次数
    weights = ones((n, 1))  # [[ 1.][ 1.][ 1.]]回归系数函数
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights


# 随机梯度上升算法
def stocGradAscent0(dataMatrix, classLabels, numIter=150):
    m, n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del (dataIndex[randIndex])
    return weights


# 画出分割线
def plotBestFit(wei):
    import matplotlib.pyplot as plt
    weights = wei  # Return `self` as an `ndarray` object.
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


# 开始分类
def classifyVector(inX, weights):  # 输入一条数据
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0


def colicTest():
    frTrain = open("c:\\mldata\\horseColicTraining.txt")
    frTest = open("c:\\mldata\\horseColicTest.txt")
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent0(array(trainingSet), trainingLabels, 500)
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split("\t")
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestVec)
    print "the errorRate is %f" % errorRate
    return errorRate


# dataArr, labelMat = loadDataSet()
# # weights = gradAscent(dataArr, labelMat)
# weights = stocGradAscent0(array(dataArr), labelMat)
# print weights
# plotBestFit(weights)
colicTest()
