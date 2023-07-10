result = 5 * 7 #multiplication
result = 5 ** 2 #exponentiation

zeros = [0] * 10  #create element 0, 10 times
print(zeros) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

zeros = [0, 1] * 10 # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

zeros = (0, 1) * 10 #tuple

zeros = "AB" * 10 #string
print(zeros) #ABABABABABABABABABAB



#args and kwargs
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args: #args is a tuple
        print(arg)
    for key in kwargs: #kwargs is a dict
        print(key, kwargs[key])


def foo(a, b, *, c): #after * all arguments are keyword arguments
    print(a, b, c)
foo(1, 2, c=3) 


#unpacking into function arguments
def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list) #unpacking list into positional arguments

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict) #unpacking dict into keyword arguments


#unpacking containers
numbers = [1, 2, 3, 4, 5, 6]

*beginning, last = numbers
print(beginning) # [1, 2, 3, 4, 5]
print(last) # 6
# it unpacks the list into beginning and last, beginning is a list, last is an integer
#if used with tuple, unpack into list

beginning, *last = numbers
print(beginning) # 1
print(last) # [2, 3, 4, 5, 6]

beginning, *middle, last = numbers
print(beginning) # 1
print(middle) # [2, 3, 4, 5]
print(last) # 6

beginning, *middle, second_last, last = numbers
print(beginning) # 1
print(middle) # [2, 3, 4]
print(second_last) # 5
print(last) # 6


#merge
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
new_list = [*my_tuple, *my_list] #unpacking tuple and list (or set) into new_list
print(new_list) # [1, 2, 3, 4, 5, 6]

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
my_dict = {**dict_a, **dict_b} #unpacking dict into my_dict
print(my_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}




