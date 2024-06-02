# RETURN daha sonra islemlerde kullanilabilmesi amaciyla kullanilir.


liste = []
uzunluk = len(liste)        # Daha sonra kullanabilmek için uzunluk değişkenine atama yapıldı. Fonksiyonlarda bunu return ile sağlayabiliyoruz.

def us_alma(x, y):
    sonuc = x ** y
    print(sonuc)
a = 25
b = 2
us_alma(a,b)                # Bu sonuc sadece ekrana yazdirir. Daha sonra kullanilamaz.

def toplama(z, t):
    sonuc = z + t
    print(sonuc)
c = 10
d = 5
toplama(c,d)



# RETURN BASIT ORNEK:
def selamla():
    return "merhaba"
a = selamla()
print(a)


# RETURN ORTA ORNEK:
def us_alma(x, y):
    sonuc = x ** y
    print("Fonksiyon ici us: ", sonuc)
    return sonuc
    print("Return sonrasi")             # Fonksiyon returnden sonra yazilanlari gormez.


def toplama(z, t):
    sonuc = z + t
    print("Fonksiyon ici toplam: ", sonuc)
    return sonuc

c = 10
d = 5
a = c + d
b = 2

toplam_sonuc = toplama(c,d)
us_sonuc = us_alma(a,b)
islem_sonuc = us_sonuc

print("Islem sonucu: ", islem_sonuc)



# RETURN KULLANILMAZSA ISLEM SONUCU YOKTUR.

def us_alma(x, y):
    sonuc = x ** y
    print("Fonksiyon ici us: ", sonuc)



def toplama(z, t):
    sonuc = z + t
    print("Fonksiyon ici toplam: ", sonuc)


c = 10
d = 5
a = c + d
b = 2

toplam_sonuc = toplama(c,d)
us_sonuc = us_alma(a,b)
islem_sonuc = us_sonuc

print("Islem sonucu: ", islem_sonuc)