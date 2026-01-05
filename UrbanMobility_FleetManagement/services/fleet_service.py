from models.vehicle import Vehicle
from models.electric_vehicle import ElectricCar, ElectricScooter

class FleetService:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        #Add a Vehicle, ElectricCar, or ElectricScooter instance.
        
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Must be a Vehicle or subclass instance")
        self.vehicles.append(vehicle)
        return vehicle

    def get_all_vehicles(self):
        return self.vehicles
