# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:15:50 2018

@author: 梓鑫
"""

import pandas as pd  
import numpy as np  
from numpy import float64  
from sklearn import preprocessing  
from matplotlib import pyplot as plt  
from pandas import Series  
from scipy.spatial import distance  
from mpl_toolkits.mplot3d import Axes3D  
      
Height_cm = np.array([164, 167, 168, 169, 169, 170, 170, 170, 171, 172, 172, 173, 173, 175, 176, 178], dtype=float64)  
Weight_kg = np.array([54,  57,  58,  60,  61,  60,  61,  62,  62,  64,  62,  62,  64,  56,  66,  70], dtype=float64)  
hw = {'Height_cm': Height_cm, 'Weight_kg': Weight_kg}  
hw = pd.DataFrame(hw)  
print(hw)  
      
is_height_outlier = abs(preprocessing.scale(hw['Height_cm'])) > 2  
is_weight_outlier = abs(preprocessing.scale(hw['Weight_kg'])) > 2  
is_outlier = is_height_outlier | is_weight_outlier  
color = ['g', 'r']  
pch = [1 if is_outlier[i] == True else 0 for i in range(len(is_outlier))]  
cValue = [color[is_outlier[i]] for i in range(len(is_outlier))]  
    # print is_height_outlier  
    # print cValue  
fig = plt.figure()  
plt.title('Scatter Plot')  
plt.xlabel('Height_cm')  
plt.ylabel('Weight_kg')  
plt.scatter(hw['Height_cm'], hw['Weight_kg'], s=40, c=cValue)  
plt.show()  
      
      
n_outliers = 2  
m_dist_order = Series([float(distance.mahalanobis(hw.iloc[i], hw.mean(), np.mat(hw.cov().as_matrix()).I) ** 2) for i in range(len(hw))]).sort_values(ascending=False).index.tolist()  
is_outlier = [False, ] * 16  
for i in range(n_outliers):  
    is_outlier[m_dist_order[i]] = True  
color = ['g', 'r']  
pch = [1 if is_outlier[i] == True else 0 for i in range(len(is_outlier))]  
cValue = [color[is_outlier[i]] for i in range(len(is_outlier))]  
fig = plt.figure()  
plt.title('Scatter Plot')  
plt.xlabel('Height_cm')  
plt.ylabel('Weight_kg')  
plt.scatter(hw['Height_cm'], hw['Weight_kg'], s=40, c=cValue)  
plt.show()  