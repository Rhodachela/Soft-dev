class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return (f"{self.name} is {self.age} years old")
    def __del__(self):
        print (f"Your object {self.name} was deleted")
    def read(self):
        print(f"{self.name} is able to read pretty well")
persona = Person("Maryjane", 24)
persona.read()
del persona

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} was written by {self.author} and has {self.pages} pages"
    def __repr__(self):
        return f"Book(Title = {self.title},Author = {self.author}, Pages = {self.pages})"
book1 = Book("It ends with us", "Coleen Hoover", 300)
print(book1)
print(repr(book1))

class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food
    def eat(self):
        return f"{self.name} eats {self.food}"
    def sleep(self):
        return f"{self.name} sleeps very late at night"
class Dog(Animal):
    def barks(self):
        return f"{self.name} barks a lot at night"
animal1 = Animal("Giraffe", "Leaves")
print(animal1.eat())

dog1 = Dog("Jimmy", "Bones")
print(dog1.sleep())

class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"{self.name} makes a generic animal sound")
class Dog(Animal):
    def __init__(self, name, breed, color):
        super().__init__(name)
        self.breed = breed
        self.color = color
    def make_sound(self):
        print("Wooooof!!!")

anim = Animal("Giant")
anim.make_sound()

dog5 = Dog("Pablo", "German Shepherd", "Black")
dog5.make_sound()

class Car:
    def __init__(self, engine):
        self.engine = engine
    def start(self):
        self.engine.start()
class Engine:
    def start(self):
        print("Engine starting")
car = Car(Engine())
car.start()

class Girl:
    def __init__(self, hair):
        self.hair = hair
    def flipping(self):
        self.hair.flipping()
class Hair:
    def flipping(self):
        print("Chela's hair is flipping")
gal = Girl(Hair())
gal.flipping()