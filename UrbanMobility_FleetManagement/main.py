from services.fleet_service import FleetService
from models.vehicle import Vehicle
from models.electric_vehicle import ElectricCar, ElectricScooter


def main():
    print("Welcome to Eco-Ride Urban Mobility System")
    fleet_service = FleetService()

    while True:
        try:
            num = int(input("How many vehicles do you want to add? "))
            break
        except ValueError:
            print("Enter a valid number!")

    for i in range(num):
        print(f"\nEnter details for Vehicle {i + 1}:")
        vehicle_type = input("Enter type (Vehicle / ElectricCar / ElectricScooter): ").strip().lower()

        vid = input("Enter Vehicle ID: ")
        model = input("Enter Vehicle Model: ")

        while True:
            try:
                battery = int(input("Enter Battery Percentage (0-100): "))
                break
            except ValueError:
                print("Enter a valid number!")

        status = input("Enter Maintenance Status (OK / SERVICE_DUE / UNDER_REPAIR): ").strip().upper()

        while True:
            try:
                price = float(input("Enter Rental Price per day: "))
                break
            except ValueError:
                print("Enter a valid price!")

        try:
            if vehicle_type == "electriccar":
                seating = int(input("Enter Seating Capacity: "))
                vehicle = ElectricCar(vid, model, battery, status, price, seating)

            elif vehicle_type == "electricscooter":
                speed = int(input("Enter Max Speed Limit (km/h): "))
                vehicle = ElectricScooter(vid, model, battery, status, price, speed)

            else:
                vehicle = Vehicle(vid, model, battery, status, price)

            fleet_service.add_vehicle(vehicle)
            print("Vehicle added successfully!")

        except ValueError as e:
            print(f"Error: {e}")
            print("Vehicle not added. Please re-enter details.")

    print("\nFleet Details:")
    for v in fleet_service.get_all_vehicles():
        print(v)


if __name__ == "__main__":
    main()
