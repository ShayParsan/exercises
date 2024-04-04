class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books =[]

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for i in self.books:
            if i.title == book.title and i.author == book.author:
                self.books.remove(i)
                
                

    def search_books(self, search_string):
        
        results = []
        for j in self.books:
            search_string = search_string.lower()
            if search_string in j.title.lower() or search_string in j.author.lower():
                results.append(j)
        
        return results
