from utils import VehicleType
from vehicle.vehicle import Vehicle


class Motorbike(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.MOTORBIKE, ticket)