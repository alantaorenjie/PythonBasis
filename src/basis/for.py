# Python的循环有两种，
# 一种是for...in循环，依次把list或tuple中的每个元素迭代出来
# 第二种循环是while循环，只要条件满足，就不断循环

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数：
a = list(range(5))
print(a)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环

sum = 0
n = 99
while (n > 0):
    sum += n
    n -= 2
print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：

names = ['Bart', 'Lisa', 'Adam']

for name in names:
    print("hello,", name)

i = 0
while (i < len(names)):
    print("hello,", names[i])
    i += 1

# break 跳出循环
# continue 跳出本次循环
