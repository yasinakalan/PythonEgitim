# toplulaştırma anlamina gelmektedir.

# aggregation : 
"""
mean(), 
count(), 
min(), 
max(), 
sum(), 
std(), 
var(), 
describe(), 
transpoze alma, 
Eksik verilere ait indekslerin hesaptan cikarilmasi, 
first(),    --> ilk degeri bulur.
last(),     --> son degeri bulur.
median()    --> medyanı bulur.
"""

import seaborn as sns       # Seaborn kutuphanesinin icinde hazir verisetleri vardir.

df = sns.load_dataset("planets")
print("df: ", df)
a = df.head()       # Ilk 5 satiri goruntuler.
print("a: ", a)

b = df.shape
print("b: ", b)

# mean() FONKSIYONU KULLANIMI:
# mean()
c = df.mean()       # mean() fonksiyonu ortalama alir.
print("c: \n", c)

# sadece belirli bir indeksin ortalamasini almak icin:
d = df["year"].mean()
print("d: \n", d)



# count() FONKSIYONU KULLANIMI:
# count()
e = df["year"].count()      # count fonksiyonu kac adet veri oldugunu sayar.
print("e: \n", e)



# min() FONKSIYONU KULLANIMI:
# min()
f = df["year"].min()        # min fonksiyonu veriler icindeki en kucuk degeri verir.
print("f: \n", f)



# max() FONKSIYONU KULLANIMI:
# max()
g = df["year"].max()        # max fonksiyonu veriler icindeki en buyuk degeri verir.
print("g: \n", g)



# sum() FONKSIYONU KULLLANIMI:
# sum()
h = df["mass"].sum()        # sum fonksiyonu verilerin toplamini verir.
print("h: \n", h)



# std() FONKSIYONU KULLANIMI:
# std()
i = df["mass"].std()        # std fonksiyonu verilerin standart sapmasini verir.
print("i: \n", i)



# var() FONKSIYONU KULLANIMI:
# var()
j = df["mass"].var()        # var fonksiyonu verilerin varyansini verir.
print("j: \n", j)



# describe() FONKSIYONU KULLANIMI:
# describe()
k = df.describe()           # verilerin tüm ozelliklerini verir.
print("k: \n", k)
"""
k: 
             number  orbital_period        mass     distance         year
count  1035.000000      992.000000  513.000000   808.000000  1035.000000
mean      1.785507     2002.917596    2.638161   264.069282  2009.070531
std       1.240976    26014.728304    3.818617   733.116493     3.972567
min       1.000000        0.090706    0.003600     1.350000  1989.000000
25%       1.000000        5.442540    0.229000    32.560000  2007.000000
50%       1.000000       39.979500    1.260000    55.250000  2010.000000
75%       2.000000      526.005000    3.040000   178.500000  2012.000000
max       7.000000   730000.000000   25.000000  8500.000000  2014.000000
"""



# transpoze alma:
l = df.describe().T
print("l: \n", l)
"""
l: 
                  count         mean           std          min         25%        50%       75%       max
number          1035.0     1.785507      1.240976     1.000000     1.00000     1.0000     2.000       7.0
orbital_period   992.0  2002.917596  26014.728304     0.090706     5.44254    39.9795   526.005  730000.0
mass             513.0     2.638161      3.818617     0.003600     0.22900     1.2600     3.040      25.0
distance         808.0   264.069282    733.116493     1.350000    32.56000    55.2500   178.500    8500.0
year            1035.0  2009.070531      3.972567  1989.000000  2007.00000  2010.0000  2012.000    2014.0
"""



# Eksik verilere ait indekslerin hesaptan cikarilmasi:
m = df.count()          # 1035 veri satir oldugu gorulmektedir.
print("m: \n", m)
"""
veri adetleri:
m: 
 method            1035
number            1035
orbital_period     992
mass               513
distance           808
year              1035
dtype: int64
"""

n = df["mass"].count()      # sayim da kullanilan indekse ait 513 adet veri vardir ve bu toplam satir sayisindan az oldugu icin eksik veriler vardir.
print("n: \n", n)
"""
n:
 513
"""
o = df.dropna().describe().T        # 513 adet verinin indexlerine gore tum ozellikler listelenmistir. Eksik veriler hesaplara dahil edilmemistir.
print("o: \n", o)
"""
o: 
                 count         mean          std        min         25%       50%        75%      max
number          498.0     1.734940     1.175720     1.0000     1.00000     1.000     2.0000      6.0
orbital_period  498.0   835.778671  1469.128259     1.3283    38.27225   357.000   999.6000  17337.5
mass            498.0     2.509320     3.636274     0.0036     0.21250     1.245     2.8675     25.0
distance        498.0    52.068213    46.596041     1.3500    24.49750    39.940    59.3325    354.0
year            498.0  2007.377510     4.167284  1989.0000  2005.00000  2009.000  2011.0000   2014.0
"""