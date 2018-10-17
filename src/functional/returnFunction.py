# 返回函数
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
def lazy_sum(*agrs):
    def sum():
        ax = 0
        for a in agrs:
            ax += a
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)

# 调用函数f时，才真正计算求和的结果：
print(f())
print(f)


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def createCounter():
    i = 0

    def counter():
        nonlocal i
        i = i + 1
        return i

    return counter


counter = createCounter()
print(counter(), counter(), counter(), counter(), counter(), counter())


# 匿名函数
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
l = list(filter(lambda x: x % 2 == 1, range(1, 20)))
l = list(filter(lambda x: x & 1, range(1, 20)))

print(L, l)
