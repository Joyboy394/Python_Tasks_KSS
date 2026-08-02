class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


car1 = Car("Toyota", 180)
bike1 = Bike("Yamaha", 120)

print("Car Details:")
car1.display()

print("\nBike Details:")
bike1.display()
