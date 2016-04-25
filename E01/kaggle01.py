# -*- coding:utf-8 -*-
# 手写数字识别，使用KNN
import pandas as pd
import csv as csv
from sklearn.neighbors import KNeighborsClassifier

train_raw = pd.read_csv('c://mldata//train.csv', header=0)
test_raw = pd.read_csv('c://mldata//test.csv', header=0)

knn = KNeighborsClassifier()

train = train_raw.values  # 将读取的数据其转换为矩阵形式
test = test_raw.values

print 'Start training'  # 开始训练
knn.fit(train[0::, 1::], train[0::, 0])  # 注意：这是行、列的表示形式

print 'Start predicting'  # 开始预测
out = knn.predict(test)

print 'Start writing!'
n, m = test.shape  # test这个矩阵的行和列
ids = range(1, n + 1)  # 图片的id
predictions_file = open("c://mldata//out.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerows(["ImageId", "Label"])
open_file_object.writerows(zip(ids, out))  # 注意这个zip,zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
predictions_file.close()
print 'All is done'
