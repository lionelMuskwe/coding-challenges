from Book import *

class Library():
    def __init__(self, library_name):
        self.name = library_name
        self.books = []

    def addBook(self, book):
        self.books.append(book)


    def checkOutBook(self, bookTitleToCheckOut):
        bookToCheckout = self.doesBookExistInLibrary(bookTitleToCheckOut)
        if bookToCheckout != False:
            bookToCheckout.checkout()
            return True
        else:
            return False

    def returnBook(self, bookTitleToReturn):
        bookToRetun = self.doesBookExistInLibrary(bookTitleToReturn)
        if bookToRetun != False:
            bookToRetun.checkin()
            return True
        else:
            return False

    def listAllAvailableBooks(self):
        for availableBook in self.books:
            if availableBook.isBookAvailable():
                print(f"\t {availableBook.title} by {availableBook.author} is available")

    def listAllCheckedoutBooks(self):
        for checkoutBook in self.books:
            if checkoutBook.isBookAvailable():
                print(f"\t {checkoutBook.title} by {checkoutBook.author} is currently checked out")


    def doesBookExistInLibrary(self, searchTitle):
        for book in self.books:
            if book.getTitle() == searchTitle:
                return book
            else:
                return False
