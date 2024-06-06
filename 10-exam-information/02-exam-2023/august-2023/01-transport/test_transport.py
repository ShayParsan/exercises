import pytest
from transport import Passenger, Vehicle, Taxi, Bus


@pytest.mark.parametrize('name', [
    "Name Lane",
])
def test_name(name):
    passenger1 = Passenger(2, name, 7)

    assert passenger1.get_name() == name

def test_passenger_of_a_bus():
    passenger2 = Passenger('2', 'NAME Lane', 7)
    bus = Bus(license_plate='PLACE PLACE', amount_of_seats=2)
    bus.board(passenger2)

    assert bus.occupant_names == [passenger2.get_name()]