bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hardware')

# print (bob, sue)

db = {}
db['bob'] = bob
db['sue'] = sue

print (db['bob']['name'])   #? Bob Smith

db['sue']['pay'] = 50000    #? Changes Sue's pay to 50000
db['sue']['pay']            #? fetch Sue's pay

import pprint

pprint.pprint(db)           #? Prints the database in a more readable format


for key in db: 
    print(key, '=>', db[key]['name']) 
                                            #? Prints the name of each person in the database
                                            
for key in db: 
    print(key, '=>', db[key]['pay']) 
                                            #? Prints the pay of each person in the database
                                            
for key in db: 
    print(db[key]['name'].split()[-1])
    db[key]['pay'] *= 1.10
    
for record in db.values(): 
    print(record['pay'])