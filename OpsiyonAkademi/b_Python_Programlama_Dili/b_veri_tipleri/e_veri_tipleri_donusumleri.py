a = 5
b = 3.84
c = "8"
d = "2.71"
e = "python"

f = float(a)
print("İnteger ifadenin floata dönüşmüş hali: ", f)

g = str(a)
print("İnteger ifadenin stringe dönüşmesi: ", g)
print("Stringe dönüşmüş sayılarda matematiksel işlem yapılmaz (5+5): ", g+g)

h = int(b)
print("Float ifadeyi integera çevirme: ", h)    # Float ifade integere dönüşürken sayının ondalık kısmını dikkate almaz. Dolayısıyla 3.99 da olsa 3 olarak dönüşmüş olur.

i = int(c)
print("String bir ifadenin integer a çevrilmesi: ", i)

j = float(c)
print("String(integer) bir ifadenin float a çevrilmesi: ", j)

k = float(d)
print("String(float) bir ifadenin float a çevrilmesi: ", k)

# l = int(d)    # integera çevrilirken stringin içerisinde sadece sayı olması gerekiyor. içinde "." olduğu için çevirmez.
# print("String(float) bir ifadenin integer a çevrilmesi: ", l)

# m = float(e)    # floata çevrilirken stringin içerisinde sadece "sayı" ve "." olması gerekiyor. içinde "harf vb." olduğu için çevirmez.
# print("String(float) bir ifadenin integer a çevrilmesi: ", l)