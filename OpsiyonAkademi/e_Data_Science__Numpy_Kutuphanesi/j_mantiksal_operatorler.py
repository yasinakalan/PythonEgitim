# Mantiksal sinamalar

import numpy as np

a = np.arange(0,30,3)
print(a)
print(a > 6)
print(a < 13)


print(a[a>3])       # fancy metodu: 3 den buyuk olan indexleri yazdirir. Yani a > 3 icin True olan indexlerin degerlerini yazdirir. False olanlari yazdirmaz.
print(a[a<13])      # fancy metodu: 13 den kucuk olan indexleri yazdirir. Yani a < 13 icin True olan indexlerin degerlerini yazdirir. False olanlari yazdirmaz.
print(a[a<=15])      # fancy metodu: 15 den kucuk veya esit olan indexleri yazdirir. Yani a <= 13 icin True olan indexlerin degerlerini yazdirir. False olanlari yazdirmaz.
print(a[a>=15])
print(a[a==15])
print(a[a!=15])