cubuklar = [1,2,3,4,5,4,2,3,1,4,3,1,1,2,5,3,5,4]

# En uzun ve en kısa çubuk uzunluğu bulunacak ve kaç adet olduğuda bulunacak:
en_uzun_cubuk = 0
sayac = 0

for i in cubuklar:
    if i > en_uzun_cubuk:
        en_uzun_cubuk = i
print("en uzun çubuk: ", en_uzun_cubuk)


for j in cubuklar:
    if j == en_uzun_cubuk:
        sayac = sayac +1
print("sayac: ", sayac)


# Bir sayıdan kaç tane olduğunu bulma:
sorgulanacak_sayi = 2
sayac_sayi = 0

for k in cubuklar:
    if k == sorgulanacak_sayi:
        sayac_sayi = sayac_sayi + 1
print("sayac_sayi: ", sayac_sayi)