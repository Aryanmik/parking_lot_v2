import uuid

class ParkingSlots:

    def __init__(self, spot_type, is_available=True):
        self.slot_id = f"SID-{uuid.uuid1().hex[:6]}"
        self.is_available = is_available
        self.spot_type = spot_type

    def book_slot(self):
        self.is_available = False
        return self.slot_id

    def free_slot(self):
        self.is_available = True