import sqlite3

# create a connection object
conn = sqlite3.connect('/mnt/c/Users/aecke/Desktop/python/corpusLLM/database/corpusLLM.db')

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
