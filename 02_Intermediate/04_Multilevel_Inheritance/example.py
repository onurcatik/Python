class Prey:
    def flee(self):
        print("The prey is fleeing.")

class Predator:
    def hunt(self):
        print("The predator is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()

hawk.hunt()

fish.flee()
fish.hunt()

#  -------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")


rabbit = Prey("Rabbit")
rabbit.eat()  
rabbit.sleep()  
rabbit.flee()  

lion = Predator("Lion")
lion.eat()  
lion.sleep()  
lion.hunt() 


