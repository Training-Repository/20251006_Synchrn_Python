# def Logger(func):
#     def wrapper():
#         print(f"Enter {func.__name__}")
#         func()
#         print(f"Exit {func.__name__}")
#     return wrapper



# def SayHi():
#     print("Hi there")

# # fn = SayHi
# # SayHi = wrapper

# def SayHello():
#     print("Hello there!")



# SayHi = Logger(SayHi)
# SayHello = Logger(SayHello)


# #------------------------------------------


# SayHi()
# # fn()
# # wrapper()
# # print(type(SayHi))

# SayHello()

##################################################################


def Logger(func):
    def wrapper(*args, **kwargs):
        wrapper.__doc__ = func.__doc__
        print(f"Enter {func.__name__}")
        ret_data = func(*args, **kwargs)
        print(f"Exit {func.__name__}")
        return ret_data
    return wrapper


@Logger
def SayHi():
    """Says Hi"""
    print("Hi there")

# SayHi = Logger(SayHi)


@Logger
def SayHello():
    """Says Hello"""
    print("Hello there!")

# SayHello = Logger(SayHello)


@Logger
def add(a, b):
    """Adds  data"""
    return a + b

#------------------------------------------


SayHi()
SayHello()
print(add(1, 2))

print(SayHi.__doc__)
print(add.__doc__)