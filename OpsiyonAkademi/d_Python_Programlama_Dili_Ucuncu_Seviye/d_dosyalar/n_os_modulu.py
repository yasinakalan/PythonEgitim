 # os : operation system : isletim sistemi

# os.getcwd : get current working directory, suanda uzerinde calisilan dizini dondur.
# os.listdir : list directory, su andaki calisilan dizini listeler.
# os.chdir : change directory, calisilan dizini degistirir.
# os.makedirs : make directories, bulundugumuz dizinde klasorler olusturur.
# os.rename : dosyayi yeniden adlandirir. os.rename(eski adi, yeni adi)
# os.remove(dosya_adi) : belirtilen dosyayi siler/kaldirir.
# os.rmdir(klasor_adi) : klasoru siler.


import os

dizin = os.getcwd()
print("dizin: ", dizin)            # -PS C:\Users\Yasin AKALAN\Desktop\Opsiyon_Akademi-Yapay_Zeka\Dersler> 

liste = os.listdir()
print("liste: ", liste)            # ['a.Yapay_Zeka_Egitimine_Giris', 'b.Python_Programlama_Dili', 'c.Python_Programlama_Dili_Ikinci_Seviye', 'd.Python_Programlama_Dili_Ücüncü_Seviye', 'e.Data_Science-Numpy_Kutuphanesi', 'f.Data_Science-Pandas_Kutuphanesi']


os.chdir("./d_Python_Programlama_Dili_Ucuncu_Seviye")       # . bulunan dizini ifade eder. yani (".") ==> C:\Users\Yasin AKALAN\Desktop\Opsiyon_Akademi-Yapay_Zeka\Dersler
dizin = os.getcwd()
print("dizin: ", dizin)
liste = os.listdir()
print("liste: ", liste)


for dosya in liste:
    if dosya.endswith(".py"):           # .py ile biten dosya varsa True yoksa False dondurur.
        print(dosya)



# makedirs: 
os.makedirs("test/test2/test3")         # Sirali olarak klasorleri ic ice olusturur.


# os.rename:
os.rename("./test/deneme.txt", "deneme_yeni.txt")       # isim degistirirken adreste belirtilirse dosyanin konumunuda degistirebiliriz. Yani dosyayi tasiyabiliriz.


# os.remove(dosya_adi):
os.remove("deneme.txt")             # Silindikten sonra geri donusu yoktur. Dikkatli olmak gerekir.


# os.rmdir(klasor_adi):
os.rmdir("test/test2/test3")        # klasor bos degilse klasoru silmez, once klasorun icinin silinmesi gerekir.
os.rmdir("test/test2")
os.rmdir("test")