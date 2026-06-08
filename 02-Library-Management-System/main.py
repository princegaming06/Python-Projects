class Book:
    def __init__(self, title, author, ID):
        self.title = title
        self.author = author
        self.Id = ID
        self.original_books = 0
        self.book_remain = 0
    def __repr__(self):
        return f"book(title = {self.title}, author = {self.author}, id = {self.Id}, available = {self.book_remain})"
    
class Library:
    def __init__(self):
        self.books = []
        self.issued_book = []
    def addBook(self, book):
        book_arr = self.books
        if len(book_arr) == 0:
            book_arr.append(book)
        else:
            for checkBook in book_arr:
                if not book.Id == checkBook.Id:
                    book_arr.append(book)
        book.original_books += 1
        book.book_remain += 1
        # inner chain method
        def inner(next_book):
            checkBook_id = set()
            for checkBook in book_arr:
                checkBook_id.add(checkBook.Id)
            if not next_book.Id in checkBook_id:
                book_arr.append(next_book)
            next_book.original_books += 1
            next_book.book_remain += 1
            return inner
        print(f"books Added Successfully!\n")
        return inner
    def remove(self, Id):
        book_locate = False
        for book in self.books:
            if (Id == book.Id):
                book_locate = True
                self.books.remove(book)
                book.original_books -= 1
                book.book_remain -= 1
                print(f"{book} Removed Successfully.\n")
        if (book_locate == False):
            print(f"Book Note Removed! at {Id}\n")
    def findBook(self, Id):
        book_locate = False
        book_result = False
        for book in self.books:
            if (Id == book.Id):
                book_result = True
                book_locate = True
                resulted_book = book
                resulted_book_remain = book.book_remain
        if (book_result == True):
            if (resulted_book_remain == 1):
                print(f"{resulted_book_remain} copy is available of {resulted_book}.\n")
            else:
                print(f"{resulted_book_remain} copies are available of {resulted_book}.\n")
        if (book_locate == False):
            for book in self.issued_book:
                if (Id == book.Id):
                    book_locate = True
                    print(f"{book} is issued! we'll get this book very soon!")
        if (book_locate == False):
            print(f"Book Not Found! at id: {Id}\n")
    def issueBook(self, Id):
        book_locate = False
        book_result = False
        for book in self.books:
            if (Id == book.Id):
                book_locate = True
                self.books.remove(book)
                self.issued_book.append(book)
                book.book_remain -= 1
                book_result = True
                resulted_book = book
                resulted_book_remain = book.book_remain
        if (book_result == True):
            if (resulted_book_remain == 1):
                print(f"{resulted_book} is issued! {resulted_book_remain} copy is available of {resulted_book}.\n")
            else:
                print(f"{resulted_book} is issued! {resulted_book_remain} copies are available of {resulted_book}.\n")
        if (book_locate == False):
            book_result = False
            for book in self.issued_book:
                if (Id == book.Id):
                    book_locate = True
                    book_result = True
                    resulted_book = book
                    resulted_book_remain = book.book_remain
            if (book_result == True):
                print(f"{resulted_book_remain} copies are available for issue of book: {resulted_book}\n")
            if (book_locate == False):
                print(f"Book Not Found for issue! at id: {Id}\n")   
    def returnBook(self, Id):
        book_locate = False
        book_result = False
        for book in self.issued_book:
            if (Id == book.Id):
                book_locate = True
                self.books.append(book)
                self.issued_book.remove(book)
                book.book_remain += 1
                book_result = True
                resulted_book = book
                resulted_book_remain = book.book_remain
        if (book_result == True):
            if (resulted_book_remain== 1):
                print(f"{book} is Returned! Now {resulted_book_remain} copy is available of {resulted_book}.\n")
            else:
                print(f"{book} is Returned! Now {resulted_book_remain} copies are available of {resulted_book}.\n")
        if (book_locate == False):
            print(f"Book Not Found for Return! at id: {Id}\n")
    def showAllBook(self):
        print("Available Books:")
        for book in self.books:
            print(book)
        if (len(self.issued_book) > 0):
            print("\nIssued Books")
            for book in self.issued_book:
                print(book)
        print()
        
# Save Book in Book Class
book1 = Book("Ayurdarshan", "Vimaleshvaranand", 101)
book2 = Book("Sadhna Path", "Osho", 102)
book3 = Book("What Are You Doing With Your Life", "J. KrishnaMurti", 103)
book4 = Book("Art Of Netroar Studios", "Prince Singh", 104)

# Save an Library
netLibrary = Library()

# Add Books in Library
netLibrary.addBook(book1)(book2)(book3)(book4)(book3)(book4)(book4)
netLibrary.showAllBook()
netLibrary.findBook(101)
# netLibrary.findBook(104)
netLibrary.issueBook(104)
# netLibrary.issueBook(101)
netLibrary.showAllBook()
netLibrary.returnBook(104)
netLibrary.remove(104)
