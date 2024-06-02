# METODLAR = Bir objeye veya Class a bağlı bir fonksiyon yazılırsa bunlara metod denir.
# FONKSİYONLAR = Obje veya Class tan bağımsız bir fonksiyon yazılırsa bunlara fonksiyon denir.

"""
# Harf büyültme-küçültme metodları (NLP - Natural Language Processing (Doğal Dil İşleme)):
    -capitalize, upper, lower, swapcase, title
        -capitalize: Yalnızca ilk harfi büyük harfe dönüştürür.
        -upper: Küçük harfleri büyültmeye yarar.
        -lower: Büyük harfleri küçültmeye yarar.
        -swapcase: Büyük harfleri küçük harflere; küçük harfleri de büyük harflere çevirir.
        -title: Her kelimenin ilk harflerini büyük yazdırır.

# Sorgulama metodları (Sorguya göre True veya False değerleri döndürür.):
    -starswith, endswith, isalpha, isnumeric, isalnum, isupper, islower, istitle, isspace
        -startswith: Ne ile başladığını tespit eder.
        -endswith: Ne ile bittiğini tespit eder.
        -isalpha: İfadenin tamamının HARF lerden oluşup oluşmadığını kontrol eder.
        -isnumeric: İfadenin tamamının sadece SAYI lardan oluşup oluşmadığını kontrol eder.
        -isalnum: İfadenin sadece SAYI ve HARF lerden oluşup oluşmadığını kontrol eder.
        -isupper: İfadenin sadece BÜYÜK HARF lerden oluşup oluşmadığını kontrol eder.
        -islower: İfadenin sadece KÜÇÜK HARF lerden oluşup oluşmadığını kontrol eder.
        -istitle: İfadenin sadece kelimelerin İLK HARF lerinin BÜYÜK HARF lerden oluşup oluşmadığını kontrol eder.
        -isspace: İfadenin sadece BOŞLUK lardan oluşup oluşmadığını kontrol eder.

# Özellik metodları:
    -len, max, min, count, find, index, rfind, rindex
        -len: İfadenin uzunluğunu söyler. Kaç indexten (kaç karakterden) oluştuğunu söyler.
        -max: Alfabetik sırada en sondaki harflerden maksimum olarak sorgulamaya başlar. Sayılarda ise maksimum değeri sorgular.
        -min: Alfabetik sırada en baştaki harflerden minimum olarak sorgulamaya başlar. Sayılarda ise minimum değeri sorgular.
        -count: Yapıda yer alan bir ifadenin kaç tane olduğunu sorgular.
        -find: Bir ifadenin index numarasını sorgular. Aranan ifade yapıda mevcut değilse find metodu -1 değerini döndürür.
        -index: İfadenin yapı içerisinde kaçıncı sırada olduğunu sorgular. Aranan ifade yapıda mevcut değilse index metodu HATA MESAJI döndürür.
        -rfind: Bir ifadenin yapı içerisindeki ilk sırasının sondan kaçıncı olduğunu sorgular.
        -rindex: Bir ifadenin yapı içerisindeki ilk sırasının sondan kaçıncı olduğunu sorgular.

# Diğer metodlar:
    -join, replace, center, ljust, lstrip, rjust, rstrip, split, strip
        -join: Bir yapıdaki tüm parametreleri birleştirip tek kelimelik bir string elde eder.
        -replace: Bir yapıdaki bir ifadeyi çıkarıp yerine başka bir ifade yazılabilir.:
        -center: Bir yapının sağ ve soluna belirli sayıda karakter ekleyerek, yapıyı ortalamak için kullanılır.
        -ljust: Bir yapının sağına belirli sayıda karakter ekleyerek, yapıyı sola yaslamak için kullanılır.
        -rjust: Bir yapının soluna belirli sayıda karakter ekleyerek, yapıyı sağa yaslamak için kullanılır.
        -strip: Bir yapının sağında ve solunda bulunan belirli karakterleri çıkararak, istenilen ifadenin kalmasını sağlar.
        -lstrip: Bir yapının solunda bulunan belirli karakterleri çıkararak, istenilen ifadenin kalmasını sağlar.
        -rstrip: Bir yapının sağında bulunan belirli karakterleri çıkararak, istenilen ifadenin kalmasını sağlar.
        -split: Bir yapının belirli karakterlerden farklı yapılara ayrılmasını sağlar.
"""



# HARF BÜYÜLTME-KÜÇÜLTME METODLARI (NLP - NATURAL LANGUAGE PROCESSING (DOĞAL DİL İŞLEME)):
print("# HARF BÜYÜLTME-KÜÇÜLTME METODLARI (NLP - NATURAL LANGUAGE PROCESSING (DOĞAL DİL İŞLEME)):")

# capitalize:
a = "capitalize"
b = "merhaba dünya!"
c = b.capitalize()
print(
"""
metod               : {0}
Orjinal metin       : {1}
dönüştürülen metin  : {2}

""".format(a, b, c))

# title:
a = "title"
b = "merhaba dünya!"
c = b.title()
print(
"""
metod               : {0}
Orjinal metin       : {1}
dönüştürülen metin  : {2}

""".format(a, b, c))

# upper:
a = "upper"
b = "merhaba dünya!"
c = b.upper()
print(
"""
metod               : {0}
Orjinal metin       : {1}
dönüştürülen metin  : {2}

""".format(a, b, c))

# lower:
a = "lower"
b = "MERHABA DÜNYA!"
c = b.lower()
print(
"""
metod               : {0}
Orjinal metin       : {1}
dönüştürülen metin  : {2}
""".format(a, b, c))

# swapcase:
a = "swapcase"
b = "Merhaba DÜNYA!"
c = b.swapcase()
print(
"""
metod               : {0}
Orjinal metin       : {1}
dönüştürülen metin  : {2}
""".format(a, b, c))




# SORGULAMA METODLARI (SORGUYA GÖRE TRUE VEYA FALSE DEĞERLERİ DÖNDÜRÜR.):
print("# SORGULAMA METODLARI (SORGUYA GÖRE TRUE VEYA FALSE DEĞERLERİ DÖNDÜRÜR.):")

# startswith:
a = "startswith"
b = "01_deneme.txt"
c = "txt"
d = b.startswith(c)
e = "01"
f = b.startswith(e)
print(
"""
metod               : {0}
Sorgulanan Yapı     : {1}
Sorgulanan ifade-1  : {2}
Sonuç-1             : {3}
Sorgulanan ifade-2  : {4}
Sonuç-2             : {5}

""".format(a, b, c, d, e, f))

# endswith:
a = "endswith"
b = "01_deneme.txt"
c = "txt"
d = b.endswith(c)
e = "01"
f = b.endswith(e)
print(
"""
metod               : {0}
Sorgulanan Yapı     : {1}
Sorgulanan ifade-1  : {2}
Sonuç-1             : {3}
Sorgulanan ifade-2  : {4}
Sonuç-2             : {5}

""".format(a, b, c, d, e, f))

# isalpha:
a = "isalpha"
b = "python"
c = b.isalpha()
d = "126545"        #Sadece string ifadelerde arama yapar.
e = d.isalpha()
f = "sayı4654"
g = f.isalpha()
h = "sayı4654!"
i = h.isalpha()
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# isnumeric:
a = "isnumeric"
b = "python"
c = b.isnumeric()
d = "126545"        #Sadece string ifadelerde arama yapar.
e = d.isnumeric()
f = "sayı4654"
g = f.isnumeric()
h = "sayı4654!"
i = h.isnumeric()
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# isalnum:
a = "isalnum"
b = "python"
c = b.isalnum()
d = "126545"        #Sadece string ifadelerde arama yapar.
e = d.isalnum()
f = "sayı4654"
g = f.isalnum()
h = "sayı4654!"
i = h.isalnum()
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# isupper:
a = "isupper"
b = "merhaba dünya !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
c = b.isupper()
d = "Merhaba Dünya !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
e = d.isupper()
f = "MERHABA DÜNYA !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
g = f.isupper()
h = "merhaba DÜNYA 1234 !"   #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
i = h.isupper()
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# islower:
a = "islower"
b = "merhaba dünya !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
c = b.islower()
d = "Merhaba Dünya !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
e = d.islower()
f = "MERHABA DÜNYA !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
g = f.islower()
h = "merhaba DÜNYA 1234 !"   #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
i = h.islower()
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# istitle:
a = "istitle"
b = "merhaba dünya !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
c = b.istitle()
d = "Merhaba Dünya !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
e = d.istitle()
f = "MERHABA DÜNYA !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
g = f.istitle()
h = "merhaba DÜNYA 1234 !"   #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
i = h.istitle()
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# isspace:
a = "isspace"
b = "merhaba dünya !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
c = b.isspace()
d = "Merhaba Dünya !"        #Sadece alfabetik karakterleri sorgular, sembolleri sorguya dahil etmez.
e = d.isspace()
f = "      "
g = f.isspace()
h = "      -     "
i = h.isspace()
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))



# ÖZELLİK METODLARI:
print("# ÖZELLİK METODLARI:")

# len:
a = "len"
b = "merhaba dünya !"
c = len(b)
d = "MerhabaDünya"
e = len(d)
f = "123 456"
g = len(f)
h = "1654sdaf46"
i = len(h)
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# max: ABCDEFG....Zabcdefg....z (min==>max)
a = "max"
b = "merhaba dünya !"
c = max(b)
d = "MerhabaDünya"
e = max(d)
f = "123 456"
g = max(f)
h = "1654sdaf46"
i = max(h)
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# min: ABCDEFG....Zabcdefg....z (min==>max)
a = "min"
b = "merhaba dünya !"
c = min(b)
d = "MerhabaDünya"
e = min(d)
f = "123 456"
g = min(f)
h = "1654sdaf46"
i = min(h)
print(
"""
metod               : {0}
Sorgulanan Yapı-1   : {1}
Sonuç-1             : {2}
Sorgulanan Yapı-2   : {3}
Sonuç-2             : {4}
Sorgulanan Yapı-3   : {5}
Sonuç-3             : {6}
Sorgulanan Yapı-4   : {7}
Sonuç-4             : {8}

""".format(a, b, c, d, e, f, g, h, i))

# count:
a = "count"
b = "merhaba dünya !"
c = "a"
d = b.count(c)
print(
"""
metod               : {0}
Sorgulanan Yapı     : {1}
Sorgualanan İfade   : {2}
Sonuç               : {3}
""".format(a, b, c, d))

# find:
a = "find"
b = "merhaba dünya !"
c = "a"
d = b.find(c)
e = "z"
f = b.find(e)
print(
"""
metod               : {0}
Sorgulanan Yapı     : {1}
Sorgualanan İfade-1 : {2}
Sonuç-1             : {3}
Sorgualanan İfade-2 : {4}
Sonuç-2             : {5}
""".format(a, b, c, d, e, f))

# index:
a = "index"
b = "merhaba dünya !"
c = "a"
d = b.index(c, 5)       # b.index("aranacak ifade", "kaçıncı indexten sorgulamaya başlanacak")
e = "e"                 # "z" olduğunda hata mesajı vermektedir.
f = b.index(e)
print(
"""
metod               : {0}
Sorgulanan Yapı     : {1}
Sorgualanan İfade-1 : {2}
Sonuç-1             : {3}
Sorgualanan İfade-2 : {4}
Sonuç-2             : {5}
""".format(a, b, c, d, e, f))

# rfind:
a = "rfind"
b = "merhaba dünya !"
c = "a"
d = b.rfind(c)
e = "z"
f = b.rfind(e)
print(
"""
metod               : {0}
Sorgulanan Yapı     : {1}
Sorgualanan İfade-1 : {2}
Sonuç-1             : {3}
Sorgualanan İfade-2 : {4}
Sonuç-2             : {5}
""".format(a, b, c, d, e, f))

# rindex:
a = "rindex"
b = "merhaba dünya !"
c = "a"
d = b.rindex(c)
e = "e"     #"z" olduğunda hata mesajı vermektedir.
f = b.rindex(e)
print(
"""
metod               : {0}
Sorgulanan Yapı     : {1}
Sorgualanan İfade-1 : {2}
Sonuç-1             : {3}
Sorgualanan İfade-2 : {4}
Sonuç-2             : {5}
""".format(a, b, c, d, e, f))



# DİĞER METODLAR:
print("# DİĞER METODLAR:")

# join:
a = "join"
b = ["a", "b", "c", "d", "e"]
c = "".join(b)
d = " ".join(b)
e = "-".join(b)
f = "***".join(b)
print(
"""
metod               : {0}
İşlenecek Yapı      : {1}
Sonuç-1             : {2}
Sonuç-2             : {3}
Sonuç-3             : {4}
Sonuç-4             : {5}
""".format(a, b, c, d, e, f))

# replace:
a = "replace"
b = "merhaba dunya!"
c = "python"
d = b.replace("dunya", c)
print(
"""
metod               : {0}
İşlenecek Yapı      : {1}
Değişecek İfade     : {2}
Sonuç               : {3}

""".format(a, b, c, d))

# center:
a = "center"
b = "python"
c = b.center(20)
d = b.center(20, "-")
e = b.center(20, "*")
print(
"""
metod               : {0}
İşlenecek Yapı      : {1}
Sonuç-1             : {2}
Sonuç-2             : {3}
Sonuç-3             : {4}
""".format(a, b, c, d, e))

# ljust:
a = "ljust"
b = "python"
c = b.ljust(20)
d = b.ljust(20, "-")
e = b.ljust(20, "*")
print(
"""
metod               : {0}
İşlenecek Yapı      : {1}
Sonuç-1             : {2}
Sonuç-2             : {3}
Sonuç-3             : {4}
""".format(a, b, c, d, e))

# rjust:
a = "rjust"
b = "python"
c = b.rjust(20)
d = b.rjust(20, "-")
e = b.rjust(20, "*")
print(
"""
metod               : {0}
İşlenecek Yapı      : {1}
Sonuç-1             : {2}
Sonuç-2             : {3}
Sonuç-3             : {4}
""".format(a, b, c, d, e))

# strip:
a = "strip"
b = "   python       "
c = b.strip()
d = "-----------python-------"
e = d.strip("-")
print(
"""
metod               : {0}
İşlenecek Yapı-1    : {1}
Sonuç-1             : {2}
İşlenecek Yapı-2    : {3}
Sonuç-2             : {4}
""".format(a, b, c, d, e))

# lstrip:
a = "lstrip"
b = "   python       "
c = b.lstrip()
d = "-----------python-------"
e = d.lstrip("-")
print(
"""
metod               : {0}
İşlenecek Yapı-1    : {1}
Sonuç-1             : {2}
İşlenecek Yapı-2    : {3}
Sonuç-2             : {4}
""".format(a, b, c, d, e))

# rstrip:
a = "rstrip"
b = "   python       "
c = b.rstrip()
d = "-----------python-------"
e = d.rstrip("-")
print(
"""
metod               : {0}
İşlenecek Yapı-1    : {1}
Sonuç-1             : {2}
İşlenecek Yapı-2    : {3}
Sonuç-2             : {4}
""".format(a, b, c, d, e))

# split:
a = "split"
b = "132,465,789,147,258,369,159,357,546465465465"
c = b.split(",")
print("""
metod               : {0}
Ayrıştırılacak Yapı : {1}
Sonuç               : {2}
""".format(a, b, c))