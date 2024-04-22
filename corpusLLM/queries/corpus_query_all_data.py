import sqlite3

# create a connection object
conn = sqlite3.connect('/mnt/c/Users/aecke/Desktop/python/corpusLLM/database/corpusLLM.db')

# create a cursor object
cursor = conn.cursor()

# execute a SELECT query
cursor.execute('''
SELECT * FROM books
''')

# fetch all rows from the result set
rows = cursor.fetchall()

# print the rows
for row in rows:
    print(row)

# close the connection
conn.close()
