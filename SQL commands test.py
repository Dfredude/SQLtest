import sqlite3
#Creating database on RAM 
conn = sqlite3.connect(":memory:")
c = conn.cursor() #Creating db's cursor

#Creating a table with two columns (title, pages)
c.execute('''CREATE TABLE IF NOT EXISTS books
            (title TEXT, pages INTEGER)''')

#Inserting one book into table
c.execute('INSERT INTO books VALUES ("Are you my mother", 72)')
c.execute('SELECT * FROM books')
print('•Created a table with one book: ', c.fetchall(), sep= '\n')

#Creating a list of books
books = [
    ("Are you my mother", 72),
    ("Steve Jobs", 532),
    ("Zero to one", 220)
]
#Inserting a list of books
c.executemany('INSERT INTO books VALUES (?,?)', books)
conn.commit() #Commiting/Writing data

#Selecting and printing data from the table
c.execute('SELECT * FROM books')
data = c.fetchall() #Get data from cursor
print("•Inserted 3 more books:  ", data, sep = '\n') #Show data

#Delete items from table with logical statements
c.execute('DELETE FROM books WHERE title="Are you my mother"')
conn.commit() #Writing to db
print('•Deleted "Are you my mother" book: ')

c.execute('SELECT * FROM books')
data = c.fetchall()
print(data)

#Inserting one book with one value
c.execute('INSERT INTO books (title) VALUES ("CODE")')
conn.commit()
c.execute('SELECT * FROM books')
data = c.fetchall()
print('•Added "CODE" book without its "pages" value: ', data, sep = '\n')

#Updating pages of the "CODE" book
c.execute('UPDATE  books SET pages=450 WHERE title="CODE"')
conn.commit()
c.execute('SELECT * FROM books')
data = c.fetchall()
print('Updated "CODE" pages value: ', data, sep= '\n')