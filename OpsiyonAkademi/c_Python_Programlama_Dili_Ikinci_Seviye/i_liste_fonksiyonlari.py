# len       : Listenin uzunluğunu verir.
# max       : Listedeki maximum elemanı verir.
# min       : Listedeki minimum elemanı verir.
# enumarate : Listedeki herbir elemanı indeksi ile beraber tuple (demet) olarak döndürür.


# len KULLANIMI:
liste = [1,2,3,4,5,6,7,8,9]
a = len(liste)
print(a)

for i in liste:
    print(i)

print("RANGE ile kullanım:")
for index in range(1, len(liste)+1):
    print(index)

# enumarate KULLANIMI:
print("ENUMARATE ile kullanım:")
for index, eleman in enumerate(liste):
    print("index    : ", index)
    print("eleman   : ", eleman)

    
# max KULLANIMI:
print("MAX-MIN KULLANIMI:")
a = max(liste)
print(a)

# min KULLANIMI:
a = min(liste)
print(a)