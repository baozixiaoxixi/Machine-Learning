# -*- coding:utf-8 -*-

import pandas as pd

# 根据菜品销量之间的相关性可以得到不同菜品之间的关系

data = pd.read_excel('c:\\mldata\\catering_sale_all.xls', index_col=u'日期')

print data

print data.corr()  # 相关系数矩阵
