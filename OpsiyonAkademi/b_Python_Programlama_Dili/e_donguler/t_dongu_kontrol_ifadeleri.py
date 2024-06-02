# break, continue döngü kontrol ifadeleridir. Hem while hem de for döngülerinde kullanılırlar.


# break:
a = 0
while True:
    a += 1
    print("a: ", a)
    if a == 5000:
        break
    print("a 1 artırıldı.")
print("while-break döngüsü sonlandırıldı.")


for i in range(100):
    if i == 50:
        break
    print("i: ", i)
print("for-break döngüsü sonlandırıldı.")



# continue:
a = 0
while True:     # Tek sayıları yazdırmak.
    a += 1
    if a %2 == 0:
        continue        # eğer a çift sayı ise döngünün başına dön yazdırma.
    print("a: ", a)
    if a > 1299:
        break

print("while-continue döngüsü bitti.")