class Movie:
    def __init__(self, title: str, duration: str, rating: float, show_times: str):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.show_times = show_times
        self.founded = False
        self.seats_count = 30
        self.available_seats = list(range(1, 31))


class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.booked_movies = []
        self.tickets = ''


class System:
    def __init__(self):
        self.movies = []
        self.users = []
        self.report = ''

    def register_movie(self, movie: Movie):
        self.movies.append(movie)

    def register_user(self, user: User):
        self.users.append(user)

    def search_movie(self, search_title: str):
        for i in self.movies:
            if i.title.lower() == search_title.lower():
                i.founded = True
                print('Searching results:\n')
                print(f'Title: {i.title}, duration:{i.duration}, show time: {i.show_times}')
                break
        else:
            print('No such movie in list.')

    def generate_ticket(self, movie: Movie, user: User, seat: int):
        user.ticket = f"Ticket:\nUser info: {user.name},{user.contact_info}\nMovie info: {movie.title},{movie.duration}," \
                      f"{movie.show_times}\nSeat number:{seat}"
        print(user.ticket)

    def save_report(self, movie: Movie):
        self.report = f"Movie:{movie.title},\nShow times:{movie.show_times},\nAvailable seats count" \
                      f":{movie.seats_count},\nAvailable seats : {movie.available_seats}"

        f = open(f"{movie.title}'s report.txt", 'w')
        f.write(self.report)
        f.close()

    def book_tickets(self, user: User, movie: Movie):
        if movie.founded is True:
            if movie.seats_count != 0:
                print('Available seats: ')
                for i in movie.available_seats:
                    print(i, end=' ')
                inp = input('\nChoose your seat for booking: ')
                try:
                    inp = int(inp)
                except:
                    print('Wrong input')
                    return
                if inp in movie.available_seats:
                    user.booked_movies.append(movie)
                    movie.seats_count -= 1
                    movie.available_seats.remove(inp)
                    print('Booking was successfully done.')
                    self.generate_ticket(movie, user, inp)
                else:
                    print('Seat is not available.')
                    return

            else:
                print('No available seats,showtime is fully blocked.')
        else:
            print('Movie not found')


movie = Movie('title1', '2:15:00', 4.75, '14:00')
user = User('Anna', '+4654165')
sys = System()
sys.register_user(user)
sys.register_movie(movie)
sys.search_movie('title1')
sys.book_tickets(user, movie)
sys.save_report(movie)
