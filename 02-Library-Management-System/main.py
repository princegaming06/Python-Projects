class Book:
    def __init__(self, title, author, ID):
        self.title = title
        self.author = author
        self.Id = ID
        self.original_books = 0
        self.book_remain = 0
    def __repr__(self):
        return f"book(title = {self.title}, author = {self.author}, id = {self.Id})"
    
class Library:
    def __init__(self):
        self.books = []
        self.issued_book = []
        
    def addBook(self, book):
        self.books.append(self.book)
        book.original_books += 1
        book.book_remain += 1
        print("Added Success!\n")
    def remove(self, Id):
        book_locate = False
        for book in self.books:
            if (Id == book.Id):
                self.books.remove(book)
                print(f"{book} Removed Successfully.\n")
                book_locate = True
                book.original_books -= 1
                book.book_remain -= 1
        if (book_locate == True):
            book.original_books -= 1
            book.book_remain -= 1
        else:
            print(f"Book Note Removed! at {Id}\n")
    def findBook(self, Id):
        book_locate = False
        for book in self.books:
            if (Id == book.Id):
                if (book.book_remain == 1):
                    print(f"{book.book_remain} copy is available of {book}.\n")
                else:
                    print(f"{book.book_remain} copies are available of {book}.\n")
                book_locate = True
        if (book_locate == False):
            print(f"Book Not Found! at id: {Id}\n")
    def issueBook(self, Id):
        book_locate = False
        for book in self.books:
            if (Id == book.Id):
                book_locate = True
                self.books.remove(book)
                self.issued_book.append(book)
                book.book_remain -= 1
                if (book.book_remain == 1):
                    print(f"{book} is issued! {book.book_remain} copy is available of {book}.\n")
                else:
                    print(f"{book} is issued! {book.book_remain} copies are available of {book}.\n")
        if (book_locate == False):
            for book in self.issued_book:
                if (Id == book.Id):
                    book_locate = True
                    print(f"{book.book_remain} copies are available for issue of book: {book}\n")
            if (book_locate == False):
                print(f"Book Not Found for issue! at id: {Id}\n")   
    def returnBook(self, Id):
        book_locate = False
        for book in self.issued_book:
            if (Id == book.Id):
                book_locate = True
                self.books.append(book)
                self.issued_book.remove(book)
                book.book_remain += 1
                if (book.book_remain == 1):
                    print(f"{book} is Returned! {book.book_remain} copy is available of {book}.\n")
                else:
                    print(f"{book} is Returned! {book.book_remain} copies are available of {book}.\n")
        if (book_locate == False):
            print(f"Book Not Found for Return! at id: {Id}\n")
    def showAllBook(self):
        print("Available Books\n")
        for book in self.books:
            print(book)
        print("\nIssued Books\n")
        for book in self.issued_book:
            print(book)
        print()
        
                
