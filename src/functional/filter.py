# filter

# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

def delete(a: int):
    return a % 2 == 1


a = list(filter(delete, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)


def loop(a):
    s = str(a)
    # 字符串切片将字符串反转
    s2 = s[::-1]
    return s == s2

a = list(filter(loop, list(range(10,200))))
print(a)