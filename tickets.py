from flights import Flights


class Tickets():
    def __init__(self, name_of_passenger: str, airline: str, flight_number: str, destination: str) -> None:
        self.name_of_passenger = name_of_passenger
        self.airline = airline
        self.flight_number = flight_number
        self.destination = destination

    def __str__(self) -> str:
        return f'{self.name_of_passenger} foglalása: {self.airline} - {self.flight_number} Úticél: {self.destination}'
