def Baz():
    print("Baz")
    raise FloatingPointError("Didn't see that coming")
    raise TypeError("User has provided incorrect type of data")
    raise ValueError("Invalid value provided by user")
    i = 10/0
    print("Exiting Baz")

def Bar():
    print("Bar")
    Baz()
    print("Exiting Bar")

def Foo():
    print("Foo")
    try:
        Bar()
    except ZeroDivisionError as ex:
        print(f"Handling the ZeroDivErr --> {ex!r}")
    except (ValueError, TypeError) as ex:
        print(f"{ex!r}")
    except Exception as ex:
        print(f"Unexpected Error --> {ex!r}")
        print("Releasing locks...")
        print("Releasing connections...")
        raise
    print("Exiting Foo")

def Main():
    print("Main")
    Foo()
    print("Exiting Main")

Main()