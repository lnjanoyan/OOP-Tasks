class TravelPackage:
    def __init__(self, destination: str, price: float, slots: int):
        self.destination = destination
        self.price = price
        self.slots = slots
        self.available_slots = slots
        self.is_search_result = False


class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.booked_packages = []
        self.tickets = ''


class Administrator:
    def create_package(self, destination, price, slots):
        return TravelPackage(destination, price, slots)


class System:
    def __init__(self):
        self.users = []
        self.packages = []
        self.report = ''

    def register_user(self, user):
        self.users.append(user)

    def register_packages(self, package):
        self.packages.append(package)

    def search(self, price, slots):
        for i in self.packages:
            if i.price <= price:
                if i.available_slots >= slots:
                    i.is_search_result = True
                    print(i.destination, i.price, i.available_slots)

    def generate_ticket(self, package, user):
        user.tickets = f"information ({package.destination} alarel em grem)"
        print(user.tickets)

    def generate_report(self, package: TravelPackage):
        self.report = f"Package info:\ndestination:{package.destination}\nprice:{package.price}\nbooked slots:" \
                      f"{package.slots - package.available_slots}"

        f = open(f"{package.destination}'s report.txt", 'a')
        f.write(self.report)
        f.close()

    def book_package(self, package: TravelPackage, user: User):
        if package in self.packages:
            if package.is_search_result:
                user.booked_packages.append(package)
                package.available_slots -= 1
                self.generate_ticket(package, user)
                print('Booking is successfully done!')


user1 = User('name1', '+45165313')
admin1 = Administrator()
pack1 = admin1.create_package('dest1', 250, 45)
sys = System()
sys.register_user(user1)
sys.register_packages(pack1)
sys.search(300, 4)
sys.book_package(pack1, user1)
sys.generate_report(pack1)

