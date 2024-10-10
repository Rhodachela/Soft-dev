class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def multiply(x, y):
        return x * y
print(MathUtils.add(500, 67))
print(MathUtils.multiply(4555, 2345))

#Practice exercise 1
class Book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1
    @classmethod
    def display_total_books(cls):
        return f"The total number of books created is {cls.total_books}"
book1 = Book("It ends with us", "Coleen")
book2 = Book("Motivation", "Ben Carson")
book3 = Book("KLB", "Wakenya")
print(Book.display_total_books())

#Practice exercise 2
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    def multiply(x, y, z):
        return x * y * z

print(Calculator.add(56, 34))
print(Calculator.multiply(900, 3, 4))

#Practice exercise 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def create_child(cls, name):
        return cls(name, 0)
    def __str__(self):
        return f"Child: {self.name}, Age: {self.age}"
child = Person.create_child("Tashy")
print(child)