# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index = dates, columns = ['A','B','C','D'])

##print (df.A, df['A'])
##print (df[0:3], df['20130101':'20130103'])

#select by label: loc
#print (df.loc['20130102'])
#print (df.loc[:,['A','B']])

#select by position:iloc
#print (df.iloc[3,2])

#mixed selection:ix
#print (df.ix[3, ['A']])

#Boolean indexing
#print (df[df.A > 8])

#设置值

df.iloc[3,3] = 1111
df.loc['20130102','C'] = 232
df.B[df.A > 8] = 4
df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6],index = pd.date_range('20130101', periods = 6))
print (df)