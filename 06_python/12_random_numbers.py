import random
#sudo random number generator; the are not truly random, reproducible with the same seed

a = random.random() #random float between 0 and 1
print(a)

a = random.uniform(1, 10) #random float between 1 and 10
print(a)

a = random.randint(1, 10) #random integer between 1 and 10
print(a)

a = random.randrange(1, 10) #random integer between 1 and 9
print(a)

a = random.normalvariate(0, 1) #random float from a normal distribution; mean 0, standard deviation 1


mylist = list("ABCDEFGH")
print(mylist)
a = random.choice(mylist) #random element from a list
print(a)

a = random.sample(mylist, 3) #random 3 unique elements from a list
print(a)

a = random.choices(mylist, k=3) #random 3 elements from a list; can be repeated
print(a)

a = random.shuffle(mylist) #shuffle a list
print(mylist)

#seed the random number generator
#not recommended to use in production
random.seed(1) 
print(random.random())
print(random.randint(1, 10))

random.seed(2) 
print(random.random())
print(random.randint(1, 10))

random.seed(1) 
print(random.random())
print(random.randint(1, 10))

random.seed(2) 
print(random.random())
print(random.randint(1, 10))



import secrets
#passwords, security tokens, authentication (take more time to generate)

a = secrets.randbelow(10) #random integer between 0 and 9
print(a)

a = secrets.randbits(4) #random integer with 4 bits of entropy
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist) #random element from a list

#numpy
import numpy as np
a = np.random.rand(3) #random floats in a numpy array
print(a)

a = np.random.rand(3, 3) #random floats in a numpy array
print(a)

a = np.random.randint(0, 10, 3) #random integers in a numpy array; between 0 and 9
print(a)

a = np.random.randint(0, 10, (3, 4)) #random integers in a 3D numpy array; between 0 and 9
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr) #shuffle a numpy array on the first axis
print(arr)

#seed the random number generator; use in production
np.random.seed(1)
print(np.random.rand(3, 3)) 
np.random.seed(1)
print(np.random.rand(3, 3)) 