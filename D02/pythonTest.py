# -*- coding:utf-8 -*-
from scipy.optimize import fsolve  # 导入求解方程组的函数
from scipy import integrate  # 导入积分函数
import numpy as np
import matplotlib.pyplot as plt  # 导入Matplotlib
import pandas as pd
from statsmodels.tsa.stattools import adfuller as ADF  # 导入ADF检验
from sklearn.linear_model import LinearRegression  # 导入线性回归模型
from sklearn import datasets  # 导入为我们提供的数据集
from sklearn import svm  # 导入SVM模型

model = LinearRegression()  # 建立线性回归模型
print model

iris = datasets.load_iris()  # 加载数据集
# print iris
print iris.data.shape  # 查看数据集的大小
# print iris.target
# print iris.data

clf = svm.LinearSVC()  # 建立线性SVM分类器
clf.fit(iris.data, iris.target)  # 用数据训练模型
print clf.predict([[5.0, 3.6, 1.3, 0.25]])  # 输入新的数据进行预测
print clf.coef_  # 查看训练好的模型


# print ADF(np.random.rand(100))  # 返回结果有ADF值，p值等

# s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # 创建一个序列s
# print s
# d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])  # 创建一个表
# print d
# print pd.DataFrame(s)  # 利用已有的序列来创建表格
#
# print d.head()  # 预览前5行数据
# print d.describe()  # 数据基本统计量

# x = np.linspace(0, 10, 1000)  # 作图的变量自变量
# y = np.sin(x) + 1
# z = np.cos(x ** 2) + 1
# plt.figure(figsize=(8, 4))  # 设置图像大小
# plt.plot(x, y, label='$\sin x+1$', color='red', linewidth=2)
# plt.plot(x, z, 'b--', label='$\cos x^2+1$')
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.title('A simple example')
# plt.ylim(0, 2.2)  # y轴范围
# plt.legend()  # 显示图例
# plt.show()

# def f(x):
#     x1 = x[0]
#     x2 = x[1]
#     return [2 * x1 - x2 ** 2 - 1, x1 ** 2 - x2 - 2]
#
# result = fsolve(f, [1, 1])
# print result
#
# def g(x):  # 定义被积函数
#     return (1 - x ** 2) ** 0.5
#
# pi_2, err = integrate.quad(g, -1, 1)  # 积分结果和误差
# print pi_2, err


# a = np.array([2, 0, 1, 5])
# print a
# print a[:3]
# print a.min()
# a.sort()
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print b
# print b * b
