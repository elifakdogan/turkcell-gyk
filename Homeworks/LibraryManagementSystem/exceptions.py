class BookAlreadyExistsError(Exception):
    def __init__(self, message = "Bu ISBN numarasına sahip kitap var!"):
        super().__init__(message)