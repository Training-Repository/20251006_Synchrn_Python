print("Global 1")

def add(a, b):
    res = a + b
    sum = res
    return sum

print("Global 2")

def seperator(len):
    print("=" * len)

def calc():
    x = 10
    y = 20
    result = add(x, y)
    # load x to register
    # load y to register
    # load addr of 'add' to register
    # 'call' executes
    # read register to populate 'result'
    # move to next python statement 
    seperator(45)
    print("result =", result)
    seperator(45)

print("Global 3")

calc()

print("Global 4")
