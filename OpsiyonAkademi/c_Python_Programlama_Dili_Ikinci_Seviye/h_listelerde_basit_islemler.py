# +, *, in

# LİSTELERDE TOPLAMA (concatenate):
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

liste3 = liste1 + liste2
print(liste3)       # liste3 = [1, 2, 3, 4, 5, 6]

liste4 = liste2 + liste1
print(liste4)       # liste4 = [4, 5, 6, 1, 2, 3]


# LİSTELERDE ÇAPMA:
liste5 = ["a", 6.15, 8]
liste6 = liste5 * 3
print(liste6)       # liste6 = ['a', 6.15, 8, 'a', 6.15, 8, 'a', 6.15, 8]


# in OPERATÖRÜ
liste7 = [1,2,5,4,8,6,8,4,3]
print(5 in liste7)      # True
print("5" in liste7)    # False
print(5.0 in liste7)    # True
print("beş" in liste7)  # False
print(8 in liste7)      # True