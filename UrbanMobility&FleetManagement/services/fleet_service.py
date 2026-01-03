from models.vehicle import Vehicle


class FleetService:

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle_id, model, battery_percentage):
        vehicle = Vehicle(vehicle_id, model, battery_percentage)
        self.vehicles.append(vehicle)
        return vehicle

    def get_all_vehicles(self):
        return self.vehicles
