def toplama(*args):     # verilen tüm argümanları args = () tuple içine ekler. İstediğin kadar argüman ile çalışmayı sağlar.
    print(args)
    toplam = 0
    for i in args:
        toplam += i
    print(toplam)
toplama(10,5,5,25,30,84,46.564)

def toplama(x, y, *args):   # en az iki argüman vermek zorunludur.
    print(args)
    toplam = x + y
    for i in args:
        toplam += i
    print(toplam)
toplama(10,5,5,25,30,84,46.564)

def toplama(x, y, *args):   # en az iki argüman vermek zorunludur.
    print(args)
    toplam = x + y
    for i in args:
        toplam += i
    print(toplam)
toplama(10,5)

def toplama(x=0, y=0, *args):
    print(args)
    toplam = x + y
    for i in args:
        toplam += i
    print(toplam)
toplama(10)

def toplama(x=0, y=0, *args):
    print(args)
    toplam = x + y
    for i in args:
        toplam += i
    print(toplam)
toplama(10,20,30,40,50,546.65446)