# 1 e ve kendisine tam bolunebilen 1 den buyuk olan sayilardir.
# Asal sayilar: 2,3,5,7,11,13,17,.....

# Kullanicinin girdigi sayiya kadar olan asal sayilar yazdirilacaktir.



def asal_sayilar(x):

    if x < 2:
        return []       # x, 2 den kucukse herhangi bir asal sayi olmayacagindan bos liste dondurur.
    elif x == 2:
        return [2]
    asallar = [2]
    for i in range(3, x +1):        # range: 3,4,5,6,7....
        asal_mi = True
        for j in range(2,i):        # range1: 2, range2: 2,3, range3: 2,3,4.....
            if i %j ==0:
                asal_mi = False
                break
#        if asal_mi == True:        # False durumunda dongu break ile kirildigi icin == True yazilmasa da fonksiyon dogru calisir.
        if asal_mi:    
            asallar.append(i)       # asal_mi sorgusundan alinan True yanitlari asallar listesinin sonuna tek tek ekliyor. 
    return asallar

x = int(input("Asal sayilar icin maksimum sayiyi giriniz :"))

asallar = asal_sayilar(x)
print("Asal sayilar: ", asallar)
