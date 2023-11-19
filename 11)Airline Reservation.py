import abc


class Flight:
    def __init__(self, number: int, origin: str, destination: str, departure: str, datetime: str, available_seats):
        self.number = number
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.datetime = datetime
        self.available_seats = available_seats
        self.seats = dict().fromkeys(range(1, available_seats + 1))


class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.booked_seats = []
        self.ticket = ''


class System(abc.ABC):
    @abc.abstractmethod
    def register_user(self, user: User):
        pass

    @abc.abstractmethod
    def register_flight(self, flight: Flight):
        pass

    @abc.abstractmethod
    def search_flight(self, search_by: str, search_word: str):
        pass

    @abc.abstractmethod
    def book_seat(self, user: User, flight: Flight, ):
        pass


class MySystem(System):
    def __init__(self):
        self.users = []
        self.flights = []

    def register_user(self, user: User):
        self.users.append(user)

    def register_flight(self, flight: Flight):
        self.flights.append(flight)

    def search_flight(self, search_by: str, search_word: str):
        if search_by.lower() == 'destination':
            for i in self.flights:
                if i.destination == search_word.lower():
                    print(f'Flight with {search_word} destination was found')

        elif search_by.lower() == 'origin':
            for i in self.flights:
                if i.origin == search_word.lower():
                    print(f'Flight with origin {search_word} was found')

        elif search_by.lower() == 'datetime':
            for i in self.flights:
                if i.datetime == search_word.lower():
                    print(f'Flight with date {search_word} was found')
        else:
            print('No such flight with parameter', search_word)

    def generate_ticket(self, user: User, flight: Flight, seat_num: int):
        user.ticket = f"User:\nName: {user.name}\nContact info: {user.contact_info}\nFlight info: \n" \
                      f"Flight number: {flight.number}\nDate/time: {flight.datetime}\nSeat number: {seat_num}"
        print(user.ticket)

    def book_seat(self, user: User, flight: Flight, ):
        if flight.available_seats == 0:
            print('No available seats in this flight')
            return
        else:
            print('Here are available seats:')

        for i in flight.seats.keys():
            if flight.seats[i] is None:
                print(i)

        inp = int(input('Choose number of seat you want to book:'))
        if inp in flight.seats.keys():
            if flight.seats[inp] is None:
                flight.seats[inp] = user.name
                flight.available_seats -= 0
                user.booked_seats.append(inp)
                self.generate_ticket(user, flight, inp)
                print('Booking successfully done!!!')
            else:
                print('Seat is not available now')
        else:
            print('No such seat number available')

    def save_ticket(self, user: User):
        f = open(f"{user.name}'s Ticket.txt", 'w')
        f.write(user.ticket)
        f.close()


user1 = User('Anna', '+6544')
flight = Flight(15, 'orig', 'dest', 'depart', '21.02', 40)
sys = MySystem()
sys.register_user(user1)
sys.register_flight(flight)
sys.search_flight('number', '15')
sys.search_flight('ORigin', 'orig')
sys.book_seat(user1, flight)
sys.book_seat(user1, flight)
sys.save_ticket(user1)
