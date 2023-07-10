# function and class decorators

# decorator is a function that takes another function as an argument and returns a new function
# without changing the source code of the original function that was passed in
# allow you to extend and modify the behavior of a callable (functions, methods, and classes) without permanently modifying the callable itself

""" @my_decorator
def dosomething():
    pass """

def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@start_end_decorator
def print_name():
    print("Alex")

print_name() # Alex
print_name = start_end_decorator(print_name) # Start, Alex, End
print_name() # Start, Alex, End



import functools
def start_end_decorator2(func):
    @functools.wraps(func) # to fix the problem of print(help(add5)) and print(add5.__name__)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator2
def add5(x):
    return x + 5

add5(10) # TypeError: wrapper() takes 0 positional arguments but 1 was given; add *args and **kwargs to wrapper() to fix this
# and return result

result = add5(10)
print(result) # Start, End, 15

print(help(add5)) # add5(x)
print(add5.__name__) # wrapper; to fix this, use functools.wraps



# decorators with arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alex") # Hello Alex, Hello Alex, Hello Alex



#nested decorators
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper



@debug
@start_end_decorator2
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello("Alex")

""" Calling say_hello('Alex')
Start
Hello Alex
End
'say_hello' returned 'Hello Alex' """


#class decorators (for maintaining and update state)
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()

""" This is executed 1 times
Hello
This is executed 2 times
Hello
This is executed 3 times
Hello """

#use cases: logging, timing, register plugins, enforcing access control and authentication, etc.