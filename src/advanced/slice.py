# 切片
l = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素
print(l[0:3])
# 第一个元素是0，可以省略
print(l[:3])
# 取2-3个元素
print(l[1:3])
# 取最后一个
print(l[-1])
print(l[-2:])
print(l[-2:-1])

l = list(range(100))
print(l)
# 每5个取一次
print(l[::5])
