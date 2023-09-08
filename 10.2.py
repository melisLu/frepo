import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("""INSERT INTO user(password, name) VALUES
                (87657, 'fillip');""")
connection.commit()
connection.close()

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("""SELECT * FROM user;""")
data = cursor.fetchall()
print(data)
connection.commit()
connection.close()