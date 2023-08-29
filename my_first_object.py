class car:
    def __init__(self,color,milage):
        self.color=color
        self.milage=milage

    def __str__(self):
        return f" the {self.color} car has {self.milage} miles"

car1=car(color="blue",milage="20,000")
car2=car("red","30,000")

print(car1)
print(car2)
car2.color
