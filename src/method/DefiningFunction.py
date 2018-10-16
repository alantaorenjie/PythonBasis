# 定义函数

def abs_my(x):
    if not isinstance(x, int):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


print(abs_my(100))
print(abs_my(-100))


# 定义空函数
# pass的使用
def nof():
    pass


print(nof())

n = 200
if n > 100:
    pass

# 定义返回多个值的函数
import math


def move(x, y, step=1, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


print(move(x=0, y=0, step=1, angle=90))


# 一元二次方程
def qu(a, b, c):
    if b * b > 4 * a * c:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 / a
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 / a
        return x1, x2
    return 0


print(qu(2, 3, 1))
print(qu(1, 2, 3))


# m默认参数
def add_end(l=None):
    if l is None:
        l = []
    l.append('end')
    return l


print(add_end())
print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(calc(1, 2, 3, 4))


# 关键字参数
def person(name, age, **other):
    print("name:", name, 'age', age, 'other', other)


person("Alan", 23)
person("Alan", 23, sex='male')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数
def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)


print(person2('Bob', 23, job='Engineer'))

# *numbers  可变参数
# **other   关键字参数
# *, city   命名关键字参数
