# -*- coding:utf-8 -*-
import trees
import treePlotter

# 预测隐形眼镜的类型
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript','astigmatic','tearRate']
lensesTree = trees.createTree(lenses,lensesLabels)
treePlotter.createPlot(lensesTree)
