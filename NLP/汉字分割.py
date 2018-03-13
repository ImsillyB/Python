# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 19:11:05 2018

@author: 梓鑫
"""
from __future__ import print_function
#import numpy as np
import pandas as pd
import os
import jieba.analyse as analyse


path = os.getcwd()+'\\2016年变电一次设备缺陷汇总-截止10月23日.csv'
f = open(path)
data = pd.read_csv(f)
#print(data.head())



lines = data['缺陷描述']
#print (lines)
#for i in lines:
#    print(" ".join(analyse.textrank(i, topK = 10, withWeight = False, allowPOS = ('n', 'v'))))
lst = {}

for i in lines:
    lst[i] = ("/".join(analyse.textrank(i, topK = 15, withWeight = False, allowPOS = ('n', 'v', 'a')))) 

f = open('测试.txt','w')
for key in lst:
    print(key , ':', lst[key], '\n', file = f)
    print(lst[key])
f.close()



