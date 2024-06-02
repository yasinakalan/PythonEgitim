# def ile yazilmaz, tek satirda isi bitirmis oluruz.

toplama = lambda x,y : x + y

print(toplama(5,2))
print(toplama)      # Argumanlar verilmeden yazilirsa fonksiyonun RAM deki adresini verir.



# # INTEGER LISTEYI KULLANMA (US ALMA): --> h.map fonksiyonu kısmında anlatıldı.
liste = [1,3,5,8]

a = list(map(lambda x: x ** 2, liste))
print(a)