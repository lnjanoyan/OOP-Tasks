# jamanak unelu depqum sra jamery kdzes Els)
import abc


class Book:
    def __init__(self, title: str, author: str, genre: str, available_status: bool):
        self.title = title
        self.author = author
        self.genre = genre
        self.available_status = available_status
        self.searching_criteria = ''
        self.unavailable_hours = 0
        self.borrow_hours = 0


class Member:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.borrowed_books = []


class LibrarySystem(abc.ABC):

    @abc.abstractmethod
    def member_register(self, member: Member):
        pass

    @abc.abstractmethod
    def book_register(self, book: Book):
        pass

    @abc.abstractmethod
    def borrow_book(self, book: Book, member: Member, borrow_hours: float):
        pass

    @abc.abstractmethod
    def search_book(self, search_by: str, search_word):
        pass

    @abc.abstractmethod
    def return_book(self, book: Book, member: Member):
        pass

    @abc.abstractmethod
    def overdue_report_creation(self, book: Book, member: Member):
        pass


class MySystem(LibrarySystem):
    def __init__(self):
        self.library_books = []
        self.registered_members = []
        self.searching_category = None

    def member_register(self, member: Member):
        self.registered_members.append(member)

    def book_register(self, book: Book):
        self.library_books.append(book)

    def borrow_book(self, book: Book, member: Member, borrow_hours: float):
        if book.available_status is False:
            print('Book is not available now.')
            return
        book.available_status = False
        book.unavailable_hours += borrow_hours
        book.borrow_hours = borrow_hours
        member.borrowed_books.append(book)
        print(f"{book.title} book is borrowed by {member.name} for {book.borrow_hours} hours.")

    def search_book(self, search_by: str, search_word: str):
        if search_by.lower() == 'author':
            for i in self.library_books:
                if i.author == search_word.lower():
                    print(f'Book {search_word} was found')
        elif search_by.lower() == 'title':
            for i in self.library_books:
                if i.title == search_word.lower():
                    print(f'Book {search_word} was found')
        elif search_by.lower() == 'genre':
            for i in self.library_books:
                if i.genre == search_word.lower():
                    print(f'Book {search_word} was found')
        else:
            print('No such book in library books.')

    def overdue_report_creation(self, book: Book, member: Member):
        fl = open('report_file.txt', 'w')
        fl.write(f'Book  information \ntitle: {book.title}, genre:{book.genre}, author: {book.author}\n '
                 f'Member information \n name: {member.name},contact: {member.contact_info}')
        fl.close()

    def return_book(self, book: Book, member: Member):
        book.available_status = True
        if book in member.borrowed_books:
            if book.borrow_hours <= book.unavailable_hours:
                member.borrowed_books.remove(book)
                book.unavailable_hours = 0
                print(f"{book.title} was returned back to library.")
            else:
                self.overdue_report_creation(book, member)

        else:
            print('No such book in your borrowed books list')

    def view_library(self):
        print('Library books: ')
        for i in self.library_books:
            print(i.title, sep=', ')


member = Member('name1', '+6358131')
book1 = Book('title1', 'author1', 'genre1', True)
book2 = Book('title2', 'author2', 'genre2', True)
sys = MySystem()
sys.book_register(book1)
sys.view_library()
sys.search_book('title','title1')
sys.borrow_book(book1, member, 3)
sys.return_book(book1, member)
sys.overdue_report_creation(book1,member)
