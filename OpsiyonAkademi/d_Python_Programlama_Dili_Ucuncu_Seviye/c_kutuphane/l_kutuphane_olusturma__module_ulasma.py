import k_kutuphane_olusturma__hesap_makinesi as hesap_makinesi

a = hesap_makinesi.us_alma()
print(a)


import k_kutuphane_olusturma__hesap_makinesi as hm

b = hm.bolme()
print(b)

c = hm.toplama()
print(c)


from k_kutuphane_olusturma__hesap_makinesi import faktoriyel as fk

d = fk()
print(d)


from k_kutuphane_olusturma__hesap_makinesi import toplama, cikarma

e = toplama()
print(e)

f = cikarma()
print(f)


from k_kutuphane_olusturma__hesap_makinesi import *        # Kutuphane adini yazmadan tüm fonksiyonlara ulasmak icin

g = carpma()
print(g)

h = kok_alma()
print(h)