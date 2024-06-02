"""
Terminalde karsilasilan bazi hatalar: (Farkli hatalar icin python kilavuzuna bakilabillir.)

ZeroDivisionError       : Sifira bolunme hatasi
AssertionError          : Bir ifadenin true ya da false oldugunu iddia ediyorsak, iddiamızın sonucu true cikarsa bu hatayi dondurur. Bir sonraki derste daha detayli anlatildi.
ModuleNotFoundError     : Modul bulunamadi hatasi mesela os yerine osd yazilirsa bu hatayi aliriz.
KeyboardInterrupt       : Sonsuz dongu yazildiginda donguden cikmak icin terminal ekraninda Ctrl + C yapildiginda dongu sonlanir ve bu hata ekrana yazdirilir. Dongu klavye ile sonlandirildi anlamina gelir.
IndexError              : Mesela bir liste icerisinde olmayan bir indexe ulasilmak istendiginde, bu hata cikar.
KeyError                : Sozluklerde tanimli olmayan bir key cagirildiginda bu hata cikar.
NameError               : Tanimlanmamis bir degisken cagirildiginda bu hata cikar.
SyntaxError             : Python formatinda yazim hatasi oldugunda bu hata cikar.

"""

"""
# ZeroDivisionError       : sifira bolunme hatasi
6/0

# ModuleNotFoundError     : Modul bulunamadi hatasi mesela os yerine osd yazilirsa bu hatayi aliriz.
import osd

# KeyboardInterrupt       : Sonsuz dongu yazildiginda donguden cikmak icin terminal ekraninda Ctrl + C yapildiginda dongu sonlanir ve bu hata ekrana yazdirilir. Dongu klavye ile sonlandirildi anlamina gelir.
while True:
    print("merhaba")

# IndexError              : Mesela bir liste icerisinde olmayan bir indexe ulasilmak istendiginde, bu hata cikar.
liste = [1,2,3,4]
a = liste[6]
print(a)

# KeyError                : Sozluklerde tanimli olmayan bir key cagirildiginda bu hata cikar.
sozluk = {"a" : "b"}
print(sozluk["c"])

# NameError               : Tanimlanmamis bir degisken cagirildiginda bu hata cikar.
a = 5
print(b)

# SyntaxError             : Python formatinda yazim hatasi oldugunda bu hata cikar.
if True:
"""