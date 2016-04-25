# -*- coding:utf-8 -*-
import numpy as np
import time
import theano
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD

# 安装成功theano
# A = np.random.rand(1000, 10000).astype(theano.config.floatX)
# B = np.random.rand(10000, 1000).astype(theano.config.floatX)
# np_start = time.time()
# AB = A.dot(B)
# np_end = time.time()
# X, Y = theano.tensor.matrices('XY')
# mf = theano.function([X, Y], X.dot(Y))
# t_start = time.time()
# tAB = mf(A, B)
# t_end = time.time()
# print "NP time: %f[s], theano time: %f[s] (times should be close when run on CPU!)" % (
#     np_end - np_start, t_end - t_start)
# print "Result difference: %f" % (np.abs(AB - tAB).max(),)

# 测试安装keras
model = Sequential()  # 模型初始化
model.add(Dense(20, 64))  # 添加输入层（20个节点），第一隐藏层（64节点）的连接
model.add(Activation('tanh'))  # 第一层使用tanh作为激活函数
model.add(Dropout(0.5))  # 使用Dropout防止过拟合
model.add(Dense(64,64)) #添加第一隐藏层（64节点），第二隐藏层（64节点）的连接
model.add(Activation('tanh'))  # 第二层使用tanh作为激活函数
model.add(Dropout(0.5))  # 使用Dropout防止过拟合
model.add(Dense(64,1)) #添加第一隐藏层（64节点），输出层（1节点）的连接
model.add(Activation('sigmoid'))  # 输出层使用sigmoid作为激活函数

sgd = SGD(lr=0.1,decay=1e-6,momentum=0.9,nesterov=True) #定义求解算法
model.compile(loss='mean_squared_error',optimizer=sgd)#编译生成模型，损失函数为平均误差平方和
