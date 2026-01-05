from models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,
                 maintenance_status="OK", rental_price=0.0,
                 seating_capacity=4):
        super().__init__(vehicle_id, model, battery_percentage,
                         maintenance_status, rental_price)
        self.seating_capacity = seating_capacity

    def __str__(self):
        return super().__str__() + f" - Seating Capacity: {self.seating_capacity} seats"


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,
                 maintenance_status="OK", rental_price=0.0,
                 max_speed_limit=60):
        super().__init__(vehicle_id, model, battery_percentage,
                         maintenance_status, rental_price)
        self.max_speed_limit = max_speed_limit

    def __str__(self):
        return super().__str__() + f" - Max Speed: {self.max_speed_limit} km/h"
