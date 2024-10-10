class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count +=1 #Increment count on instance creation

    @classmethod
    def display_count(cls):
        return f"Total persons created: {cls.count}"
person1 = Person("Julie")
person2 = Person("Henry")
person3 = Person("Barry")
person4 = Person("Jimmy")
person5 = Person("Jack")
print(Person.display_count())