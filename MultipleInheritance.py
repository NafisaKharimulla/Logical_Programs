class Swimmer:  # Parent 1
    def swim(self):
        print("Swimming in water")

class Flyer:   # Parent 2
    def fly(self):
        print("Flying in sky")

class Duck(Swimmer, Flyer):  # Child from both
    def quack(self):
        print("QUACK!")

# Test
duck = Duck()
duck.swim()  
duck.fly()   
duck.quack() 
