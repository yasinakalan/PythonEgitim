# nested: içiçe koşullu durumlar

liste1 = [1,2,3,4,5,6]
liste2 = [7,8,9,10,11,12]

a, b = 8, 54

if a in liste2:
    if b in liste1:
        print("a liste2 de var, b liste1 de var")
    elif b in liste2:
        print("a liste2 de var, b liste2 de var")
    else:
        print("a liste2 de var, b listelerde yok.")
elif a in liste1:
    if b in liste1:
        print("a liste1 de var, b liste1 de var")
    elif b in liste2:
        print("a liste1 de var, b liste2 de var")
    else:
        print("a liste1 de var, b listelerde yok.")
else:
    if b in liste1:
        print("a listelerde yok, b liste1 de var")
    elif b in liste2:
        print("a listelerde yok, b liste2 de var")
    else:
        print("a ve b listelerde yok.")