import numpy as np
import pandas as pd

a = np.random.randint(1,30,(10,3))
b = pd.DataFrame(a,columns=["col1", "col2", "col3"])

print(b)
"""
   col1  col2  col3
0    27     7     2
1     4    23    18
2    25     7    26
3    13     8     2
4    23    20     1
5    22    29    19
6    17    12    14
7     1     3    29
8    24     2    25
9    20    16    21
"""

print(b["col2"])
"""
0     7
1    23
2     7
3     8
4    20
5    29
6    12
7     3
8     2
9    16
Name: col2, dtype: int32
"""

print(b["col2"][0:2])
"""
0    26
1     3
Name: col2, dtype: int32
"""

print(b.col2)
"""
0    26
1     3
2    26
3    19
4     4
5    29
6    21
7    19
8    17
9    18
Name: col2, dtype: int32
"""


# KOŞULLU DURUMLAR:

print(b[b.col2 > 20])
"""
   col1  col2  col3
3     4    23    20
9     3    29     5
"""

print(b[b.col2 > 20]["col2"])
"""
3    23
9    29
Name: col2, dtype: int32
"""

fancy = ["col1", "col2"]        # fancy metodu ile sorgulama
print(b[b.col2 > 20][fancy])
"""
   col1  col2
3     4    23
9     3    29
"""

print(b[(b.col2 < 25) & (b.col1 > 5)])
"""
   col1  col2  col3
0    20    17    21
2    11     1    19
3    28    10    17
4    19     9    13
5    26    19    14
6    17    16    22
7     7     7    29
9     6    16    12
"""

print(b.loc[(b.col2 < 25), ["col1", "col3"]])
"""
   col1  col3
0    25    18
1    11    15
2     7     2
3    29     6
5    14    24
6    15    10
7     4    24
8    18    25
9     5    23
"""

fancy = ["col1", "col3"]
print(b.loc[(b.col2 < 25)][fancy])       # fancy
"""
   col1  col3
0     3    17
1    25    11
2    28    12
3    14    24
4    26     2
6    15     8
8    15     1
"""