"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
 """

# Parameters are the variables in the function definition.
# Arguments are the data passed into the function.

def print_name(name): # name is parameter
    print(name)

print_name("Alex") # Alex is argument

# Positional arguments
def foo(a, b, c):
    print(f"a={a}, b={b}, c={c}")

foo(1, 2, 3) # positional arguments
foo(a=1, c=3, b=2) # keyword arguments
foo(1, c=3, b=2) # a is positional, b and c are keyword arguments

def foo(a, b, c, d=4):
    print(f"a={a}, b={b}, c={c}, d={d}")

foo(1, 2, 3,) # a=1, b=2, c=3, d=4
foo(1, b=2, c=3, d=100) # a=1, b=2, c=3, d=100


# Variable-length arguments (*args and **kwargs = any number of arguments)
def foo(a, b, *args, **kwargs):
    print (a,b) 
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7) # 1, 2, 3, 4, 5, six=6, seven=7

#force keyword arguments
def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, c=3, d=4) # 1, 2, 3, 4 # a and b are positional arguments, c and d are keyword arguments, force keyword arguments

def foo(*args, last): # last is a required keyword argument
    for arg in args:
        print(arg)
    print(last)

foo(1, 2, 3, 4, last=5) # 1, 2, 3, 4, 5


# unpacking into function arguments
def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list) # * unpacking list into positional arguments (list, tuple, set, dict), len of list must match len of parameters

my_dict = {'a': 1, 'b': 2, 'c': 3} #key names must match parameter names
foo(**my_dict) # ** unpacking dict into keyword arguments (len of dict must match len of parameters)


# Local vs. global arguments
def foo():
    global number # if not global, local variable is replaced by global variable 
    x = number
    number = 3 # local variable
    print("number inside function:", x)

number = 0 # global variable
foo()


""" ## Parameter passing
Python uses a mechanism, which is known as "Call-by-Object" or "Call-by-Object-Reference. The following rules must be considered:
- The parameter passed in is actually a reference to an object (but the reference is passed by value)
- Difference between mutable and immutable data types 

This means that:

1. Mutable objects (e.g. lists,dict) can be changed within a method.
  * But if you rebind the reference in the method, the outer reference will still point at the original object.
3. Immutable objects (e.g. int, string) cannot be changed within a method.
  * But immutable object CONTAINED WITHIN a mutable object can be re-assigned within a method. """

def foo(x):
    x = 5

var = 10  #immutable type int
foo(var)
print(var) # 10


def foo(a_list):
    a_list.append(4)

my_list = [1, 2, 3] # mutable object can be changed within a method
foo(my_list)
print(my_list) # [1, 2, 3, 4]


def foo(a_list):
    a_list.append(4)
    a_list[0] = -100

my_list = [1, 2, 3] # inner immutable object can be re-assigned within a method
foo(my_list)
print(my_list) # [-100, 2, 3, 4]



def foo(a_list):
    a_list = [200, 300, 400] #local variable
    a_list.append(4)
    a_list[0] = -100

my_list = [1, 2, 3]
foo(my_list)
print(my_list) # [1, 2, 3] outer reference will still point at the original object


###########################################################
def foo(a_list):
    a_list += [200, 300, 400]

my_list = [1, 2, 3]
foo(my_list)
print(my_list) # [1, 2, 3, 200, 300, 400] += is a shortcut for extend() method


def foo(a_list):
    a_list = a_list + [200, 300, 400]

my_list = [1, 2, 3]
foo(my_list)
print(my_list) # [1, 2, 3] + creates a new list, a_list is a local variable
