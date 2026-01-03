class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage,
                 maintenance_status="OK", rental_price=0.0):

        self.vehicle_id = vehicle_id
        self.model = model
        
        # Private attributes
        self.__battery_percentage = None
        self.__maintenance_status = None
        self.__rental_price = None

        # Use setters to ensure validation applies at creation
        self.set_battery_percentage(battery_percentage)
        self.set_maintenance_status(maintenance_status)
        self.set_rental_price(rental_price)

    # ---------- GETTERS ----------

    def get_battery_percentage(self):
        return self.__battery_percentage

    def get_maintenance_status(self):
        return self.__maintenance_status

    def get_rental_price(self):
        return self.__rental_price

    # ---------- SETTERS ----------

    def set_battery_percentage(self, value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    def set_maintenance_status(self, status):
        allowed = ["OK", "SERVICE_DUE", "UNDER_REPAIR"]
        if status in allowed:
            self.__maintenance_status = status
        else:
            raise ValueError(f"Maintenance status must be one of {allowed}")

    def set_rental_price(self, price):
        if price < 0:
            raise ValueError("Rental price cannot be negative")
        self.__rental_price = price

    def __str__(self):
        return (
            f"[{self.vehicle_id}] {self.model} - "
            f"Battery: {self.__battery_percentage}% - "
            f"Status: {self.__maintenance_status} - "
            f"Price: ₹{self.__rental_price}/day"
        )
