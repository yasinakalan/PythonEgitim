# Hesap makinesi olusturulacak: +,-,*,/,**,faktoriyel,kok alma

def toplama():
    # Fonksiyon cagrildiginda yardim penceresinde not birakilabilir.
    """
    toplama islemini yapar.
    """
    liste = input("Toplama yapilacak sayilari virgul ile ayirarak giriniz:\n")
    liste = liste.split(",")
    liste = map(float, liste)
    liste = list(liste)
    sonuc = 0
    for i in liste:
        sonuc += i
    return sonuc

def cikarma():
    # Fonksiyon cagrildiginda yardim penceresinde not birakilabilir.
    """
    cikarma islemini yapar.
    """
    liste = input("Cikarma yapilacak sayilari virgul ile ayirarak giriniz:\n")
    liste = liste.split(",")
    liste = map(float, liste)
    liste = list(liste)
    sonuc = liste[0]
    for i in liste[1 : len(liste)]:
        sonuc -= i
    return sonuc

def carpma():
    # Fonksiyon cagrildiginda yardim penceresinde not birakilabilir.
    """
    carpma islemini yapar.
    """
    liste = input("Carpma yapilacak sayilari virgul ile ayirarak giriniz:\n")
    liste = liste.split(",")
    liste = map(float, liste)
    liste = list(liste)
    sonuc = liste[0]
    for i in liste[1 : len(liste)]:
        sonuc *= i
    return sonuc

def bolme():
    # Fonksiyon cagrildiginda yardim penceresinde not birakilabilir.
    """
    bolme islemini yapar.
    """
    liste = input("Bolme yapilacak sayilari virgul ile ayirarak giriniz:\n")
    liste = liste.split(",")
    liste = map(float, liste)
    liste = list(liste)
    sonuc = liste[0]
    for i in liste[1 : len(liste)]:
        sonuc /= i
    return sonuc

def us_alma():
    # Fonksiyon cagrildiginda yardim penceresinde not birakilabilir.
    """
    us_alma ustel islemini yapar.
    """
    liste = input("Us alma yapilacak sayilari us alma sirasina gore virgul ile ayirarak giriniz:\n")
    liste = liste.split(",")
    liste = map(float, liste)
    liste = list(liste)
    sonuc = liste[0]
    for i in liste[1 : len(liste)]:
        sonuc **= i
    return sonuc

def faktoriyel():
    # Fonksiyon cagrildiginda yardim penceresinde not birakilabilir.
    """
    faktoriyel alma islemini yapar.
    """
    x = int(input("Faktoriyeli alinacak sayiyi giriniz: "))
    sonuc = 1
    if x < 0 or int(x) != x:
        print("Sayinin faktoriyeli yoktur.")
    elif x == 0 or x == 1:
        sonuc = 1
        return sonuc
    else:
        while x > 1:
            sonuc *= x
            x -= 1
        return sonuc

def kok_alma():
    # Fonksiyon cagrildiginda yardim penceresinde not birakilabilir.
    """
    kok alma islemini yapar.
    """
    liste = input("Kok alma yapilacak sayilari kok alma sirasina gore virgul ile ayirarak giriniz:\n")
    liste = liste.split(",")
    liste = map(float, liste)
    liste = list(liste)
    sonuc = liste[0]
    for i in liste[1 : len(liste)]:
        sonuc **= (1 / i)
    return sonuc


if __name__ == "__main__":      # bu bloğun altına yazılan sorgulamalar sadece bu dosyada çalışır. Başka dosya da çağrıldığında sorgular görülmez.
    print(faktoriyel())     # bu pencere çalıştırılırsa görülür. Ancak başka pencerede kütüphane olarak kullanıldığında görülmez.
    