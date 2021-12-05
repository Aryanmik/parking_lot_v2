from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self._license_number = license_number
        self._type = vehicle_type
        self._ticket = ticket

    @abstractmethod
    def assign_ticket(self, ticket):
        self._ticket = ticket




