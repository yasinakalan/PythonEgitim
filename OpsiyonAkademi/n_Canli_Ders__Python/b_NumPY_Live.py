import numpy as np

# xox_oyunu / basit hesap makinesi

# X O O
# O O O
# O O O


# a = np.arange(15)                       # 1 boyutlu
# b = np.arange(15).reshape(3,5)          # 2 boyutlu
# c = np.arange(8).reshape(2,2,2)         # 3 boyutlu
# d = np.arange(16).reshape(2,2,2,2)      # 4 boyutlu

# print(a)
# print(b)
# print(c)
# print(d)


class matrix_hesap_makinesi():
    def __init__(self):
        a = np.ones(1)

    def set_matrix(self, matrix):
        self.a = np.array(matrix)

    def get_matrix(self):
        return self.a
    
    def return_sum(self):
        return self.a.sum()
    
    def return_cumsum(self):
        return self.a.cumsum(axis=0)
    
HM = matrix_hesap_makinesi()
HM.set_matrix([(1,2,3), (1,2,3)])
print(HM.get_matrix())
print(HM.return_sum())
print(HM.return_cumsum())