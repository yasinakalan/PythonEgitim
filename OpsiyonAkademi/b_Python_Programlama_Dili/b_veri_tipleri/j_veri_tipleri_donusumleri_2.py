# dictionary-set-tuple-listeler arası veri tipi dönüşümleri

list_liste = [5,5,4,3,2,1,1,6]
tuple_demet = (3,3,2,1,5,8,7,6)
dictionary_sozluk = {"a":1,"b":2,"c":3,"d":4}
set_kume = {7,6,2,4,5,3,1,9}

# listeyi demete dönüştürme:
a = tuple(list_liste)
print("listeyi demete dönüştürme: ", a)

# listeyi kümeye dönüştürme:
b = set(list_liste)
print("listeyi kümeye dönüştürme: ", b)

# demeti listeye dönüştürme:
c = list(tuple_demet)
print("demeti listeye dönüştürme: ",c)

# demeti kümeye dönüştürme:
d = set(tuple_demet)
print("demeti kümeye dönüştürme: ", d)

# sözlüğü listeye dönüştürme:
e = list(dictionary_sozluk)
print("sözlüğü listeye dönüştürme: ", e)

# sözlüğü demete dönüştürme:
f = tuple(dictionary_sozluk)
print("sözlüğü demete dönüştürme: ", f)

# sözlüğü kümeye dönüştürme:
g = set(dictionary_sozluk)
print("sözlüğü kümeye dönüştürme: ", g)

# listeyi sözlüğe dönüştürme:
yeni_liste = [("a",1), ("b",2), ("c",3)]
h = dict(yeni_liste)
print("listeyi sözlüğe dönüştürme: ", h)

# demeti sözlüğe dönüştürme:
yeni_demet = (("a",1), ("b",2), ("c",3))
i = dict(yeni_demet)
print("demeti sözlüğe dönüştürme: ", i)

# tek elemanlı demeti sözlüğe dönüştürme:   // Tuple ın kendi özelliğinden dolayı elemandan sonra virgül koyulmalıdır. Yoksa dönüştürülemez.
tek_elemanli_demet = ((1,2),)
j = dict(tek_elemanli_demet)
print("tek elemanlı demeti sözlüğe dönüştürme: ", j)