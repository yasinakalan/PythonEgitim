# Arrayleri ayirmak icin kullanilir. Kelime anlami ayirmaktir.

# Array Ayirma = np.split(x, [a, b]) --> x bolunecek arrayi, a ve b bolunme indekslerini temsil eder.
# n kadar bolunme indisi, n+1 adet array olusturur. (Ornegin: Bir cubugu 2 ye bolersek, 3 parca olusur.)


import numpy as np




# BIR BOYUTLU ARRAY LERIN BOLUNMESI:
x = np.array([12,52,41,33,66,78,83,91])

y = np.split(x, [3,5])              # 3, 5 ==> 3 ve 5 indistir. (Index degildir.)
print(y)                            # [array([12, 52, 41]), array([33, 66]), array([78, 83, 91])]


a, b, c = np.split(x, [3,5])        # 3, 5 ==> 3 ve 5 indistir. (Index degildir.)
print("a: ", a)                     # a:  [12 52 41]
print("b: ", b)                     # b:  [33 66]   
print("c: ", c)                     # c:  [78 83 91]




# IKI BOYUTLU ARRAY LERIN BOLUNMESI:
d = 4                               # Burada indis secimi f dikkate alinarak yapilmalidir. Satır sayısı
e = 4                               # Burada indis secimi f dikkate alinarak yapilmalidir. Sütun sayısı
f = d * e                           # f sayisi d ve e indisli matrisi olusturamayacak bir deger olursa hata verir.

g = np.arange(f).reshape(d, e)      # Ikı boyutlu bir matris (array) elde edildi.
print(g)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
"""


# SATIR DAN BOLME: vsplit ==> vertical split
bol_1 = np.vsplit(g, [2])
print(bol_1)
"""
[array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
                              [12, 13, 14, 15]])]
"""

bol_1, bol_2 = np.vsplit(g, [2])
print("bol_1: ", bol_1)
print("bol_2: ", bol_2)
"""
bol_1:  
[[0 1 2 3]
 [4 5 6 7]]

bol_2:  
[[ 8  9 10 11]
 [12 13 14 15]]
"""

# SUTUN DAN BOLME: hsplit ==> horizontal split
bol_1 = np.hsplit(g, [2])
print(bol_1)
"""
[array([[ 0,  1],
        [ 4,  5],
        [ 8,  9],
        [12, 13]]), array([[ 2,  3],
                          [ 6,  7],
                          [10, 11],
                          [14, 15]])]
"""

bol_1, bol_2 = np.hsplit(g, [2])
print("bol_1: ", bol_1)
print("bol_2: ", bol_2)
"""
bol_1:  
[[ 0  1]
 [ 4  5]
 [ 8  9]
 [12 13]]
bol_2:  
[[ 2  3]
 [ 6  7]
 [10 11]
 [14 15]]
"""