# -*- coding:utf-8 -*-
# 使用ID3决策树算法预测销量高低
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC

# 参数初始化
data = pd.read_excel("c://mldata//sales_data.xls", index_col=u'序号')

data[data == u"好"] = 1
data[data == u"是"] = 1
data[data == u"高"] = 1
data[data != 1] = -1

train_data = data.values  # 将读取的数据其转换为矩阵形式
train_x = train_data[0::, :3]
train_label = train_data[0::, 3].astype(int)  # 为什么必须要加这个玩意呢？

print train_label

dtc = DTC(criterion="entropy")  # 建立决策树模型，基于信息上
dtc.fit(train_x, train_label)  # 训练模型

print dtc.predict([1, 1, -1])
