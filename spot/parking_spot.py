from abc import ABC


class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.number = number
        self.free = True
        self.vehicle = None
        self.parking_spot_type = parking_spot_type

    def is_free(self):
        return self.free

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.free = False

    def remove_vehicle(self):
        self.vehicle = None
        self.free = True
