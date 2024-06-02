sozluk = dict()     #Boş bir sözlük oluşturur.

sozluk = {}
print(type(sozluk))


# Sözlük ekleme:
sozluk["adi"] = "yasin", "büşra", "yasir", "yüsra"
sozluk["soyadi"] = "akalan"
sozluk["numarasi"] = 161, 185
print(sozluk)



# sozluk guncelleme:
sozluk["numarasi"] = sozluk["numarasi"][0],sozluk["numarasi"][1],2167
print(sozluk)

sozluk["numarasi"] = sozluk["numarasi"], 2167
print(sozluk)

print(sozluk["numarasi"])
print(len(sozluk["numarasi"]))



# sozlukte bir bölüme eleman ekleme için önce bir listeye elemanlar toplanır. liste tuple yappılarak value değerleri güncellenir.

sozluk["numarasi"] = 161, 185, 2167, 554

liste = [("a", "b"), 456, 1654, 456 ,654]         # eklenecek öğre listesi

for i in range(len(sozluk["numarasi"])):
    liste.append(sozluk["numarasi"][i])
    print(liste)

liste_tuple_donusum = tuple(liste)
print(liste_tuple_donusum)

sozluk["numarasi"] = liste_tuple_donusum
print(sozluk["numarasi"])
print(sozluk)
