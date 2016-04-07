# -*- coding:utf-8 -*-
from numpy import *
import operator     #运算符模块

#本章主要介绍：k-近邻算法
#测量不同特征值之间的距离方法进行分类

#通用函数
def createDataSet():    #创造数据集和标签，可以在坐标图上看出来，AA在一块，BB在一块
    group = array ([ [1.0,1.1],[1.0,1.0],[0,0],[0,0.1] ])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX, dataSet, labels, k):     # k近邻算法具体实现，inX为用于分类的输入向量，dataSet为输入的训练样本集，labels为标签向量，k为用于选择最近邻居的数目
    dataSetSize = dataSet.shape[0]  # 4-----> shape函数是numpy中的函数，它的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度
    diffMat = tile(inX, (dataSetSize,1)) - dataSet  #tile函数位于python模块 numpy中，他的功能是重复某个数组。比如tile(A,n)，功能是将数组A重复n次，构成一个新的数组
                                                    #([2,3],(4,1)) --->组内重复一次，变成4组---->[[2,3],[2,3],[2,3],[2,3]]
    sqDiffMat = diffMat**2 #平方
    sqDistances = sqDiffMat.sum(axis=1)         # 当加入axis=1以后就是将一个矩阵的每一行向量相加
    distances = sqDistances**0.5        #取得距离
    sortedDistIndicies = distances.argsort()    #注意这个排序，是对距离数组的角标进行排序，从小到大
    print sortedDistIndicies
    classCount = {}     # 字典
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1   #字典中统计数目
    print classCount   #----->{'A': 2, 'B': 1}
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)   # iteritems()为字典的迭代器
                                                                                                # Python内置的排序函数sorted可以对list或者iterator进行排序,
                                                                                                # itemgetter函数用于获取对象的哪些维的数据
                                                                                                # reverse是一个bool变量，默认为false（升序排列），定义为True时将按降序排列
    print sortedClassCount  # [('A', 2), ('B', 1)]
    return sortedClassCount[0][0]


group,labels = createDataSet()

print classify0([0,0],group,labels,3)