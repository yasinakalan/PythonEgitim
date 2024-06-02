# tuple (demet)

a = [123, "abc", 2.71]  # liste: elemanlarına hem ulaşıp hem değiştirilebilir.
b = (123, "abc", 2.71)  # tuple: elemanlarına sadece ulaşılabilir, değiştirilemez.

print("liste: ", a)
print("tuple: ", b)

# Tek elemandan oluşann bir demet oluşturmak için elemandan sonra virgül koyulmalıdır. Yoksa demet olarak algılanmaz.
c = (1)
print("İnteger olarak tanınan tek elemanlı demet(hatalı gösterilmiş): ", c)

d = (1,)
print("demet olarak tanınan tek elemanlı demet(doğru gösterim): ", d)
