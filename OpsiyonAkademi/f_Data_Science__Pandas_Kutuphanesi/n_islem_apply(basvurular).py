import pandas as pd
import numpy as np

df = pd.DataFrame({'aileler':['a','b','c','a','b','c'],
                   'yas':[10,25,64,13,72,44],
                   'para':[53,261,355,488,153,611]},
                   columns=['aileler', 'yas', 'para'])
print(df)
"""
  aileler  yas  para
0       a   10    53
1       b   25   261
2       c   64   355
3       a   13   488
4       b   72   153
5       c   44   611
"""

# VERİLERİN TOPLANMASI:

a = df.apply(np.sum)
print(a)
"""
aileler    abcabc
yas           228
para         1921
dtype: object
"""


a = df.groupby('aileler').apply(np.sum)
print(a)
"""
        aileler  yas  para
aileler
a            aa   23   541
b            bb   97   414
c            cc  108   966
"""


# VERİLERİN ORTALAMASI:

a = df.groupby('aileler').apply(np.mean)
print(a)
"""
aileler
a    141.00
b    127.75
c    268.50
dtype: float64
"""

