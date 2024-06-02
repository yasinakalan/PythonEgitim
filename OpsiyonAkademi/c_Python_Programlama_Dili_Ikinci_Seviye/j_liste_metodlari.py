"""

# append : Listenin sonuna ekleme yapar. Her seferinde tek eleman eklenebilir.
# count : Liste içerisinde verilen veri tipine göre sayma yapar.
# index : İstenilen elemanın indexini belirtir.
# insert : Listede verilecek indexe ekleme yapar, sonraki gelen indexler bir sıra kayarlar.
# pop : İndeks verilmediiğinde son elemanı listeden atar, indeks verilirse verilen indekstekini atar.
# remove : Verilen indeksi kaldırır. Yani içine yazılan ifadeyi liste içinde baştan sayarak bulur ve 1 tanesini kaldırır.
# reverse : Listeyi tersine sıralar.
# sort : Listeyi küçükten büyüğe sıralar. Sayısal verileri.

"""



liste = [123,456,789,852,963,741,123,123,123]

# append : Listenin sonuna ekleme yapar.
print("APPEND METODU:")

liste.append(("python", 1, 2))
liste.append(1)
liste.append(2)
print(liste)
print(liste[9])
print(liste[9][0])
print(liste[9][1])
print(liste[9][2])


# count : Liste içerisinde verilen veri tipine göre sayma yapar.
print("COUNT METODU:")

sayac = liste.count(123)
print(sayac)

sayac = liste.count("123")
print(sayac)


# index : İstenilen elemanın indexini belirtir.
print("INDEX METODU:")

i = liste.index(852)
print(i)


# insert : Listede verilecek indexe ekleme yapar, sonraki gelen indexler bir sıra kayarlar.
print("INSERT METODU:")

liste.insert(2, "yasin")
print(liste)


# pop : İndeks verilmediiğinde son elemanı listeden atar, indeks verilirse verilen indekstekini atar.
print("POP METODU:")

a = liste.pop()
print(a)
print(liste)

a = liste.pop(1)
print(a)
print(liste)

a = liste.pop(0)
print(a)
print(liste)


# remove : Verilen indeksi kaldırır. Yani içine yazılan ifadeyi liste içinde baştan sayarak bulur ve 1 tanesini kaldırır.
print("REMOVE METODU:")

a = liste.remove(123)
print(a)
print(liste)

for i in range(liste.count(123)):
    liste.remove(123)
    print(liste)


# reverse : Listeyi tersine sıralar.
print("REVERSE METODU:")

liste.reverse()
print(liste)

liste.reverse()
print(liste)


# sort : Listeyi küçükten büyüğe sıralar. Sayısal verileri.
print("SORT METODU:")


liste.remove("yasin")               # string verileri sıralamaya koyamıyor, hata veriyor. Listeden çıkarılmalı.
liste.remove(("python", 1, 2))      # string verileri sıralamaya koyamıyor, hata veriyor. Listeden çıkarılmalı.

liste.sort()
print(liste)

liste.reverse()
print(liste)
