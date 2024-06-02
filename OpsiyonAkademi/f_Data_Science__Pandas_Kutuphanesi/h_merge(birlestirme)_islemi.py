import pandas as pd


df1 = pd.DataFrame({"kiracilar":["ali", "ahmet", "ayse", "oya"], "bloklar":["a", "b", "b", "c"]})
print(df1)
"""
  kiracilar bloklar
0       ali       a
1     ahmet       b
2      ayse       b
3       oya       c
"""

df2 = pd.DataFrame({"kiracilar":["ali", "ahmet", "ayse", "oya"], "tasinma":["2010", "2009", "2007", "2021"]})
print(df2)
"""
  kiracilar tasinma
0       ali    2010
1     ahmet    2009
2      ayse    2007
3       oya    2021
"""


# ONE TO ONE / BİREBİR BİRLESTİRME:
a = pd.merge(df1, df2)      # birleştirmeyi otomatik seçer.
print(a)
"""
  kiracilar bloklar tasinma
0       ali       a    2010
1     ahmet       b    2009
2      ayse       b    2007
3       oya       c    2021
"""

a = pd.merge(df1, df2, on="kiracilar")      # birleştirme "kiracilar" key değerlerine göre yapılsın.
print(a)
"""
  kiracilar bloklar tasinma
0       ali       a    2010
1     ahmet       b    2009
2      ayse       b    2007
3       oya       c    2021
"""





# MANY TO ONE / GENELDEN ÖZELE / ÇOKTAN AZA BİRLEŞTİRME:

df3 = pd.merge(df1, df2)
print(df3)
"""
  kiracilar bloklar tasinma
0       ali       a    2010
1     ahmet       b    2009
2      ayse       b    2007
3       oya       c    2021
"""

df4 = pd.DataFrame({"bloklar":["a", "b", "c"], "yoneticiler":["mehmet", "fatma", "rifat"]})
print(df4)
"""
  bloklar yoneticiler
0       a      mehmet
1       b       fatma
2       c       rifat
"""

b = pd.merge(df3, df4)
print(b)
"""
  kiracilar bloklar tasinma yoneticiler
0       ali       a    2010      mehmet
1     ahmet       b    2009       fatma
2      ayse       b    2007       fatma
3       oya       c    2021       rifat
"""






# MANY TO MANY / GENELDEN GENELE / ÇOKTAN ÇOKA BİRLEŞTİRME:

df5 = pd.DataFrame({"bloklar":["a", "a", "b", "b", "c", "c"], "aidatlar":["300", "295", "290", "285", "280", "275"]})
print(df5)
"""
  bloklar aidatlar
0       a      300
1       a      295
2       b      290
3       b      285
4       c      280
5       c      275
"""

c = pd.merge(df1, df5)
print(c)
"""
  kiracilar bloklar aidatlar
0       ali       a      300
1       ali       a      295
2     ahmet       b      290
3     ahmet       b      285
4      ayse       b      290
5      ayse       b      285
6       oya       c      280
7       oya       c      275
"""