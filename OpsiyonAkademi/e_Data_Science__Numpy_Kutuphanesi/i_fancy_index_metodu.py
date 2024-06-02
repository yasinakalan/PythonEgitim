# fancy index: index numaralarini degiskene atayarak bir liste olusturup, bu listeyi index olarak cekmeye calismaya fancy metodu denir.

import numpy as np

# BIR BOYUTLU ARRAY LERDE FANCY METODU:

a = np.arange(0,30,3)
print(a)
print(a[0])
print(a[3])

b = [a[0], a[3], a[6]]
print(b)

fancy = [0,3,6]
print(fancy)
print(a[fancy])






# IKI BOYUTLU ARRAY LERDE FANCY METODU:

a = np.arange(9).reshape(3,3)
print(a)

satir = np.array([0,1])
sutun = np.array([1,2])
print(a[satir, sutun])




a = np.arange(9).reshape(3,3)
print(a)

satir = np.array([0,1])
sutun = np.array([1,2])
print(a[0, sutun])      # basit index ile




a = np.arange(9).reshape(3,3)
print(a)

satir = np.array([0,1])
sutun = np.array([1,2])
print(a[0:,sutun])      # slice ile belirli araliktaki indexlere ulasilabilir.




a = np.arange(9).reshape(3,3)
print(a)

satir = np.array([0,1])
sutun = np.array([1,2])
print(a[0:1])           # slice ile belirli araliktaki indexlere ulasilabilir.
