

import numpy as np
import pandas as pd


# pandas serisinin icine numpy serisi yollayalim:
a = np.array([24,56,321,85,72])
b = pd.Series(a)
print("a: ", a)
print("b: ", b)
"""
a:  [ 24  56 321  85  72]

b:  
0     24
1     56
2    321
3     85
4     72
dtype: int32
"""

# indexlere ulasma:
print("b[0]     : ", b[0])
print("b[0:4]   : ", b[0:4])
"""
b[0]     :  24

b[0:4]   :  
0     24
1     56
2    321
3     85
dtype: int32
"""




abc = pd.Series([1,2,3,4,5], index=["a","b","c","d","e"])
print("abc: \n", abc)
"""
abc:
a    1
b    2
c    3
d    4
e    5
dtype: int64
"""
print(abc.index)            # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print(abc.items())          # <zip object at 0x000001F835A88E40>
print(list(abc.items()))    # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
print(abc.items)
"""
<bound method Series.items of a    1
                              b    2
                              c    3
                              d    4
                              e    5
                              dtype: int64>
"""
print(abc.keys)
"""
<bound method Series.keys of a    1
                             b    2
                             c    3
                             d    4
                             e    5
                             dtype: int64>
"""
print(abc.values)           # [1 2 3 4 5]
print("a" in abc)           # True
print("ali" in abc)         # False

# Fancy metodu:
liste = ["a", "b", "c"]
print(abc[liste])
"""
a    1
b    2
c    3
dtype: int64
"""


# Indexlerde degisiklik yapma:
print(abc["a"])             # 1
abc["a"] = 10               # abc["a"] indexine 10 degeri atanmistir.
print(abc["a"])             # 10
print(abc)
"""
a    10
b     2
c     3
d     4
e     5
dtype: int64
"""