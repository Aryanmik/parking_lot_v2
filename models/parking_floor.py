from typing import List

from models.parking_slots import ParkingSlots


class ParkingFloor:

    def __init__(self, floor_number, slots : List[ParkingSlots]):
        self.floor_number = floor_number
        self.slots = slots

