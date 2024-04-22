# a script that creates a database and a table in it

import sqlite3

# create a connection object, if not existing, it will be created
conn = sqlite3.connect('/path/to/your/database.db')

# create a cursor object
cursor = conn.cursor()

# create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, subtitle TEXT, body TEXT)
''')

# commit the changes
conn.commit()

# close the connection
conn.close()
