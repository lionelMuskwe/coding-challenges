class User:

    def __init__(self, name):
        self.name = name
        self.books = []

    def checkoutBook(self, book):
        self.books.append(book)