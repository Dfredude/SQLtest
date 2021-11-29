from book import Book
import booksSDK

book = Book("Steve Jobs", 500)
booksSDK.updateBook(book, "Zero to One", 72)
booksSDK.showTable()
