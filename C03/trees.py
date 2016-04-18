# -*- coding:utf-8 -*-

from math import log


# 计算信息熵，熵越高，混合的数据也越多
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # 对象的长度
    labelsCounts = {}  # 字典{键:值}
    # 为所有可能分类创造字典{所有的标签：所有标签的数目}
    for featVec in dataSet:     # dataSet为[ [], [], []]类型，featVec为其中的一个[]
        currentLabel = featVec[-1]
        if currentLabel not in labelsCounts.keys():
            labelsCounts[currentLabel] = 0
        labelsCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelsCounts:
        prob = float(labelsCounts[key]) / numEntries  # prob为选择该分类的概率
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

# 按照给定特征划分数据集，相当于开始决策
def splitDataSet(dataSet,axis,value):   # 待划分的数据集、划分数据集的特征、特征的返回值
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:      # featVec的第axis个元素(索引)和value相等
            reducedFeatVec = featVec[:axis]     # [0->axis]的元素--------->为[]
            reducedFeatVec.extend(featVec[axis+1:]) # [axis+1->最终]的元素
            retDataSet.append(reducedFeatVec)
    return retDataSet

# 选择最好的数据集划分方式
