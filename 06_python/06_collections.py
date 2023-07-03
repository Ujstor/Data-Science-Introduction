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