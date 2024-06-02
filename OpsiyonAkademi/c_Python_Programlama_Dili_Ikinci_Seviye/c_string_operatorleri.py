# +, * matematiksel operatörleri stringler içinde kullanılabilir.
# in mantıksal operatörü stringler içinde kullanılabilir.

# "+" (TOPLAMA İŞLEMİ)
a = "Merhaba"
b = " "
c = "Dünya"
d = "!"

e = a + b + c + d
print("e: ", e)

f = "Merhaba" + " " + "Dünya" + "!"
print("f: ", f)

g = "Merhaba Dünya!"
h = "Python"

i = g[ : 8] #0. indexten başlayıp belirlenen indexe kadar olan aralığı alır.
j = g[-1] #-1. index karakterini alır.
string_toplam = i + h + j
print("String Toplamı: ", string_toplam)


# "*" (ÇARPMA İŞLEMİ)
l = "Python"
m = 10
string_carpim = l * m
print("String Çarpımı: ", string_carpim)


# "in" (String içeriğini karakter grubu olarak değerlendirme)
n = "Merhaba Dünya!"
o = "er"
p = o in n
print("'{0}' içinde '{1}' karakter dizisi var mı?\nCevap: ".format(n, o), p)