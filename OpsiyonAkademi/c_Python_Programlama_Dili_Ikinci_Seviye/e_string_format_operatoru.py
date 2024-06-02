# .formmat operatörü bir metin içerisine parametre yazdırmaya yarar.

# ÖZET
a = float(input("a nın değerini girin: "))
b = float(input("b nin değerini girin: "))

sonuc = a+b

print("{0} + {1} =".format(a, b), sonuc)
print("{0} + {1} = {2}".format(a, b, sonuc))
print("%i + %i = %i"%(a,b,sonuc))
print("%f + %f = %f"%(a,b,sonuc))

c = input("isminizi girin: ")
print("%s bugün işe geldi mi?" %(c))

print(round(22/7, 2))
print("pi sayısı: %.4f"%(22/7))
print("Ali\nAyse\nEce")
print("""Ali
Ayşe
Ece""")





# ÖRNEK: BASİT BİR HESAP MAKİNESİ YAPIMI (TOPLAMA İŞLEMİ)
a = input("1.Sayıyı(a) giriniz: ")
b = input("2.Sayıyı(b) giriniz: ")
toplam = float(a) + float(b)
print("{0} ve {1} sayılarının toplamın sonucu: ".format(a, b), toplam)

# Alternatif gösterim metodu: (%i: okunan parametreyi integer olarak görür. %f: okunan parametreyi float olarak görür. %s: okunan parametreyi string olarak görür.)
print("%i ve %i sayılarının toplamının sonucu: %f" %(float(a), float(b), toplam))

# String deneme:
c = "Yasin"
print("%s bugün işe geldi mi?" %(c))

# float bir ifadede virgülden sonraki basamak sayısını belirleme:
d = 22 / 7
print("Sayı: ", d)
#1.Yol - Yuvarlama
print("Yuvarlama metodu: ", round(d, 2))
#2.Yol - format yüzde metodu
print("Format metodu: %.2f"%(d))

# Alt satıra geçme operatörü (\n)
print("Ali\nAyşe\nBetül")

# Alt satıra geçme operatörü (Üç tırnak metodu: (""" İfadeler """))
print(  """   
        Ali

        Ayşe

        Betül
        """)