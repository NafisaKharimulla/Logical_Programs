class Animal:
    def move(self):
        print("Animals can move")

class Snake(Animal):
    def move(self):
        print("Snake slithers")

Snake().move()
