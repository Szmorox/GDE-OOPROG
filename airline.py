class Airline():
    def __init__(self, name: str, id: str) -> None:
        self.flights = []
        self.airline_names = []

        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f'Airlines: {self.name} ({self.id} \n    {len(self.flights)} flights'

    def type_of_flight(self):
        pass

    def add_flight(self, ticket_to):
        self.flights.append(ticket_to)
