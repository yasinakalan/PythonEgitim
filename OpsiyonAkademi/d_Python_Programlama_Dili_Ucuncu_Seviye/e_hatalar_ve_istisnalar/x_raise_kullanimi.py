# raise: yukseltmek anlamina gelir.

# Error verdirmemizi saglar.

#raise SyntaxError("Yazim hatasi yaptiniz.")

def faktoriyel_2(a):
    if int(a) != a:
        raise ValueError("Verdiginiz deger float olmamalidir.")
    if a < 0:
        raise ZeroDivisionError("Verdiginiz deger sifirdan buyuk olmalidir.")

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