# Ordered Immutable Collection of Non-homogeneous objects

lst = [1, 2, 3, 4, 5]
tup1 = (1, 2, 3, 4, 5)
tup2 = tuple()
tup3 = tuple(lst)


print(type(tup1), tup1)
print(type(tup2), tup2)
print(type(tup3), tup3)

tup4 = ()
print(type(tup4), tup4)

lst = [1]
tup5 = (1,)
print(type(tup5), tup5)

