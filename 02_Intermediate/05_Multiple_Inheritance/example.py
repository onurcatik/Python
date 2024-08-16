class Prey:
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator :
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.name = "Bugs"
rabbit.flee()

hawk.name = "Tony"
hawk.hunt()

fish.name = "Nemo"
fish.flee()
fish.hunt()


# -------------------------

class Animal:
    def __init__(self, name):
        self.name= name
    def eat(self):
          print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
     print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Ali")

rabbit.eat()
rabbit.sleep()
rabbit.flee()

hawk.eat()
hawk.sleep()
hawk.hunt()

fish.eat()
fish.sleep()
fish.flee()
fish.hunt()  # Output: Ali is hunting

