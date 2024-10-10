# #Encapsulation
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def __str__(self):
#         return f"{self.name} is {self.age} years old and has grade {self.grade}"
#     def enroll(self):
#         print (f"{self.name} whose age is {self.age} has been enrolled")
#     def view_grade(self):
#         print (f"{self.name}'s grade is {self.grade}")
    
# s1 = Student("Julie", 23, "A")
# s2 = Student("Chela_bae", 39, "A+")
# print(s1)

#Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print (f"Hello, my name is {self.name}, I am {self.age} years old.")
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def __str__(self):
        return f"{self.name} is {self.age} years old and has grade {self.grade}"
    def enroll(self):
        print (f"{self.name} whose age is {self.age} has been enrolled")
    def view_grade(self):
        print (f"{self.name}'s grade is {self.grade}")
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def introduce(self):
        print (f"Hello, my name is {self.name}, I am a teacher who teaches {self.subject}")
    def teach(self):
        return f"I teach {self.subject}."
    def assign_grade(self, student, grade):
        student.grade = grade
        print(f"{self.name} has assigned grade {grade} to {student.name}")

student1 = Student("Bliss", 23, "A")
student1.introduce()
# print(student1)
# student1.view_grade()
teacher1 = Teacher("Jane", 45, "English")
teacher1.introduce()

teacher1.assign_grade(student1, "B")
# print(teacher1.teach())

# student1 = Student("Bliss", 23, "A")
# print(student1)
# student1.view_grade()

# person1 = Person("Hylla", 70)
# person1.introduce()

#Polymorphism
