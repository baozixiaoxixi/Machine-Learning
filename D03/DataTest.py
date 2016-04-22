# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt  # 导入图像库

# 使用箱图进行异常值分析

data = pd.read_excel('c:\\mldata\\catering_sale.xls', index_col=u'日期')  # 指定日期为索引列
statistics = data.describe()  # 保存基本统计量
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']  # 极差
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']  # 变异系数
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']  # 四分位数间距
print statistics

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.figure()  # 建立图像
p = data.boxplot()  # 画箱线图，直接使用DataFrame的方法
x = p['fliers'][0].get_xdata()  # 'flies'即为异常值的标签
y = p['fliers'][0].get_ydata()
y.sort()  # 从小到大排序，该方法直接改变原对象

print x
print y

# 用annotate添加注释
# 其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制。
# 以下参数都是经过调试的，需要具体问题具体调试。
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))  # xytext为注释文本所在的位置
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

plt.show()  # 展示箱线图
