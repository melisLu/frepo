import sqlite3

'''connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE users(id INTEGER PRIMARY KEY, 
                name VARCHAR NOT NULL, email VARCHAR, password VARCHAR);""")
connection.commit()
connection.close()'''

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("""INSERT INTO users(name, email, password) VALUES
                ('LINA', 'email', 6866868);""")
connection.commit()
connection.close()

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("""SELECT * FROM users;""")
data = cursor.fetchall()
print(data)
connection.commit()
connection.close()

update_us = "UPDATE users SET name='VITA' WHERE id=1"
cursor.execute(update_us)





