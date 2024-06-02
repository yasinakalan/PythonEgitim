# Ali ve Beyza bir yaris yapiyor ve toplam 6 turda 6sar puan aliyorlar. Skorlari belirleyip kazanan kisiyi bulacagiz.
# ali_skorlar = [4,7,2,9,10,3]
# beyza_skorlar = [5,7,10,1,6,8]

# Ali ve Beyza için toplam skorlar yazilacak.
# Her turun kazanani belirlenip, kazanan sayilar hangisinde fazla ise yarismayi kazanan olacak.
# Total sonuc yazilacak. Ali kazandi, Beyza kazandi, Berabere.

# ali_skorlar = [4,7,2,9,10,3]
# beyza_skorlar = [5,7,10,1,6,8]

print("Skorlari virgul ile ayirarak giriniz.")

ali_skorlar = input("Ali nin skorlarini giriniz:")
ali_skorlar = ali_skorlar.split(",")        # Veriler string formatta oldugundan integer e donusturmek gereklidir.
# print(ali_skorlar)                        
ali_skorlar = map(int, ali_skorlar)         # Hafizaya atar. // map komutu kullanımı 8.liste_manipulasyonu dersinde aciklanmistir.
# print(ali_skorlar)                        # Adresini gosterir.
ali_skorlar = list(ali_skorlar)             # Liste ve integer formata donusturulmus olur.
# print(ali_skorlar)

beyza_skorlar = input("Beyza nin skorlarini giriniz:")
beyza_skorlar = beyza_skorlar.split(",")    # Veriler string formatta oldugundan integer e donusturmek gereklidir.
# print(beyza_skorlar)                      
beyza_skorlar = map(int, beyza_skorlar)     # Hafizaya atar. // map komutu kullanımı 8.liste_manipulasyonu dersinde aciklanmistir.
# print(beyza_skorlar)                      # Adresini gosterir.
beyza_skorlar = list(beyza_skorlar)         # Liste ve integer formata donusturulmus olur.
# print(beyza_skorlar)

tur = 0
ali_skor = 0
beyza_skor = 0

for i in range(0, len(ali_skorlar)):
    tur += 1
    if ali_skorlar[i] > beyza_skorlar[i]:
        ali_skor += 1
        print("{0}. tur kazanani: Ali dir.".format(tur))
    elif ali_skorlar[i] < beyza_skorlar[i]:
        beyza_skor += 1
        print("{0}. tur kazanani: Beyza dir.".format(tur))
    else:
        print("{0}. tur beraberedir.".format(tur))

print("Ali nin toplam puani: {0}".format(ali_skor))
print("Beyza nin toplam puani: %i" %(beyza_skor))

if beyza_skor > ali_skor:
    print("Yarisma kazanani Beyza dir.")
elif ali_skor > beyza_skor:
    print("Yarisma kazanani Ali dir.")
else:
    print("Yarisma beraberlikle sonuclanmistir.")