# w --> dosyayi acar, eger ayni adda dosya varsa o dosyayi silip yeni dosya olusturur.
# a --> dosyayi acar, eger ayni adda dosya varsa o dosyanin sonuna ekler/yazar.
# x --> dosyayi acar, eger ayni adda dosya varsa hata dondurur.

import os

dizin = os.getcwd()
print("dizin: ", dizin) 

os.chdir("./Dersler/d_Python_Programlama_Dili_Ucuncu_Seviye/d_dosyalar")      # calistigimiz dizini degistirmis olduk.



# w --> dosyayi acar, eger ayni adda dosya varsa o dosyayi silip yeni dosya olusturur.

dosya = open("o_deneme.txt", "w")     # deneme.txt dosyasi yoksa dosyayi olusturur, dosya varsa icini sifirdan degistirir.

#dosya.read()                       # "w"-writable acildigi icin okuma yapilamaz.

print(dosya.tell())                 # dosyadaki imlecin konumunu gosterir.
dosya.write("merhaba dunya")        # dosyanin icine yazar, ancak turkce karakter kullanmak icin encoding ini degistirmek gerekir.
dosya.write("python")               # python kelimesini dunyapython olarak bitisik yazar.

print(dosya.tell())                 # dosyadaki imlecin konumunu gosterir.
dosya.write("\nmerhaba dunya\n")    # \n koyularak bir alt satira gecmesi saglanir. her \n eklendiginde imlec konumu 2 karakter ilerler.
print(dosya.tell())                 # dosyadaki imlecin konumunu gosterir.
dosya.write("python\n")
print(dosya.tell())                 # dosyadaki imlecin konumunu gosterir.


liste = ["merhaba\n", "dunya\n", "python\n"]
dosya.writelines(liste)             # tek seferde bir listeyi yazdirmak icin kullanilir.

dosya.close()       # Dosya ile ilgili islemler tamamlanmis olur.





# a --> dosyayi acar, eger ayni adda dosya varsa o dosyanin sonuna ekler/yazar.
dosya = open("o_deneme.txt", "a")     # deneme.txt dosyasi yoksa dosyayi olusturur, dosya varsa icini degistirmez ekleme yapar.

print(dosya.tell())                 # dosyadaki imlecin konumunu gosterir.
liste = ["merhaba\n", "dunya\n", "python\n"]
dosya.writelines(liste)             # tek seferde bir listeyi yazdirmak icin kullanilir.
print(dosya.tell())                 # dosyadaki imlecin konumunu gosterir.

dosya.close()       # Dosya ile ilgili islemler tamamlanmis olur.





# # x --> dosyayi acar, eger ayni adda dosya varsa hata dondurur.
# dosya = open("o_deneme.txt", "x")     # deneme.txt dosyasi yoksa dosyayi olusturur, dosya varsa hata verir.

# print(dosya.tell())                 # dosyadaki imlecin konumunu gosterir.
# liste = ["merhaba\n", "dunya\n", "python\n"]
# dosya.writelines(liste)             # tek seferde bir listeyi yazdirmak icin kullanilir.
# print(dosya.tell())                 # dosyadaki imlecin konumunu gosterir.

# dosya.close()       # Dosya ile ilgili islemler tamamlanmis olur.