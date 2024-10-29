class Shape:
    def calculate_area(self):
          return None    
class Rectangle(Shape):
    def calculate_area(self, length, width):
        area = length * width
        return area
rect = Rectangle()
print(rect.calculate_area(45, 59))        

class Bird:
    def fly(self):
        return ("It can fly high up in the sky")
class Mammal:
    def run(self):
        return ("It rans really fast")
class Bat(Bird, Mammal):
    pass
batman = Bat()
print(batman.run())

class Dog:
    def make_sound(self):
        return "Woof!"
class Cat:
    def make_sound(self):
        return "Meoww!"
class Bird:
    def make_sound(self):
        return "Chiriri!"
def let_them_speak(animals):
    for animal in animals:
        print (animal.make_sound())

dog1 = Dog()
cat1 = Cat()
birdie = Bird()
animals = [dog1, cat1, birdie]
let_them_speak(animals)