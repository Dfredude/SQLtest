import sqlite3
conn = sqlite3.connect(":memory:")

c = conn.cursor()
c.execute('''CREATE TABLE books
            (title TEXT, pages INTEGER)''')

c.execute('INSERT INTO books VALUES ("Are you my mother", 72)')

books = [
    ("Are you my mother", 72),
    ("Steve Jobs", 532),
    ("Zero to one", 220)
]

c.executemany('INSERT INTO books VALUES (?,?)', books)
conn.commit()

c.execute('SELECT * FROM books')
data = c.fetchall()
print(data)

c.execute('DELETE FROM books WHERE title="Are you my mother"')
conn.commit()

c.execute('SELECT * FROM books')
data = c.fetchall()
print(data)