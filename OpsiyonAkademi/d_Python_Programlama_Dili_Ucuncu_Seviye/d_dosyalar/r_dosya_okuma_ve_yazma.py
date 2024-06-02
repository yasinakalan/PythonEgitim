# open("dosya_adi", "r+") --> dosyayi acar ve imleci en basa konumlandirir. Yazmaya ve okumaya izin verir.
# open("dosya_adi", "a+") --> dosyayi acar ve imleci en sona konumlandirir. Yazmaya ve okumaya izin verir.
# open("dosya_adi", "w+") --> eger dosya mevcutsa siler ve yeni bir dosya olusturur. Yazmaya ve okumaya izin verir.
# readable() ve writable() okunabilirlik ve yazilabilirligi sorgular. Bool(True ya da False) bir deger dondurur.

import os

dizin = os.getcwd()
print("dizin: ", dizin) 

os.chdir("./Dersler/d_Python_Programlama_Dili_Ucuncu_Seviye/d_dosyalar")      # calistigimiz dizini degistirmis olduk.


# dosya = open("dosyaadi", "r+")
dosya = open("r_deneme.txt", "r+")
#dosya.write("merhaba")             # "r+" acildigi icin, hem yazma hem de okuma yapar.

print(dosya.readable())             # okunabilirligini sinar. True ya da False deger dondurur.
print(dosya.writable())             # yazilabilirligini sinar. True ya da False deger dondurur.

dosya.write("merhaba\n")
dosya.write("yasin\n")

a = dosya.read()                    # string olarak okuma saglar. Tum icerigi "icerik\nicerik2\nicerik3" seklinde tek kelime gibi gosterir.
print(a)

dosya.close()




# dosya = open("dosyaadi", "r+")
dosya = open("r_deneme.txt", "r+")

print(dosya.tell())
dosya.write("selam")
print(dosya.tell())

dosya.close()




# sona metin ekleme:
dosya = open("r_deneme.txt", "r+")

print(dosya.tell())
dosya.seek(0,2)         # imleci sona attik.
print(dosya.tell())
dosya.write("merhaba\n")
print(dosya.tell())

dosya.close()




# sona metin ekleme-2.yol:
dosya = open("r_deneme.txt", "a+")    # "a+" imleci sona konumlandirdigindan dosya.seek(0,2) ye gerek yoktur.

print(dosya.tell())
dosya.write("merhaba\n")
print(dosya.tell())

dosya.close()




# sifirdan dosyanin icerigini silip bastan yazmaya baslamak icin:
dosya = open("r_deneme.txt", "w+")    # "w+" dosyayi sifirlar ve bastan yazmaya baslar.

print(dosya.tell())
dosya.write("merhaba\n")
print(dosya.tell())

dosya.close()