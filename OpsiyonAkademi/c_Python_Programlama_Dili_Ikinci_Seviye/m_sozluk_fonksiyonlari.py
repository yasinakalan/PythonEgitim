sozluk = {"adi" : "yasin", "soyadi" : "akalan", "numarasi" : 161}

# len:
print(len(sozluk))

# str:
a = str(sozluk)     # Sözlüğü stringe dönüştürmek için kullanılır. Yalnız çıktıda süslü parantez stringin ilk indeksi olarak gelir.
print(a)
print(a[0])
print(a[20])

# list:
a = list(sozluk)    # Listeye dönüştürme işlemi için kullanılır. Yalnız sadece key leri alır, value leri almaz.
print(a)
print(a[1])