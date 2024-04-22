import sqlite3

# create a connection object
conn = sqlite3.connect('/path/to/your/database')

# create a cursor object
cursor = conn.cursor()

# execute a DROP TABLE query to remove the 'users' table
cursor.execute('''
DROP TABLE IF EXISTS books
''')

# commit the changes
conn.commit()

# close the connection
conn.close()
