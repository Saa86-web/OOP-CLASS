class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Create instances
my_car = Car()
my_plane = Plane()

# Test polymorphism
print(my_car.move())  # Output: Driving 🚗
print(my_plane.move())  # Output: Flying ✈️
