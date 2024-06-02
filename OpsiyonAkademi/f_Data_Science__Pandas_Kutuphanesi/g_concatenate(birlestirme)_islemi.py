



import numpy as np
import pandas as pd



a = np.random.randint(1,30, size=(5,3))
print("a:\n", a)
"""
a:
 [[27  5 21]
 [23 26 19] 
 [24 12 21] 
 [26 14 11] 
 [27 24 27]]
"""
b = pd.DataFrame(a, columns=["col1", "col2", "col3"])
print("b:\n", b)
"""
b:
    col1  col2  col3
0    27     5    21 
1    23    26    19 
2    24    12    21 
3    26    14    11 
4    27    24    27
"""
c = b + 50
print("c:\n", c)
"""
c:
    col1  col2  col3
0    77    55    71
1    73    76    69
2    74    62    71
3    76    64    61
4    77    74    77
"""

# Concat ile birlestirme:
d = pd.concat([b,c])
print("d:\n", d)
"""
d:
    col1  col2  col3
0    27     5    21
1    23    26    19
2    24    12    21
3    26    14    11
4    27    24    27
0    77    55    71
1    73    76    69
2    74    62    71
3    76    64    61
4    77    74    77
"""

# Satir indekslerini duzenleme:
e = pd.concat([b,c], ignore_index=True)
print("e:\n", e)
"""
e:
    col1  col2  col3
0    27     5    21
1    23    26    19
2    24    12    21
3    26    14    11
4    27    24    27
5    77    55    71
6    73    76    69
7    74    62    71
8    76    64    61
9    77    74    77
"""

# Sutun indekslerindeki birlesme bozulmalari:
f = pd.DataFrame(a, columns=["col1", "col2", "xyz"])
print("f:\n", f)
"""
f:
    col1  col2  xyz
0    27     5   21
1    23    26   19
2    24    12   21
3    26    14   11
4    27    24   27
"""
g = pd.concat([b,f])
print("g:\n", g)
"""
g:
    col1  col2  col3   xyz
0    27     5  21.0   NaN
1    23    26  19.0   NaN
2    24    12  21.0   NaN
3    26    14  11.0   NaN
4    27    24  27.0   NaN
0    27     5   NaN  21.0
1    23    26   NaN  19.0
2    24    12   NaN  21.0
3    26    14   NaN  11.0
4    27    24   NaN  27.0
"""

# Sutun indekslerini duzenleme: (Bozulmalarin olmamasi icin sutun kesisim indekslerini birlestirme icin kullanip, digerlerini almaz)
h = pd.concat([b,f], join="inner")
print("h:\n", h)
"""
h:
    col1  col2
0    27     5
1    23    26
2    24    12
3    26    14
4    27    24
0    27     5
1    23    26
2    24    12
3    26    14
4    27    24
"""

# Sutun indexleri ile birlikte satir indexlerinide duzenleme:
i = pd.concat([b,f], join="inner", ignore_index=True)
print("i:\n", i)
"""
i:
    col1  col2
0    27     5
1    23    26
2    24    12
3    26    14
4    27    24
5    27     5
6    23    26
7    24    12
8    26    14
9    27    24
"""
