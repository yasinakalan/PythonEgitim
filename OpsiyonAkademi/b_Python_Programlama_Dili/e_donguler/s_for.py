# while: Durdurulmadığı veya True olduğu sürece sonsuza kadar devam eder.
# for: Belli limitleri vardır.

a = [1,2,3,4,5,6,7,8,9,10]

for i in a:
    print("i: ", i)

print("for dongusu bitti.")



b = range(0,10,1)    # 3 farklı parametre alır. ilk değer-başlangıç değeri; ikinci parametre-sonlanacağı değer(dahil değil): üçüncü parametre-artış moktarıdır.

for i in b:
    print("i: ", i)

print("for dongusu bitti.")



for i in range(4,20,4):
    print("i: ", i)

print("for dongusu bitti.")



for i in range(4,21,4):
    print("i: ", i)

print("for dongusu bitti.")



for i in range(4,10):       # 3.parametre verilirse birer birer artırır.
    print("i: ", i)

print("for dongusu bitti.")



for i in range(10):       # 1.parametre verilirse sıfırdan başlar ve birer birer artırır.
    print("i: ", i)

print("for dongusu bitti.")



# ÖRNEK: Sıfırdan 100e kadar çift sayıları yazdıralım.
for i in range(100 + 1):
    if i%2==0:
        print("i: ", i)
print("Çift sayıların yazılması tamamlandı.")