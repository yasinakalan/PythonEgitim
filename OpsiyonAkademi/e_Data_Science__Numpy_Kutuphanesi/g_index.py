# Index ile elemanlara nasil erisilebilir gosterilecek.

import numpy as np

a = np.random.randint(10, size=10)
a = np.array([1,0,8,2,3,6,5,2,5,7])


# BIR BOYUTLU ARRAY LERDE INDEX ISLEMLERI:
# Indexe ulasma:
print("a     : ", a)
print("a[0]  : ", a[0])
print("a[1]  : ", a[1])
print("a[2]  : ", a[2])
print("a[3]  : ", a[3])
print("a[4]  : ", a[4])
print("a[5]  : ", a[5])
print("a[6]  : ", a[6])
print("a[7]  : ", a[7])
print("a[8]  : ", a[8])
print("a[9]  : ", a[9])

print("a[-1] : ", a[-1])
print("a[-2] : ", a[-2])
print("a[-3] : ", a[-3])
print("a[-4] : ", a[-4])



"""
a    :  [1 0 8 2 3 6 5 2 5 7]
a[0]  :  1
a[1]  :  0
a[2]  :  8
a[3]  :  2
a[4]  :  3
a[5]  :  6
a[6]  :  5
a[7]  :  2
a[8]  :  5
a[9]  :  7
a[-1] :  7
a[-2] :  5
a[-3] :  2
a[-4] :  5

"""


# Indexe yeni deger atama:

a[0] = 31

print("a     : ", a)
print("a[0]  : ", a[0])
print("a[1]  : ", a[1])
print("a[2]  : ", a[2])
print("a[3]  : ", a[3])
print("a[4]  : ", a[4])
print("a[5]  : ", a[5])
print("a[6]  : ", a[6])
print("a[7]  : ", a[7])
print("a[8]  : ", a[8])
print("a[9]  : ", a[9])

print("a[-1] : ", a[-1])
print("a[-2] : ", a[-2])
print("a[-3] : ", a[-3])
print("a[-4] : ", a[-4])



"""
a    :  [31 0 8 2 3 6 5 2 5 7]
a[0]  :  31
a[1]  :  0
a[2]  :  8
a[3]  :  2
a[4]  :  3
a[5]  :  6
a[6]  :  5
a[7]  :  2
a[8]  :  5
a[9]  :  7
a[-1] :  7
a[-2] :  5
a[-3] :  2
a[-4] :  5

"""








# IKI BOYUTLU ARRAY LERDE INDEX ISLEMLERI:
# Indexe ulasma:

a = np.random.randint(10, size=(3,5))
#a = np.array([1,0,8,2,3,6,5,2,5,7])


print("a        : ", a)
print("a[0,0]   : ", a[0,0])
print("a[1,1]   : ", a[1,1])
print("a[2,4]   : ", a[2,4])


print("a[-1,3]  : ", a[-1,3] )
print("a[-2,0]  : ", a[-2,0] )
print("a[2,-2]  : ", a[2,-2] )
print("a[-2,-1] : ", a[-2,-1])



"""
a        :  
[[5 1 3 8 2]
 [9 4 5 1 4]
 [3 2 2 9 8]]
 
a[0,0]   :  5
a[1,1]   :  4
a[2,4]   :  8
a[-1,3]  :  9
a[-2,0]  :  9
a[2,-2]  :  9
a[-2,-1] :  4

"""

# Indexe yeni deger atama:

a[-1,3] = 31

print("a        : ", a)
print("a[0,0]   : ", a[0,0])
print("a[1,1]   : ", a[1,1])
print("a[2,4]   : ", a[2,4])


print("a[-1,3]  : ", a[-1,3] )
print("a[-2,0]  : ", a[-2,0] )
print("a[2,-2]  : ", a[2,-2] )
print("a[-2,-1] : ", a[-2,-1])

"""
a        :  
[[ 5  1  3  8  2]
 [ 9  4  5  1  4]
 [ 3  2  2 31  8]]

a[0,0]   :  5
a[1,1]   :  4
a[2,4]   :  8
a[-1,3]  :  31
a[-2,0]  :  9
a[2,-2]  :  31
a[-2,-1] :  4

"""