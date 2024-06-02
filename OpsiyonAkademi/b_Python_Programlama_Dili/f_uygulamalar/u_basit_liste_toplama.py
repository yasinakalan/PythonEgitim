# Listenin elemanlarının toplamını bulma:

liste = [132, 456, 515, 4863, 2458, 67]

toplam = 0
for i in liste:
    toplam = toplam + i

print("toplam1: ", toplam)



toplam = 0
for i in range(4):
    toplam += i

print("toplam2: ", toplam)