from typing import List

from models.parking_floor import ParkingFloor


class ParkingLot:

    def __init__(self, name, parking_lot_id, no_of_floors, slots_per_floor , parking_floors: List[ParkingFloor] = None):
        self.name = name
        self.parking_lot_id = parking_lot_id
        self.no_of_floors = no_of_floors
        self.slots_per_floor = slots_per_floor
        self.parking_floors = parking_floors
