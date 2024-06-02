# def faktoriyel_fonksiyonu(sayi):
#     if(sayi == 0):
#         return 1
#     print(sayi * faktoriyel_fonksiyonu(sayi-1))
#     return sayi * faktoriyel_fonksiyonu(sayi-1)



class hesap_makinesi_sinifi():
    def __init__(self):
        self.fakt_yazdir = 1

    def faktoriyel_fonksiyonu(self, sayi):
        if(sayi == 0):
            return 1
        return sayi * self.faktoriyel_fonksiyonu(sayi-1)
    
    def fakt_yazdir(self, cikti):
        print(cikti)

hesap_makinesi = hesap_makinesi_sinifi()
hesap_makinesi.fakt_yazdir(hesap_makinesi_sinifi.faktoriyel_fonksiyonu(6))