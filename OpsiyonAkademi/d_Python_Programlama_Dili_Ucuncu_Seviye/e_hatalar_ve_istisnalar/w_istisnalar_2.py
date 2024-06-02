# try:
#     # kod yazilir.
# except:
#     # kod bulunur.



import os

dizin = os.getcwd()
print("dizin: ", dizin) 

os.chdir("./Dersler/d_Python_Programlama_Dili_Ucuncu_Seviye/e_hatalar_ve_istisnalar")      # calistigimiz dizini degistirmis olduk.





try:
    with open("w_deneme.txt", "x") as dosya:  # "x" olarak ekleyemezse "a olarak eklesin. Hata vermesin."
        dosya.write("python")

except FileExistsError:
    with open("w_deneme.txt", "a") as dosya:
        dosya.write("python")
    print("except calisti.")

else:
    # Try blogunda hata meydana gelmezse calisacak.
    print("yeni dosya olusturuldu.")

# Burada Try blogunda hata meydana gelirse except, gelmezse else blogu calisir.






try:
    with open("w_deneme.txt", "a") as dosya:  # "a" olarak calisin ve hata vermesin.
        dosya.write("python")

except FileExistsError:
    with open("w_deneme.txt", "a") as dosya:
        dosya.write("python")
    print("except calisti.")

else:
    # Try blogunda hata meydana gelmezse calisacak.
    print("yeni dosya olusturuldu.")

# Burada Try blogunda hata meydana gelirse except, gelmezse else blogu calisir.







try:
    with open("w_deneme.txt", "a") as dosya:  # "a" olarak calisin ve hata vermesin.
        dosya.write("python")

except FileExistsError:
    with open("w_deneme.txt", "a") as dosya:  # "a" olarak calisin ve hata vermesin.
        dosya.write("python")
    print("except calisti.")

finally:
    # Ne olursa olsun calisir.
    print("finally calisti..")

# Burada Try blogunda hata olsa da olmasa da finally her turlu calisacaktir. Ancak except de hata alirsa finally calismaz.







try:
    with open("w_deneme.txt", "x") as dosya:  # "x" olarak calissin ve hata versin.
        dosya.write("python")

except FileExistsError:
    with open("w_deneme.txt", "x") as dosya:  # "x" olarak calissin ve hata versin.
        dosya.write("python")
    print("except calisti.")

finally:
    # Ne olursa olsun calisir.
    print("finally calisti..")

# Burada Try blogunda hata olsa da olmasa da finally her turlu calisacaktir. Ancak except de hata alirsa finally calismaz.







try:
    with open("w_deneme.txt", "x") as dosya:  # "x" olarak calissin ve hata versin.
        dosya.write("python")

except FileExistsError:
    with open("w_deneme.txt", "a") as dosya:  # "a" olarak calisin ve kod blogunu calistirsin.
        dosya.write("python")
    print("except calisti.")

finally:
    # Ne olursa olsun calisir.
    print("finally calisti..")

# Burada Try blogunda hata olsa da olmasa da finally her turlu calisacaktir. Ancak except de hata alirsa finally calismaz.







try:
    with open("w_deneme.txt", "a") as dosya:  # "a" olarak calisin ve hata vermesin.
        dosya.write("python")

except FileExistsError:
    with open("w_deneme.txt", "x") as dosya:  # "x" olarak calissin ve hata versin.
        dosya.write("python")
    print("except calisti.")

finally:
    # Ne olursa olsun calisir.
    print("finally calisti..")

# Burada Try blogunda hata olsa da olmasa da finally her turlu calisacaktir. Ancak except de hata alirsa finally calismaz.







try:
    with open("w_deneme.txt", "x") as dosya:  # "a" olarak calisin ve hata vermesin.
        dosya.write("python")

except SyntaxError:                         # SyntaxError oldugunda except hata vereceginden finally yine calismaz. Kod hata verir ve durur.
    with open("w_deneme.txt", "a") as dosya:  # "x" olarak calissin ve hata versin.
        dosya.write("python")
    print("except calisti.")

finally:
    # Ne olursa olsun calisir.
    print("finally calisti..")

# Burada Try blogunda hata olsa da olmasa da finally her turlu calisacaktir. Ancak except de hata alirsa finally calismaz.