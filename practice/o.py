'''Create a Student class with name and age.

age must be private
Create a setter for age
If age is less than 18, raise a custom InvalidAgeException
Create a getter for age
Create a display() method
Create an object and handle the exception using try/except'''

class InvalidAgeException(Exception):
    pass


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        if age < 18:
            raise InvalidAgeException("Invalid age")
        self.__age = age

    def get_age(self):
        return self.__age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.__age}")


try:
    s = Student("A", 20)
    s.set_age(15)
    s.display()
except InvalidAgeException as e:
    print(e)

    