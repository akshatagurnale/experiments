def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4)



def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"(key):(value)")
print_info(name="Alice",age=30)



def multiply(a,b):
    return a*b
result=multiply(4,5)
print(result)


def my_function():
    x = 10 #local variable
    print(x)
my_function()

import os
print(os.cwd())


def my_decorators(func):
    def wrapper():
        print("something is happening before the function")
        func()
        print("Something is happenening after the function is ")
        return wrapper


print(math.sqrt(16))
      



@my_decorator
def say_hello():
    print("Hello")
say_hello()
