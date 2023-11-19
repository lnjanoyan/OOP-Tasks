import abc


class Room:
    def __init__(self, number: int, type: str):
        self.number = number
        self.type = type
        self.is_available = True


class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.booked_rooms = []
        self.total_price = 0
        self.report = ''


class System(abc.ABC):
    @abc.abstractmethod
    def book_room(self, customer: Customer, room: Room, type: str):
        pass


class MySystem(System):
    def __init__(self):
        self.rooms = []
        self.customers = []

    def register_room(self, room: Room):
        self.rooms.append(room)

    def register_customer(self, customer: Customer):
        self.customers.append(customer)

    def book_room(self, customer: Customer, room: Room, type: str):
        if room in self.rooms and room.is_available:
            if type.lower() == room.type:
                customer.booked_rooms.append(room)
                room.is_available = False
                print('Booking successfully done!')
            else:
                print('Not your type of room')
        else:
            print('Room is not available')

    def generate_bill(self, customer: Customer):
        for i in customer.booked_rooms:
            if i.type.lower() == 'single':
                customer.total_price += 10
            elif i.type.lower() == 'double':
                customer.total_price += 20
            elif i.type.lower() == 'suite':
                customer.total_price += 30
            else:
                print('No such type room')

        customer.report = f"{customer.name}'s reserved rooms numbers :"
        for i in customer.booked_rooms:
            customer.report += str(i.number)
        customer.report += f"\nTotal price of reservations: {customer.total_price}$"
        print(customer.report)

    def save_bill(self, customer: Customer):
        f = open('Bill.txt', 'a')
        f.write(customer.report)
        f.close()


room1 = Room(14, 'single')
room2 = Room(16, 'double')
room3 = Room(10, 'sigl')
cust = Customer('Anna', '+644165')
sys = MySystem()
sys.register_room(room1)
sys.register_room(room2)
sys.book_room(cust, room1, 'Single')
sys.book_room(cust, room2, 'Doble')
sys.generate_bill(cust)
sys.save_bill(cust)
