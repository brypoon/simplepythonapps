


lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')

class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name

gandalf = Wizard("Gandalf", 42)
print(gandalf.__dict__)

print(lookup)
print(lookup['loc'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

import collections

user = collections.namedtuple('User', 'id, name, email')
users = [
    user(1, 'user1', 'user1@gmail.com'),
    user(2, 'user2', 'user2@gmail.com'),
    user(3, 'user3', 'user3@gmail.com'),
    user(4, 'user4', 'user4@gmail.com'),
    user(5, 'user5', 'user5@gmail.com')
]

lookup = dict()

for i in users:
    lookup[i.id] = i

print(lookup[1])

for e in users:
    lookup[e.email] = e

print(lookup['user3@gmail.com'])