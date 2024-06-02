# linalg fonksiyonunu kullanarak matris biciminde denklemin cozumu:
# np.linalg.solve (katsayilar, sonuclar)

# Iki bilinmeyenli denklem ornegi:

# 6x + 2y = 15
# x + 4y = 10

# x = ?
# y = ?


import numpy as np

a = np.array([[6, 2], [1, 4]])      # denklemdeki bilinmeyenlerin sirasina gore once birinci denklemin x ve y katsayilari,  sonra ikinci denklemin x ve y katsayilari yazilarak iki boyutlu matris olusturulur.
print("x ve katsayilar matrisi      : ", a)
b = np.array([15, 10])              # sonuclar icinde bir boyutlu sonuc matrisi olusturulur.
print("denklem sonuclari matrisi    : ", b)
sonuc = np.linalg.solve(a, b)       # linalg metodu ile a, b matrislerinin cozumu sonuc degiskenine atanir.    
print("x ve y'nin degerleri matrisi : ", sonuc)

"""
x ve katsayilar matrisi      :  [[6 2]
                                 [1 4]]
denklem sonuclari matrisi    :  [15 10]

x ve y'nin degerleri matrisi :  [1.81818182 2.04545455]
"""