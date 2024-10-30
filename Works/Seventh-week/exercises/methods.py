#Class Methods
class Dog:
    breed = "Bulldog" #Class variable

    def __init__(self, name):
        self.name = name #instance variable

    @classmethod
    def change_breed(cls, new_breed):
        cls.breed = new_breed
    def show_info(self):
        print(f"{self.name} is a {self.breed}")
    def __str__(self):
        return f"{self.name} is a {self.breed}"
dog1 = Dog("Pablo")
dog1.show_info()
dog2 = Dog("Manny")
dog2.show_info()
Dog.change_breed("Germand shepherd")
dog2.show_info()
dog3 = Dog("Jimmy")
dog3.change_breed("Chiuawa")
print(dog3)

#Static Methods
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    @staticmethod
    def weekly_salary(daily_wage, num_of_days):
        return daily_wage * num_of_days 
employee1 = Employee("Judy", 34)
print(employee1)
print(employee1.weekly_salary(500, 5))

class Employee:
    company_name = "Tech Innovations"

    def __init__(self, name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    @staticmethod
    def weekly_salary(daily_wage, num_of_days):
        return daily_wage * num_of_days
    @classmethod
    def get_company_names(cls):
        return cls.company_name
employee2 = Employee("Bobby", 45)
print(employee2.get_company_names())
print(employee2.weekly_salary(400, 10))