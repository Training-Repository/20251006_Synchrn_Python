fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
bowl = []
for x in fruits:
    if 'a' in x:
        bowl.append(x)
print(bowl)

bowl2 = [x        for x in fruits        if 'a' in x]
print(type(bowl2), bowl2)


obj = [fr          for fr in fruits  if 'a' in fr]; print(type(obj), obj)
obj = {fr          for fr in fruits  if 'a' in fr}; print(type(obj), obj)
obj = {fr:len(fr)  for fr in fruits  if 'a' in fr}; print(type(obj), obj)
obj = tuple(fr     for fr in fruits  if 'a' in fr); print(type(obj), obj)
obj = (fr          for fr in fruits  if 'a' in fr); print(type(obj), obj)

for x in obj:
    print(x)


#########################################################################################
a = 10
b = "Test"
print(dir(a))
print(dir(b))
print()

print("Public Members ->", [member   for member in dir(a)  if member.startswith("_") == False])
print("Public Methods ->", [member   for member in dir(a)  if callable(getattr(a, member)) and member.startswith("_") == False])
