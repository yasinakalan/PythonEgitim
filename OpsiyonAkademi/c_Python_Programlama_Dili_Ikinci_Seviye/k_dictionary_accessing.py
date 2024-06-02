# ev : tanım.... (key : value)

sozluk = {"adi" : "yasin", "soyadi" : "akalan", "numarasi" : 161}
print(sozluk)

a = sozluk["adi"]
print(a)

b = sozluk["numarasi"]
print(b)

anahtarlar = sozluk.keys()
print(anahtarlar)

anahtar_listesi = list(anahtarlar)
print(anahtar_listesi)

tanimlar = sozluk.values()
print(tanimlar)

tanim_listesi = list(tanimlar)
print(tanim_listesi)