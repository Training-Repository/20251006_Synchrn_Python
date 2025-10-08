# Ordered Mutable Collection of Non-homogeneous objects

l1 = []
l2 = list()
l3 = [1, 2, 3, 4, 5]
l4 = list(l3)

s1 = "Test String"
l5 = list(s1)

print(l1, l2, l3, l4, l5, sep='\n')

l6 = l3
l7 = list(l3)
print(f"{id(l3) = }")
print(f"{id(l6) = }")
print(f"{id(l7) = }")

l8 = [1, 2, "Test", 5, 2.75]
print(type(l8), l8)

# Members
print(l7)
l7.append('a')
l7.append('b')
print(l7)

l7.insert(2, 'c')
print(l7)

l7.extend(l8)
print(l7)

print(l7.count(5))
print('Test' in l7)

l7.remove(1)
print(l7)

print(l3)
l3.clear()
print(l3)

print(l7.index(2))
print(l7.index(2, 1))

print(l7.pop(3))
print(l7)

print(l7.count(5))

l7.reverse()
print(l7)

l7.remove('Test')
l7.remove('a')
l7.remove('b')
l7.remove('c')

l7.sort()
print(l7)



print(len(l7))
print(min(l7))
print(max(l7))
print(sum(l7))


print("\n\n\n", "="*45)
s1 = "Manish"
s2 = s1
s1 += "!!"
print(s1, s2, sep='\n')


l1 = [1, 2, 3, 4, 5]
l2 = l1
l1[1] = 200
print(l1, l2, sep='\n')


l3 = list(l1)
l4 = l1[:]
l1[2] = 300

print(l1, l3, l4, sep='\n')
