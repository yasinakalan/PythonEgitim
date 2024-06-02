# Sorting islemi: Array siralama

import numpy as np


# BIR BOYUTLU ARRAY LERDE SORTING ISLEMI:
a = np.array([2,6,9,4,3,1,7,8,5])
print(a)                                # [2 6 9 4 3 1 7 8 5]

b = np.sort(a)                          # Bu sekilde a.sort() kullaniminda a nin orjinal yapisini bozmaz.
print(b)                                # [1 2 3 4 5 6 7 8 9]
print(a)                                # [2 6 9 4 3 1 7 8 5]   ==> Bu sekilde a.sort() kullaniminda a nin orjinal yapisini bozmaz o yuzden bu kullanim daha guvenlidir.

c = a.sort()                            # Bu sekilde a.sort() kullaniminda a nin orjinal yapisini bozar.
print(c)                                # None
print(a)                                # [1 2 3 4 5 6 7 8 9]   ==> Bu sekilde a.sort() kullaniminda a nin orjinal yapisini bozar.



# IKI BOYUTLU ARRAY LERDE SORTING ISLEMI:
d = np.random.normal(20, 5, (3,3))
print(d)
"""
[[23.05344065 20.84374988 11.94743351]
 [25.25096996 15.80515712 19.68149369]
 [20.43369363 23.11891414 14.07560312]]
 """

e = np.sort(d, axis=0)                  # Sutun bazinda siralama yapar.
f = np.sort(d, axis=1)                  # Satir bazinda siralama yapar.

print("e: ", e)
"""
e:  
[[20.43369363 15.80515712 11.94743351]
 [23.05344065 20.84374988 14.07560312]
 [25.25096996 23.11891414 19.68149369]]
 """

print("f: ", f)
"""
f:  
[[11.94743351 20.84374988 23.05344065]
 [15.80515712 19.68149369 25.25096996]
 [14.07560312 20.43369363 23.11891414]]
 """