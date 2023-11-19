class Taxi:
    def __init__(self, number: int, driver: str, taxi_class: str):
        self.number = number
        self.driver = driver
        self.taxi_class = taxi_class
        self.is_available = True
        self.current_ride_fee = None


class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.booked_taxis = []


class System:
    def __init__(self):
        self.users = []
        self.taxis = dict()
        self.report = ''

    def register_taxi(self, taxi: Taxi):
        self.taxis[taxi.number] = dict(driver=taxi.driver, taxi_class=taxi.taxi_class, is_available=taxi.is_available)

    def register_user(self, user: User):
        self.users.append(user)

    def book_taxi(self, user: User):
        print('Here are available taxis numbers')
        available_numbers = []
        for key in self.taxis:
            if self.taxis[key]['is_available'] is True:
                available_numbers.append(key)
        print(available_numbers)
        try:
            inp = int(input('Choose the number of the taxi you want to book: '))
        except:
            print('Wrong input')
            return
        else:
            if inp in available_numbers:
                self.taxis[inp]['is_available'] = False
                user.booked_taxis.append(inp)
                print(f'Booking of {inp}th taxi is successfully done!')

    def generate_receipt(self, taxi: Taxi, user: User):
        self.report = f"\n{user.name}'s ride receipt:\nRide fee:{taxi.current_ride_fee}\nTaxi info:\nNumber: {taxi.number}," \
                      f" Driver: {taxi.driver}, Class: {taxi.taxi_class}"
        print(self.report)

    def calculate_fee(self, taxi: Taxi, distance: float):
        try:
            distance = float(distance)
        except:
            print('Wrong input for distance,must be float. ')
            return
        if taxi.taxi_class.lower() == 'start':
            rate = 1
        elif taxi.taxi_class.lower() == 'comfort':
            rate = 1.8
        elif taxi.taxi_class.lower() == 'business':
            rate = 3
        else:
            print('No such class')
            return
        taxi.current_ride_fee = rate * 100 * distance
        print('Your ride fee = ', taxi.current_ride_fee)
        self.generate_receipt(taxi, user)
        return taxi.current_ride_fee

    def save_report(self, user: User):
        f = open(f"{user.name}'s receipt.txt", 'w')
        f.write(self.report)
        f.close()


user = User('Ann', '+654566')
taxi1 = Taxi(10, 'Bob', 'business')
taxi2 = Taxi(9, 'Andrew', 'comfort')
sys = System()
sys.register_taxi(taxi1)
sys.register_taxi(taxi2)
sys.book_taxi(user)
sys.calculate_fee(taxi1, 8)
sys.save_report(user)
