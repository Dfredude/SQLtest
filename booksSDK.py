import sqlite3
from sqlite3.dbapi2 import Cursor
from book import Book

def cursor():
    return sqlite3.connect("booksDB.db").cursor()

c = cursor()
c.execute('''CREATE TABLE IF NOT EXISTS books
    (title TEXT, pages INTEGER)''')
c.connection.close()

def addBook(book:Book):
    c = cursor()
    with c.connection:
        c.execute(f'INSERT INTO books VALUES ("{book.title}", {book.pages})')
    c.connection.close()
    return c.lastrowid

def getBooks():
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM books')
    books = c.fetchall()
    c.connection.close()
    return books

def getBookByTitle(book_title:str):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM books WHERE title=?', (book_title,))
    data = c.fetchall()
    c.connection.close()
    if not data:
        return None
    return data


def removeBookByTitle(title:str):
    c = cursor()
    with c.connection:
        c.execute(f'DELETE FROM books WHERE title="{title}" ')
    c.connection.close()

def removeBookByRowID(rowid:int):
    c = cursor()
    with c.connection:
        c.execute(f'DELETE FROM books WHERE title="{rowid}" ')
    c.connection.close()

def updateBook(book:Book, new_title, new_pages):
    c = cursor()
    with c.connection:
        c.execute('''UPDATE books SET title=?, pages=? WHERE title=? AND pages=?''',
        (new_title, new_pages, book.title, book.pages))
    c.connection.close()

def showTable():
    c = cursor()
    c.execute("SELECT * FROM books")
    print(c.fetchall())
    c.connection.close()