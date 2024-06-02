# pandas ile olusturulan seriler index bilgisi ile gelir.
# numpy ile pandas serileri arasindaki tek fark pandas indexler ile birlikte degerleri cikti olarak dondurur, numpy ise sadece degerleri cikti olarak dondurur.

import pandas as pd

a = pd.Series([1,2,3,4,5,6,7,8,9])
print(a)
"""
Burada 1. sutun index bilgisi, 2. sutunlar degerlerdir. En altta ise seri tipi integer64 olarak gosterilmistir.
0    1
1    2
2    3
3    4
4    5
5    6
6    7
7    8
8    9
dtype: int64
"""
print(type(a))          # <class 'pandas.core.series.Series'>
# yapisal bilgilere erisilebilir:
print(a.axes)           # [RangeIndex(start=0, stop=9, step=1)]
# dtype ina bakilabilir:
print(a.dtype)          # int64
# size bilgisine erisilebilir:
print(a.size)           # 9
# boyut bilgisine ulasilabilir:
print(a.ndim)           # 1
# sadece degerlere ulasilabilir (index bilgisini vermez):
print(a.values)         # [1 2 3 4 5 6 7 8 9]
# mesela ilk 5 eleman ve indexlerine ulasilabilir:
print(a.head(5))
"""0    1
1    2
2    3
3    4
4    5
dtype: int64
"""
# son 4 elemana ve indeklerine ulasilabilir:
print(a.tail(4))
"""5    6
6    7
7    8
8    9
dtype: int64
"""


b = pd.Series([66,77,21,45,92,35,48])
print(b)
"""
Burada 1. sutun index bilgisi, 2. sutunlar degerlerdir. En altta ise seri tipi integer64 olarak gosterilmistir.
0    66
1    77
2    21
3    45
4    92
5    35
6    48
dtype: int64
"""
print(type(b))          # <class 'pandas.core.series.Series'>
# yapisal bilgilere erisilebilir:
print(b.axes)           # [RangeIndex(start=0, stop=7, step=1)]
# dtype ina bakilabilir:
print(b.dtype)          # int64
# size bilgisine erisilebilir.
print(b.size)           # 7
# boyut bilgisine ulasilabilir:
print(b.ndim)           # 1
# sadece degerlere ulasilabilir (index bilgisini vermez):
print(b.values)         # [66 77 21 45 92 35 48]
# mesela ilk 5 eleman ve indexlerine ulasilabilir:
print(b.head(5))
"""
0    66
1    77
2    21
3    45
4    92
dtype: int64
"""
# son 4 elemana ve indeklerine ulasilabilir:
print(b.tail(4))
"""
3    45
4    92
5    35
6    48
dtype: int64
"""








# Sozlukler ile de pandas dizileri olusturulabilir (Indexlerin adlandirilmasi gibi de dusunulebilir):
sozluk = {"ali":1, "ayse":2, "oya":3, "ahemt":4}
print("sozluk: ", sozluk)
c = pd.Series(sozluk)
print(c)
"""
sozluk:  {'ali': 1, 'ayse': 2, 'oya': 3, 'ahemt': 4}

Bir sozluk verildiginde keyleri index ve degerleri de value olarak alir. 
NOT: Buradan da anlasilabilecegi gibi indexlerde adlandirilabilir.

ali      1
ayse     2
oya      3
ahemt    4
dtype: int64
"""

# Index adlandirmasi icin farkli bir yontem:
d = pd.Series([66,77,21,45], index=["sifir: ", 1, "iki", "uc"])
print(d)
"""
sifir:     66
1          77
iki        21
uc         45
dtype: int64
"""



index_listesi = ["sifir: ", 1, "iki", "uc"]
e = pd.Series([66,77,21,45], index=index_listesi)
print(e)
"""
sifir:     66
1          77
iki        21
uc         45
dtype: int64
"""

# Indexe ulasma ve belirli araliktaki indexlere ulasma:
index_listesi = ["sifir: ", 1, "iki", "uc"]
f = pd.Series([66,77,21,45], index=index_listesi)
print(f)
"""
sifir:     66
1          77
iki        21
uc         45
dtype: int64
"""
print(f["iki"])         # 21
print(f[1:"iki"])
"""
1      77
iki    21
dtype: int64
"""


# Seriler birlestirilebilir:
sozluk = {"ali":1, "ayse":2, "oya":3, "ahemt":4}
g = pd.Series(sozluk)
print(g)
"""
ali      1
ayse     2
oya      3
ahemt    4
dtype: int64
"""

h = pd.concat([g,g,g])    # Serilerin birlestirme islemidir.
print(h)
"""
ali      1
ayse     2
oya      3
ahemt    4
ali      1
ayse     2
oya      3
ahemt    4
ali      1
ayse     2
oya      3
ahemt    4
dtype: int64
"""