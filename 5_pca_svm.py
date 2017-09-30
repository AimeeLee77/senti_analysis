#!/usr/bin/env python
# -*- coding: utf-8  -*-
# PCA  SVM
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn import metrics


# 获取数据 [1995 rows x 400 columns]
fdir = ''
df = pd.read_csv(fdir + '2000_data.csv')
y = df.iloc[:,1]
x = df.iloc[:,2:]


# PCA降维
##计算全部贡献率
n_components = 400
pca = PCA(n_components=n_components)
pca.fit(x)
#print pca.explained_variance_ratio_

##PCA作图
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.axes([.2, .2, .7, .7])
plt.plot(pca.explained_variance_, linewidth=2)
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_')
plt.show()



##根据图形取100维
x_pca = PCA(n_components = 100).fit_transform(x)


# SVM (RBF)
# using training data with 100 dimensions

clf = svm.SVC(C = 2, probability = True)
clf.fit(x_pca,y)

print 'Test Accuracy: %.2f'% clf.score(x_pca,y)

#Create ROC curve
pred_probas = clf.predict_proba(x_pca)[:,1] #score

fpr,tpr,_ = metrics.roc_curve(y, pred_probas)
roc_auc = metrics.auc(fpr,tpr)
plt.plot(fpr, tpr, label = 'area = %.2f' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.legend(loc = 'lower right')
plt.show()



