#region Basic Structure
# def Foo():
#     pass

# # This function add the data and retuns sum
# def add(a: int, b: int) -> int:
#     """This function add the data and retuns sum
#     Usage: add(<data1>, <data2>) --> returns sum"""
#     sum = a + b
#     return sum
#     # diff = a - b
#     # return sum, diff

# # result = add(7, 5)
# # print(type(result), result)

# print(add("Test", "String"))
# # print(add("Test", 3))
# # print(add("1", 3))

# fn = add

# print(fn.__doc__)
#endregion

#region Arguments 1 ############################################

# def add(a, b, c=0):
#     print(f"{a = }, {b = }, {c = }")
#     sum =  a + b + c
#     return sum

# print(add(2, 3))        # Positional args

# print(add(a=2, b=3))    # Named args / Keyworded args
# print(add(b=3, a=2))

# print(add(a=2, b=3, c=5))   # Using default args

#endregion

#region Packing/Unpacking

# lst = [1, 2, 3]
# # a = lst[0]
# # b = lst[1]
# # c = lst[2]

# a, b, c = 1, 2, 3
# a, b, c = lst       # Upacks

# print(f"{a = }, {b = }, {c = }")


# def add (a, b, c):
#     return a + b + c


# print(add(*lst))


# lst = [1, 2, 3, 4, 5]
# a, *b, c = lst
# print(f"{a = }, {b = }, {c = }")

# first, *_, last = lst
# print(f"{first = }, {last = }")



# for _ in range(5):
#     print("Hi")


# a = 10
# b = a
# 10 = b


# def add(a, b, *data):                                           # Variable Arguments
#     print(f"{a = }, {b = }, {data = }, {type(data) = }")
#     sum =  a + b
#     for val in data:
#         sum += val
#     return sum

# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))
# print(add(1, 2, 3, 4, 5))


# def PrintEmp(ceo, cto, **emps):     # Keyworded variable arg list OR kwargs
#     print(f"{ceo = }")
#     print(f"{cto = }")
#     for k, v in emps.items():
#         print(k, "=", v)

# PrintEmp("Rakesh", "Pravin")
# PrintEmp("Rakesh", "Pravin", cfo="Vishaal", cxo="Vineet")

#endregion