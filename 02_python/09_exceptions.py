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






