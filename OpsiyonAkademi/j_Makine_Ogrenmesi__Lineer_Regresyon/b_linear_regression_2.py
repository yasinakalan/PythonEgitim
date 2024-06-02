import pandas as pd
a = pd.read_csv("D:\Egitimler\Opsiyon_Akademi__Yapay_Zeka\Dersler\j_Makine_Ogrenmesi__Lineer_Regresyon\datasets\Advertising.csv", usecols = [1, 2, 3, 4])
df = a.copy()
print(df.head())
df.info()

df_T = df.describe().T
print(df_T)


import seaborn as sns
import matplotlib.pyplot as plt

# sns.pairplot(df, kind="reg")
# plt.show()

# sns.jointplot(x = "TV", y = "sales", data = df, kind="reg")
# plt.show()

import statsmodels.api as sm
b = df[["TV"]]
print(b[0:10])

c = df["sales"]
print(c[0:10])

lm = sm.OLS(c, b)

m = lm.fit()

print(m.summary())