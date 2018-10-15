classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# 使用len()函数获取长度
print("长度为:", len(classmates))
print("最后一个元素为:", classmates[-1])

# 追加元素
classmates.append("Dav")
print("最后一个元素为:", classmates[-1])

classmates.insert(1, "rand1")
print("下表一元素为:", classmates[1])


# list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
print(L)

# list元素也可以是另一个list，比如：
# 数组嵌套数组
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s)
print(s[2][1])