# oop/book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor called when the instance is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation, should recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)          # __str__ → 1984 by George Orwell, published in 1949
    print(repr(my_book))    # __repr__ → Book('1984', 'George Orwell', 1949)

    del my_book             # __del__ → Deleting 1984

if __name__ == "__main__":
    main()


