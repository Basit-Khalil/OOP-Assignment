class Book:
    total_books = 0  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book("Harry Potter and the Half-Blood Prince", "J.K. Rowling")
book2 = Book("Sherlock Holmes: The Hound of the Baskervilles", "Conan Doyle")

print(Book.total_books)