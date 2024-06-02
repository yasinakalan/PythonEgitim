# Rastgelelik

import random

a = random.random() # 0-1 arasında rastgele float bir sayı üretir.
print("a: ", a)

sayi1 = 1
sayi2 = 6
b = random.randint(sayi1, sayi2)    # sayi1 ile sayi2 arasında rastgele tamsayı üretir.
print("b: ", b)

torba = [1, 654, 1654, 6165, 31, 55, 8454, 321]
c = random.choice(torba)    # torba listesinden rastgele seçim yapar.
print("c: ", c)

print("Karıştırılmamış Torba: ", torba)
random.shuffle(torba)   # torba listesini karıştırır.
print("Karıştırılmış Torba  : ", torba)