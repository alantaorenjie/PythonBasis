# Dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d2 = {74: "Michael", 'Bob': 75, 'Tracy': 85}
print(d2[74])

# 获取
print(d.get('Michael'))

# 删除
print(d.pop('Michael'))
print(d)

# Set
print('\nSet')
s = set([1, 2, 3])
print(s)

s = set([1, 1, 2, 2, 3, 3])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

for x in s:
    print(x)
