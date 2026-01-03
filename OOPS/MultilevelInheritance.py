class Vehicle:  # Grandparent
    def __init__(self, wheels):
        self.wheels = wheels
    
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):  # Parent
    def __init__(self, wheels, fuel_type):
        super().__init__(wheels)
        self.fuel_type = fuel_type
    
    def start(self):
        print("Car engine started")

class ToyotaCar(Car):  # Child 
    def __init__(self, wheels, fuel_type, model):
        super().__init__(wheels, fuel_type)
        self.model = model
    
    def honk(self):
        print(f"{self.model} honks!")


toyota = ToyotaCar(4, "Hybrid", "Prius")
toyota.move()   
toyota.start()  
toyota.honk()  
print(toyota.wheels)  
