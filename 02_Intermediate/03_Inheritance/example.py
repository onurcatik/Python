class Animal: 
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self): 
        print(f"{self.name} is asleep.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} is squeaking.")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Jerry")

dog.eat()
dog.bark()
cat.sleep()
cat.meow()
mouse.eat()
mouse.squeak()
