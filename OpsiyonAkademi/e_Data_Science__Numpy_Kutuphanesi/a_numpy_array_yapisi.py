# Tek boyut: Vektor
# Iki boyut: Matris


import numpy as np

a = np.array([1,2,3,4,5])
print(a)
print(type(a))


b = np.array([3.14,6.11,18])
print(b)
print(type(b))

c = np.array([3.14,6.11,18], dtype="int")
print(c)
print(type(c))



# Sifirdan veri olusturma:

a = np.zeros(10)                    # Bu sekilde verileri float olarak cikariyor.
print(a)                            # a = [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

a = np.zeros(10, dtype="int")       # Bu sekilde verileri integera cevirebiliyoruz.
print(a)                            # a = [0 0 0 0 0 0 0 0 0 0]

a = np.ones((5,6))                  # Bu sekilde verileri float olarak ve (i,j) ==> i: satir sayisi, j: sutun sayisi
print(a)                            
"""
[[1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]] """
                                             
a = np.ones((5,6), dtype=int)       # Bu sekilde verileri integera cevirebiliyoruz ve (i,j) ==> i: satir sayisi, j: sutun sayisi
print(a)                            

"""
[[1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]] """


a = np.full((3,4), 6)               # Bu sekilde verilerinin tamami 6 (integer) dan olusan 3 satir ve 4 sutunluk matris olusturur.
print(a)
"""
[[6 6 6 6]
 [6 6 6 6]
 [6 6 6 6]]
"""
a = np.full((3,4), 6.0)               # Bu sekilde verilerinin tamami 6.0 (float) dan olusan 3 satir ve 4 sutunluk matris olusturur.
print(a)
"""
[[6. 6. 6. 6.]
 [6. 6. 6. 6.]
 [6. 6. 6. 6.]]
"""

a = np.full((3,4), 3.14)               # Bu sekilde verilerinin tamami 3.14 (float) dan olusan 3 satir ve 4 sutunluk matris olusturur.
print(a)
"""
[[3.14 3.14 3.14 3.14]
 [3.14 3.14 3.14 3.14]
 [3.14 3.14 3.14 3.14]]
"""

a = np.arange(0, 52, 5)                 # 0 dan baslayan 52 ye kadar(52 dahil degil) 5er 5er artan sayilarin dizisini verir.
print(a)                                # [ 0  5 10 15 20 25 30 35 40 45 50]

a = np.arange(0, 33, 3)                 # 0 dan baslayan 33 e kadar(33 dahil degil) 3er 3er artan sayilarin dizisini verir.
print(a)                                # [ 0  3  6  9 12 15 18 21 24 27 30]


a = np.linspace(0, 1, 10)               # 0 ile 1 arasinda 10 adet sayi uretir. ((i, j, k) ==> i: baslangic, j: bitis, k: miktar)
print(a)                                # [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.        ]

a = np.random.normal(10, 4, (3,4))      # Aritmetik ortalamasi 10, standart sapmasi 4 olan 3 satir 4 sutunluk bir iki boyutlu dagilim matrisi uretir.
print(a)
"""
[[11.95722382  9.66750734  6.89676501  7.11780411]
 [ 1.40155622  8.8514368   8.78054299 10.61860452]
 [13.43744468  6.13059851 10.54352615 20.37175567]]
"""

a = np.random.randint(0,15,(4,4))       # Sifir ile onbes arasinda 4x4 luk bir rasgele dagilmis bir integer veri tipinde matris uretilir.
print(a)
"""
[[ 3  4 13  7]
 [10  1  2  4]
 [ 1  3  3 12]
 [ 1  5 11  2]]
"""