# java scrypt object notation
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}


#serialize into json
personJson = json.dumps(person, indent=4, sort_keys=True)
print(personJson)

""" {
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
} """

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# deserialize json
person = json.loads(personJson)
print(person) # {'name': 'John', 'age': 30, 'city': 'New York', 'hasChildren': False, 'titles': ['engineer', 'programmer']}

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)


# encoding custom objects
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable') 


from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o) # call the default method of the parent class, rewrite the default method


user = User('Max', 27)
userJson = json.dumps(user, default=encode_user)
print(userJson) # {"name": "Max", "age": 27, "User": true}

userJson = json.dumps(user, cls=UserEncoder)
print(userJson) # {"name": "Max", "age": 27, "User": true}

userJson = UserEncoder().encode(user)
print(userJson) # {"name": "Max", "age": 27, "User": true} #directly use the UserEncoder class



# decoding custom objects
userJson = userJson = UserEncoder().encode(user)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJson)
print(user) # {'name': 'Max', 'age': 27, 'User': True} #python dict not User object

user = json.loads(userJson, object_hook=decode_user)
print(user) # <__main__.User object at 0x000001F4F2F3F4C0> #User object
print(user.name) # Max
print(user.age) # 27
