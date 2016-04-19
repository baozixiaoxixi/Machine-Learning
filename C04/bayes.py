# -*- coding:utf-8 -*-
from numpy import *


# 实验样本
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1代表侮辱性文字，0代表正常言论
    return postingList, classVec


# 创建一个包含在所有文档中出现的不重复词的列表：全部词汇放在一个列表里，不重复
def createVocabList(dataSet):
    vocabSet = set([])  # set()去除列表中的重复对象，
    # 注意使用了set方法后------>输出为set([]),demo:seq = [1,2,3,1,2,3,'a','hello','a','world'] ,seq_set = set(seq)，输出：set(['a', 1, 2, 3, 'world', 'hello'])  #去除了重复对象
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 两个集合的并集，set(['a', 1, 2, 3, 'world', 'hello'])  #去除了重复对象
    return list(vocabSet)  # list() 方法用于将元组转换为列表。区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。


# 将当前文档中的单词与所有词汇进行比较，如果该单词存在于词汇列表中，将词汇列表的那个位置的值标为1，其他位置为0
# 将一组单词转换为一组数据
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary:" % word
    return returnVec


# 训练算法
def trainNB0(trainMatrix, trainCategory):  # trainMatrix：输入参数文档矩阵，trainCategory：每篇文档类别标签所构成的向量
    numTrainDocs = len(trainMatrix)  # 一共有几个向量（几句话）
    numWords = len(trainMatrix[0])  # 一共有多少个单词（不重复）
    pAbusive = sum(trainCategory) / float(numTrainDocs)  # 训练集中侮辱性言论占总体的比例
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0  # p1表示侮辱性言论，p0表示正常言论
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]  # 所有侮辱言论中单词出现的次数在列表中标出
            p1Denom += sum(trainMatrix[i])  # 所有侮辱言论的单词总数
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


# 分类器
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):  # vec2Classify要分类的向量
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []  # 训练样本向量表示
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(trainMat, listClasses)

    testEntry = ['love', 'my', 'dalmation']
    thisDoc = setOfWords2Vec(myVocabList, testEntry)
    print classifyNB(thisDoc, p0V, p1V, pAb)

    testEntry = ['stupid', 'garbage']
    thisDoc = setOfWords2Vec(myVocabList, testEntry)
    print classifyNB(thisDoc, p0V, p1V, pAb)


# 文件解析器
def textParse(bigString):  # 将字符串拆分成字符
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


# 处理电子邮件
def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):  # 1-25
        wordList = textParse(open('c://email//spam//%d.txt' % i).read())  # 垃圾邮件
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('c://email//ham//%d.txt' % i).read())  # 正常邮件
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)  # 全部词汇放在一个列表里，不重复
    trainingSet = range(50)  # [0-49]
    testSet = []
    # 随机构建训练集
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))  # uniform()方法将随机生成下一个实数，它在[x,y]范围内。
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))  # 将词汇转成向量
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(trainMat, trainClasses)
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(wordVector, p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print "the error rate is : ", float(errorCount) / len(testSet)

spamTest()