# -*- coding:utf-8 -*-
from numpy import *

print random.rand(4,4)  # 产生4*4的数组

randMat = mat(random.rand(4,4))    # mat()将数组转换成矩阵

print randMat

invRandMat =  randMat.I     # .I操作实现了矩阵的逆运算

myEye =  randMat*invRandMat    # 两个矩阵相乘，结果应该是单位矩阵，但是实际中矩阵里还留下了非常小的元素，这是计算机处理误差产生的结果

print myEye - eye(4)           # eye(4)创建4*4的单位矩阵，其结果为误差值