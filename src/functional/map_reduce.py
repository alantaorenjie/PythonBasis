# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。


def f(x):
    return x * x


m = map(f, [1, 2, 3])

print(list(m))
print(tuple(m))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比方说对一个序列求和，就可以用reduce实现：
from functools import reduce


def add(a, b):
    return a + b


sum = reduce(add, list(range(1, 11)))
sum2 = reduce(add, [1, 3, 5, 7, 9])
print(sum)
print(sum2)


def fn(a, b):
    return a * 10 + b


x = reduce(fn, [1, 3, 5, 7, 9])

print(x)


def char2Num(a):
    return int(a)


m = map(char2Num, '13579')
print(list(m))
x = reduce(fn, map(char2Num, '13579'))

print(x)

s = ['adam', 'LISA', 'barT']


def toName(s: str):
    r = s.lower()[1:len(s)]
    l = s[0:1].upper()
    m = l + r

    # 或者使用系统函数capitalize
    # m = s.capitalize()
    return m


m = list(map(toName, s))
print(m)


def prod(a, b):
    return a * b


s = reduce(prod, [1, 3, 5, 7, 9])
print(s)
