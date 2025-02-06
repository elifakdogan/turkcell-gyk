from book import Book
from exceptions import BookAlreadyExistsError

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        for existing_book in self.books:
            if existing_book._Book__isbn == book._Book__isbn:
                raise BookAlreadyExistsError(f"Kitap zaten ekli: {book.book_name} - {book._Book__isbn}")
        self.books.append(book)
        print(f"Kitap eklendi: {book.book_info()}")

    def remove_book(self, isbn: str):
        for book in self.books:
            if book._Book__isbn == isbn:
                self.books.remove(book)
                print(f"Kitap silindi: {book.book_info()}")
                return
        print(f"Kitap bulunamadı: {isbn}")

    def show_books(self):
        if not self.books:
            print("Kütüphanede hiç kitap yok!")
            return

        print("Kütüphanedeki Kitaplar:")
        for book in self.books:
            print(f"  - {book.book_info()}")
