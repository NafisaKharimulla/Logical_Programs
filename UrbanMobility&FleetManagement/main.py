print("Welcome to Eco-Ride Urban Mobility System")

from services.fleet_service import FleetService


def main():
    fleet_service = FleetService()

    num = int(input("How many vehicles do you want to add? "))

    for i in range(num):
        print(f"\nEnter details for Vehicle {i+1}:")
        vehicle_id = input("Enter Vehicle ID: ")
        model = input("Enter Vehicle Model: ")

        # validate battery input
        while True:
            try:
                battery = int(input("Enter Battery Percentage (0–100): "))
                if 0 <= battery <= 100:
                    break
                else:
                    print("Battery must be between 0 and 100. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        fleet_service.add_vehicle(vehicle_id, model, battery)

    print("\nFleet Vehicles Added:")
    for v in fleet_service.get_all_vehicles():
        print(v)


if __name__ == "__main__":
    main()
