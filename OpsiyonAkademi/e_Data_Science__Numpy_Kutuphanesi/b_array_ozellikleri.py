# ndim: boyut sayisini belirtir.
# shape: boyut bilgisi
# size: toplam eleman sayisi
# dtype: array veri tipi

import numpy as np

a = np.random.randint(15, size=10)
print(a)                                    # [ 6  8  7  0  5  8  9  7 10  4]
print(a.ndim)                               # 1 ==> 1 boyutlu olduğu için
print(a.shape)                              # (10,) ==> boyutunu verir.
print(a.size)                               # 10 ==> eleman sayisini verir.???
print(a.dtype)                              # int32 ==> veri tipini verir.





a = np.random.randint(6, 36, (5,6))
print(a)
"""
[[21 26 10  7 33 13]
 [28 20 25 28 23 25]
 [10 25 32 19 10 26]
 [ 7 17  9 14  8 24]
 [20 12 23 18 13 24]]
 """
print(a.ndim)                               # 2 ==> 2 boyutlu olduğu için
print(a.shape)                              # (5, 6) ==> boyutunu verir.
print(a.size)                               # 30 ==> eleman sayisini verir.???
print(a.dtype)                              # int32 ==> veri tipini verir.