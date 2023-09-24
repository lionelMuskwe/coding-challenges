from Library import *
from Book import *
from User import *

class LibraryInterface():
    spacer = "\t"

    def __init__(self, library, user):
        self.library = library
        self.user = user
        print("New Lib Interface")


    def startInterface(self):
        while True:
            self.showUserOptions()
            userMenuInput = self.getUserInterfaceOption()
            self.findAppropriateAction(userMenuInput)


    def showUserOptions(self):
        print("1: Display available books")
        print("2: Display non-available books")
        print("3: Checkout book")
        print("4: Exit application")

    def getUserInterfaceOption(self):
        userInput = input("\n\tPlease select an option i.e 1: " )
        validOptions = ["1", "2", "3", "4"]

        if userInput in validOptions:
            return userInput
        else:
            print(f"\n\t\t {userInput} is not a valid input \n ")

    def findAppropriateAction(self, action):
        if action == "1":
            self.handleDisplayAllAvailableBooks()
        elif action == "2":
            self.handleDisplayAllCheckedoutBooks
        elif action == "3":
            self.handleCheckoutBook()
        elif action == "4":
            self.handleApplicationClose()


    def handleDisplayAllAvailableBooks(self):
        self.library.listAllAvailableBooks()


    def handleDisplayAllCheckedoutBooks(self):
        self.library.listAllCheckedoutBooks()


    def handleCheckoutBook(self):
        while True:
            print(f"{self.spacer} [Book Checkout]- Checkout book menu ")
            targetBookTitle = input("\t Enter book name: ")

            book = self.library.doesBookExistInLibrary(targetBookTitle)
            print(f"**** {book}")
            if book != False:
                self.user.checkoutBook(book)
                self.library.checkOutBook(targetBookTitle)
                print(f"{self.spacer} [SUCCESS] Succesfully checked out {book.getTitle()}")
                break
            else:
                print(f"{self.spacer} [ERROR] Failed to find your book in our records")
                break


    def handleApplicationClose(self):
        exit()

