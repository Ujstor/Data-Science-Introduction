
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
