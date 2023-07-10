org = 5
cpy = org # both variables point to the same object

cpy = 6 # rebind cpy to a new object
print(org) # 5, org still points to the original object
print(cpy) # 6, cpy points to the new object


#with mutable objects, both variables point to the same object
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(org) # [-10, 1, 2, 3, 4]
print(cpy) # [-10, 1, 2, 3, 4]
# = is not making a copy, it is just making a new reference to the same object

import copy
# - shallow copy: one level deep, only references of nested child objects
# - deep copy: full independent copy

# shallow copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
""" more than one option to make a shallow copy:
cpy = org.copy()
cpy = org[:]
cpy = list(org)
 """
cpy[0] = -10
print(org) # [0, 1, 2, 3, 4]
print(cpy) # [-10, 1, 2, 3, 4]


# deep copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(org) # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
print(cpy) # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
# only the outer list is copied, the inner list is still referenced

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(org) # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
print(cpy) # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]


#works with any object, not just lists, tuples, dicts
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Alex', 25)
p2 = p1

p2.age = 28

print(p1.age) # 28
print(p2.age) # 28

p1 = Person('Alex', 25)
p2 = copy.copy(p1)



class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Alex', 55)
p2 = Person('Joe', 28)

#shallow copy
company = Company(p1, p2)
company_clone = copy.copy(company)

company_clone.boss.age = 56
print(company_clone.boss.age) # 56
print(company.boss.age) # 56

#deep copy
company_clone = copy.deepcopy(company)
company_clone.boss.age = 57
print(company_clone.boss.age) # 57
print(company.boss.age) # 56




