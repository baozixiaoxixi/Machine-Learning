# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# 菜品盈利数据 帕累托图

data = pd.read_excel('c:\\mldata\\catering_dish_profit.xls', index_col=u'菜品名')
data = data[u'盈利'].copy()
data.sort(ascending=False)
print data

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 在一个图上画两种类型
plt.figure()
data.plot(kind='bar')  # 水平直方图
plt.ylabel(u'盈利(元)')
print data.cumsum()
p = 1.0 * data.cumsum() / data.sum()  # **********注意：累加sumsum
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6 * 0.9, p[6] * 0.9),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()
