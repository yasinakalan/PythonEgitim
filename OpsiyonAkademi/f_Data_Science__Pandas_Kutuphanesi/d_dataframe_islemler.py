

import numpy as np
import pandas as pd

n1 = np.random.randint(10, size=5)
n2 = np.random.randint(10, size=5)
n3 = np.random.randint(10, size=5)


# NOT: Seriler random olusturuldugu icin veriler degisken olacaktir. Onemli olan sutun ve satir basliklariyla yapilan islemlerdir.

# Sozluk ile DataFrame islemleri:
sozluk = {"a" : n1, "b" : n2, "c" : n3}
print(sozluk)                               # {'a': array([1, 6, 0, 6, 7]), 'b': array([4, 0, 8, 1, 1]), 'c': array([8, 9, 1, 6, 8])}

pandas_seri = pd.DataFrame(sozluk)
print(pandas_seri)

"""
   a  b  c
0  1  4  8
1  6  0  9
2  0  8  1
3  6  1  6
4  7  1  8
"""
print(pandas_seri.index)                    # RangeIndex(start=0, stop=5, step=1)

# Indexte degisiklik yapma:
pandas_seri.index = ["q","w","e","r","t"]
print(pandas_seri)
"""
   a  b  c
q  3  3  7
w  1  4  4
e  6  9  6
r  0  6  2
t  8  4  1
"""

# Belirli bir araliktaki indexlere erisme:
print(pandas_seri["w":"r"])
"""
   a  b  c
w  0  0  9
e  0  2  7
r  8  3  2
"""

# Indexlerden bir satir silmek icin:
satir_silme = pandas_seri.drop("q", axis=0)             # ilk olarak silinmesi istenen index girilir. Ardindan axis = 0 veya axis = 1 ile satir-sutun secimi yapilir. Ayrica silme islemi hafiza da tutulmaz.
print(satir_silme)
"""
   a  b  c
w  7  5  7
e  7  1  7
r  2  3  2
t  6  9  1
"""
print(pandas_seri)                                      # Hafizada tutulmadigi icin silme islemi burada gorunmez.
"""
   a  b  c
q  5  8  5
w  2  3  4
e  6  5  5
r  8  3  2
t  3  4  3
"""
satir_silme = pandas_seri.drop("q", axis=0, inplace=True)     # inplace = True degeri verilirse silme islemi hafizada tutulur.
print(satir_silme)
"""
   a  b  c
w  1  0  1
e  8  6  1
r  5  9  9
t  9  7  3
"""

print(pandas_seri)                                      # Hafizada tutuldugu icin silme islemi artik seriye kaydedilmistir.
"""
   a  b  c
q  1  1  1
w  1  0  1
e  8  6  1
r  5  9  9
t  9  7  3
None
"""


# Fancy metodu ile disaridan degisken vererek silme islemini yapmak:
silinecek = ["w", "r"]                                  # "q" zaten az once silinmisti.
satir_silme = pandas_seri.drop(silinecek, axis=0, inplace=True)
print(pandas_seri)
"""
   a  b  c
e  9  3  6
t  9  7  0
"""


# Sorgulama yapmak:
print("a" in pandas_seri)           # True --> Burada sutun ismi ile sorgulama yapidi.


yeni_liste = ["a", "d", "c"]
for i in yeni_liste:
    print("{0}. sutun indexi seride mevcut mudur:".format(i), i in pandas_seri)
"""
a. sutun indexi seride mevcut mudur: True
d. sutun indexi seride mevcut mudur: False
c. sutun indexi seride mevcut mudur: True
"""



# indexlere ulasma:
print(pandas_seri["a"])
"""
e    9
t    4
Name: a, dtype: int32
"""



# index atama:
pandas_seri["d"] = np.array([1,2])
print(pandas_seri)
"""
   a  b  c  d
e  3  6  1  1
t  4  6  6  2
"""


# index atama (sifirdan):
sozluk = {"a" : n1, "b" : n2, "c" : n3}
print(sozluk)                               # {'a': array([2, 6, 3, 2, 4]), 'b': array([1, 6, 6, 3, 6]), 'c': array([7, 3, 1, 1, 6])}

pandas_seri = pd.DataFrame(sozluk)
print(pandas_seri)
"""
   a  b  c
0  2  1  7
1  6  6  3
2  3  6  1
3  2  3  1
4  4  6  6
"""

pandas_seri.index = ["q","w","e","r","t"]
print(pandas_seri)
"""
   a  b  c
q  2  1  7
w  6  6  3
e  3  6  1
r  2  3  1
t  4  6  6
"""

pandas_seri["d"] = np.array([1,2,3,4,5])
print(pandas_seri)
"""
   a  b  c  d
q  2  1  7  1
w  6  6  3  2
e  3  6  1  3
r  2  3  1  4
t  4  6  6  5
"""




# Indexlerden bir sutun silmek icin:
satir_silme = pandas_seri.drop("c", axis=1)             # ilk olarak silinmesi istenen index girilir. Ardindan axis = 0 veya axis = 1 ile satir-sutun secimi yapilir. Ayrica silme islemi hafiza da tutulmaz.
print(satir_silme)
"""
   a  b  d
q  3  0  1
w  3  1  2
e  6  6  3
r  4  3  4
t  5  3  5
"""
print(pandas_seri)                                      # Hafizada tutulmadigi icin silme islemi burada gorunmez.
"""
   a  b  c  d
q  3  0  7  1
w  3  1  3  2
e  6  6  5  3
r  4  3  6  4
t  5  3  4  5
"""
satir_silme = pandas_seri.drop("c", axis=1, inplace=True)     # inplace = True degeri verilirse silme islemi hafizada tutulur.
print(satir_silme)
"""
   a  b  d
q  3  0  1
w  3  1  2
e  6  6  3
r  4  3  4
t  5  3  5
"""

print(pandas_seri)                                      # Hafizada tutuldugu icin silme islemi artik seriye kaydedilmistir.
"""
   a  b  d
q  3  0  1
w  3  1  2
e  6  6  3
r  4  3  4
t  5  3  5
"""


# Fancy metodu ile disaridan degisken vererek silme islemini yapmak:
silinecek_sutun = ["a", "d"]                                  # "q" zaten az once silinmisti.
satir_silme = pandas_seri.drop(silinecek_sutun, axis=1, inplace=True)
print(pandas_seri)
"""
   b
q  5
w  3
e  4
r  4
t  9
"""
