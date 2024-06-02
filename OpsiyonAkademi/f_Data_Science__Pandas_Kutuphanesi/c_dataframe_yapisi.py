# Excel veri tipine benzerler.

# numpy sabit tipli veriler için daha yaygın kullanılır.
# pandas ise değişken tipli veriler için daha kullanışlıdır.

import pandas as pd
import numpy as np


liste = [10,20,30,40,50,60,70,80]
dizi = np.arange(1,10).reshape((3,3))

a = pd.DataFrame(liste, columns=["ilk dataframe"])
print(a)
"""
   ilk dataframe
0             10
1             20
2             30
3             40
4             50
5             60
6             70
7             80
"""
print(dizi)
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 """


# DataFrame icerisine numpy dizisi gondermek:
a = pd.DataFrame(dizi, columns=["ilk","ikinci","ucuncu"])
print(a)
"""
   ilk  ikinci  ucuncu
0    1       2       3
1    4       5       6
2    7       8       9
"""


# Sutun isimlerini degistirme:
a.columns = ("first", "second", "third")            # Burada onemli olan isim degisikligi disaridan yapilacaksa koseli parantez yerine normal parantez kullanilir.
print(a)
"""
   first  second  third
0      1       2      3
1      4       5      6
2      7       8      9
"""


# Bazi ozelliklere erisme:
print(type(a))              # <class 'pandas.core.frame.DataFrame'>
print(a.axes)               # [RangeIndex(start=0, stop=3, step=1), Index(['first', 'second', 'third'], dtype='object')]
print(a.shape)              # (3, 3)
print(a.ndim)               # 2 (2 boyutlu)
print(a.size)               # 9
print(a.values)             # values fonksiyonu bir donusum islemi yapar. type ina bakilmazsa degerleri gosterir.
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
print(type(a.values))       # <class 'numpy.ndarray'> (cekilen values degerler numpy array dizisi tipinde cikar bu yüzden donusum islemi yapilmis olur.)

# Donusum islemini liste uzerinde de incelemek:
liste = [10,20,30,40,50,60,70,80]

a = pd.DataFrame(liste, columns=["first df"])
print(a)
"""
   first df
0        10
1        20
2        30
3        40
4        50
5        60
6        70
7        80
"""
print(type(a.values))       # <class 'numpy.ndarray'> (cekilen values degerler numpy array dizisi tipinde cikar bu yüzden donusum islemi yapilmis olur.)
print(a.values)             # values fonksiyonu bir donusum islemi yapar. type ina bakilmazsa degerleri gosterir.
"""
[[10]
 [20]
 [30]
 [40]
 [50]
 [60]
 [70]
 [80]]
"""

