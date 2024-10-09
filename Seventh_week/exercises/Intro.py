class Dog:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is getting created")

    def __del__(self):
        print(f"{self.name} is getting destroyed")

dog1 = Dog("Jimmy")
print(dog1.name)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed}"

    def __repr__(self):
        return f"Dog (name = {self.name}, breed = {self.breed})"

dog1 = Dog("Pablo", "Chiuawa")
print(dog1)
print(repr(dog1))

#Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

my_dog = Dog("Jimmy")
print(my_dog.speak())

#Multiple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
class Swimmer:
    def swim(self):
        return f"{self.name} is swimming"
class Dog(Animal, Swimmer):
    pass

dog1 = Dog("Pablo")
print(dog1.swim())

#Multilevel Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
class Mammal(Animal):
    def feed_babies(self):
        return f"{self.name} is feeding babies"
class Dog(Mammal):
    def bark(self):
        return f"{self.name} barks"

dog1 = Dog("Pablo Griffins")
print(dog1.feed_babies())
print(dog1.bark())

mam = Mammal("Mummy")
print(mam.feed_babies())

#Composition
class Engine:
    def start(self):
        return "Engine is starting"

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()
    def drive(self):
        return f"{self.model} is driving. {self.engine.start()}"
car1 = Car("Audi")
print(car1.drive())

class Wheel:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def __str__(self):
        return f"{self.color}"
wheel1 = Wheel("Black", 10)

class Tyre:
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand
    def __str__(self):
        return f"{self.brand}"
tyre1 = Tyre(20, "Michelin")

class Car:
    def __init__(self, wheel1, tyre1):
        self.wheel1 = wheel1
        self.tyre1 = tyre1
    def __str__(self):
        return f"{self.wheel1} {self.tyre1}"
car1 = Car(wheel1, tyre1)
print(car1.wheel1)
