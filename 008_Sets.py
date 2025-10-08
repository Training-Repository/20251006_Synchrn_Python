# Unordered Mutable Collection of unique Non-homogeneous keys
# Key - Hashable entity
# Hashability --> requires the object to be an immutable

a1 = 10
a2 = 10.5
b = "Test"
c = [1, 2, 3]

print(hash(a1))
print(hash(a2))
print(hash(b))
# print(hash(c))

# s1 = {} # <-- Results in a dictionary
s1 = set()
s2 = {1, 2, 3}
s3 = set(c)
print(type(s1))

d = [1, 2, 2, 3, 3, 4, 5]
s4 = set(d)
s4.add(7)
s4.add(8)
s4.add(5)
print(s4)

s5 = set(b)
s5.add('c')
s5.add(10)
s5.update(s4)
print(s5)

s2.update(['b', 'c', 's'])

print(s5 & s2)
print(s5.intersection(s2))

print(s2 | s5, s2.union(s5))

print(s5 - s2, s5.difference(s2))
print(s5 ^ s2, s5.symmetric_difference(s2))

