"""
5-6 tane öğrenci bir dersten notlar almış ve 40 dan az alan öğrenciler kalacak.

Aldıkları notları aşağı ve yukarı 5 likler halinde yuvarlanacak ve yeni liste oluşturulacak.

1-87
2-64
3-29
4-61
5-39
6-55

"""


notlar = [87, 64, 29, 61, 39, 55, 93, 63, 91, 92]

for i in notlar:
    if i < 40:
        print("Öğrenci dersten kaldı. Not: ", i)
    else:
        if i %5 == 0:
            print("Öğrencinin notu değişmedi. Not: ", i)
        elif i %5 >= 3:
            yeni_not = i + (5 - i%5)
            print("Öğrencinin notu yukarı yuvarlandı. Not: ", yeni_not)
        else:
            yeni_not = i - (i%5)
            print("Öğrencinin notu aşağı yuvarlandı. Not: ", yeni_not)