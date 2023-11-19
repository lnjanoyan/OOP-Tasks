# hamarya done
import abc


class Car(abc.ABC):
    def __init__(self, make: str, model: str, price: float):
        self.make = make
        self.model = model
        self.price = price


class ElectricCar(Car):
    def __init__(self, make: str, model: str, price: float):
        super().__init__(make, model, price)
        self.inventory_rate = 20


class HybridCar(Car):
    def __init__(self, make: str, model: str, price: float):
        super().__init__(make, model, price)
        self.inventory_rate = 10


class SalesPeople:
    def __init__(self, name: str, commission_rate: float):
        self.name = name
        self.commission_rate = commission_rate
        self.cars_list = []
        self.history = []

    def get_new_car(self, make: str, model: str, price: float):
        new_car = Car(make, model, price)
        self.cars_list.append(new_car)
        return new_car

    def manage_inventory(self, car: Car):
        print(f'Inventory successfully done. Cost: {car.inventory_rate * 200}')

    def view_history(self):
        for i in self.history:
            print(f'model:{i.model}, maker: {i.maker}, price: {i.price}')


class Customer:

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def search_car(self, model_name: str, maker_name: str, salespeople):
        for i in salespeople.cars_list:
            if i.model == model_name and i.make == maker_name:
                print('Available car')
                self.available = True
                break
        else:
            print('Not available')

    def purchase(self, car: Car, salespeople: SalesPeople):
        Customer.search_car(self, car.make, car.model, salespeople)
        if self.available:
            salespeople.history.append(self)


