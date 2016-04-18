# -*- coding:utf-8 -*-

from math import log
import operator


# 计算数据集合的信息熵，熵越高，混合的数据也越多，信息熵：H = - 求和（PlogP）(M为一个标签的数量)
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # 对象的长度
    labelsCounts = {}  # 字典{键:值}
    # 为所有可能分类创造字典{所有的标签：所有标签的数目}
    for featVec in dataSet:  # dataSet为[ [], [], []]类型，featVec为其中的一个[]
        currentLabel = featVec[-1]  # -1为最后一个元素，表示标签
        if currentLabel not in labelsCounts.keys():
            labelsCounts[currentLabel] = 0
        labelsCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelsCounts:
        prob = float(labelsCounts[key]) / numEntries  # prob为选择该分类的概率
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 按照给定特征划分数据集，相当于开始决策，从第一个元素开始判断
def splitDataSet(dataSet, axis, value):  # 待划分的数据集、划分数据集的特征、特征的返回值
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:  # featVec的第axis个元素(索引)和value相等
            reducedFeatVec = featVec[:axis]  # [0->axis]的元素--------->为[]
            reducedFeatVec.extend(featVec[axis + 1:])  # [axis+1->最终]的元素
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 选择最好的数据集划分方式：遍历整个数据集合，循环计算香农熵和splitDataSet函数
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # dataSet集合中一个数据的长度
    baseEntropy = calcShannonEnt(dataSet)  # dataSet集合的香农熵
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # i代表的是特征，为列
        # 创建唯一的分类标签列表
        featList = [example[i] for example in dataSet]  # i=0,[1, 1, 1, 0, 0]
        uniqueVals = set(featList)  # Python的set, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素.   [0,1]
        newEntropy = 0.0
        # 计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)  # dataSet的每个子元素中索引为i的元素的值是否为value
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy  # dataSet的信息熵-子集的信息熵
        # 计算最好的信息熵
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


# 统计频率出现的次数
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter, reverse=True)  # 排序字典
    return sortedClassCount


# 创建树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # ['yes', 'yes', 'no', 'no', 'no']
    print classList
    # print classList.count(classList[0]) Python count() 方法用于统计字符串里某个字符出现的次数
    if classList.count(classList[0]) == len(classList):  # 类别完全相同则停止划分
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])  # del用于list列表操作，删除一个或者连续几个元素。
    featValues = [example[bestFeat] for example in dataSet]
    print featValues
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        print splitDataSet(dataSet, bestFeat, value)
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)  # 循环
    return myTree
