class Animal:
    def __init__(self):
        self.alive= True

    def speak(self):
        raise NotImplementedError("İmplement this method")
    
class Dog(Animal):
    def speak(self):
        return "wooof"
    
class Cat(Animal):
    def speak(self):
        return "meow"
    
class Car:
    def __init__(self):
        self.alive= False
    def speak(self):
        return "Honk"
    
def main():
    dog = Dog()
    cat = Cat()
    car = Car()

    animals = [dog, cat, car]

    for animal in animals:
        print(f"{animal.speak()} - Alive: {animal.alive}")

if __name__ == "__main__":
    main()
