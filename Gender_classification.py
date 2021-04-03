# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:36:39 2021

@author: yujie
"""
from sklearn import tree

# height, weigth, shoe size
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()
# train
clf = clf.fit(X,Y)

# predict 
predict = clf.predict([[150,40,32]])
print(predict)