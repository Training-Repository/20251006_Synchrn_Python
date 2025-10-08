# a = 10

# # Value
# print(a)

# # Type
# print(type(a))

# # ID
# print(id(a))


# b = a
# print(b)
# print(type(b))
# print(id(b))

# print(a is b)

# print("=" * 40)


# print(id(a), id(b), sep="\n")
# print()

# a += 1
# print(id(a), id(b), sep="\n")
# print()

# b += 1
# print(id(a), id(b), sep="\n")
# print()

#--------------------------------------------------



# s1 = "Test"
# print(s1, id(s1))
# s1 += "String"
# print(s1, id(s1))

# print(s1[0])
# # s1[0] = 'B'  # <-- ERROR
# # print(s1)


s1 = "Test"
s2 = "Te"
s2 += "st"

print(s1 == s2, s1, s2)
print(s1 is s2, id(s1), id(s2))
