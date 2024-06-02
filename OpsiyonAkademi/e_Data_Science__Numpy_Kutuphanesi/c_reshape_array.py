# reshape: yeniden sekillendirme, yeniden boyutlandirma
# Bazen verisetlerinde verilerde bazi duzenlemeler yapmak gerekiyor. Tek boyutluyu Iki boyutluya donusturmek gibi vs. bu ve benzeri isler icin reshape kullanilir.

import numpy as np

# a = np.arange(0,10)
# print(a)                    # [0 1 2 3 4 5 6 7 8 9]

# b = a.reshape((3,3))        # a dizisinin uzunlugu 10 oldugundan 3,3 bir matris olusturulamaz. Hata almamak icin size a uygun bir donusum secilmelidir.
# print(b)



a = np.arange(0,9)
print(a)                    # [0 1 2 3 4 5 6 7 8]

b = a.reshape((3,3))
print(b)
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""



a = np.arange(0,9)
print(a)                    # [0 1 2 3 4 5 6 7 8]
print(a.ndim)               # 1 boyutlu
b = a.reshape((1,9))        # 1x9 dan 2 boyuta donusturulmus olundu.
print(b)                    # [[0 1 2 3 4 5 6 7 8]]
print(b.ndim)               # 2 boyutlu