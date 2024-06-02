# Kullanıcıdan veri almak için kullanılır. (ATM lerdeki şifre gibi.)

a = input("Birşeyler yazın: ")  #Yazılan herşey bir string ifadedir. Sayılarıda string olarak alır.
print("Yazdığınız: ", a)

# ÖRNEK: BASİT BİR HESAP MAKİNESİ YAPIMI (TOPLAMA İŞLEMİ)
b = input("1.Sayıyı giriniz: ")
c = input("2.Sayıyı giriniz: ")
d = int(input("integer sayı gir: "))
e = float(input("float sayı gir: "))
toplam = float(b) + float(c) + d + e
print("Toplamın sonucu: ", toplam)