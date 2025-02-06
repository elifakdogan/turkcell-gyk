from book import Book
from library import Library
from exceptions import BookAlreadyExistsError

def main():
    library = Library() 
    
    book1 = Book("1984", "George Orwell", 328, "9780451524935")
    book2 = Book("Hayvan Çiftliği", "George Orwell", 112, "9789750719387")
    book3 = Book("Dönüşüm", "Franz Kafka", 74, "9786053325964")

    try:
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        library.add_book(book1)
    except BookAlreadyExistsError as e:
        print(f"Hata: {e}")

    library.show_books()

    library.remove_book("9780451524935")
    library.remove_book("0000000000000")

    library.show_books()

if __name__ == "__main__":
    main()