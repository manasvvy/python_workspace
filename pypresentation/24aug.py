class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
s1 = Student("Manasvi", 101, 85)
s2 = Student("maddy", 102, 90)
s1.display()
s2.display()

print("--------------------------------------------------------------------------------------------------")

class Smartphone:
    def takePhoto(self):
        print("say cheese")
class iPhone15(Smartphone):
    def takePhoto(self):
        super().takePhoto()
        print("clicking pics")
phone = iPhone15()
phone.takePhoto()

print("--------------------------------------------------------------------------------------------------")

class Employee:  
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Salary: {self.salary}")
e1 = Employee(101, "kav", 50000)
e1.display()

print("--------------------------------------------------------------------------------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
s1 = Student("chandu", 22, "Computer Science")
s1.display()