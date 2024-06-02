# faktoriyel
# 5! = 5*4*3*2*1
# KURALLAR:
# Faktoriyel alinacak sayi pozitif tam sayi olmalidir.
# 0 dan buyuk olmalidir.
# 0! = 1 olmalidir.
# 1! = 1 olmalidir.

def faktoriyel():
    
    sayi = int(input("Faktoriyeli alinacak sayiyi giriniz: "))
    if int(sayi) == sayi and sayi > 1:
        carpim = 1
        for i in range(2, sayi + 1):
            carpim *= i
            print("adim: {0}\n sonuc: {1}".format(i, carpim))
        print("{0} sayisinin faktoriyeli: {1}".format(sayi, carpim))
    elif int(sayi) == sayi and (sayi == 1 or sayi == 0):
        carpim = 1
        print("Sayinin faktoriyeli {0} dir.".format(carpim))
    else:
        print("Sayinin faktoriyeli yoktur.")

faktoriyel()




# def faktoriyel_2():
#     sayi = float(input("Faktöriyeli alınacak sayıyı giriniz: "))
#     carpim = 1

#     if sayi < 0 or int(sayi) != sayi:
#         print("Sayının faktöriyeli yoktur.")
#     elif sayi == 0 or sayi == 1:
#         print("Faktöriyel = ", 1)
#     else:

#         for i in range(1, int(sayi+1)):
#             carpim = carpim * i
#         print("Faktöriyel = ", carpim)

# faktoriyel_2()




# def faktoriyel_3(x):
#     sonuc = 1
#     if x<0 or int(x) != x:
#         print("Sayinin faktoriyeli yoktur.")
#     elif x == 0 or x == 1:
#         print(sonuc)
#     else:
#         while x > 1:
#             sonuc *= x  # sonuc = sonuc * x
#             x -= 1      # x = x -1
#         print(sonuc)

# x = float(input("Sayıyı giriniz: "))
# faktoriyel_3(x)