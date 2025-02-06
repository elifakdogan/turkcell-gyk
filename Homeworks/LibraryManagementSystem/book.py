class Book:
    def __init__(self, book_name, author,number_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.number_pages = number_pages
        self.__isbn = isbn

    def is_isbn_match (self,isbn):
        return self.__isbn == isbn
    
    def book_info(self):
        return f"Kitap: {self.book_name} - Yazar: {self.author} - Sayfa Sayısı: {self.number_pages} - ISBN: {self.__isbn}"

