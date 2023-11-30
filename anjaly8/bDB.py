import sqlite3
con=sqlite3.connect('database.db')
print('opened database successfull')
con.execute('CREATE TABLE book(name char(20),author char(20),pdf char(20));')
print("Table created successfully")
con.close()