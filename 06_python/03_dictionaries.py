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
