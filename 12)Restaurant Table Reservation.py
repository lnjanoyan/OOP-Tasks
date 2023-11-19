import abc
import datetime


class Table:
    def __init__(self, number: int, seating_capacity: int):
        self.number = number
        self.seating_capacity = seating_capacity
        self.is_available = True
        self.booked_user = ''
        self.booking_days = []


class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.booked_tables = []


class System(abc.ABC):
    @abc.abstractmethod
    def register_user(self,user):
        pass

    @abc.abstractmethod
    def register_table(self,table):
        pass


class RestaurantSystem(System):
    def __init__(self, table_counts):
        self.users = []
        self.tables = dict()
        self.report = ''

    def register_user(self, user: User):
        self.users.append(user)

    def register_table(self, table: Table):
        self.tables[table.number] = [table.seating_capacity, table.is_available, table.booked_user, table.booking_days]

    def search_and_book_table(self, user: User, seating_capacity: int):
        res = []
        print('Here are available tables based on your search parameters:')
        for i in self.tables.keys():
            if self.tables[i][0] == seating_capacity:
                if self.tables[i][1] is True:
                    res.append(i)
                    print(i)
        try:
            inp = int(input('\nChoose a number of table you want to book:'))

        except:
            print('Wrong input')
            return
        if inp in res:
            self.tables[inp][2] = user.name
            self.tables[inp][1] = False
            user.booked_tables.append(inp)
            self.tables[inp][3].append(datetime.datetime.now().day)
            print('Booking successfully done!!!')

        else:
            print('No such table in suggestion list')

    def generate_report(self, day: int):
        self.report+=f"Day: {day}, Reserved tables numbers: "
        for u in self.users:
            for n in u.booked_tables:
                if day in self.tables[n][3]:
                    self.report += f"{str(n)} "

        print(self.report)

    def save_report(self, user: User):
        f = open(f"Report.txt", 'a')
        f.write(self.report)
        f.close()


user1 = User('Anna', '+6544')
table1 = Table(1, 6)
table2 = Table(2, 6)
sys = RestaurantSystem(10)
sys.register_user(user1)
sys.register_table(table1)
sys.register_table(table2)
sys.search_and_book_table(user1, 6)
sys.search_and_book_table(user1,6)
sys.generate_report(13)
sys.save_report(user1)