# 排序
print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('aisa', 88)]
print(l)


def sortName(t):
    return str(t[0]).lower()


print(sorted(l, key=sortName))
