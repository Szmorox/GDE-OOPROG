from tickets import Tickets


class Reservation_system(Tickets):
    def __init__(self):
        self.reservations = []

    def to_reserve(self, name_of_passenger: str, flight_number, destination: str, airline: str):
        reserve = Tickets(name_of_passenger, flight_number,
                          destination, airline)
        self.reservations.append(reserve)

    def cancel(self, name_of_passenger: str, flight_number):
        for i in self.reservations:
            if i.name_of_passenger == name_of_passenger and i.flight_number == flight_number:
                self.reservations.remove(i)
                return True
        return False

    def listing_flights(self, flight):
        print('\n=== Available flights: ===')
        for i, flight in enumerate(flight):
            print(f'{i + 1}. {flight}')

    def menu(self):
        print("\n=== Repülőjegy Foglalási Rendszer ===")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("0. Kilépés")
