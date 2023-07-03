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

