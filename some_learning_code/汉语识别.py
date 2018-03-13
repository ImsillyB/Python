# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:54:46 2018

@author: 梓鑫
"""
##关键词提取
import jieba.analyse as analyse

list = open('地形图.txt').read()
print(" ".join(analyse.textrank(list, topK = 20, withWeight = False, allowPOS = ('ns', 'n', 'vn', 'v'))))
print("----------------")
print(" ".join(analyse.textrank(list, topK = 20, withWeight = False, allowPOS = ('ns', 'n'))))

import jieba.posseg as pseg
words = pseg.cut(list)
for word, flag in words:
    print('%s %s' %(word, flag))


##并行程序
#import sys
#import time
#import jieba
#
#jieba.enable_parallel()
#content = open(u'地形图.txt', "r").read（）
#t1 = time.time()
#words = "/".join(jieba.cut(content))
#t2 = time.time()
#tm_cost = t2 - t1
#print('并行分词速度为 %s bytes/second' % (len(content)/tm_cost))
#
#jieba.disable_parallel()
#content = open(u'地形图.txt', "r").read（）
#t1 = time.time()
#words = "/".join(jieba.cut(content))
#t2 = time.time()
#tm_cost = t2 - t1
#print('非并行分词速度为%s bytes/second' % (len(content)/tm_cost))

