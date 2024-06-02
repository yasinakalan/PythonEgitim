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

# ÖRNEK DONUSTURME:
print(df['yas']*10)
"""
0    100
1    250
2    640
3    130
4    720
5    440
Name: yas, dtype: int64
"""

# STRING İFADELERİN ILOC İLE ÇIKARILMASI:
a = df.iloc[:,1:3]
print(a)
"""
   yas  para
0   10    53
1   25   261
2   64   355
3   13   488
4   72   153
5   44   611
"""

# TEK SATIRLIK FONKSİYON İLE:
b = a.transform(lambda x: x - x.mean())
print(b)
"""
    yas        para
0 -28.0 -267.166667
1 -13.0  -59.166667
2  26.0   34.833333
3 -25.0  167.833333
4  34.0 -167.166667
5   6.0  290.833333
"""

# TEK SATIRLIK FONKSİYON İLE:
b = a.transform(lambda x: x - (x.mean())/x.std())
print(b)
"""
         yas        para
0   8.552525   51.462403
1  23.552525  259.462403
2  62.552525  353.462403
3  11.552525  486.462403
4  70.552525  151.462403
5  42.552525  609.462403
"""


# DIŞ FONKSİYON İLE:
def donustur(x):
    return x - (x.mean()/x.std())

b = a.transform(donustur)
print(b)
"""
         yas        para
0   8.552525   51.462403
1  23.552525  259.462403
2  62.552525  353.462403
3  11.552525  486.462403
4  70.552525  151.462403
5  42.552525  609.462403
"""