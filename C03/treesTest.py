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

print trees.splitDataSet(myDat,0,1) #找到dataSet对象中索引为0的值看是否和1相等，如果相等，返回后边的值
