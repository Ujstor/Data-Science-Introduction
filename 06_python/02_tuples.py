# Tuple: ordered, immutable, allows duplicate elements

mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple = tuple(["Max", 28, "Boston"]) # tuple constructor

item = mytuple[0] 
print(item) # Max; prints first item in tuple, same as list

#mytuple[0] = "Tim" # TypeError: 'tuple' object does not support item assignment; tuples are immutable


for i in mytuple:
    print(i) # prints each item in the tuple

if "Max" in mytuple:
    print("yes") # yes if Max is in the tuple, no if not



mytuple = ('a', 'p', 'p', 'l', 'e', 'c')
print(len(mytuple)) # 6; length of tuple

print(mytuple.count('p')) # 2; counts the number of times p appears in the tuple

print(mytuple.index('p')) # 1; returns the index of the first occurrence of p in the tuple

my_list = list(mytuple) # converts tuple to list
print(my_list)

mytuple2 = tuple(my_list) # converts list to tuple
print(mytuple2)



# slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = a[2:5]
print(b) # (3, 4, 5)

b = a[::-1] # reverses the tuple

b = a[1:6:2] # (2, 4, 6) starts at index 1, ends at index 6, steps by 2


# unpacking
mytuple = "Max", 28, "Boston"
name, age, city = mytuple
print(name) # Max
print(age) # 28
print(city) # Boston Elements in the tuple must match the number of variables in the tuple

mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple
print(i1) # 0
print(i2) # [1, 2, 3]
print(i3) # 4 * is called a splat operator; it takes the rest of the elements in the tuple and puts them in a list


# tuples are faster and efficient than lists
import sys
mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes") # 104 bytes
print(sys.getsizeof(mytuple), "bytes") # 88 bytes

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) # 0.066 seconds
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # 0.011 seconds