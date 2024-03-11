class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    


    def get_description(self):
        return f"{self.title} By {self.author}"
    

book = Book("Harry Potter And the Deathly Hallows", "J.K Rowling")

book.get_description()