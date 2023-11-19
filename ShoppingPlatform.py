import abc


class Product:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

    def change_description(self, new_desc: str):
        self.description = new_desc


class Electronics(Product):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.warranty = '3 years'


class Clothing(Product):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.import_from = 'usa'


class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.shopping_cart = []
        self.history = []


class Order:
    def __init__(self, customer: Customer, product: Product, tot_price: float):
        self.customer = customer
        self.product = product
        self.tot_price = tot_price


class OrderOperation(abc.ABC):

    @abc.abstractmethod
    def search_product(self, product: Product):
        pass

    @abc.abstractmethod
    def view_order_history(self, customer: Customer):
        pass

    @abc.abstractmethod
    def purchase(self, customer: Customer):
        pass


class MySystem(OrderOperation):
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def view_order_history(self, customer: Customer):
        print(customer.history)

    def search_product(self, product: Product):
        if product in self.products:
            print('Product is available')
            return True
        print('Not available')
        return False

    def add_to_cart(self, product: Product, customer: Customer):
        customer.shopping_cart.append(product)

    def purchase(self, customer: Customer):
        for i in customer.shopping_cart:
            customer.history.append(i)
