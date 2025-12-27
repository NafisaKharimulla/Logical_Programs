class Car:  
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
    
    def start(self):
        print("Car started")

class ToyotaCar(Car):  
    def __init__(self, name, fuel_type):
        super().__init__(fuel_type)
        self.name = name
    
    def honk(self):
        print(f"{self.name} honks!")


toyota = ToyotaCar("Camry", "Petrol")
toyota.start()  
toyota.honk()   
print(toyota.fuel_type)  
