class Book:
    def __init__(self, title: str, author: str, genre: str, price: float, quantity: int):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity
        self.purchase_count = 0


class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.purchased_books = []
        self.shopping_cart = []
        self.history_report = ''


class System:
    def __init__(self):
        self.books = []
        self.customers = []

    def register_customer(self, customer: Customer):
        self.customers.append(customer)

    def register_book(self, book: Book):
        self.books.append(book)

    def add_to_cart(self, customer: Customer, book: Book):
        if book.quantity==0:
            print('Book is not available now')
            return
        customer.shopping_cart.append(book)
        print(f"{book.title} added to {customer.name}'s cart.")

    def remove_from_cart(self, customer: Customer, book: Book):
        if book in customer.shopping_cart:
            customer.shopping_cart.remove(book)
            print(f"{book.title} was removed from {customer}'s cart.")

    def calculate_cart_books(self, customer: Customer):
        sum = 0
        for i in customer.shopping_cart:
            sum += i.price
        print('Total cost of the shopping cart books is ', sum)

    def purchase(self, customer, book):
        if book in self.books:
            if book.quantity >= 1:
                customer.purchased_books.append(book)
                book.purchase_count += 1
                print(f'{book.title} book"s purchase successfully done!')
            else:
                print('Unfortunately this book is not available now,please try again later. ')
        else:
            print('No such book in bookstore')
        if book in customer.shopping_cart:
            book.quantity -= 1

    def generate_history(self, customer: Customer):
        total_price = 0
        for i in customer.purchased_books:
            customer.history_report += f"Book:{i.title}, Author:{i.author}, Genre:{i.genre}, Price:{i.price}," \
                                       f" Count:{i.purchase_count}\n"
            total_price += i.price
            customer.history_report += f"Total amount: {total_price}"
            print(customer.history_report)

    def save_history(self, customer: Customer):
        f = open(f"{customer.name}'s purchase history.txt", 'w')
        f.write(customer.history_report)
        f.close()


book1 = Book('title1', 'author1', 'genre1', 25, 4)
book2 = Book('title2', 'author2', 'genre2', 30, 2)
cust1 = Customer('name', '+65163516')
sys = System()
sys.register_customer(cust1)
sys.register_book(book1)
sys.register_book(book2)
sys.add_to_cart(cust1, book1)
sys.add_to_cart(cust1, book2)
sys.calculate_cart_books(cust1)
sys.purchase(cust1, book1)
sys.purchase(cust1, book1)
sys.generate_history(cust1)
sys.save_history(cust1)
