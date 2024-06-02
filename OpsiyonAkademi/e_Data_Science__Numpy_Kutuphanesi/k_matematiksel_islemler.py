# Matematiksel islemler:
# Bir boyutlu array ler bir vektor belirtir. Vektorlerde yapilabilen matematiksel islemler bir boyutlu array lerde de gecerlidir.

# ufunc metodu ile numpy kutuphanesini kullanarak matematiksel islemler.


import numpy as np


# BIR BOYUTLU ARRAY LERDE MATEMATIKSEL ISLEMLER:
a = np.array([1,2,3,4,5,6,7,8,9])
print(a)

toplam = a + 5
cikarma = a - 3
bolme = a / 4
carpma = a * 5
kalan = a %2        # 2 ile bolumunden kalan
us_alma = a ** 3
karekok_alma = a ** (3/8)


print("toplam       : ", toplam)
print("cikarma      : ", cikarma)
print("bolme        : ", bolme)
print("carpma       : ", carpma)
print("kalan        : ", kalan)
print("us_alma      : ", us_alma)
print("karekok alma : ", karekok_alma)

"""
toplam       :  [ 6  7  8  9 10 11 12 13 14]
cikarma      :  [-2 -1  0  1  2  3  4  5  6]
bolme        :  [0.25 0.5  0.75 1.   1.25 1.5  1.75 2.   2.25]
carpma       :  [ 5 10 15 20 25 30 35 40 45]
kalan        :  [1 0 1 0 1 0 1 0 1]
us_alma      :  [  1   8  27  64 125 216 343 512 729]
karekok alma :  [1.         1.29683955 1.50980365 1.68179283 1.8285791  1.95797309 2.074492   2.18101547 2.27950706]
"""




# ufunc metodu ile numpy kutuphanesini kullanarak matematiksel islemler:
toplam = np.add(a, 5)
cikarma = np.subtract(a, 3)
bolme = np.divide(a, 4)
carpma = np.multiply(a, 5)
kalan = np.mod(a, 2)
us_alma = np.power(a, 3)
karekok_alma = np.power(a, (3/8))


print("toplam       : ", toplam)
print("cikarma      : ", cikarma)
print("bolme        : ", bolme)
print("carpma       : ", carpma)
print("kalan        : ", kalan)
print("us_alma      : ", us_alma)
print("karekok alma : ", karekok_alma)

"""
toplam       :  [ 6  7  8  9 10 11 12 13 14]
cikarma      :  [-2 -1  0  1  2  3  4  5  6]
bolme        :  [0.25 0.5  0.75 1.   1.25 1.5  1.75 2.   2.25]
carpma       :  [ 5 10 15 20 25 30 35 40 45]
kalan        :  [1 0 1 0 1 0 1 0 1]
us_alma      :  [  1   8  27  64 125 216 343 512 729]
karekok alma :  [1.         1.29683955 1.50980365 1.68179283 1.8285791  1.95797309 2.074492   2.18101547 2.27950706]
"""

# Diger bazi islemler:

# mutlak deger, sinus, cosinus:
mutlak = np.absolute(np.array([-9]))
sinus = np.sin(360)
cosinus = np.cos(180)
logaritma = np.log(a)
log_tabanli = np.log2(a)        # 2 tabaninda logaritma

print("mutlak       : ", mutlak)
print("sinus        : ", sinus)
print("cosinus      : ", cosinus)
print("logaritma    : ", logaritma)
print("log_tabanli  : ", log_tabanli)

"""
mutlak       :  [9]
sinus        :  0.9589157234143065
cosinus      :  -0.5984600690578581
logaritma    :  [0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947 1.94591015 2.07944154 2.19722458]
log_tabanli  :  [0.         1.         1.5849625  2.         2.32192809 2.5849625 2.80735492 3.         3.169925  ]
"""