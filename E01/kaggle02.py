# -*- coding:utf-8 -*-
# 手写数字识别，使用SVM和PCA降维
import pandas as pd
import csv as csv
from sklearn import svm
from sklearn.decomposition import RandomizedPCA

train_raw = pd.read_csv('c://mldata//train.csv', header=0)
test_raw = pd.read_csv('c://mldata//test.csv', header=0)

train = train_raw.values  # 将读取的数据其转换为矩阵形式
test = test_raw.values

print 'Start PCA to 50'
train_x = train[0::, 1::]
train_label = train[0::, 0]
pca = RandomizedPCA(n_components=50, whiten=True).fit(train_x)
train_x_pca = pca.transform(train_x)
test_x_pca = pca.transform(test)

print 'Start training'  # 开始训练
rbf_svc = svm.SVC(kernel='rbf')
rbf_svc.fit(train_x_pca, train_label)

print 'Start predicting'  # 开始预测
out = rbf_svc.predict(test_x_pca)

print 'Start writing!'
n, m = test_x_pca.shape  # test这个矩阵的行和列
ids = range(1, n + 1)  # 图片的id
predictions_file = open("c://mldata//out3.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["ImageId", "Label"])
open_file_object.writerows(zip(ids, out))  # 注意这个zip,zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
predictions_file.close()
print 'All is done'
