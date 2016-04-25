# -*- coding:utf-8 -*-
# 数据规范化
import pandas as pd
import numpy as np

data = pd.read_excel("c://mldata//normalization_data.xls", header=None)
print data

print (data - data.min()) / (data.max() - data.min())  # 最小-最大规范化
print (data - data.mean()) / data.std()  # 零均值规范化
print data / 10 ** np.ceil(np.log10(data.abs().max()))  # 小数定标规范化
