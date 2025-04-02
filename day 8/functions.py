def greet(name="guest"):
    print(f"hello,{name}")

greet()



def power(base,exponent):
    return base ** exponent

print(power(2,3))

def multiply(a,b):
    return a * b
print(multiply(5,7))


def outer():
    print("this is outer funnction")
    def inner():
        print("this is inner function")
    inner()
outer()


def global_function():
    print("this is a global function")
global_function()

def another_function():
    global_function()
another_function()
    