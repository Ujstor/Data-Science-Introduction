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