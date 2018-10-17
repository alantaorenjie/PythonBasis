# 偏函数

import functools

# 定义一个偏函数
int2 = functools.partial(int, base=2)

print(int2('0101010'))

# 所以，简单总结functools.partial的作用就是，
# 把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
