names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hardware']

list(zip(names, values)) #* [('name', 'Sue Jones'), ('age', 45), ('pay', 40000), ('job', 'hardware')]
#! zips the two lists together into a list of tuples

sue = dict(zip(names, values)) #* {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hardware'}
#! zips the two lists together into a dictionary

