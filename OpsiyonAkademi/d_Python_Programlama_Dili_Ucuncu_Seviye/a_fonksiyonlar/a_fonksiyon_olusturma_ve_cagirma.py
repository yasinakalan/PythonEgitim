
print("yasin")      # Ekrana yazdırma fonksiyonu
range(10)           # Belirli bir aralıkta sayıları sıralar.

# definition (tanım) --> def

def selamla():
    print("Merhaba arkadaşlar")

selamla()
selamla()


def topla(sayi1, sayi2):
    toplam = float(sayi1) + float(sayi2)
    print(toplam)

topla(3, 5)


def topla():
    sayi1 = input("1.Sayıyı giriniz: ")
    sayi2 = input("2.Sayıyı giriniz: ")

    toplam = float(sayi1) + float(sayi2)
    print(toplam)

topla()