"""Járat"""
"""Absztrakt osztály"""


from abc import ABC, abstractmethod
class Flights(ABC):
    def __init__(self, airline: str, flight_number: str, destination: str, ticket_price: str) -> None:
        self.flight_number = flight_number
        self. destination = destination
        self.ticket_price = ticket_price
        self.airline = airline

    def __str__(self) -> str:
        return f'{self.type_of_journey()} - {self.airline}, {self.flight_number} -> {self.destination} ...... {self.ticket_price}' + '€'

    @abstractmethod
    def type_of_journey(self) -> str:
        pass
