# def square(num):
#     return num ** 2

# square = lambda num : num**2

tools = []
tools.append(lambda num : num**2)
tools.append(lambda num : num**3)
tools.append(lambda num : num**4)

print(tools[0](5))
print(tools[1](5))
print(tools[2](5))

# One codeline
# No loops
# No code-blocking
# Can use simple if else

num =  15
state = "Greater" if num > 10 else "Lesser"
