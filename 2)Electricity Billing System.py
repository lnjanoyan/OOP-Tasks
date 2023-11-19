# almost done

import abc
import datetime


class Customer:
    def __init__(self, name: str, contact_info: str, meter_number: float):
        self.name = name
        self.contact_info = contact_info
        self.meter_number = meter_number
        self.bill = None
        self.consumption=None


class System(abc.ABC):
    @abc.abstractmethod
    def register_customer(self, customer: Customer):
        pass

    @abc.abstractmethod
    def get_consumption(self):
        pass

    @abc.abstractmethod
    def calculate_bill(self):
        pass

    @abc.abstractmethod
    def generate_bill(self):
        pass

    @abc.abstractmethod
    def save_bill(self):
        pass


class MySystem:
    def __init__(self):
        self.customers = []
        self.consumption = ''

    def register_customer(self, customer: Customer):
        self.customers.append(customer.name)

    def get_consumption(self,customer:Customer):
        while True:
            consumption = input('Input electricity consumption with KWatts ')
            if consumption.isdigit():
                customer.consumption = float(consumption)
                break
            else:
                print('Consumption must be a float number,try again.')
        # check validations

    def calculate_bill(self, customer: Customer, preset_rate):
        customer.bill = self.consumption * preset_rate
        print(f"Calculated bill = {customer.bill}")
        return customer.bill

    def generate_bill(self, customer: Customer):
        customer.bill = f"\n{customer.name}'s bill:\nCustomer info- Name:{customer.name}, Contact info:" \
                        f"{customer.contact_info}, Meter number:{customer.meter_number}\n" \
                        f"Electricity consumption:{self.consumption} \nBill: {customer.bill}"
        print(customer.bill)

    def save_bill(self, customer: Customer):
        filename = f"{customer.name}' bill at {datetime.datetime.now().strftime('%d.%m.%Y %H;%M;%S')}"
        f = open(filename, 'w')
        f.write(customer.bill)
        f.close()


customer1 = Customer('Lily', '+365841655', 456)
customer2 = Customer('Bob', '+5165513', 786)
system = MySystem()
system.register_customer(customer1)
system.register_customer(customer2)
print('Customers: ', system.customers)
system.get_consumption()
system.calculate_bill(customer1, 0.45)
system.generate_bill(customer1)
system.save_bill(customer1)
