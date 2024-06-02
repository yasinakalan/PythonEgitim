# assert                  : Aslinda bu bir hata metodudur.

# AssertionError          : Bir ifadenin true ya da false oldugunu iddia ediyorsak, iddiamızın sonucu true cikarsa bu hatayi dondurur. Bir sonraki derste daha detayli anlatildi.

# Mesela bir fonksiyonumuz olsun, bazi kosullara gore hata mesajlari almasini isteyelim.

# assert bool, "hata mesaji" --> bool: True/False


# Örnek olarak 5.5 float sayısının faktöriyeli yoktur ama bunu belirtmezsek faktöriyel hesabına girer.

def faktoriyel(a):
    sonuc = 1
    while a > 1:
        sonuc *= a
        a -= 1
    return sonuc

b = faktoriyel(5)
print("b:", b)




def faktoriyel_2(a):
    assert int(a) == a, "Verdiginiz sayi tam sayi olmalidir."           # Tam sayi oldugunu anlamak icin int(a) == a yapilmalidir.
    assert a >= 0, "Verdiginiz sayi 0 veya 0'dan buyuk olmalidir."
    sonuc = 1
    while a > 1:
        sonuc *= a
        a -= 1
    return sonuc

c = faktoriyel_2(5.5)         # Mesela faktoriyel tam sayi olmalidir. Burada hata vermesini saglamaliyiz.
print("c:", c)

d = faktoriyel_2(-5)          # Mesela faktoriyel pozitif olmalidir. Burada hata vermesini saglamaliyiz.
print("d:", d)

e = faktoriyel_2(-5.5)        # Burada ise fonksiyon icinde ilk hata mesajini verir.
print("d:", d)