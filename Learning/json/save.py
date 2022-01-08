import json

data = {}

data['students'] = []
data['students'].append({
    'name': 'Scott',
    'age': 20,
    'email': 'scott@gmail.com'
})

data['students'].append({
    'name': 'Teddy',
    'age': 101,
    'email': 'Teddy@apple.com'
})

with open('students.txt', 'w') as outfile:
    json.dump(data, outfile)
