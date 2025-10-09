from collections import namedtuple

tup1 = ("Manish", 12, 7)
print(tup1[0], tup1[1], tup1[2])

Student = namedtuple('Student', ['name', 'age', 'standard'])

s1 = Student("Abhijeet", 16, 10)
print(type(s1), s1)
print(s1[0], s1[1], s1[2])
print(s1.name, s1.age, s1.standard)


tup2 = (10, 20)

Point = namedtuple("Point", 'x y')
p1 = Point(10, 20)
print(p1)
print(p1.x, p1.y)