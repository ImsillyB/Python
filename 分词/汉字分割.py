# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 19:11:05 2018

@author: 梓鑫
"""
#from __future__ import print_function
#import numpy as np
import pandas as pd

import jieba.analyse as analyse
import jieba
import time
#import sys

#def fen_ci(lst, dataframe):
#  for i in lst:

time_start = time.time()

jieba.load_userdict('词典.txt')

data = pd.read_excel('缺陷数据（老系统中数据）.xlsx')



df = pd.DataFrame(columns = ['缺陷描述', '地点', '设备名称', '消缺情况'])
df_1 = data['缺陷描述']
df_2 = data['地点']
df_3 = data['设备名称']
df_4 = data['消缺情况']

def fenci(df, i):
    df_fenci = ("/".join(analyse.textrank(str(df[i]), topK = 10, withWeight = False, allowPOS = ('mq', 'nz', 'v', 'z', 'a', 'n', 'ns'))))
    return df_fenci

for i in range(data.iloc[:,0].size):
    df_11 = fenci(df_1, i)
    df_22 = fenci(df_2, i)
    df_33 = fenci(df_3, i)
    df_44 = fenci(df_4, i)
    df = df.append(pd.DataFrame({'缺陷描述':df_11, '地点':df_22, '设备名称':df_33, '消缺情况':df_44}, index =[i]))
    if i % 40 == 0:
        print('完成',i / data.iloc[:,0].size * 100, '%')
    
    

df.to_csv('缺陷数据分词.csv', index = True, sep = ',', na_rep ='nan')

    
#lines = data['缺陷描述']
#print (lines)
#for i in lines:
#    print(" ".join(analyse.textrank(i, topK = 10, withWeight = False, allowPOS = ('n', 'v'))))
#lst = {}

#for i in lines:
#    lst[i] = ("/".join(analyse.textrank(i, topK = 15, withWeight = False, allowPOS = ('n', 'v', 'a')))) 

#f = open('测试.txt','w')
#for key in lst:
#    print(key , ':', lst[key], '\n', file = f)
##    print(lst[key])
#f.close()

time_end = time.time()

print(time_end- time_start, 's')



