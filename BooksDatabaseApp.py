from book import Book
import booksSDK

def mainMenuPrint():
    print('''____________________________________
    Select an option:
    1. Get Book
    2. Add Book
    3. Update Book
    4. Delete Book
    5. Show Books
____________________________________''')

print("Welcome to our books database")
while True: 
    choice = None
    mainMenuPrint()
    try:
        choice = int(input("Press 'Enter' after typing your choice: "))
        if choice == 1: #Get book
            book_name = str(input("Enter the book's name: "))
            findings = booksSDK.getBookByTitle(book_name)
            for iteration in findings: print(iteration)
        elif choice == 2: #Add book
            book_name = str(input("Enter the book's name: "))
            book_pages = int(input("Enter the book's number of pages: "))
            booksSDK.addBook(Book(book_name, book_pages))
        elif choice == 3: #Update book
            book_name_to_update, book_number_of_pages_to_update = input("Enter the name, and number of pages of the book you want to update(Separated by a comma): ").split(',')
            book_name_to_update, book_number_of_pages_to_update = str(book_name_to_update), int(book_number_of_pages_to_update)
            new_title = str(input("Please enter the new title of the book you want to update: "))
            new_number_of_pages = int(input("Please enter the new number of pages of the book you want to update: "))
            booksSDK.updateBook(Book(book_name_to_update, book_number_of_pages_to_update), new_title, new_number_of_pages)
        elif choice == 4: #Delete book
            book_name = str(input("Enter the book's name you want to delete: "))
            booksSDK.removeBookByTitle(book_name)
        elif choice == 5: #Show books
            print("\nHere is the table of books: ")
            for book in booksSDK.getBooks():
                print(book)
            print()
    except: 
        decision = input("Oops! Something went wrong\nDo you want to keep using this app? (Y/N): ")
        decision_first_char = str(decision)[0].lower()
        if decision_first_char == 'n': break
        elif decision_first_char == 'y': pass
