# -*- coding:utf-8 -*-

import trees


def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


myDat, labels = createDataSet()
print myDat
# print trees.calcShannonEnt(myDat)   #熵越高，则混合的数据越多，如果增加maybe分类myDat[0][-1]='maybe'，则信息熵更高了

# print trees.splitDataSet(myDat, 0, 1)  # 循环dataSet对象，对于每一个循环值，索引为0的值看是否和1相等，如果相等，返回后边的值
# print trees.chooseBestFeatureToSplit(myDat)

print trees.createTree(myDat, labels)
