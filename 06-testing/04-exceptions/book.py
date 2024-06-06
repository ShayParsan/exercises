class Book:
    def __init__(self, title, isbn):
        if not title or not isbn:
            raise ValueError("Title and ISBN cannot be empty")

        self.title = title
        if self.valid_isbn(isbn):
            self.isbn = isbn
        else:
            raise ValueError("Invalid ISBN")

    def valid_isbn(self, isbn_string):
        isbn = isbn_string.replace('-', '').replace(' ', '')
        if len(isbn) != 13 or not isbn.isdigit():
            return False

        checksum = sum(int(isbn[i]) * (3 if i % 2 != 0 else 1) for i in range(12)) % 10

        return (10 - checksum) % 10 == int(isbn[12])  # Compare checksum with the last digit


new_book = Book('Watchmen', '978-1779501127')
