# 列表生成式

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
l = [x * x for x in range(1, 11)]
print(l)

l = [x * x for x in range(1, 11) if x % 2 == 0]
print(l)

l = [m + n for m in 'ABC' for n in 'XYZ']
print(l)

import os

l = [n for n in os.listdir('.')]
print(l)

L = ['Hello', 'World', 18, 'Apple', None]
l = [s.lower() for s in L if isinstance(s, str)]
print(l)
