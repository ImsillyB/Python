# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:50:30 2018

@author: 梓鑫
"""

from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 4)
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
#print(knn.score(x_test, y_test))
from sklearn.cross_validation import cross_val_score
#scores = cross_val_score(knn, x, y, cv = 5, scoring='accuracy')
#print(scores.mean())

k_range = range(1, 31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
#    scores = cross_val_score(knn, x, y, cv = 10, scoring = 'accuracy')
    loss = -cross_val_score(knn, x, y, cv = 10, scoring = 'mean_squared_error')
    k_scores.append(loss.mean())


plt.plot(k_range, k_scores)
plt.xlabel('Value of K for knn')
plt.ylabel('Cross-Validated Accuracy')
plt.show()