import sqlite3
connection=sqlite3.connect('OurDataBase.db')
cursor=connection.cursor()
name=input('Enter your username::')
UID=input('Enter your UID::')
cursor.execute('INSERT INTO table1 VALUES(?,?)',(name,UID))
connection.commit()
