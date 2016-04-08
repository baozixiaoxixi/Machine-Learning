# -*- coding:utf-8 -*-
from numpy import *
import os
from KNNTest import classify0
import operator     #运算符模块

#本章主要介绍：k-近邻算法手写识别系统

#将图像转换成向量
#图像为32*32的二进制图像-------------->将其转换成1*1024的向量
def img2vector(filename):
    returnVect = zeros((1,1024))    # #numpy，0矩阵，每行1024列，一共1行
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

#手写数字识别系统测试
def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('C:\\a\\trainingDigits')
    m = len(trainingFileList)   #一共多少个训练样本
    trainingMat = zeros((m,1024))   #训练样本一共m行，每一行1024列，为其内容
    for i in range(m):
        fileNameStr = trainingFileList[i]   #获取文件名称
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])    #从文件名中解析出分类数字
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('C:\\a\\trainingDigits\\'+fileNameStr)

    testFileList = os.listdir('C:\\a\\testDigits')  #这是测试样本
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]  # 获取文件名称
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])  # 从文件名中解析出分类数字
        vectorUnderTest = img2vector('C:\\a\\testDigits\\'+fileNameStr)
        #开始KNN识别
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)    #输入函数与每个训练函数--->差的平方在开方--->寻找出最小的数
        print "the classifier came back with: %d ,the real answer is:%d" %(classifierResult , classNumStr)
        if(classifierResult != classNumStr):
            errorCount += 1.0

    print "\nthe total number of errors is:%d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))


returnVect = handwritingClassTest()

#总结：
#算法的执行效率并不高，因为算法需要为每个测试向量做2000次距离计算，每个距离计算包括了1024个维度的浮点运算，总共执行9000次
#k决策树就是k-近邻算法的优化版，可以节省大量的计算开销
