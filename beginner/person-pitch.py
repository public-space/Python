

people = [
    ['Bob Smith', 42, 30000, 'software'], 
    ['Sue Jones', 45, 40000, 'hardware']
]

#? A database list

for person in people: 
    print(person)

#* Now the list represents our database, and we can access its fields by position

people[0][0] #* 'Bob Smith'
people[1][2] #* 40000

for person in people: 
    print(person[0].split()[-1]) #* last name
    person[2] *= 1.20 #* give each a 20% raise
    
pays = [person[2] for person in people] #? collect all pay in a new list

pays = map((lambda x: x[2]), people) #? ditto, but with map

#? The map call here is equivalent to the list comprehension, but it is a bit faster

print(sum(person[2] for person in people)) #* sum all pay

#! LIST OPERATIONS
people.append(['Tom', 50, 0, None]) #* add a record
people[-1][0] #* Tom
