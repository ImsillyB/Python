# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:16:06 2018

@author: 梓鑫
"""

import pandas as pd
import numpy as np
import os

#trainFile = u'D:/汪梓鑫/毕业设计/现有资料/4数据/csv格式数据文件/电流互感器总结紧急重大缺陷.csv'
#pwd = os.getcwd()
#os.chdir(os.path.dirname(trainFile))
#trainData = pd.read_csv(os.path.basename(trainFile), encoding ='gbk')
#os.chdir(pwd)


path = os.getcwd()+'\\2016年变电一次设备缺陷汇总-截止10月23日.csv'
f = open(path)
data = pd.read_csv(f)
print(data.head())
