# loc ve iloc secim yapmaya yarar.
# loc --> Tanimlandigi haliyle secim yapar.
# iloc --> Indexleme mantigi ile secim yapar.

import pandas as pd
import numpy as np


# NOT: Seriler random olusturuldugu icin veriler degisken olacaktir. Onemli olan sutun ve satir basliklariyla yapilan islemlerdir.

a = np.random.randint(1,30, size=(10,3))
b = pd.DataFrame(a, columns=["col1", "col2", "col3"])
print(b)
"""
   col1  col2  col3
0    21    26    29
1     1    18     7
2    26    22    28
3    15     3    28
4    28    16    22
5    11    27    25
6    14     1    12
7    14     1    25
8    21    19    28
9     2    16    25
"""

# loc --> Tanimlandigi haliyle secim yapar. slicing veya index den farkli olarak son degeri dahil eder.
c = b.loc[0:5]          # burada 0 da 5 te araliga dahil edilir. 5 ide dahil etmesinden dolayi slicing veya index den farklidlr.
print(c)
"""
Belirlenen araliktaki degerleri alir.
   col1  col2  col3
0    12    24    13
1    11    20    29
2     4    18    19
3     1    15     1
4    15     6     3
5    18     2    17
"""


# iloc --> Indexleme mantigi ile secim yapar.
d = b.iloc[0:5]         # burada 0 araliga dahil edilirken, 5 araliga dahil edilmemistir.
print(d)
"""
   col1  col2  col3
0    16    19    11
1     4    20    28
2     2    16     9
3    11    10    14
4     3    13     4
"""



# loc: Belirli bir araliktaki sutunlari alma:
e = b.loc[0:5, "col2"]
print(e)
"""
0    19
1    20
2    16
3    10
4    13
5     4
Name: col2, dtype: int32
"""



# iloc: Belirli bir araliktaki sutunlari alma:
f = b.iloc[0:3, :2]     # Burada 0dan 3e ve 0dan 2ye seklinde bir aralik secimi yapilmistir. Ilk aralik satir index araligi iken; ikinci aralik sutun index araligi icindir.
print(f)
"""
   col1  col2
0    16    19
1     4    20
2     2    16
"""


# iloc: Belirli bir araliktaki sutunlari alma:
g = b.iloc[0:3, "col2"]     # loc formatinda araligi bu sekilde belirleyebilirken, iloc icin bu formatta aralik secilemez hata verir.
# ValueError: Can only index by location with a [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array]
# Bu hatanin aciklamasi: integer, integer slice, integer listesi ve boolean veri tiplerini alabilir. (String bir ifade alamaz.)
print(g)
"""
# ValueError: Can only index by location with a [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array]
# Bu hatanin aciklamasi: integer, integer slice, integer listesi ve boolean veri tiplerini alabilir. (String bir ifade alamaz.)

ille de sadece o aralik gorulmek isteniyorsa integer index araligi girilerek string ifade olmadan istenen verilere ulasilabilir.
Yani;

g = b.iloc[0:3, "col2"] ==> g = b.iloc[0:3, 1:2]        # Burada col1 ==> 0:1, col2 ==> 1:2 ve col3 ==> 2:3 araliklari secilebilir.

kullanilirsa col2 sutunu secilmis olur. Ya da diger bir yontem indexleme metodudur:
"""

h = b.iloc[0:3]["col2"]
print(h)
"""
0    19
1    28
2    10
Name: col2, dtype: int32
"""