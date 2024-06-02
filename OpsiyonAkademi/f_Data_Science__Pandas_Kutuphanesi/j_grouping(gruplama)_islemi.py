import pandas as pd
import seaborn as sns


df = pd.DataFrame({'gruplar':['a', 'b', 'c', 'a', 'b', 'c'],    
                   'veriler':[3,8,15,29,45,62]}, columns=['gruplar', 'veriler'])        # pandas dataframe ekleme
print(df)   
"""
  gruplar  veriler
0       a        3
1       b        8
2       c       15
3       a       29
4       b       45
5       c       62
"""


a = df.groupby('gruplar').mean()        # Gruplama ve ortalama alma
print(a)
"""
gruplar
a           16.0
b           26.5
c           38.5
"""






df_2 = sns.load_dataset('planets')      # Seaborn dataset ekleme
b = df_2.head()
print(b)
"""
            method  number  orbital_period   mass  distance  year
0  Radial Velocity       1         269.300   7.10     77.40  2006
1  Radial Velocity       1         874.774   2.21     56.95  2008
2  Radial Velocity       1         763.000   2.60     19.84  2011
3  Radial Velocity       1         326.030  19.40    110.62  2007
4  Radial Velocity       1         516.220  10.50    119.47  2009
"""






c = df_2.groupby('method')['orbital_period'].mean()     # Gruplama ve ortalama alma
print(c)
"""
method
Astrometry                          631.180000
Eclipse Timing Variations          4751.644444
Imaging                          118247.737500
Microlensing                       3153.571429
Orbital Brightness Modulation         0.709307
Pulsar Timing                      7343.021201
Pulsation Timing Variations        1170.000000
Radial Velocity                     823.354680
Transit                              21.102073
Transit Timing Variations            79.783500
Name: orbital_period, dtype: float64
"""





d = df_2.groupby('method')['orbital_period'].describe()
print(d)
"""
                               count           mean            std          min          25%           50%           75%            max
method
Astrometry                       2.0     631.180000     544.217663   246.360000   438.770000    631.180000    823.590000    1016.000000
Eclipse Timing Variations        9.0    4751.644444    2499.130945  1916.250000  2900.000000   4343.500000   5767.000000   10220.000000
Imaging                         12.0  118247.737500  213978.177277  4639.150000  8343.900000  27500.000000  94250.000000  730000.000000
Microlensing                     7.0    3153.571429    1113.166333  1825.000000  2375.000000   3300.000000   3550.000000    5100.000000
Orbital Brightness Modulation    3.0       0.709307       0.725493     0.240104     0.291496      0.342887      0.943908       1.544929
Pulsar Timing                    5.0    7343.021201   16313.265573     0.090706    25.262000     66.541900     98.211400   36525.000000
Pulsation Timing Variations      1.0    1170.000000            NaN  1170.000000  1170.000000   1170.000000   1170.000000    1170.000000
Radial Velocity                553.0     823.354680    1454.926210     0.736540    38.021000    360.200000    982.000000   17337.500000
Transit                        397.0      21.102073      46.185893     0.355000     3.160630      5.714932     16.145700     331.600590
Transit Timing Variations        3.0      79.783500      71.599884    22.339500    39.675250     57.011000    108.505500     160.000000
"""




e = df_2.groupby('method')['orbital_period'].describe().T
print(e)
"""
method   Astrometry  Eclipse Timing Variations        Imaging  Microlensing  ...  Pulsation Timing Variations  Radial Velocity     Transit  Transit Timing Variations
count      2.000000                   9.000000      12.000000      7.000000  ...                          1.0        553.00000  397.000000                   3.000000
mean     631.180000                4751.644444  118247.737500   3153.571429  ...                       1170.0        823.35468   21.102073                  79.783500
std      544.217663                2499.130945  213978.177277   1113.166333  ...                          NaN       1454.92621   46.185893                  71.599884
min      246.360000                1916.250000    4639.150000   1825.000000  ...                       1170.0          0.73654    0.355000                  22.339500
25%      438.770000                2900.000000    8343.900000   2375.000000  ...                       1170.0         38.02100    3.160630                  39.675250
50%      631.180000                4343.500000   27500.000000   3300.000000  ...                       1170.0        360.20000    5.714932                  57.011000
75%      823.590000                5767.000000   94250.000000   3550.000000  ...                       1170.0        982.00000   16.145700                 108.505500
max     1016.000000               10220.000000  730000.000000   5100.000000  ...                       1170.0      17337.50000  331.600590                 160.000000
"""