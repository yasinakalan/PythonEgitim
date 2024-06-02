# mutlak değer (absolute value) --> abs(x)
a = -3.345
print("mutlak değer: ", abs(a))

# yuvarlama (round) --> round(x) veya round(x, y) ==> Tek parametrelide yuvarlama integerdir. Çift parametrelide ikinci parametre virgülden sonraki basamak sayısı bilgisidir.
b = 22/7
print("yuvarlanacak sayı(b): ", b)
print("yuvarlama_integer: ", round(b))
print("yuvarlama_float: ", round(b,5))

# min, max:
c = max(15,26,15,5465,135,46,546,4651,168,987,16)
print(c)
# alternatif yol:
liste = [15,26,15,5465,135,46,546,4651,168,987,16]
print("maksimum bulma: ", max(liste))
print("minimum bulma: ", min(liste))