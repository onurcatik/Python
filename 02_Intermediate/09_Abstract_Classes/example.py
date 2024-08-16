from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        """Method to move the vehicle"""
        pass

    @abstractmethod
    def stop(self):
        """Method to stop the vehicle"""
        pass
  
# vehicle = Vehicle()

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")

car = Car()
car.go()    # Output: You drive the car
car.stop()  # Output: You stop the car

motorcycle = Motorcycle()
motorcycle.go()    # Output: You ride the motorcycle
motorcycle.stop()  # Output: You stop the motorcycle

boat = Boat()
boat.go()    # Output: You sail the boat
boat.stop()  # Output: You anchor the boat




