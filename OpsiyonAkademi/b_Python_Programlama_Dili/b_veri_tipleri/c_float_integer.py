# Float veri tipi ondalıklı sayılara ait bir veri tipidir. "float" olarak kullanılır.

# Integer veri tipi tam sayılara ait bir veri tipidir. "int" olarak kullanılır.

sayi_1 = 15
sayi_2 = 5.4
sayi_3 = 5.0

print("1. Sayının veri tipi: ", type(sayi_1))       # 1. Sayının veri tipi:  <class 'int'>
print("2. Sayının veri tipi: ", type(sayi_2))       # 2. Sayının veri tipi:  <class 'float'>
print("3. Sayının veri tipi: ", type(sayi_3))       # 3. Sayının veri tipi:  <class 'float'>


# Matematiksel İşlemleri:
sayi_toplam = sayi_1 + sayi_2 + sayi_3
print("Sayıların Toplamı: ", sayi_toplam, "Sayıların toplamının veri tipi: ", type(sayi_toplam))    # Sayıların Toplamı:  25.4 Sayıların toplamının veri tipi:  <class 'float'>

sayi_carpim = sayi_1 * sayi_2 * sayi_3
print("Sayıların Çarpımı: ", sayi_carpim, "Sayıların çarpımının veri tipi: ", type(sayi_carpim))    # Sayıların Çarpımı:  405.0 Sayıların çarpımının veri tipi:  <class 'float'>