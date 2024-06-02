# Listenin içindeki bir ifadeyi değiştirmek:

# Listedeki bir indexi bir ifade ile değiştirme:
a = [1,2,3,4,5,6,7,8,9]
a[4] = "python"
print("a listesinin yeni hali: ", a)        # a = [1, 2, 3, 4, 'python', 6, 7, 8, 9]

# Listedeki bir aralığı bir ifade ile değiştirme:
a = [1,2,3,4,5,6,7,8,9]
a[1:4] = "dunya"        # index aralığı 3 iken eklenecek ifade 5 karakter olduğundan her karakteri aralığa sığdırır.
b = len(a)
print("""
a listesinin yeni hali          : {0}
a listesinin karakter sayısı    : {1}
""".format(a, b))


# Listedeki bir aralığı bir ifade ile değiştirme:
a = [1,2,3,4,5,6,7,8,9]
a[1:4] = "dunya", "merhaba", "!"        # index aralığı 3 iken eklenecek ifade 3 string ifade olduğundan index numaralarına tam atanır.
b = len(a)
print("""
a listesinin yeni hali          : {0}
a listesinin karakter sayısı    : {1}
""".format(a, b))



# liste[index]

a = [1,2,3,4,5,6,7,8,9]

"""
Burada a listesinin indexleri sırasıyla;
    0.index = 1
    1.index = 2
    2.index = 3
    3.index = 4
    4.index = 5
    5.index = 6
    6.index = 7
    7.index = 8
    8.index = 9
"""

print("Düz index sıraları: ")   #Düz saymaya 0 dan başlanır.
print("0. index : ", a[0])
print("1. index : ", a[1])
print("2. index : ", a[2])
print("3. index : ", a[3])
print("4. index : ", a[4])
print("5. index : ", a[5])
print("6. index : ", a[6])
print("7. index : ", a[7])
print("8. index : ", a[8])

print("\nTersten index sıraları: ") #Tersten saymaya -1 den başlanır. (\n ifadesi cümleyi bir satır aşağı indirir.)
print("-1. index : ", a[-1])
print("-2. index : ", a[-2])
print("-3. index : ", a[-3])
print("-4. index : ", a[-4])
print("-5. index : ", a[-5])
print("-6. index : ", a[-6])
print("-7. index : ", a[-7])
print("-8. index : ", a[-8])
print("-9. index : ", a[-9])


print("\nBirden fazla index almak için: ")  # a[başlangıç indexi : son index + 1]
baslangic_indexi = 2
son_index = 6
aralik_listesi = a[baslangic_indexi: son_index + 1] #Belirlenen index aralığını alır.
metin = "{0} - {1}. indexleri arası karakterler: "  #Tanımlayıcı cümleyi oluşturur.
print(metin.format(baslangic_indexi, son_index), aralik_listesi)    #Ekrana yazdırır.
#print("{0} - {1}. indexleri arası karakterler: ".format(baslangic_indexi, son_index), a[baslangic_indexi: son_index +1])   #Üç işlemi tek satırda yazar.


print("\nBaşlangıç indexinden son indexe kadar olanı almak için: ")  # a[başlangıç indexi : ]
baslangic_indexi = 4
aralik_listesi = a[baslangic_indexi: ] #Başlangıçtan son indexe kadar olan aralığını alır.
metin = "{0}. indexten son indexe kadar olan karakterler: "  #Tanımlayıcı cümleyi oluşturur.
print(metin.format(baslangic_indexi), aralik_listesi)    #Ekrana yazdırır.
#print("{0}. indexten son indexe kadar olan karakterler: ".format(baslangic_indexi), a[baslangic_indexi:)   #Üç işlemi tek satırda yazar.

print("\nBirden fazla indexi belirli aralıklı almak için: ")  # a[başlangıç indexi : son index + 1 : atlama_araligi]
baslangic_indexi = 2
son_index = 10
atlama_araligi = 2
aralik_listesi = a[baslangic_indexi: son_index + 1 : atlama_araligi] #Belirlenen index aralığını ve atlama aralığını alır.
metin = "{0} - {1}. indexleri arası {2} karakter atlamalı karakterler: "  #Tanımlayıcı cümleyi oluşturur.
print(metin.format(baslangic_indexi, son_index, atlama_araligi), aralik_listesi)    #Ekrana yazdırır.
#print("{0} - {1}. indexleri arası {2} karakter atlamalı karakterler: ".format(baslangic_indexi, son_index, atlama_araligi), a[baslangic_indexi: son_index +1 : atlama_araligi])   #Üç işlemi tek satırda yazar.

print("\nBaşlangıç indexinden son indexe kadar belirli aralıklı almak için: ")  # a[başlangıç indexi : : atlama_araligi]
baslangic_indexi = 4
atlama_araligi = 3
aralik_listesi = a[baslangic_indexi: : atlama_araligi] #Başlangıçtan son indexe kadar atlama aralığını alır.
metin = "{0}. indexten son indexe kadar {1} karakter atlamalı karakterler: "  #Tanımlayıcı cümleyi oluşturur.
print(metin.format(baslangic_indexi, atlama_araligi), aralik_listesi)    #Ekrana yazdırır.
#print("{0}. indexten son indexe kadar {1} karakter atlamalı karakterler: ".format(baslangic_indexi, atlama_araligi), a[baslangic_indexi: : atlama_araligi])   #Üç işlemi tek satırda yazar.
