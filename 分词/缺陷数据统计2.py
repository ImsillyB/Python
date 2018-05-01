# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 19:41:24 2018

@author: 梓鑫
"""


import sys, time
import pandas as pd
#import numpy as np
import jieba.analyse as analyse
import jieba


#def fen_ci(lst, dataframe):
#  for i in lst:

time_start = time.time()

jieba.load_userdict('词典.txt')

f = open('缺陷统计（新系统中数据）.csv')
data = pd.read_csv(f)



df = pd.DataFrame(columns = ['缺陷类型', '缺陷描述', '设备类别', '生产厂家'])
df2 = pd.DataFrame(columns = ['缺陷类型', '缺陷描述', '设备类别', '生产厂家'])
df_1 = data['缺陷类型']
df_2 = data['缺陷描述']
df_3 = data['设备类别']
df_4 = data['生产厂家']

class ShowProcess():
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    i = 0 # 当前的处理进度
    max_steps = 0 # 总共需要处理的次数
    max_arrow = 50 #进度条的长度

    # 初始化函数，需要知道总共的处理次数
    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.i = 0

    # 显示函数，根据当前的处理进度i显示进度
    # 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps) #计算显示多少个'>'
        num_line = self.max_arrow - num_arrow #计算显示多少个'-'
        percent = self.i * 100.0 / self.max_steps #计算完成进度，格式为xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' #带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(process_bar) #这两句打印字符到终端
        sys.stdout.flush()

    def close(self, words='done'):
        print ('')
        print (words)
        self.i = 0
        
        


def fenci(df, i):
    df_fenci = ("/".join(analyse.textrank(str(df[i]), topK = 10, withWeight = False, allowPOS = ('mq', 'nz', 'v', 'z', 'a', 'n', 'ns'))))
    return df_fenci

def fenci_2(df, i):
    df_fenci = ('/'.join(jieba.cut(str(df[i]))))
    return df_fenci

if __name__=='__main__':
    max_steps = data.iloc[:,0].size

    process_bar = ShowProcess(max_steps)

    for i in range(data.iloc[:,0].size):
        if i % 400 == 0:
            process_bar.show_process(i)        
        df_11 = fenci(df_1, i)
        df_21 = fenci(df_2, i)
        df_31 = fenci(df_3, i)
        df_41 = fenci(df_4, i)
        df_12 = fenci_2(df_1, i)
        df_22 = fenci_2(df_2, i)
        df_32 = fenci_2(df_3, i)
        df_42 = fenci_2(df_4, i)
        df = df.append(pd.DataFrame({'缺陷类型':df_11, '缺陷描述':df_21, '设备类别':df_31, '生产厂家':df_41}, index =[i]))
        df2 = df2.append(pd.DataFrame({'缺陷类型':df_12, '缺陷描述':df_22, '设备类别':df_32, '生产厂家':df_42}, index =[i]))

#            time.sleep(0.05)
    process_bar.close()


df.to_csv('缺陷数据关键词提取(new).csv', index = True, sep = ',', na_rep = 'NAN')
df2.to_csv('缺陷数据分词(new).csv', index = True, sep = ',', na_rep = 'NAN')

time_end = time.time()

print(time_end- time_start, 's')