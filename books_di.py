"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""


class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book:
    def __init__(self, author: set, title):
        self.author = author
        self.title = title


class BookFe:
    def __init__(self, author_name, author_surname, title):
        self.author = Author(author_name, author_surname)
        self.title = title


if __name__ == '__main__':
    boleslaw_prus = Author('Bolesław', 'Prus')

    book = Book({boleslaw_prus}, 'Lalka')
    book_2 = Book({boleslaw_prus}, 'Cokolwiek')

    print(f'Book: "{book.title}" written by: {book.author} {book.author}')
    print(f'Book: "{book_2.title}" written by: {book_2.author} {book_2.author}')
