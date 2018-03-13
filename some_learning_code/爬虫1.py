# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:21:20 2018

@author: 梓鑫
"""

import requests


def get_province_entry(url):
    content = requests.get(url).content.decode('gb2312')
    print(content)
    start = content.find('<map name=\"map_86\" id=\"map86\">')
    end = content.find('</map>')
    print(start, end)
    content = content[start:end + len('</map>')].strip()
    print(content)
    
provinces = get_province_entry('http://www.ip138.com/post')
print(provinces)