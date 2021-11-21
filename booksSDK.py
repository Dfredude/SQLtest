import sqlite3
from book import Book

def cursor(name:str):
    return sqlite3.connect(name).cursor()

def addBook(book:Book)