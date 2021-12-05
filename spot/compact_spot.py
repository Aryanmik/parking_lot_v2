from spot.parking_spot import ParkingSpot
from utils import ParkingSpotType


class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)