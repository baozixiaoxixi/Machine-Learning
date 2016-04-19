# -*- coding:utf-8 -*-
import re
from numpy import *

mySent = 'This book is the best book on Python.'

regEx = re.compile('\\W*')  # *匹配前面的子表达式零次或多次。
# \W	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。注意此处W必须是大写
# ['This', 'book', 'is', 'the', 'best', 'book', 'on', 'Python', '']里面有空字符串必须去除
listOfTokens = regEx.split(mySent)
print [tok.lower() for tok in listOfTokens if len(tok) > 0]  # ok

emailText = open("c://email//ham//6.txt").read()
print regEx.split(emailText)

trainingSet = range(50)  # [0-49]
testSet = []
# 随机构建训练集
for i in range(10):
    randIndex = int(random.uniform(0, len(trainingSet)))
    testSet.append(trainingSet[randIndex])
    del (trainingSet[randIndex])

print trainingSet
print testSet
