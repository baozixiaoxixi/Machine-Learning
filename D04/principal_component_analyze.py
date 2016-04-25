# -*- coding:utf-8 -*-
# 主成分分析
import pandas as pd
from sklearn.decomposition import PCA

data = pd.read_excel("c://mldata//principal_component.xls", header=None)

# pca = PCA()
# pca.fit(data)
# print pca.components_  # 返回模型的各个特征向量
# print pca.explained_variance_ratio_  # 返回各个成分各自的方差百分比

pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data)  # 用它来降低维度
pd.DataFrame(low_d).to_excel("c://mldata//principal_component1.xls")  # 保存结果
