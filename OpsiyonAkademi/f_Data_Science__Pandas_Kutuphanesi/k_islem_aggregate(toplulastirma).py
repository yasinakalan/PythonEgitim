# VIDEONUN 2:14. DAKİKASINDA UDEMY EĞİTİMİNİN ALINNDIĞI LİNK MEVCUTTUR.


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

a = df.groupby('aileler').mean()
print(a)
"""
aileler
a        11.5  270.5
b        48.5  207.0
c        54.0  483.0
"""


a = df.groupby('aileler').aggregate(['min', np.median, max])        # min ve max pandas içinden, median ise numpy içerisinden çekilen fonksiyonlardır.
print(a)
"""
        yas            para
        min median max  min median  max
aileler
a        10   11.5  13   53  270.5  488
b        25   48.5  72  153  207.0  261
c        44   54.0  64  355  483.0  611
"""


a = df.groupby('aileler').aggregate({'yas':[min,'max'], 'para':'max'})
print(a)
"""
        yas     para
        min max  max
aileler
a        10  13  488
b        25  72  261
c        44  64  611
"""