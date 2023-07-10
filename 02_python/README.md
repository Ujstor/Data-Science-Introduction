# Intermediate Python Programming <!-- omit in toc -->




## Here's a summary of some of the intermediate-level topics for Python programming covered in this [YouTube](https://www.youtube.com/watch?v=HGOBQPFzWKo&t=213s) video. <!-- omit in toc -->
<br/>

1. Data types: lists, tuples, dictionaries, sets, and strings
2. Collections: specialized data structures like named tuples, deque, counter, and defaultdict
3. Itertools: functions that work with iterable data types to create efficient iterators
4. Lambda functions: anonymous functions that can take any number of arguments and return a single value
5. Exceptions and Errors: how to handle unexpected events or errors that occur during program execution
6. Logging: techniques for logging program output and error messages
7. JSON: working with JSON data using the built-in json module
8. Random numbers: generating random numbers for various use cases
9. Decorators: modifying or enhancing the functionality of existing functions using decorators
10. Generators: creating iterable sequences using generator functions
11. Threading vs Multiprocessing: understanding the difference between these two techniques for running multiple tasks simultaneously
12. Multithreading: using threads to execute multiple tasks concurrently within a single program
13. Multiprocessing: running multiple processes in parallel to increase program performance
14. Function Arguments: how to pass arguments to functions and work with default arguments, keyword arguments, and variable-length argument lists
15. Shallow vs Deep Copying: understanding the difference between these two techniques for copying objects in Python
16. Context Managers: using the "with" statement to manage resources and ensure proper clean-up of objects after use.
17. Object-Oriented Programming: an introduction to object-oriented programming concepts like classes, objects, inheritance, and polymorphism
<br/>
<br/>

<!-- omit in toc -->
## Content: 





- [1. Lists](#1-lists)
- [2. Tuples](#2-tuples)
- [3. Dictionaries](#3-dictionaries)
- [4. Sets](#4-sets)
- [5. Strings](#5-strings)
- [6. Collections](#6-collections)
- [7. Itertools](#7-itertools)
- [8. Lambda Functions](#8-lambda-functions)
- [9. Exceptions and Errors](#9-exceptions-and-errors)
- [10. Logging](#10-logging)
- [11. Json](#11-json)
- [12. Random numbers](#12-random-numbers)
- [13. Decorators](#13-decorators)
- [14. Generators](#14-generators)
- [15. Threading and Multiprocessing](#15-threading-and-multiprocessing)
- [16. Threading](#16-threading)
- [17. Multiprocessing](#17-multiprocessing)
- [18. Function Arguments](#18-function-arguments)
- [19. The Asterisk (\*) Operator](#19-the-asterisk--operator)
- [20. Shallow vs Deep Copying](#20-shallow-vs-deep-copying)
- [21. Context Managers](#21-context-managers)
- [22. Object Oriented Programming](#22-object-oriented-programming)


## Cheat Sheets <!-- omit in toc -->
Python cheat sheets are a useful reference tool for programmers looking to improve their coding skills. They provide a condensed summary of essential syntax and functions, making it easier to write code quickly and accurately. Cheat sheets cover a variety of topics, including data types, control structures, functions, modules, and libraries. Whether you are a beginner or an experienced programmer, Python cheat sheets are a valuable resource to have at your fingertips.
<br/>
<br/>

### [Python Cheat Sheet [pdf 1]](https://courses.cs.washington.edu/courses/cse163/22wi/resources/python-cheat-sheet.pdf) 

### [Python Cheat Sheet [pdf 2]](https://faculty.ncssm.edu/~morrison/resources/python/py_cheat.pdf) 
### [Python Crash Course [Book summary]](https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf) 
<br/>
<br/>

## 1. Lists
[🔼 Back to top](#content)

```python

```python
# lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]
print(mylist)



item = mylist[0]
print(item) 

for i in mylist:
    print(i) # prints each item in the list



if "banana" in mylist:
    print("yes")
else:
    print("no") # yes if banana is in the list, no if not


print(len(mylist)) # 3; length of list



mylist.append("lemon")
print(mylist) # adds lemon to the end of the list


mylist.insert(1, "blueberry")
print(mylist) # inserts blueberry at index 1



item = mylist.pop()
print(item) # removes last item in list



item = mylist.remove("cherry")
print(mylist) # removes cherry from list


item = mylist.clear()
print(item) # clears the list


mylist.reverse()
print(mylist) # Changes the list; uses in place modification

mylist.sort()
print(mylist) # Changes the list; uses in place modification

mylist = [4, 3, 1, -1, -5, 10]
print(mylist)
new_list = sorted(mylist)
print(new_list) 


mylist = [0] * 5
print(mylist) # [0, 0, 0, 0, 0] duplicates the list 5 times

mylist2 = [1, 2, 3, 4, 5]

new_list = mylist + mylist2
print(new_list) # [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]


#slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a) # [2, 3, 4, 5]

#step
b = mylist[::2] # [start:end:step]
print(b) # [1, 3, 5, 7, 9] ; skips every other element


list_org = ["banana", "cherry", "apple"]
list_cpy = list_org # this is not a copy, it is a reference to the original in memory
list_cpy.append("lemon")
print(list_cpy) # ['banana', 'cherry', 'apple', 'lemon']
print(list_org) # ['banana', 'cherry', 'apple', 'lemon']

# to make a copy
list_cpy = list_org.copy()
list_cpy = list(list_org)
list_cpy = list_org[:]

# list comprehension
a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a] 
print(b) # [1, 4, 9, 16, 25, 36] ; squares each element in a and adds it to b in a new list [expression for item in list]
```
<br/>
<br/>

## 2. Tuples
[🔼 Back to top](#content)
```Python
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
```
<br/>
<br/>

## 3. Dictionaries
[🔼 Back to top](#content)
```Python
# Dictionary: key-value pairs, unordered, mutable

my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)

my_dict2 = dict(name="Mary", age=27, city="Boston") # dict constructor
print(my_dict2)

value = my_dict["name"]
print(value) # Max; prints value of key name


# dictionaries are mutable; add or change items
my_dict["email"] = "max@mail.com"
print(my_dict) # adds email to dictionary

my_dict["email"] = "madmax@mail.com"
print(my_dict) # overwrites email in dictionary


# delete items
del my_dict["name"]
print(my_dict) # deletes name from dictionary

my_dict.pop("age")
print(my_dict) # deletes age from dictionary

my_dict.popitem()
print(my_dict) # deletes last item from dictionary



my_dict = {"name": "Max", "age": 28, "city": "New York"}
if "name" in my_dict:
    print(my_dict["name"]) # Max;  checks if key name is in dictionary, if not, prints default value


try:
    print(my_dict["lastname"]) # KeyError: 'lastname'; checks if key lastname is in dictionary, if not, prints error
except:
    print("Error")


# loop through dictionary
for key in my_dict:
    print(key) # prints each key in the dictionary

for key in my_dict.keys():
    print(key) # prints each key in the dictionary

for value in my_dict.values():
    print(value) # prints each value in the dictionary

for key, value in my_dict.items():
    print(key, value) # prints each key and value in the dictionary


# copy dictionary
my_dict_cpy = my_dict # copies the reference to the dictionary
print(my_dict_cpy)

my_dict_cpy["email"] = "max@mail.com"
print (my_dict)
print(my_dict_cpy) # adds email to dictionary, and modifies both dictionaries, with assignment operator '=' both dictionaries point to the same reference in memory

my_dict_cpy = my_dict.copy() # actual copies the dictionary
my_dict_cpy = dict(my_dict) # copies the dictionary and creates a new dictionary

# update method
my_dict = {"name": "Max", "age": 28, "email": "max@mail.com"}
my_dict2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict2) 
print(my_dict) # updates my_dict with my_dict2, overwrites values in my_dict with values in my_dict2, if keys are the same


my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict) # {3: 9, 6: 36, 9: 81}; keys can be numbers

mytuple = (8, 7)
my_dict = {mytuple: 15}
print(my_dict) # {(8, 7): 15}; keys can be tuples
# We can't use lists as keys because lists are mutable and can be changed, it not hashable. Tuples are immutable and can't be changed, so they can be used as keys.
```
<br/>
<br/>

## 4. Sets
[🔼 Back to top](#content)
```Python
# Set: unordered collection of unique elements, mutable (can be changed)

myset = {1, 2, 3, 4, 5, 5, 5} # only unique elements
print(myset) # {1, 2, 3, 4, 5}

myset = set([1, 2, 3, 4, 5, 5, 5]) # set constructor
print(myset) # {1, 2, 3, 4, 5}

myset = set("Hello")
print(myset) # {'e', 'H', 'l', 'o'}; order is not guaranteed

myset = {} # this is a dictionary, not a set
print(type(myset)) # <class 'dict'>


myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)

print(myset) # {1, 2}

myset.discard(3) # does not throw an error as remove if 3 is not in the set
myset.clear() # clears the set

myset = {1, 2, 3, 4, 5, 6}
myset.pop() # removes a random element from the set
print(myset) # {2, 3, 4, 5, 6}

for i in myset:
    print(i) # prints each element in the set

if 1 in myset:
    print("yes") # yes if 1 is in the set, no if not
else:
    print("no")


# Union
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) # combines the sets
print(u) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}



# Intersection
i = odds.intersection(primes) # returns the common elements
print(i) # {3, 5, 7}

i = evens.intersection(odds)
print(i) # {}



# Difference
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 3, 5, 7, 9, 11, 13, 15}

diff = setA.difference(setB) # returns the elements in setA that are not in setB
print(diff) # {8, 2, 4, 6}

diff = setB.difference(setA) # returns the elements in setB that are not in setA
print(diff) # {11, 13, 15}


# Symmetric Difference
diff = setA.symmetric_difference(setB) # returns the elements that are not in both sets
print(diff) # {2, 4, 6, 8, 11, 13, 15}

# Union, intersection, difference will not modify the original sets, they will return a new set



# Update
setA.update(setB) # adds the elements from setB to setA without duplicates
print(setA) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15}

# intersection_update

setA.intersection_update(setB) # removes the elements from setA that are not in setB
print(setA) # {1, 3, 5, 7, 9}

# difference_update
print(setA) # {1, 3, 5, 7, 9}
print(setB) # {1, 3, 5, 7, 9, 11, 13, 15}
setA.difference_update(setB) # removes the elements from setA that are in setB
print(setA) # set()

# symmetric_difference_update
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 3, 5, 7, 9, 11, 13, 15}
setA.symmetric_difference_update(setB) # removes the elements that are in both sets and adds the elements that are not in both sets
print(setA) # {2, 4, 6, 8, 11, 13, 15}


# subset
setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}
setE = {7, 8, 9}

print(setC.issubset(setD)) # False; all elements in setC are not in setD


# superset
print(setC.issuperset(setD)) # True; all elements in setD are in setC
print(setD.issuperset(setC)) # False; all elements in setC are not in setD

# disjoint
print(setC.isdisjoint(setD)) # False; there are common elements in both sets
print(setC.isdisjoint(setE)) # True; there are no common elements in both sets

# copy
setF = setC # creates a reference to setC
setF.add(7)
print(setC) # {1, 2, 3, 4, 5, 6, 7}; setC is also modified

setF = setC.copy() # creates a copy of setC
setF = set(setC) # creates a copy of setC


# frozen set
a = frozenset([1, 2, 3, 4]) # immutable set; cannot be changed
print(a) # frozenset({1, 2, 3, 4})
# Union, intersection, difference, symmetric_difference, issubset, issuperset, isdisjoint, copy are supported
```
<br/>
<br/>

## 5. Strings
[🔼 Back to top](#content)
```Python
# Strings: ordered, immutable, text representation

mystring = "Hello World"
print(mystring)


char = mystring[0]
print(char) # H

# mystring[0] = "h" # TypeError: 'str' object does not support item assignment; strings are immutable

# Slicing
substring = mystring[1:5]
print(substring) # ello

substring = mystring[::2] # steps by 2
print(substring) # HloWrd

# Concatenation
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence) # Hello Tom

# Iterating
for i in greeting:
    print(i) # prints each character in the string

# in operator
if "e" in greeting:
    print("yes") # yes if e is in the string, no if not
else:
    print("no")    



# String formatting
string_2 = "Hello"
string_2 = string_2.strip() # removes whitespace
print(string_2) # Hello; immutable does not change the original string

string_2 = string_2.upper() # converts to uppercase
string_2 = string_2.lower() # converts to lowercase

print(string_2.startswith("he")) # True; checks if string starts with He
string_2.endswith("He") # False; checks if string ends with He

string_2 = string_2.find("l") # 2; returns the index of the first occurrence of l in the string
print(string_2) #if not found, returns -1

string_3 = "Hello World"
print(string_3.count("l")) # 3; counts the number of times l appears in the string

string_3 = string_3.replace("World", "Universe") # replaces World with Universe; if not found, returns original string
print(string_3) # Hello Universe; returns a new string, original string is unchanged



# String and lists
string_4 = "how are you doing"
list_1 = string_4.split(" ") # splits the string into a list of strings, using space as the delimiter
print(list_1) # ['how', 'are', 'you', 'doing']

new_string = " ".join(list_1) # joins the list of strings into a string, using space as the delimiter
print(new_string) # how are you doing

list_2 = ["a"] * 6
print(list_2) # ['a', 'a', 'a', 'a', 'a', 'a']

string_5 = ""
for i in list_2:
    string_5 += i + " " # adds each element in the list to the string, with a space in between
print(string_5) # a a a a a a  ; inefficient, better to use join

string_6 = " ".join(list_2)
print(string_6) # a a a a a a ; more efficient than the for loop above



# Formatting strings %, .format(), f-Strings
var = "Tom"
string_7 = "the variable is %s" % var # %s is a placeholder for the variable
print(string_7) # the variable is Tom

var = 3
string_7 = "the variable is %d" % var # %d is a placeholder for the integer variable
print(string_7) # the variable is 3

var = 3.1234567
string_7 = "the variable is %.2f" % var # %.2f is a placeholder for the float variable, with 2 decimal places
print(string_7) # the variable is 3.12

var = 3.1234567
string_7 = "the variable is {}".format(var) # {} is a placeholder for the float variable, with 2 decimal places
print(string_7) # the variable is 3.1234567

var = 3.1234567
var2 = 6
string_7 = "the variable is {:.2f} and {}".format(var, var2) # {} is a placeholder for the float variable, with 2 decimal places
print(string_7) # the variable is 3.12 and 6

var = 3.1234567
var2 = 6
string_7 = f"the variable is {var} and {var2}" # {} is a placeholder for the float variable, with 2 decimal places
print(string_7) # the variable is 3.1234567 and 6

string_7 = f"the variable is {var*3} and {var2:.2f}" # {} evaluates the expression inside in runtime
print(string_7) # the variable is 9.3703701 and 6.00
```
<br/>
<br/>

## 6. Collections
[🔼 Back to top](#content)
```Python
# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
# Counter is container that stores elements as dictionary keys, and their counts are stored as dictionary values.

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter) # Counter({'a': 5, 'b': 4, 'c': 3})

print(my_counter.items()) # dict_items([('a', 5), ('b', 4), ('c', 3)])
print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])
print(my_counter.values()) # dict_values([5, 4, 3])

print(my_counter.most_common(1)) # [('a', 5)] # returns the most common element
print(my_counter.most_common(2)) # [('a', 5), ('b', 4)] # returns the 2 most common elements

print(my_counter.most_common(1)[0][0]) # a # returns the most common element
 
print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']



from collections import namedtuple
# namedtuple is a container with a name for each value
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt) # Point(x=1, y=-4)

print(pt.x, pt.y) # 1 -4


from collections import OrderedDict
# OrderedDict is a dictionary subclass that remembers the order in which its contents are added
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# from python 3.7, the default dictionary is orderedfrom

from collections import defaultdict
d = defaultdict(int) # float, list, str, etc not key error if the key is not in the dictionary
d['a'] = 1
d['b'] = 2
print(d['a']) # 1
print(d['c']) # 0 # returns 0 if the key is not in the dictionary


from collections import deque
# deque is a double-ended queue that allows you to add and remove elements from both ends
d = deque()

d.append(1)
d.append(2)
print(d) # deque([1, 2])

d.appendleft(3)
print(d) # deque([3, 1, 2])

d.pop()
print(d) # deque([3, 1])

d.popleft()
print(d) # deque([1])

d.clear()
print(d) # deque([])

d.extend([4, 5, 6])
print(d) # deque([4, 5, 6])

d.extendleft([1, 2, 3])
print(d) # deque([3, 2, 1, 4, 5, 6])

d.rotate(1)
print(d) # deque([6, 3, 2, 1, 4, 5])

d.rotate(2)
print(d) # deque([4, 5, 6, 3, 2, 1])

d.rotate(-1)
print(d) # deque([5, 6, 3, 2, 1, 4])
```
<br/>
<br/>

## 7. Itertools
[🔼 Back to top](#content)
```Python
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# collection of tools for handling iterators; functions that operate on iterators to produce more complex iterators


from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b) # cartesian product of a and b
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]


b = [3]
prod = product(a, b, repeat=2) # cartesian product of a and b, repeat=2 means repeat twice
print(list(prod)) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]


from itertools import permutations
#returns all possible orderings of an input
a = [1, 2, 3]
perm = permutations(a)
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations(a, 2) # 2 means the length of the permutation
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


from itertools import combinations, combinations_with_replacement
#returns all possible combinations of an input
a = [1, 2, 3, 4]
comb = combinations(a, 2) # 2 means the length of the combination
print(list(comb)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] # no repeats

comb_wr = combinations_with_replacement(a, 2) # 2 means the length of the combination
print(list(comb_wr)) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)] # repeats




from itertools import accumulate
import operator
#returns accumulated sums
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a) # [1, 2, 3, 4]
print(list(acc)) # [1, 3, 6, 10]

acc = accumulate(a, func=operator.mul) # multiply instead of add
print(list(acc)) # [1, 2, 6, 24]

b = [1, 2, 5, 3, 4]
acc = accumulate(b, func=max) # max instead of add
print(list(acc)) # [1, 2, 5, 5, 5]




from itertools import groupby
#groups consecutive elements together based on a given key
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3) # key is a function that takes a single value as an argument and returns a key
for key, value in group_obj:
    print(key, list(value)) # True [1, 2] # False [3, 4]

#lambda function is a small anonymous function
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value)) # True [1, 2] # False [3, 4]

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value)) # 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}] 
                            # 27 [{'name': 'Lisa', 'age': 27}] 
                            # 28 [{'name': 'Claire', 'age': 28}]


from itertools import count, cycle, repeat
#count: counts up infinitely from a value
for i in count(10):
    print(i)
    if i == 15:
        break # 10 11 12 13 14 15

#cycle: infinitely iterates through an iterable (for loop)
a = [1, 2, 3]
for i in cycle(a):
    print(i) # infinite loop
    break # 1 2 3


for i in repeat(1, 4): # repeat 1 four times; will not be an infinite loop
    print(i) # 1 1 1 1
```
<br/>
<br/>

## 8. Lambda Functions
[🔼 Back to top](#content)
```Python
# lambda arguments: expression <----syntax (small, one  line anonymous function)

add10 = lambda x: x + 10
print(add10(5)) # 15

def add10_func(x):
    return x + 10

mult = lambda x, y: x * y
print(mult(2, 7)) # 14

# used  when you need a function for a short period of time


#sorted
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]'
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]
# sort by x

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted) # [(5, -1), (15, 1), (1, 2), (10, 4)]
# sort by y

def sort_by_y(x):
    return x[1]

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]
# sort by sum of x and y


# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b)) # [2, 4, 6, 8, 10]
# map each element of a to x * 2

c = [x * 2 for x in a]  # list comprehension same as map


# filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b)) # [2, 4, 6]
# filter out odd numbers

c = [x for x in a if x % 2 == 0] # list comprehension same as filter

# reduce(func, seq)
from functools import reduce
a = [1, 2, 3, 4,]

product_a = reduce(lambda x, y: x * y, a)
print(product_a) # 24
# multiply all numbers in a
```
<br/>
<br/>

## 9. Exceptions and Errors
[🔼 Back to top](#content)
```Python
# Errors and Exceptions

# Syntax Errors - also known as parsing errors

a = 5 print(a) # SyntaxError: invalid syntax

a=5
print(a)) # SyntaxError: unmatched ')'

a = 5 + '10' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

import somemodule # ModuleNotFoundError: No module named 'somemodule'

b = c # NameError: name 'c' is not defined

f = open('somefile.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

a = [1, 2, 3]
a.remove(4) # ValueError: list.remove(x): x not in list

my_dict = {'name': 'Max'}
my_dict['age'] # KeyError: 'age'


X = -5
if X < 0:
    raise Exception('X should be positive') # Exception: X should be positive

x = -5
assert (x >= 0), 'x is not positive' # AssertionError: x is not positive




# try except else finally
try:
    a = 5 / 0
except:
    print('an error happened') #program continues


try:
    a = 5 / 0
except Exception as e:
    print(e) #division by zero


try:
    a = 5 / 0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine') #else runs if no exception
finally:
    print('cleaning up...') #finally always runs





# Custom Exceptions
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

    if x < 5:
        raise ValueTooSmallError('value is too small', x)


try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value) #we can access the attributes of the exception





```
<br/>
<br/>


## 10. Logging 
[🔼 Back to top](#content)

The logging module in Python is a powerful built-in module so you can quickly add logging to your application.  
`import logging`
## Log Level <!-- omit in toc -->
There are 5 different log levels indicating the serverity of events. By default, the system logs only events with level *WARNING* and above.

```Python
import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```
## Configuration <!-- omit in toc -->
With `basicConfig(**kwargs)` you can customize the root logger. The most common parameters are the *level*, the *format*, and the *filename*. See https://docs.python.org/3/library/logging.html#logging.basicConfig for all possible arguments. See also https://docs.python.org/3/library/logging.html#logrecord-attributes for possible formats and https://docs.python.org/3/library/time.html#time.strftime how to set the time string. Note that this function should only be called once, and typically first thing after importing the module. It has no effect if the root logger already has handlers configured. For example calling `logging.info(...)` before the *basicConfig* will already set a handler.
```Python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# Now also debug messages will get logged with a different format.
logging.debug('Debug message')

# This would log to a file instead of the console.
# logging.basicConfig(level=logging.DEBUG, filename='app.log')
```
## Logging in modules and logger hierarchy <!-- omit in toc -->
Best practice in your application with multiple modules is to create an internal logger using the `__name__` global variable. This will create a logger with the name of your module and ensures no name collisions. The logging module creates a hierarchy of loggers, starting with the root logger, and adding the new logger to this hierarchy. If you then import your module in another module, log messages can be associated with the correct module through the logger name. Note that changing the basicConfig of the root logger will also affect the log events of the other (lower) loggers in the hierarchy.

```Python
# helper.py
# -------------------------------------
import logging
logger = logging.getLogger(__name__)
logger.info('HELLO')

# main.py
# -------------------------------------
import logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
import helper

# --> Output when running main.py
# helper - INFO - HELLO
```
## Propagation <!-- omit in toc -->
By default, all created loggers will pass the log events to the handlers of higher loggers, in addition to any handlers attached to the created logger. You can deactivate this by setting `propagate = False`. Sometimes when you wonder why you don't see log messages from another module, then this property may be the reason.
```Python
# helper.py
# -------------------------------------
import logging
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('HELLO')

# main.py
# -------------------------------------
import logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
import helper

# --> No output when running main.py since the helper module logger does not propagate its messages to the root logger
```
## LogHandlers <!-- omit in toc -->
Handler objects are responsible for dispatching the appropriate log messages to the handler's specific destination. For example you can use different handlers to send log messaged to the standard output stream, to files, via HTTP, or via Email. Typically you configure each handler with a level (`setLevel()`), a formatter (`setFormatter()`), and optionally a filter (`addFilter()`). See https://docs.python.org/3/howto/logging.html#useful-handlers for possible built-in handlers. Of course you can also implement your own handlers by deriving from these classes.
```Python
import logging

logger = logging.getLogger(__name__)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# Configure level and formatter and add it to handlers
stream_handler.setLevel(logging.WARNING) # warning and above is logged to the stream
file_handler.setLevel(logging.ERROR) # error and above is logged to a file

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning') # logged to the stream
logger.error('This is an error') # logged to the stream AND the file!
```
#### Example of a filter <!-- omit in toc -->
```Python
class InfoFilter(logging.Filter):
    
    # overwrite this method. Only log records for which this
    # function evaluates to True will pass the filter.
    def filter(self, record):
        return record.levelno == logging.INFO

# Now only INFO level messages will be logged
stream_handler.addFilter(InfoFilter())
logger.addHandler(stream_handler)
```
## Other configuration methods <!-- omit in toc -->
We have seen how to configure logging creating loggers, handlers, and formatters explicitely in code. There are two other configration methods:
- Creating a logging config file and reading it using the `fileConfig()` function. See example below.
- Creating a dictionary of configuration information and passing it to the `dictConfig()` function. See https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig for more information.

#### .conf file <!-- omit in toc -->
Create a *.conf* (or sometimes stored as *.ini*) file, define the loggers, handlers, and formatters and provide the names as keys. After their names are defined, they are configured by adding the words *logger*, *handler*, and *formatter* before their names separated by an underscore. Then you can set the properties for each logger, handler, and formatter. In the example below, the root logger and a logger named *simpleExample* will be configured with a StreamHandler.
```Python
# logging.conf
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```
```Python
# Then use the config file in the code
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')`
```
## Capture Stack traces <!-- omit in toc -->
Logging the traceback in your exception logs can be very helpful for troubleshooting issues. You can capture the traceback in *logging.error()* by setting the *exc_info* parameter to True.
```Python
import logging

try:
    a = [1, 2, 3]
    value = a[3]
except IndexError as e:
    logging.error(e)
    logging.error(e, exc_info=True)
```
If you don't capture the correct Exception, you can also use the *traceback.format_exc()* method to log the exception.
```Python
import logging
import traceback

try:
    a = [1, 2, 3]
    value = a[3]
except:
    logging.error("uncaught exception: %s", traceback.format_exc())
```
## Rotating FileHandler <!-- omit in toc -->
When you have a large application that logs many events to a file, and you only need to keep track of the most recent events, then use a RotatingFileHandler that keeps the files small.
When the log reaches a certain number of bytes, it gets "rolled over". You can also keep multiple backup log files before overwriting them.
```Python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')
```
## TimedRotatingFileHandler <!-- omit in toc -->
If your application will be running for a long time, you can use a TimedRotatingFileHandler. This will create a rotating log based on how much time has passed. Possible time conditions for the *when* parameter are:
- second (s)
- minute (m)
- hour (h)
- day (d)
- w0-w6 (weekday, 0=Monday)
- midnight
```Python
import logging
import time
from logging.handlers import TimedRotatingFileHandler
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)
 
for i in range(6):
    logger.info('Hello, world!')
    time.sleep(50)`
```


## Logging in JSON Format  <!-- omit in toc -->

If your application generates many logs from different modules, and especially in a microservice architecture, it can be challenging to locate the important logs for your analysis. Therefore, it is best practice to log your messages in JSON format, and send them to a centralized log management system. Then you can easily search, visualize, and analyze your log records.  
I would recommend using this Open Source JSON logger: https://github.com/madzak/python-json-logger  
`pip install python-json-logger`
```Python
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)****
```
<br/>
<br/>

## 11. Json
[🔼 Back to top](#content)
```Python
# java scrypt object notation
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}


#serialize into json
personJson = json.dumps(person, indent=4, sort_keys=True)
print(personJson)

""" {
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
} """

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# deserialize json
person = json.loads(personJson)
print(person) # {'name': 'John', 'age': 30, 'city': 'New York', 'hasChildren': False, 'titles': ['engineer', 'programmer']}

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)


# encoding custom objects
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable') 


from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o) # call the default method of the parent class, rewrite the default method


user = User('Max', 27)
userJson = json.dumps(user, default=encode_user)
print(userJson) # {"name": "Max", "age": 27, "User": true}

userJson = json.dumps(user, cls=UserEncoder)
print(userJson) # {"name": "Max", "age": 27, "User": true}

userJson = UserEncoder().encode(user)
print(userJson) # {"name": "Max", "age": 27, "User": true} #directly use the UserEncoder class



# decoding custom objects
userJson = userJson = UserEncoder().encode(user)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJson)
print(user) # {'name': 'Max', 'age': 27, 'User': True} #python dict not User object

user = json.loads(userJson, object_hook=decode_user)
print(user) # <__main__.User object at 0x000001F4F2F3F4C0> #User object
print(user.name) # Max
print(user.age) # 27

```
<br/>
<br/>

## 12. Random numbers
[🔼 Back to top](#content)
```Python
import random
#sudo random number generator; the are not truly random, reproducible with the same seed

a = random.random() #random float between 0 and 1
print(a)

a = random.uniform(1, 10) #random float between 1 and 10
print(a)

a = random.randint(1, 10) #random integer between 1 and 10
print(a)

a = random.randrange(1, 10) #random integer between 1 and 9
print(a)

a = random.normalvariate(0, 1) #random float from a normal distribution; mean 0, standard deviation 1


mylist = list("ABCDEFGH")
print(mylist)
a = random.choice(mylist) #random element from a list
print(a)

a = random.sample(mylist, 3) #random 3 unique elements from a list
print(a)

a = random.choices(mylist, k=3) #random 3 elements from a list; can be repeated
print(a)

a = random.shuffle(mylist) #shuffle a list
print(mylist)

#seed the random number generator
#not recommended to use in production
random.seed(1) 
print(random.random())
print(random.randint(1, 10))

random.seed(2) 
print(random.random())
print(random.randint(1, 10))

random.seed(1) 
print(random.random())
print(random.randint(1, 10))

random.seed(2) 
print(random.random())
print(random.randint(1, 10))



import secrets
#passwords, security tokens, authentication (take more time to generate)

a = secrets.randbelow(10) #random integer between 0 and 9
print(a)

a = secrets.randbits(4) #random integer with 4 bits of entropy
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist) #random element from a list

#numpy
import numpy as np
a = np.random.rand(3) #random floats in a numpy array
print(a)

a = np.random.rand(3, 3) #random floats in a numpy array
print(a)

a = np.random.randint(0, 10, 3) #random integers in a numpy array; between 0 and 9
print(a)

a = np.random.randint(0, 10, (3, 4)) #random integers in a 3D numpy array; between 0 and 9
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr) #shuffle a numpy array on the first axis
print(arr)

#seed the random number generator; use in production
np.random.seed(1)
print(np.random.rand(3, 3)) 
np.random.seed(1)
print(np.random.rand(3, 3)) 
```
<br/>
<br/>

## 13. Decorators
[🔼 Back to top](#content)
```Python
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
```
<br/>
<br/>

## 14. Generators
[🔼 Back to top](#content)
```Python
# special kind of function that return a lazy iterator.
#These are objects that you can loop over like a list.
#However, unlike lists, lazy iterators do not store their contents in memory
#This is great for memory efficiency

def my_generator():
    print("Inside my generator")
    yield 1
    yield 2
    yield 3

g = my_generator()
print (g) #<generator object my_generator at 0x000001BA83809A80>

for i in g:
    print(i) 


g = my_generator()

value = next(g)
print(value) #1 returns the next value in the sequence

value = next(g)
print(value) #2

value = next(g)
print(value) #3

""" value = next(g)
print(value) #StopIteration error """

print(sum(g)) #6
print(sorted(g)) #[1, 2, 3]


#execution stops when the function encounters a yield statement
#execution resumes when next() is called again
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
print(cd) #<generator object countdown at 0x000001BA83809A20>

value = next(cd) #Starts the generator
print(value) #4
print(next(cd)) #3
print(next(cd)) #2
print(next(cd)) #1
#print(next(cd)) #StopIteration error


#Generators are memory efficient because they only load the data needed to process the next value in the iterable
import sys
def firstn(n): #takes a lot of memory
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

mylist = firstn(10)
print(mylist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(firstn(10))) #45


def firstn_generator(n): #implementation as a generator object
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10))) #45 we are not saving the list in memory


print(sys.getsizeof(firstn(1000000))) #8448728 bytes
print(sys.getsizeof(firstn_generator(1000000))) #104 bytes



def fibonacci(limit):
    #0,1,1,2,3,5,8,13,21,34,55
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b

fib = fibonacci(30)
for i in fib:
    print(i) #0 1 1 2 3 5 8 13 21


#Generator Expressions
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i) #0 2 4 6 8

mygenerator = (i for i in range(1000000) if i % 2 == 0)
#print(list(mygenerator)) #[0, 2, 4, 6, 8]
print(sys.getsizeof(mygenerator)) #104 bytes

#list comprehension use square brackets []
mylist = [i for i in range(1000000) if i % 2 == 0]
#print(mylist) #[0, 2, 4, 6, 8]
print(sys.getsizeof(mylist)) #4167352 bytes


```
<br/>
<br/>

## 15. Threading and Multiprocessing 
[🔼 Back to top](#content)

We have two common approaches to run code in parallel (achieve multitasking and speed up your program) : via threads or via multiple processes.
<br/>
<br/>
### Process <!-- omit in toc -->

A Process is an instance of a program, e.g. a Python interpreter. They are independent from each other and do not share the same memory.
<br/>
<br/>

Key facts:

    A new process is started independently from the first process

    Takes advantage of multiple CPUs and cores

    Separate memory space

    Memory is not shared between processes

    One GIL (Global interpreter lock) for each process, i.e. avoids GIL limitation

    Great for CPU-bound processing

    Child processes are interruptable/killable

    Starting a process is slower that starting a thread

    Larger memory footprint

    IPC (inter-process communication) is more complicated
<br/>

```Python
#multiprocessing


from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        result = i * i
        time.sleep(0.1)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers) # if arg in func (target=square_numbers, args=(i,))
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()
    print('end main')
```
<br/>

![](https://i.imgur.com/kiCJw9f.png)
<br/>
<br/>

### Threads <!-- omit in toc -->

A thread is an entity within a process that can be scheduled for execution (Also known as "leightweight process"). A Process can spawn multiple threads. The main difference is that all threads within a process share the same memory.
<br/>
<br/>

Key facts:

    Multiple threads can be spawned within one process

    Memory is shared between all threads

    Starting a thread is faster than starting a process

    Great for I/O-bound tasks

    Leightweight - low memory footprint

    One GIL for all threads, i.e. threads are limited by GIL

    Multithreading has no effect for CPU-bound tasks due to the GIL

    Not interruptible/killable -> be careful with memory leaks

    increased potential for race conditions
<br/>

```Python
from threading import Thread
import time

def square_numbers():
    for i in range(100):
        result = i * i
        time.sleep(0.1)

if __name__ == "__main__":
    threads = []
    num_threads = 15

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers) # if arg in func (target=square_numbers, args=(i,))
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()

    print("end main")
```
<br/>

![](https://i.imgur.com/Y0PY7Yj.png)
<br/>


### GIL - Global interpreter lock <!-- omit in toc -->

This is a mutex (or a lock) that allows only one thread to hold control of the Python interpreter. This means that the GIL allows only one thread to execute at a time even in a multi-threaded architecture.
<br/>
<br/>

#### Why is it needed? <!-- omit in toc -->

It is needed because CPython's (reference implementation of Python) memory management is not thread-safe. Python uses reference counting for memory management. It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object. When this count reaches zero, the memory occupied by the object is released. The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously. If this happens, it can cause either leaked memory that is never released or incorrectly release the memory while a reference to that object still exists.
<br/>
<br/>

#### How to avoid the GIL <!-- omit in toc -->

The GIL is very controversial in the Python community. The main way to avoid the GIL is by using multiprocessing instead of threading. Another (however uncomfortable) solution would be to avoid the CPython implementation and use a free-threaded Python implementation like Jython or IronPython. A third option is to move parts of the application out into binary extensions modules, i.e. use Python as a wrapper for third party libraries (e.g. in C/C++). This is the path taken by numypy and scipy.
<br/>
<br/>

## 16. Threading
[🔼 Back to top](#content)
```Python
from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 15
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()

    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')

""" in Thread1 got 0
in Thread2 got 1
in Thread3 got 2
in Thread4 got 3
in Thread5 got 4
in Thread6 got 5
in Thread7 got 6
in Thread8 got 7
in Thread9 got 8
in Thread10 got 9
in Thread11 got 10
in Thread12 got 11
in Thread13 got 12
in Thread14 got 13
in Thread15 got 14
in Thread1 got 15
in Thread2 got 16
in Thread3 got 17
in Thread4 got 18
in Thread5 got 19
main done """
```
<br/>
<br/>

## 17. Multiprocessing
[🔼 Back to top](#content)

For more information see jupyter notebook 17_multiprocesing.ipynb

<br/>
<br/>

## 18. Function Arguments
[🔼 Back to top](#content)
```Python
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
```
<br/>
<br/>

## 19. The Asterisk (*) Operator
[🔼 Back to top](#content)
```Python
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
```
<br/>
<br/>

## 20. Shallow vs Deep Copying
[🔼 Back to top](#content)
```Python
org = 5
cpy = org # both variables point to the same object

cpy = 6 # rebind cpy to a new object
print(org) # 5, org still points to the original object
print(cpy) # 6, cpy points to the new object


#with mutable objects, both variables point to the same object
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(org) # [-10, 1, 2, 3, 4]
print(cpy) # [-10, 1, 2, 3, 4]
# = is not making a copy, it is just making a new reference to the same object

import copy
# - shallow copy: one level deep, only references of nested child objects
# - deep copy: full independent copy

# shallow copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
""" more than one option to make a shallow copy:
cpy = org.copy()
cpy = org[:]
cpy = list(org)
 """
cpy[0] = -10
print(org) # [0, 1, 2, 3, 4]
print(cpy) # [-10, 1, 2, 3, 4]


# deep copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(org) # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
print(cpy) # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
# only the outer list is copied, the inner list is still referenced

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(org) # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
print(cpy) # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]


#works with any object, not just lists, tuples, dicts
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Alex', 25)
p2 = p1

p2.age = 28

print(p1.age) # 28
print(p2.age) # 28

p1 = Person('Alex', 25)
p2 = copy.copy(p1)



class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Alex', 55)
p2 = Person('Joe', 28)

#shallow copy
company = Company(p1, p2)
company_clone = copy.copy(company)

company_clone.boss.age = 56
print(company_clone.boss.age) # 56
print(company.boss.age) # 56

#deep copy
company_clone = copy.deepcopy(company)
company_clone.boss.age = 57
print(company_clone.boss.age) # 57
print(company.boss.age) # 56
```
<br/>
<br/>

## 21. Context Managers
[🔼 Back to top](#content)
```Python
with open('notes.txt', 'w') as file:
    file.write('Hello, World!')

# this is longer version of the above code
# recurses are released automatically using with statement
file = open('notes.txt', 'w')
try:
    file.write('Hello, World!')
finally:
    file.close()


# creating a context manager
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        print('exit')
        return True

with ManagedFile('notes.txt') as file:
    print('do some stuff...')
    file.write('Hello, World!')
    file.write('bye now')
    file.something()

print('continuing...')


# context manager as a function
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('hello, world!')
    f.write('bye now')
```
<br/>
<br/>

## 22. Object Oriented Programming
[🔼 Back to top](#content)
```Python
#position, name, age, level, salary
se1 = ['Software Engineer', 'Max', 25, 'Junior', 5000]
se2 = ['Software Engineer', 'Lisa', 28, 'Senior', 7000]

#class is better structure than a list to represent software engineer

class SoftwareEngineer:

    # class attributes; can be used on class itself or on instance
    alias = 'Keyboard Magician' #belong to class; same for all instances and we can access it without creating an instance

    def __init__(self, name, age, level, salary):
        # instance attributes; belong to one instance that we create
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

# instance
se1 = SoftwareEngineer('Max', 25, 'Junior', 5000)
print(se1.name, se1.age, se1.level, se1.salary)
print(se1.alias)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer('Lisa', 28, 'Senior', 7000)

#Recap
# create a class (blueprint)
# create an instance (object)
# class vs instance
# instance attributes: defined in __init__ method
# class attributes: defined outside __init__ method
```

```Python
class SoftwareEngineer:
    #class attributes
    alias = 'Keyboard Magician'

    def __init__(self, name, age, level, salary):
        # instance attributes; belong to one instance that we create
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}...')

    #def information(self):
        #information = f'name = {self.name}, age = {self.age}, level = {self.level}'
        #return information

    #special method's (dunder/magic method)
    def __str__(self):
        information = f'name = {self.name}, age = {self.age}, level = {self.level}'
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age): #self isn't passed intentionally; use static decorator(prevent crash if we don't pass self)
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000



# instance
se1 = SoftwareEngineer('Max', 25, 'Junior', 5000)
se2 = SoftwareEngineer('Lisa', 28, 'Senior', 7000)

se4 = SoftwareEngineer('Max', 27, 'Junior', 5000)
se3 = SoftwareEngineer('Lisa', 28, 'Senior', 7000)

se1.code() #when we call this method, self will be se1 and we don't need to pass it
se2.code()
se1.code_in_language('Python')
se2.code_in_language('Java')

print(se1) #__str__ method is called and it returns the string
print(se2)

print(se2 == se3) #False without __eq__ because they are different instances in memory
print(se1 == se4)

se1.entry_salary(24) #TypeError: SoftwareEngineer.entry_salary() takes 1 positional argument but 2 were given; self is passed automatically; we need to use static method
SoftwareEngineer.entry_salary(24) #we need call it on class itself, not on instance

#Recap
# instance method: first argument is self
# can taka arguments and return values
# special dunder methods: __str__, __eq__
# static method: no self argument; can't access or modify class state
```

```Python
#inheritance all attributes and methods from parent class


#inherits, extends, overrides
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working...')


class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f'{self.name} is debugging...')

    def work(self):
        print(f'{self.name} is coding...') #override work method from parent class; same name and same arguments

class Designer(Employee):

    def draw(self):
        print(f'{self.name} is drawing...')

    def work(self):
        print(f'{self.name} is designing...')



se = SoftwareEngineer('Max', 25, 6000, "Junior")
print(se.name, se.age)
se.work()
print(se.level)
se.debug()
#se.drw() #AttributeError: 'SoftwareEngineer' object has no attribute 'drw'

d = Designer('Philipp', 28, 7000)
print(d.name, d.age)
d.work()
d.draw()
```

```Python
#Polymorphism (many forms)
#works with super class and sub classes

employees = [SoftwareEngineer('Max', 25, 6000, "Junior"),
             SoftwareEngineer('Lisa', 28, 8000, "Senior"),
             Designer('Philipp', 28, 7000)]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)

#Recap
# inheritance: ChildClass(ParentClass)
# inherit, extend, override
# super().__init__()
# polymorphism: same method name, different behavior
```

```Python
#Encapsulation and Abstraction
#hide data from outside and only expose what's necessary

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None #protected attribute (private is __salary)
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved += 1

    #getter
    def get_salary(self):
        return self._salary

    #setter
    def set_salary(self, base_value):
        #check value, enforce constraints
        """ if base_value < 1000:
            self._salary = 1000
        elif base_value > 20000:
            self._salary = 20000
        self._salary = base_value """

        self._salary = self._calculate_salary(base_value) #private method

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3



se = SoftwareEngineer('Max', 25)
print(se.name, se.age)

se.set_salary(6000)
print(se.get_salary())

for i in range(70):
    se.code()
se.set_salary(6000)
print(se.get_salary())
```

```Python
#Property decorator

class SoftwareEngineer:
    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

se = SoftwareEngineer()
se.salary = 6000
print(se.salary)

#more pythonic way
#implementing encapsulation and abstraction
```

```Python
class SoftwareEngineer:
    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        self._salary = value

se = SoftwareEngineer()
se.salary = 6000
print(se.salary)
del se.salary
print(se.salary)

#Recap
# encapsulation: hide data from outside
# abstraction: expose only what's necessary
# public, protected, private
# _foo(), _x
# getter/setter
# getter -> @property
# setter -> @x.setter
# deleter -> @x,deleter
```
