# map --> icerisine fonksiyon ve iterable alir.
# iterable --> for dongusu ile liste veya string gibi uzerinde gezinilebilen hersey iterable dir.


# STRING LISTEYI INTEGER LISTEYE CEVIRME:
liste = ["1", "3", "5", "8"]

a = map(int, liste)         # string formatta bir listedir. integer formata donusum icin kullanilir.
print(a)

a = list(a)                 # integer formatta bir adrestir. Liste formata donusum icin kullanilir.
print(a)


# INTEGER LISTEYI KULLANMA (US ALMA):
liste = [1,3,5,8]

a = list(map(lambda x: x ** 2, liste))
print(a)


# LIST COMPREHENSION METODU:

# string - integer donusumu:
liste = ["1","3","5","7"]           # Liste icindeki her veri string veri tipindedir.
print(liste)
liste = [int(i) for i in liste]     # Liste icindeki her veriyi gezinerek integer veri tipine donusturdu.
print(liste)

# string - float donusumu:
liste = ["1","3","5","7"]           # Liste icindeki her veri string veri tipindedir.
print(liste)
liste = [float(i) for i in liste]   # Liste icindeki her veriyi gezinerek float veri tipine donusturdu.
print(liste)

# string - integer donusumu ve matematiksel islem ornegi:
liste = ["1","3","5","7"]                   # Liste icindeki her veri string veri tipindedir.
print(liste)
liste = [(int(i) ** 2) for i in liste]      # Liste icindeki her veriyi gezinerek integer veri tipine donusturdu.
print(liste)

# string - float donusumu ve matematiksel islem ornegi:
liste = ["1","3","5","7"]                   # Liste icindeki her veri string veri tipindedir.
print(liste)
liste = [(float(i) ** 0.328) for i in liste]      # Liste icindeki her veriyi gezinerek integer veri tipine donusturdu.
print(liste)