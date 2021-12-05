from services.parking_lot_service import ParkingLotService
from utils import ParkingSpotType

if __name__ == "__main__":

    parking_management_service = ParkingLotService(name="TechPark Parking")
    parking_management_service1 = ParkingLotService(name="TechPark Par")

    parking_lot_1 = parking_management_service.create_parking(parking_lot_id=1, no_of_floors=5, no_of_slots_per_floor=10)
    parking_slots_compact_spot = parking_management_service.add_parking_spots(parking_lot_id = 1, no_of_spots = 2, spot_type = ParkingSpotType.COMPACT)
    parking_slots_compact_handicapped_spot = parking_management_service.add_parking_spots(parking_lot_id = 1, no_of_spots = 2, spot_type = ParkingSpotType.HANDICAPPED)
    parking_slots_compact_motorbike_spot = parking_management_service.add_parking_spots(parking_lot_id = 1, no_of_spots = 2, spot_type = ParkingSpotType.LARGE)


    park_vehicle_1 = parking_management_service.park_vehicle(parking_lot_id = 1, vehicle_type="CAR", reg_no="KIA-7", color="BLACK")
    park_vehicle_2 = parking_management_service.park_vehicle(parking_lot_id = 1, vehicle_type="BIKE", reg_no="ACTIVA", color="ORANGE")

    unpark_vehicle_1 = parking_management_service.un_park_vehicle(park_vehicle_1.ticket_id)
    free_count = parking_management_service.display(display_type="free_count", parking_lot_id = 1, vehicle_type="BIKE")
