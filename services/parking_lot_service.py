import threading

from collections import defaultdict

from database.parking_floors import ParkingFloorsDB
from database.parking_lot import ParkingLotDB
from models.parking_lot import ParkingLot
from models.parking_slots import ParkingSlots


class ParkingLotService:
    instance = None

    class OnlyOne:
        def __init__(self, name):
            self.name = name

            self.compact_spot_count = 0
            self.large_spot_count = 0
            self.motorbike_spot_count = 0
            self.electric_spot_count = 0

            self.parking_lot = ParkingLotDB()
            self.parking_floors = ParkingFloorsDB()

            self.active_tickets = {}

            self.lock = threading.Lock()

    def __init__(self, name):
        if not ParkingLotService.instance:
            ParkingLotService.instance = ParkingLotService.OnlyOne(name)
        else:
            ParkingLotService.instance.name = name

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def _create_slots(self, no_of_floors, no_of_slots_per_floor):
        pass

    def create_parking(self, parking_lot_id, no_of_floors, no_of_slots_per_floor):
        parking_lot = ParkingLot(parking_lot_id=parking_lot_id, name=self.instance.name, no_of_floors=no_of_floors,
                                 slots_per_floor=no_of_slots_per_floor)
        self.parking_lot.save(parking_lot=parking_lot)
        return parking_lot

    def add_parking_spots(self, parking_lot_id, no_of_spots, spot_type):
        parking_lot = self.parking_lot.get(parking_lot_id)
        parking_floors = defaultdict(list)
        for floor_no in range(parking_lot.no_of_floors):
            for spot_no in range(no_of_spots):
                parking_floors[floor_no].append(ParkingSlots(spot_type=spot_type))





