class Book():
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.is_available  = True

    def isAvailable(self):
        if self.is_available:
            return f"{self.title} is available"
        else:
            return f"{self.title} is not available"

    def getTitle(self):
        return self.title

    def getAvailability(self):
        return self.is_available

    def checkout(self):
        self.is_available = False

    def checkin(self):
        self.is_available = True

    def isBookAvailable(self):
        return self.is_available == True


