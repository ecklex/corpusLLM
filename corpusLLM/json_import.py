import sqlite3
import json

# create a connection object
conn = sqlite3.connect('/mnt/c/Users/aecke/Desktop/python/corpusLLM/database/corpusLLM.db')

# create a cursor object
cursor = conn.cursor()

# read JSON data from file
with open('/mnt/c/Users/aecke/Desktop/python/python_db/json_data/data.json', 'r') as json_file:
    json_data = json.load(json_file)

# add data from JSON to the table
for entry in json_data:
    cursor.execute('''
    INSERT INTO books(title, subtitle, body)
    VALUES (?, ?, ?)
    ''', (entry['title'], entry['subtitle'], entry['body']))

# commit the changes
conn.commit()

# close the connection
conn.close()
