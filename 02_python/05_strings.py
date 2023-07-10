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



