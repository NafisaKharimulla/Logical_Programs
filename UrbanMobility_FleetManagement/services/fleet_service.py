from models.vehicle import Vehicle


class FleetService:

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle_id, model, battery_percentage,
                    maintenance_status="OK", rental_price=0.0):

        vehicle = Vehicle(vehicle_id, model, battery_percentage,
                          maintenance_status, rental_price)

        self.vehicles.append(vehicle)
        return vehicle

    def get_all_vehicles(self):
        return self.vehicles
