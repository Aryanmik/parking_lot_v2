from enum import Enum


class VehicleType(Enum):
    CAR = "car"
    TRUCK = "truck"
    ELECTRIC = "electric"
    VAN = "van"
    MOTORBIKE = "motorbike"


class ParkingSpotType(Enum):
    HANDICAPPED = "handicapped"
    COMPACT = "compact"
    LARGE = "large"
    COMPROMISED = "compromised"


class ParkingTicketStatus(Enum):
    ACTIVE = "active"
    PAID = "paid"

