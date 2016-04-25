# -*- coding:utf-8 -*-
# 拉格朗日插值法
import pandas as pd
from scipy.interpolate import lagrange  # 导入拉格朗日插值函数

data = pd.read_excel("c://mldata//catering_sale.xls")
# data[u'销量'][0] 销量的第一行数据
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None


# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据的个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]  # 取数
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y))(n)  # 插值并返回插值结果


# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:  # 这是什么意思？
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel("c://mldata//catering_sale1.xls")
