from Book import *
from Library import *
from User import *
from LibraryInterface import *

library = Library("Aston University")

book_1 = Book(
    "tim",
    "J K Rowling",
    2010
    )

book_2 = Book(
    "Interstellar",
    "Christopher Nolan",
    2013
    )

book_3 = Book(
    "Rich dad, poor dad",
    "Robert Kiyosaki",
    2005
    )

library.addBook(book_1)
library.addBook(book_2)
library.addBook(book_3)

user = User("Lionel")
libraryInterface = LibraryInterface(library, user)
libraryInterface.startInterface()


print("\n-----Done running program----")