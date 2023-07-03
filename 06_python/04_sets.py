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


