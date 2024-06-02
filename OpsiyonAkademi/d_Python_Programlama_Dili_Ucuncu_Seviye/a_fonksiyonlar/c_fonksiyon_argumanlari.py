def toplama(x, y):
    print("x=", x)
    print("y=", y)
    print(x + y)
toplama(5,10)

def toplama(x=0, y=0):
    print("x=", x)
    print("y=", y)
    print(x + y)
toplama()

def toplama(x=0, y=0):
    print("x=", x)
    print("y=", y)
    print(x + y)
toplama(5)

def toplama(x=0, y=0):
    print("x=", x)
    print("y=", y)
    print(x + y)
toplama(y=6)

def toplama(x=0, y=0):
    print("x=", x)
    print("y=", y)
    print(x + y)
toplama(y=6, x=4)

# def toplama(x=0, y):        # Ilk deger atanacaksa eger en sagdakinden baslanmasi gerekir. Aksi durumda hata verir.
#     print("x=", x)
#     print("y=", y)
#     print(x + y)
# toplama(5, 2)

def toplama(x, y=0, z=0):
    print("x=", x)
    print("y=", y)
    print("z=", z)
    print(x + y + z)
toplama(5, 2)

def toplama(x, y):
    """
    Bu şekilde yorum yapılırsa, fonksiyonun adini toplama( yazdigimizda bu aciklamalar, yardim penceresinde gorulur.

    Verilen iki degeri toplar.

    Parametreler:
        x(float) : Toplanacak ilk deger.
        y(float) : Toplanacak ikinci deger.

    Returns:
        toplam(float) : Verilen sayilarin toplami.
    """
    print("x=", x)
    print("y=", y)
    print(x + y)
toplama(7,4)

def toplama(x:float, y:float):      # toplama( yazdigimizda yardim penceresinde girilecek degerin tipini gosterir.
    print("x=", x)
    print("y=", y)
    print(x + y)
toplama(6,3)