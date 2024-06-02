import pandas as pd

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

a = df.groupby('aileler').filter(lambda x: x['yas'].mean() > 30)        # aileler den yaşların ortalaması 30 dan büyük olanları filtreler.
print(a)
"""
  aileler  yas  para
1       b   25   261
2       c   64   355
4       b   72   153
5       c   44   611
"""

b = df.groupby('aileler').mean()
print(b)
"""
          yas   para
aileler
a        11.5  270.5
b        48.5  207.0
c        54.0  483.0
"""


a = df.groupby('aileler').filter(lambda x: x['para'].std() > 100)       # aileler den paraların standart sapması 100 den büyük olanları filtreler.
print(a)
"""
  aileler  yas  para
0       a   10    53
2       c   64   355
3       a   13   488
5       c   44   611
"""