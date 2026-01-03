print("Welcome to Eco-Ride Urban Mobility System")

from services.fleet_service import FleetService
def main():
    fleet_service = FleetService()

    num = int(input("How many vehicles do you want to add? "))

    for i in range(num):
        print(f"\nEnter details for Vehicle {i+1}:")
        vid = input("Enter Vehicle ID: ")
        model = input("Enter Vehicle Model: ")

        while True:
            try:
                battery = int(input("Enter Battery Percentage (0-100): "))
                break
            except ValueError:
                print("Enter a valid number!")

        status = input("Enter Maintenance Status (OK / SERVICE_DUE / UNDER_REPAIR): ")

        price = float(input("Enter Rental Price per day: "))

        try:
            fleet_service.add_vehicle(vid, model, battery, status, price)
            print("Vehicle added successfully!")

        except ValueError as e:
            print(f"Error: {e}")
            print("Vehicle not added. Please re-enter details.")

    print("\nFleet Details:")
    for v in fleet_service.get_all_vehicles():
        print(v)


if __name__ == "__main__":
    main()
