# with metodu ile dosya acma

import os

dizin = os.getcwd()
print("dizin: ", dizin) 

os.chdir("./Dersler/d_Python_Programlama_Dili_Ucuncu_Seviye/d_dosyalar")      # calistigimiz dizini degistirmis olduk.


with open("r_deneme.txt", "r") as dosya:

    print(dosya.read())