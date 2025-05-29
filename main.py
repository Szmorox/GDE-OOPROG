from airline import Airline
from domestical import Domestical
from international import International
from tickets import Tickets
from system import Reservation_system

airline1 = Airline('Ryanair', 'FR RYR')

flight1 = International('Ryanair', 'A123', 'New York City, USA', '500')
flight2 = Domestical('Ryanair', 'B456', 'Budapest, Hungary', '75')
flight3 = International('Ryanair', 'C789', 'Moscow, Russia', '165')

airline1.add_flight(flight1)
airline1.add_flight(flight2)
airline1.add_flight(flight3)

system = Reservation_system()

system.to_reserve('Ben Doover', flight1.airline,
                  flight1.flight_number, flight1.destination)
system.to_reserve('Ann Smith', flight1.airline,
                  flight1.flight_number, flight1.destination)
system.to_reserve('Károly Kovács', flight1.airline,
                  flight1.flight_number, flight1.destination)
system.to_reserve('Dorina Knock', flight1.airline,
                  flight2.flight_number, flight2.destination)
system.to_reserve('Béláné Tóth', flight1.airline,
                  flight3.flight_number, flight3.destination)
system.to_reserve('Ádám Szigeti', flight1.airline,
                  flight3.flight_number, flight3.destination)


while True:
    system.menu()
    valasztas = input("\nVálassz egy műveletet: ")

    if valasztas == "1":
        system.listing_flights(airline1.flights)
        index = int(input("\nVálassz járatot (szám): ")) - 1
        if 0 <= index < len(airline1.flights):
            name_of_passenger = input("Add meg az utas nevét: ")
            reservations = system.to_reserve(
                name_of_passenger, airline1.flights[index].airline, airline1.flights[index].flight_number, airline1.flights[index].destination)
            print(f"\nSikeres foglalás: {reservations}")
        else:
            print("\nÉrvénytelen járat választás.")
    elif valasztas == "2":
        name_of_passenger = input("\nAdd meg az utas nevét: ")
        flight_number = input("Add meg a járatszámot: ")
        sikeres = system.cancel(name_of_passenger, flight_number)
        if sikeres:
            print("\nFoglalás sikeresen lemondva.")
        else:
            print("\nNem található ilyen foglalás.")
    elif valasztas == "3":
        print("\n=== Aktuális foglalások: ===")
        for f in system.reservations:
            print(f)
    elif valasztas == "0":
        print("\nKilépés...\n")
        break
    else:
        print("\nÉrvénytelen választás.")
