#  Array in kendi yapisinda degisiklikler olmadan alt kumelerde islem yapmayi ogrenecegiz.

import numpy as np


# DEGISIKLIK OLARAK:

a = np.random.randint(10, size=(5,5))
print("a: ", a)
"""
a:  [[2 4 0 8 2]
    [3 3 5 3 8]    
    [8 9 2 8 5]    
    [3 4 9 3 7]    
    [2 0 4 8 6]] 
 """

alt_kume_a = a[0:3, 0:2]
print(alt_kume_a)
"""
[[2 4]
 [3 3]
 [8 9]]
"""

alt_kume_a[0,0] = 1234
#alt_kume_a[1,2] = 4567      # alt_kume_a da 0:2 araliginda 2 olmadigindan index bulunamadi hatasi veriyor. Detayli bakilmali.
alt_kume_a[1,0] = 4567
print(alt_kume_a)
"""
[[1234    4]
 [4567    3]
 [   8    9]]
"""

print(a)                        # alt kume isleminden sonra a arrayinde degisiklik olmustur.
"""
[[1234    4    0    8    2]
 [4567    3    5    3    8]
 [   8    9    2    8    5]
 [   3    4    9    3    7]
 [   2    0    4    8    6]]
"""






# DEGISIKLIK OLMAYARAK:
a = np.random.randint(10, size=(5,5))
print("a: ", a)
"""
a:  [[2 0 9 2 3]
    [8 6 2 9 0]
    [1 5 1 5 7]
    [7 9 1 3 1]
    [0 6 9 2 9]] 
 """

alt_kume_a = a[0:3, 0:2].copy()             # copy() metodu uygulanirsa a arrayinde degisiklik olmaz.
print(alt_kume_a)
"""
[[2 0]
 [8 6]
 [1 5]]
"""

alt_kume_a[0,0] = 1234
#alt_kume_a[1,2] = 4567      # alt_kume_a da 0:2 araliginda 2 olmadigindan index bulunamadi hatasi veriyor. Detayli bakilmali.
alt_kume_a[1,0] = 4567
print(alt_kume_a)
"""
[[1234    0]
 [4567    6]
 [   1    5]]
"""

print(a)                        # copy() metodu uygulanarak alt kume islemlerinden sonra a arrayinde degisiklik olmamistir..
"""
[[2 0 9 2 3]
 [8 6 2 9 0]
 [1 5 1 5 7]
 [7 9 1 3 1]
 [0 6 9 2 9]]
"""
