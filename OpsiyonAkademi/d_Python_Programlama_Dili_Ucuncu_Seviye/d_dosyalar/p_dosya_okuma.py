# dosya = open("dosyaadi", "r") - r: readable, okunabilir.



import os

dizin = os.getcwd()
print("dizin: ", dizin) 

os.chdir("./Dersler/d_Python_Programlama_Dili_Ucuncu_Seviye/d_dosyalar")      # calistigimiz dizini degistirmis olduk.


# dosya = open("dosyaadi", "r")
dosya = open("p_deneme.txt", "r")
#dosya.write("merhaba")     # "r"-readable acildigi icin, yazma yapilamaz.

a = dosya.read()            # string olarak okuma saglar. Tum icerigi "icerik\nicerik2\nicerik3" seklinde tek kelime gibi gosterir.
print(a)

dosya.close()




dosya = open("p_deneme.txt", "r")

liste = dosya.readlines()   # her satiri listenin bir elemani olarak gosterir. Her ifadenin sonuna \n ekler.
print(liste)

dosya.close()




dosya = open("p_deneme.txt", "r")

(print(dosya.tell()))
satir1 = dosya.readline()   # sadece ilk satiri okur.
print(satir1)

(print(dosya.tell()))
satir2 = dosya.readline()   # ilk satir okundugu icin imleci ilk satir sonuna atar ve 2. defa calistirilirsa imlec kaldigi yerden yani 2.satiri okur.
print(satir2)

(print(dosya.tell()))
satir3 = dosya.readline()   # 1 ve 2. satirlar okundugu icin imleci ikinci satir sonuna atar ve 3. defa calistirilirsa imlec kaldigi yerden yani 3. satiri okur.
print(satir3)
(print(dosya.tell()))

# Son satirdan sonra okumaya devam edilmesi istenirse, imlec en sonda takili kalacagi icin imlec konumu degismez. Bir onceki imlec konumuna esit kalir.

dosya.close()




dosya = open("p_deneme.txt", "r")

(print(dosya.tell()))
indexli_okuma = dosya.read(36)  # imlec numarasi belirtilen rakama kadar olan ifadeleri okur.
print(indexli_okuma)
(print(dosya.tell()))

(print(dosya.tell()))
indexli_okuma = dosya.read()    # imlec numarasi belirtilen rakama kadar olan ifadeleri okuduktan sonra tekrar okuma yapilirsa kaldigi yerden okumaya devam eder.
print(indexli_okuma)
(print(dosya.tell()))

dosya.close()




dosya = open("p_deneme.txt", "r")

(print(dosya.tell()))
dosya.seek(16)                  # imlec okuma yapmadan belirtilen konuma tasinir.
(print(dosya.tell()))
oku = dosya.read()              # imlecin tasindigi noktadan okuma yapilir.
print(oku)
(print(dosya.tell()))

dosya.close()




dosya = open("p_deneme.txt", "r")

(print(dosya.tell()))
dosya.seek(16, 0)               # imlec belirtilen konumdan(16) sonuna kadar(0) okuma yapar.
(print(dosya.tell()))
oku = dosya.read()              # imlecin tasindigi noktadan okuma yapilir.
print(oku)
(print(dosya.tell()))

dosya.close()




dosya = open("p_deneme.txt", "r")

(print(dosya.tell()))
dosya.seek(0, 2)                # imleci sona atar(0) ve offset(2) dahilinde hiçbirşey okumadan imlec sonda kalir. burayı anlamadım youtube dan öğrenmeye çalış.
(print(dosya.tell()))
oku = dosya.read()              # imlecin tasindigi noktadan okuma yapilir.
print(oku)
(print(dosya.tell()))

dosya.close()




dosya = open("p_deneme.txt", "r")

(print(dosya.tell()))
dosya.seek(10)                  # imlec okuma yapmadan belirtilen konuma tasinir.
(print(dosya.tell()))
dosya.seek(0, 1)                # imleci sona atar(0) ve offset(1) dahilinde imlecin tasindigi konumdan baslayarak tamamini okur. burayı anlamadım youtube dan öğrenmeye çalış.
(print(dosya.tell()))
oku = dosya.read()              # imlecin tasindigi noktadan okuma yapilir.
print(oku)
(print(dosya.tell()))

dosya.close()




# dosya = open("p_deneme.txt", "r")

# dosya.seek(0)
# a = dosya.read()
# print(a)
# dosya.seek(0)

# liste = dosya.readlines()
# print(liste[0])
# print(liste[1][2])
# print(liste[2])

# dosya.close()