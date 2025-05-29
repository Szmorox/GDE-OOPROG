from flights import Flights


class Tickets():
    def __init__(self, name_of_passenger: str, airline: str, flight_number: str, destination: str) -> None:
        self.name_of_passenger = name_of_passenger
        self.airline = airline
        self.flight_number = flight_number
        self.destination = destination

    def __str__(self) -> str:
        return f'{self.name_of_passenger}\'s reservation: {self.airline} - {self.flight_number} to {self.destination}'
        # return f'{self.name_of_passenger}\'s reservation: {self.flight_number} to {self.destination}'

    # def __add__(self, ticket: bool):
    #     self.reservation.append(ticket)

    # def get_Reservations(self):
    #     for  in self.reservation:
    #         print(f'{Flights.flight_number} - {Flights.destination} ...... {Flights.ticket_price}')

    # def __len__(self):
    #     return len(self.flights)
