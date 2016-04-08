# -*- coding:utf-8 -*-
from numpy import *
from KNNTest import classify0
import matplotlib   #散点图
import matplotlib.pyplot as plt
import operator     #运算符模块

#本章主要介绍：k-近邻算法改进约会网站的配对效果

#将文本记录转换到NumPy
def file2matrix(filename):
    fr = open(filename) #打开文件
    arrayOfLines = fr.readlines()      #读取所有的行数
    numberOfLines = len(arrayOfLines)  #得到文件的行数
    returnMat = zeros((numberOfLines,3))  #numpy，0矩阵，每行3列，一共numberOfLines行
    classLabelVector = []
    index = 0
    for line in arrayOfLines :
        line = line.strip()            #前后空格都没了，但中间间隔还保留
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]     #将这一行的前三个特征元素存储在索引为index的returnMat中
        classLabelVector.append(int64(listFromLine[-1]))  #索引-1表示最后一列元素，python会将这些元素当作整形处理
        index += 1
    return returnMat,classLabelVector

#数值归一化-->OK
def autoNorm(dataSet):
    minVals = dataSet.min(0)    #最小值[ 0. 0. 0.001156],每一列的最小值
    maxVals = dataSet.max(0)    #最大值
    ranges = maxVals - minVals  #范围
    normDataSet = zeros(shape(dataSet))     #shape函数是numpy中的函数，它的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度
    m = dataSet.shape[0]        #1000
    normDataSet = dataSet - tile(minVals,(m,1)) #tile函数位于python模块 numpy中，他的功能是重复某个数组。比如tile(A,n)，功能是将数组A重复n次，构成一个新的数组
                                                #([2,3],(4,1)) --->组内重复一次，变成4组---->[[2,3],[2,3],[2,3],[2,3]]
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.1   #测试数据所占的比重为0.1
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
    normMat, ranges, minVals = autoNorm(datingDataMat)  # 其中normMat为归一化后的正常数据，因为三个因素的权重都是相同的
    m = normMat.shape[0]            #1000,总数
    numTestVecs = int(m*hoRatio)    #100.测试数据有100个
    errorCount = 0.0
    for i in range(numTestVecs):    #开始测试数据
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "the classidier came back with :%d ,the real number is :%d" %(classifierResult,datingLabels[i])
        if(classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is :%f" % (errorCount/float(numTestVecs))

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt') #读取文本数据
    normMat, ranges, minVals = autoNorm(datingDataMat)      #归一化数据
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)  #取得正确结果
    print "you will probably like this person: " , resultList[classifierResult - 1]

c = classifyPerson()



#print datingLabels

# fig = plt.figure()
# ax = fig.add_subplot(111)       #参数349的意思是：将画布分割成3行4列，图像画在从左到右从上到下的第9块
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))   #散点图显示第二列和第三列的数据,应该是对应坐标的大小
# plt.show()