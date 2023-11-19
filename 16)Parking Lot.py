import datetime


class ParkingSpace:
    def __init__(self, number: int, size: float):
        self.number = number
        self.size = size
        self.status = 'available'
        self.start_time = None
        self.end_time = None
        self.reservers = []
        self.receipt = ''
        self.time_duration = None
        self.average_time = 0


class User:
    def __init__(self, name: str, contact_info: str, car: str):
        self.name = name
        self.contact_info = contact_info
        self.reserved_spaces = []
        self.car = car


class System:
    def __init__(self):
        self.users = []
        self.spaces = []
        self.report = ''
        self.times = 0
        self.count = 0

    def register_space(self, space: ParkingSpace):
        self.spaces.append(space)

    def register_user(self, user: User):
        self.users.append(user)

    def reserve(self, user: User, space: ParkingSpace):
        if space in self.spaces:
            if space.status == 'available':
                user.reserved_spaces.append(space)
                space.status = 'occupied'
                space.reservers.append(user)
                self.count += 1
                space.start_time = datetime.datetime.now()
                print('Successfully reserved.')
            else:
                print('Not available')
        else:
            print('Not in space list')

    def generate_receipt(self, space: ParkingSpace, cost):
        space.receipt = f"Number {space.number} space receipt:\nDuration:{space.time_duration}\nSize:{space.size}\nCost: {cost}"
        print(space.receipt)

    def calculate_fee(self, space: ParkingSpace):
        space.end_time = datetime.datetime.now()
        self.time_duration = (space.end_time - space.start_time).seconds // 3600
        size_rate = None
        time_rate = None
        self.times += self.time_duration
        if space.size < 30:
            size_rate = 0.2
        elif 30 <= space.size < 60:
            size_rate = 0.4
        elif 60 <= space.size:
            size_rate = 0.6

        if self.time_duration < 1:
            time_rate = 0.25
        elif 1 <= self.time_duration < 2:
            time_rate = 0.46
        else:
            time_rate = 0.55
        cost = size_rate * time_rate * 10000
        self.generate_receipt(space, cost)
        print('Total cost of parking: ', float(cost))
        return cost

    def generate_report(self, space: ParkingSpace):
        self.report += f"Parking area report\n"
        average = self.time_duration / self.count
        for u in self.users:
            for s in u.reserved_spaces:
                self.report += f"Car:{u.car}, duration:{s.time_duration}, cost:{self.calculate_fee(s)}\n," \
                               f"average time:{average} "

        f = open(f"{space.number}th space report.txt", 'a')
        f.write(self.report)
        f.close()


us = User('anna', '+54521', 'car_name')
space1 = ParkingSpace(1, 45)
space2 = ParkingSpace(2, 60)
sys = System()
sys.register_space(space1)
sys.register_space(space2)
sys.register_user(us)
sys.reserve(us, space1)
sys.calculate_fee(space1)
sys.generate_report(space1)
