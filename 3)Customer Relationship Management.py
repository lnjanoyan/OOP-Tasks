import abc
import datetime


class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.history = []


class Interaction(abc.ABC):
    def __init__(self, customer: Customer):
        self.customer = customer
        self.type = 'Interaction'


class Sale(Interaction):
    def __init__(self, date, customer: Customer, amount: float, warrant_period: str):
        super().__init__(customer)
        self.date = date
        self.amount = amount
        self.warranty_period = warrant_period
        self.type = 'Sale'


class WarrantyService(Interaction):
    def __init__(self, sale_info: str, customer: Customer, service_cost: float):
        super().__init__(customer)
        self.sale_info = sale_info
        self.service_cost = service_cost
        self.type = "Warranty type"


class Complaint(Interaction):
    def __init__(self, sale_info: str, customer: Customer, complaint_desc):
        super().__init__(customer)
        self.sale_info = sale_info
        self.complaint_desc = complaint_desc
        self.type = 'Complaint'


class System(abc.ABC):
    @abc.abstractmethod
    def register_customer(self, customer: Customer):
        pass

    @abc.abstractmethod
    def generate_report(self, customer: Customer):
        pass

    @abc.abstractmethod
    def record_interaction(self, customer: Customer, interaction: Interaction):
        pass

    @abc.abstractmethod
    def view_history(self, customer: Customer):
        pass

    @abc.abstractmethod
    def save_report(self, customer: Customer):
        pass


class MySystem(System):
    def __init__(self):
        self.customers = []
        self.customer_history = []
        self.report = ''

    def register_customer(self, customer: Customer):
        self.customers.append(customer.name)

    def record_interaction(self, customer: Customer, interaction: Interaction):
        customer.history.append(interaction.type)

    def view_history(self, customer: Customer):
        print(f"{customer.name}'s history: {customer.history}")

    def generate_report(self, customer: Customer):
        self.report = f"{customer.name}'s report:\nCustomer info:{customer.name}\nContact info:" \
                      f"{customer.contact_info}\nHistory:{customer.history}"
        print(self.report)

    def save_report(self, customer: Customer):
        filename = f"{customer.name}'s report {datetime.datetime.now().strftime('%d.%m.%Y,%H;%M;%S')}.txt"
        f = open(filename, 'w')
        f.write(self.report)
        f.close()


customer1 = Customer('Anna', '+65635131')
sale = Sale('02.11.2022', customer1, 325.45, '2 years')
warranty_serv = WarrantyService('info', customer1, 250)
complaint = Complaint('info', customer1, 'description')
system = MySystem()
system.register_customer(customer1)
system.record_interaction(customer1, complaint)
system.record_interaction(customer1, warranty_serv)
system.view_history(customer1)
system.generate_report(customer1)
system.save_report(customer1)
