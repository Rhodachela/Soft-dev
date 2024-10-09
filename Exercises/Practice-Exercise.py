class Student:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def display_info(self):
        return (f"My name is {self.name}, I am {self.age} years old  and I take {self.subject}")

s1 = Student("Rhoda", 23, "french")
s2 = Student("Elaine", 27, "German")
s1.display_info()
s2.display_info()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        total_value = self.quantity * self.price
        return total_value

    def display_prod_info(self):
        return f"Product: {self.name} Price: {self.price} Quantity: {self.quantity}"

prod1 = Product("Rice", 250, 5)
print(f"The total value of products is {prod1.calculate_total_value()}")

print(prod1.display_prod_info())