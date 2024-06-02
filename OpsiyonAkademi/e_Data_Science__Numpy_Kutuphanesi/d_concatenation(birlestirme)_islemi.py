# Arrayleri birlestirmek icin kullanilir. Kelime anlami birlestirmektir.

# Parantez icinde koseli parantez kullaniminin sebebi; skalar arrayler cevrilebilir, skalar olmayanlar cevrilemez.

import numpy as np


# BIR BOYUTLU ARRAYLERDE BIRLESTIRME ISLEMI:
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([7,8,9])


c = np.concatenate([x, y])      # [1 2 3 4 5 6]
print(c)

# c = np.concatenate(x, y)        # Parantez icinde koseli parantez kullaniminin sebebi; skalar arrayler cevrilebilir, skalar olmayanlar cevrilemez.
print(c)

c = np.concatenate([c, z])
print(c)

c = np.concatenate([x, y, z])
print(c)




# IKI BOYUTLU ARRAYLERDE BIRLESTIRME ISLEMI:
a = np.array([[1,2,3], 
              [4,5,6]])
print(a)
b = np.concatenate([a, a])
print(b)
"""
Birlestirme islemi satir olarak yapildi.
[[1 2 3]
 [4 5 6]
 [1 2 3]
 [4 5 6]]
"""


a = np.array([[1,2,3], 
              [4,5,6]])
print(a)
b = np.concatenate([a, a], axis=0)          # axis=0 ifadesi satir bazinda birlestirme yapar.
print(b)
"""
Birlestirme islemi satir olarak yapildi.
[[1 2 3]
 [4 5 6]
 [1 2 3]
 [4 5 6]]
"""


a = np.array([[1,2,3], 
              [4,5,6]])
print(a)
b = np.concatenate([a, a], axis=1)          # axis=1 ifadesi sutun bazinda birlestirme yapar.
print(b)
"""
Birlestirme islemi sutun olarak yapildi.
[[1 2 3 1 2 3]
 [4 5 6 4 5 6]]
"""
