# Unordered Mutable Collection of unique Non-homogeneous key-value pairs
# Key - Immutable/Hashable
# Value - Can be either mutable or immutable

lst = [1, 2, 3, 4, 5]

d1 = {}
d1 = dict()
d1 = dict(a=10, b=20, c=30)
d1 = {'a': 10, 'b': 20, 'c': 30}
d1 = dict().fromkeys(lst)
print(type(d1), d1)


d1 = {'a': 10, 'b': 20, 'c': 30}
print(len(d1))

for val in lst:
    print(val, end=', ')
print()

for val in d1:
    print(val, end=', ')
print()

lst2 = list(d1)
print(lst2)

for val in d1.keys():
    print(val, end=', ')
print()

for val in d1.values():
    print(val, end=', ')
print()

for k, v in d1.items():
    print(k, "->", v)
print()

print('a' in d1)
print('d' in d1)

print(d1['a'])
d1['a'] = 100
d1['d'] = 400

key = 'e'
if key not in d1:
    d1[key] = 500
print(d1)

try:
    print(d1['f'])
except KeyError:
    print("key not found!")

if 'f' in d1:
    print(d1['f'])

print(d1.get('f'))


d2 = {'a':1000, 'b': 2000, 1:10000}
print(d2)

d1.update(d2)
print(d1)
print(d1.pop('e'))
# print(d1.pop('e'))

it = iter(d1)
print(type(it))

try:
    while True:
        print(next(it))
except StopIteration:
    print("That's all the keys there are")
    