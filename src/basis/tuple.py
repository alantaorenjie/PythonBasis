# 另一种有序列表叫元组：tuple。tuple和list非常类似，
# 但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

classmates = ('Michael', 'Bob', 'Tracy')

# 使用小括号，当tuple只有一个元素时需要注意,多加一个逗号

s = ("213")
t = ("213",)

print(s)
print(t)


# 练习
# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[1][0])