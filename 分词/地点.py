# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:24:12 2018

@author: 梓鑫
"""

import pandas as pd
import jieba
import sys, time
import jieba.analyse as analyse
import re

time_start = time.time()

jieba.load_userdict('地名.txt')


f = open('结果.csv')
data = pd.read_csv(f)

df = pd.DataFrame(columns = ['供电局编码', '供电局名称地名', '数量'])
#df['供电局编码'] = data['供电局编码']
#df['数量'] = data['数量']
df_1 = data['供电局名称']
df_2 = data['供电局编码']
df_3 = data['数量']

pattern = re.compile(r'\d')
pattern2 = re.compile(r'\W')

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
       df_fenci = ('/'.join(jieba.cut(str(df[i]))))
       return df_fenci


if __name__=='__main__':
    max_steps = data.iloc[:,0].size

    process_bar = ShowProcess(max_steps)

    for i in range(data.iloc[:,0].size):
        if i % 400 == 0:
            process_bar.show_process(i)  
            
        if df_1[i] == '110kV':
            df_1[i] = 'nan'
        df_11 = fenci(df_1, i)
        df_12 = df_11.split('/')
        match = pattern.match(df_12[0])
        if match:
            df = df.append(pd.DataFrame({'供电局名称地名':df_12[1], '供电局编码':df_2[i], '数量':df_3[i]}, index =[i]))
        else:
            df = df.append(pd.DataFrame({'供电局名称地名':df_12[0], '供电局编码':df_2[i], '数量':df_3[i]}, index =[i]))

#            time.sleep(0.05)
    process_bar.close()
df.to_csv('地点提取.csv', index = True, sep = ',', na_rep = 'NAN')

time_end = time.time()

print(time_end- time_start, 's')