# -*- coding:utf-8 -*-
# 使用神经网络算法预测销量的高低
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# 参数初始化
data = pd.read_excel("c://mldata//sales_data.xls", index_col=u'序号')

data[data == u"好"] = 1
data[data == u"是"] = 1
data[data == u"高"] = 1
data[data != 1] = 0

train_data = data.values  # 将读取的数据其转换为矩阵形式
train_x = train_data[0::, :3].astype(int)
train_label = train_data[0::, 3].astype(int)  # 为什么必须要加这个玩意呢？

model = Sequential()  # 建立模型
model.add(Dense(10, input_dim=3))
model.add(Activation('relu'))  # 使用relu作为激活函数，能够大幅度提高准确度
model.add(Dense(1))  # 由于是0-1输出，用sigmoid作为激活函数
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', class_mode='binary')
model.fit(train_x, train_label, nb_epoch=1000, batch_size=10)  # 学习1000次
yp = model.predict_classes(train_x).reshape(len(train_label))  # 分类预测

print yp

from cm_plot import *

cm_plot(train_label, yp).show()  # 显示混淆矩阵可视化结果
