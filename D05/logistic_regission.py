# -*- coding:utf-8 -*-
# 逻辑回归：自动建模
import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

data = pd.read_excel("c://mldata//bankloan.xls", header=0)
# x = data.iloc[:, :8].as_matrix()
# y = data.iloc[:, 8].as_matrix()   和下边的两种读取数据的方式，都会带来精度的影响
train_data = data.values  # 将读取的数据其转换为矩阵形式
train_x = train_data[0::, :8]
train_label = train_data[0::, 8]

rlr = RLR()  # 建立随机回归模型，筛选变量
rlr.fit(train_x, train_label)  # 训练模型
rlr.get_support()  # 获取特征筛选结果
print u"特征筛选结束"
print u"有效特征为：%s" % u'、'.join(data.columns[rlr.get_support()])

x = data[data.columns[rlr.get_support()]].as_matrix()  # 筛选好的特征

lr = LR()
lr.fit(x, train_label)  # 用筛选好的特征数据来训练模型
print u'逻辑回归训练结束'
print u'模型的平均正确率为：%s' % lr.score(x, train_label)
