import sqlite3
from collections import Counter

# create a connection object
conn = sqlite3.connect('/path/to/your/database.db')

# create a cursor object
cursor = conn.cursor()

# execute a SELECT query to retrieve all rows from the 'users' table
cursor.execute('''
SELECT body FROM books
''')

# fetch all rows from the result set
rows = cursor.fetchall()

# close the cursor, we don't need it anymore
cursor.close()

# create a Counter object to count word frequencies
word_counter = Counter()

# iterate over each row and count the frequency of each word
for row in rows:
    # Split the body text into words
    words = row[0].split()
    
    # Update the word counter with the frequency of words in the current row
    word_counter.update(words)

# Print the frequency of each word
for word, frequency in word_counter.items():
    print(f'{word}: {frequency}')

# close the connection
conn.close()
