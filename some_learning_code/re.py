# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:30:28 2018

@author: 梓鑫
"""

#import re
#
#p = re.compile(r'(\w+) (\w+)')
#s = 'i say, hello wangzixin!'
#
#print(p.sub(r'\2 \1', s))
#
#def func(m):
#    return m.group(1).title() + ' ' + m.group(2).title()
#
#print(p.sub(func, s))


import jieba
#
#seg_list = jieba.cut("我在学习自然语言处理", cut_all = True)
#print(seg_list)
#print("Full Mode: " + "/" .join(seg_list))
#
#seg_list = jieba.cut("我在学习自然语言处理", cut_all = False)
#print("Default Mode: " + "/" .join(seg_list))
#
#seg_list = jieba.cut("他毕业于上海交通大学，在百度深度学习研究院进行研究")
#print("," .join(seg_list))
#
#seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")
#print("," .join(seg_list))
#
#result_lcut = jieba.lcut("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")
#print(result_lcut)
#print(" ".join(result_lcut))
#
#print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM = False)))
#
#jieba.suggest_freq(('中','将'), True)
#print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM = False)))

import jieba.analyse as analyse
lines = open('地形图.txt').read()
print(" ".join(analyse.extract_tags(lines, topK = 5, withWeight = False, allowPOS = ())))

