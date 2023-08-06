from mypydbsimple import DB


# Instantiate mypydbsimple DB class
# by parsing a config file
# mydbsimple will automatically read db config
db = DB('mypydb.conf')


# Connect to database to validate the config
# is valid config to connect to the database
# without specifiying dbname, connection automatically 
# database name provided in config file
db.connect()

# If database name is specified,
# mypydbsimple will take it and use it for connection
db.connect('cars')

# Getting records from database table
# as simple as below. The result will be returned
# using fetchall() method as list
query = 'select * from cars limit %s, %s'
data = (1,2)
rows = db.execute(query, data)

# Inserting records to database as simple as below example

data = {
    'manufacturer':'honda',
    'model':'CRV',
    'type':'X1',
    'color':'piano black'
}

query = """INSERT INTO articles 
    (manufacturer, model, type, color)  
    VALUES (%(manufacturer)s, %(model)s, %(type)s, %(color)s)"""


db.execute(query, data)




