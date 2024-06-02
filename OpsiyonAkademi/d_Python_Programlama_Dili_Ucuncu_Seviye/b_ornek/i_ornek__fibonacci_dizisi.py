# fibonacci dizisi : 1, 2, 3, 5, 8, 13, 21, 34 .... (1 ve 2 yazildiktan sonraki her sayi kendisinden onceki iki sayinin toplamidir. Bu sekilde altın orana yaklasir.)

# fibonacci(x1, x2, y) - x1: Baslangic degeri, x2: Ikinci sayi, y: Serinin alabilegi maksimum deger.
# return dizi

# x1, x2 ve y icin input alinacak.
# Fibonacci dizisi ekrana yazdirilacak.


def fibonacci():
    x1 = float(input("Baslangic sayisini giriniz: "))
    x2 = float(input("Ikinci sayiyi giriniz: "))
    y = int(input("Bitis sayisini giriniz: "))

 
    for i in range(y + 1):      
        seri = x1 + x2
        if seri <= y:
            
            if int(x1) == 0 or int(x2) == 0:
                oran = "Tanimsiz."
            else:
                oran = x2 / x1
            
            print("""
            adim        : {0}
            seri        : {1}
            oran        : {2}
            x1          : {3}
            x2          : {4}
            kosul       : {1} <= {5}
            """.format(i + 1, seri, oran, x1, x2, y))

            x1 = x2
            x2 = seri

        else:
            print("Dongu tamamlandi.")
            break

fibonacci()





def fibonacci_2():
    x1 = float(input("Baslangic sayisini giriniz: "))
    x2 = float(input("Ikinci sayiyi giriniz: "))
    y = int(input("Bitis sayisini giriniz: "))

    adim = 0
    seri = 0

    while (x1 + x2) <= y:
        adim += 1
        seri = x1 + x2
       
        if int(x1) == 0 or int(x2) == 0:
            oran = "Tanimsiz."
        else:
            oran = x2 / x1
        
        print("""
        adim        : {0}
        seri        : {1}
        oran        : {2}
        x1          : {3}
        x2          : {4}
        kosul       : {1} <= {5}
        """.format(adim, seri, oran, x1, x2, y))

        x1 = x2
        x2 = seri
    
    print("Dongu tamamlandi.")

fibonacci_2()





def fibonacci_3(x1, x2, y):
    dizi = [x1, x2]
    x = x1 + x2
    while y > x:
        x = dizi[-1] + dizi[-2]
        if y >= x:
            dizi.append(x)
    return dizi

x1 = float(input("Fibonacci dizisi icin ilk degeri giriniz."))
x2 = float(input("Fibonacci dizisi icin ilk degeri giriniz."))
y = int(input("Fibonacci dizisi icin ilk degeri giriniz."))

fibonacci_dizisi = fibonacci_3(x1, x2, y)
print(fibonacci_dizisi)