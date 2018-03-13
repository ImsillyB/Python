# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:48:14 2018

@author: 梓鑫
"""

import re

def remove_noise(document):
    noise_pattern = re.compile("|".join(["http\s+", "\@\w+", "\#\w+"]))
    clean_text = re.sub(noise_pattern, "", document)
    return clean_text.strip()

remove_noise("Trrmp images are now more popular than cat gifs. @Trump #trends http://www.trumptrends.html")
            