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




