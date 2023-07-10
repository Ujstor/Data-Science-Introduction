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