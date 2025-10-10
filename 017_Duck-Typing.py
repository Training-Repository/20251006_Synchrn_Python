def add(a: int, b: int) -> int:
    print("\n\nStarting the operation...")
    # return int(a) + int(b)
    return a + b  # a.__add__(b)  OR   __add__(a, b)


print(add(1, 2))
print(add(1.1, 2.2))
print(add("Test", "String"))
# print(add(1, "2"))

print("\n\n", "="*45)

class MyClass:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Data --> {self.data}"
    
    def __repr__(self):
        return f"Data --> [{self.data}]" + super().__repr__()
    
    def __add__(self, other):
        return MyClass(self.data + other.data)
    



obj1 = MyClass(10)

print(obj1)
print(str(obj1))
print(obj1.__str__())
print(obj1.__repr__())
print(repr(obj1))

print(dir(obj1))


print(obj1.data)

obj2 = MyClass([1, 2, 3, 4, 5])
print(obj2.data)

obj3 = MyClass(20)


print(add(obj1, obj3))