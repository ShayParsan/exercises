import re


def is_valid_name(name):
    valid_name = re.fullmatch(r'\b[A-Za-z]*\b\s[A-Za-z]+', name)
    if valid_name is None:
        return False
    else:
        return True


class Passenger:
    def __init__(self, id, name, money):
        self.id = id
        self.money = money
        self.__name = self.set_name(name)

    def set_name(self, name):
        if is_valid_name(name) is False:
            raise ValueError('Name must consist of at least two parts separated by a space.')
        return name

    def get_name(self):
        return self.__name


from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, license_plate: str, amount_of_seats: int):

        self.__occupants = {}
        self.license_plate = license_plate
        self.amount_of_seats = amount_of_seats

    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    @property
    @abstractmethod
    def maximum_occupants(self):
        """
        Abstract property that must be implemented by subclasses to define
        the maximum number of occupants the vehicle can hold.
        """
        pass

    def add_passenger(self, passenger):
        if passenger not in self.__occupants:
            self.__occupants['passenger.id'] = passenger
        else:
            raise ValueError('Passenger already registered')

    def remove_passenger(self, passenger):
        if passenger in self.__occupants:
            self.__occupants.pop('passenger.id')

    def remove_all_passengers(self):
        self.__occupants = {}

    @property
    @abstractmethod
    def occupant_names(self):
        pass


class Taxi(Vehicle):
    def __init__(self, license_plate: str, amount_of_seats: int):
        super().__init__(license_plate, amount_of_seats)
        self.__occupants = {}
        self.__is_available = True

    def maximum_occupants(self):
        self.amount_of_seats = 1

    def pickup(self, passengers, distance):
        if self.__is_available is False:
            raise ValueError('Taxi is not available')

        calculated_fare = 0

        if distance > 4:
            calculated_fare = distance + 1
        else:
            calculated_fare = 5

        for occupant_passenger in passengers:
            if occupant_passenger.money <= calculated_fare:
                raise RuntimeError('Not enough money')
            else:
                occupant_passenger.money -= calculated_fare
                break

        self.__occupants['occupant_passenger.id'] = passengers

        self.__is_available = False

    def number_of_occupants(self):
        return len(self.__occupants)

    def dropoff(self):
        self.__occupants.clear()
        self.__is_available = True


class Bus(Vehicle):
    def __init__(self, license_plate: str, amount_of_seats: int):
        super().__init__(license_plate, amount_of_seats)
        self.__is_available = True
        self.__occupants = {}
        self.number_of_current_riders = 0

    def maximum_occupants(self):
        self.amount_of_seats = 2 * self.amount_of_seats
        return self.amount_of_seats

    def board(self, passenger):
        if self.number_of_current_riders > self.amount_of_seats:
            raise RuntimeError('Not enough seat')
        self.__occupants[passenger.id] = passenger
        self.number_of_current_riders += 1

        passenger.money -= 2

    def number_of_occupants(self):
        return len(self.__occupants)

    def disembark(self, passenger):
        if passenger.id in self.__occupants:
            self.__occupants.pop(passenger.id)



    @property
    def occupant_names(self):
        passengers_names = []
        for passenger_id in self.__occupants:  # passenger_id is the key
            passenger = self.__occupants[passenger_id]  # Access the Passenger object
            passengers_names.append(passenger.get_name())  # Correctly call get_name()
        return passengers_names


passenger2 = Passenger('2', 'NAME Lane', 7)
bus = Bus(license_plate='PLACE PLACE', amount_of_seats=2)
bus.board(passenger2)

print(bus.occupant_names)
