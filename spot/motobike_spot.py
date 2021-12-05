from spot.parking_spot import ParkingSpot
from utils import ParkingSpotType


class MotorbikeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)