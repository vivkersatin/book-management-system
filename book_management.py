# book_management.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f'Book "{book.title}" added successfully.'

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f'Book "{book.title}" removed successfully.'
        return 'Book not found.'

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return 'Book not found.'

    def update_book(self, isbn, title=None, author=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                return f'Book "{book.title}" updated successfully.'
        return 'Book not found.'

# Test script
if __name__ == "__main__":
    manager = BookManager()

    # Add books
    manager.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890"))
    manager.add_book(Book("1984", "George Orwell", "0987654321"))

    # Find a book
    book = manager.find_book("1234567890")
    if isinstance(book, Book):
        print(f'Found book: {book.title} by {book.author}')
    else:
        print(book)

    # Update a book
    print(manager.update_book("1234567890", title="The Greatest Gatsby"))

    # Remove a book
    print(manager.remove_book("1234567890"))
