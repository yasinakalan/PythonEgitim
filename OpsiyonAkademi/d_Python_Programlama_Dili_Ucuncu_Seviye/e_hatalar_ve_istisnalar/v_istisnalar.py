# exception: istisna

import os

dizin = os.getcwd()
print("dizin: ", dizin) 

os.chdir("./Dersler/d_Python_Programlama_Dili_Ucuncu_Seviye/e_hatalar_ve_istisnalar")      # calistigimiz dizini degistirmis olduk.






# HATA YOKSA "a" KULLANILIRSA:
try:
    # kod yazilir.
    with open("v_deneme.txt", "a") as dosya:
        dosya.write("python")                   # Hataya dusmeyeceginden try: kismi calisir ve kod calismaya devam eder. dosya ya "python" kelimesini ekler.

except:
    # kod yazilir/bulunur.
    print("fileexisterror tamamlandi.")

# Once try komutuna girer ve bir hata varsa excepti calistirir. Bu sekilde hatadan kurtulunmus olunur. Aslinda bir hatadan kurtulma hilesidir. Komut hataya düşsede kodlarin calismasini engellemez.







# HATA VARSA "x" KULLANILIRSA:
try:
    # kod yazilir.
    with open("v_deneme.txt", "x") as dosya:
        dosya.write("python")

except:
    # kod yazilir/bulunur.
    print("fileexisterror tamamlandi.")

# Once try komutuna girer ve bir hata varsa excepti calistirir. Bu sekilde hatadan kurtulunmus olunur. Aslinda bir hatadan kurtulma hilesidir. Komut hataya düşsede kodlarin calismasini engellemez.





try:
    with open("v_deneme.txt", "x") as dosya:
        dosya.write("python")   

except FileExistsError:         # Burada sadece FileExistError aramasi istenir, varsa bu kismi calistirir.
    print("fileexisterror tamamlandi.")

# Once try komutuna girer ve bir hata varsa excepti calistirir. Bu sekilde hatadan kurtulunmus olunur. Aslinda bir hatadan kurtulma hilesidir. Komut hataya düşsede kodlarin calismasini engellemez.





try:
    with open("v_deneme.txt", "x") as dosya:
        dosya.write("python")

except SyntaxError:             # Burada sadece SyntaxError aramasi istenir, yoksa bu kismi atlar. Yani bu hata varsa kod calismaya devam etsin, bu hata disinda bir hata ise kod hata versin ve dursun sarti koyulmus olur.
    # kod yazilir/bulunur.
    print("syntax error tamamlandi.")

# Once try komutuna girer ve bir hata varsa excepti calistirir. Bu sekilde hatadan kurtulunmus olunur. Aslinda bir hatadan kurtulma hilesidir. Komut hataya düşsede kodlarin calismasini engellemez.





try:
    with open("v_deneme.txt", "x") as dosya:
        dosya.write("python")

except FileExistsError:
    print("file error tamamlandi.")
except SyntaxError:
    print("syntax error tamamlandi.")
except KeyboardInterrupt:
    print("keyboard tamamlandi.")

# Burada verilen hatalardan biri varsa onu calistirir. Yoksa hata verip kodu durdurur.





try:
    with open("v_deneme.txt", "x") as dosya:
        dosya.write("python")

except (SyntaxError, FileExistsError):
    print("birlesik error tamamlandi.")
except KeyboardInterrupt:
    print("keyboard tamamlandi.")

# Burada verilen hatalardan biri varsa onu calistirir. Yoksa hata verip kodu durdurur.