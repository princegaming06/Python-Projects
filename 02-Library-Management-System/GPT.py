class Book:
    def __init__(self, title, author, book_id, copies=1):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.original_books = copies
        self.book_remain = copies

    def __repr__(self):
        return (
            f"Book("
            f"title='{self.title}', "
            f"author='{self.author}', "
            f"id={self.book_id}, "
            f"available={self.book_remain}/{self.original_books}"
            f")"
        )


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                existing_book.original_books += book.original_books
                existing_book.book_remain += book.book_remain
                print(f"Added another copy of '{book.title}'")
                return

        self.books.append(book)
        print(f"Added '{book.title}'")

    def findBook(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def removeBook(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Removed '{book.title}'")
                return

        print("Book not found!")

    def issueBook(self, book_id):
        book = self.findBook(book_id)

        if not book:
            print("Book not found!")
            return

        if book.book_remain == 0:
            print(f"All copies of '{book.title}' are already issued.")
            return

        book.book_remain -= 1

        print(
            f"Issued '{book.title}'. "
            f"Available: {book.book_remain}/{book.original_books}"
        )

    def returnBook(self, book_id):
        book = self.findBook(book_id)

        if not book:
            print("Book not found!")
            return

        if book.book_remain == book.original_books:
            print("No borrowed copy to return.")
            return

        book.book_remain += 1

        print(
            f"Returned '{book.title}'. "
            f"Available: {book.book_remain}/{book.original_books}"
        )

    def showAllBooks(self):
        if not self.books:
            print("Library is empty!")
            return

        print("\n===== LIBRARY BOOKS =====")

        for count, book in enumerate(self.books, start=1):
            print(f"{count}. {book}")

        print()


# ------------------------
# Testing
# ------------------------

library = Library()

book1 = Book("Ayurdarshan", "Vimaleshvaranand", 101, 3)
book2 = Book("Sadhna Path", "Osho", 102, 2)
book3 = Book("What Are You Doing With Your Life", "J. Krishnamurti", 103, 1)

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

library.showAllBooks()

library.issueBook(101)
library.issueBook(101)
library.issueBook(101)
library.issueBook(101)

library.returnBook(101)

library.findBook(102)

library.showAllBooks()