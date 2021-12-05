from spot.parking_spot import ParkingSpot
from utils import ParkingSpotType


class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)