#presentation class topic

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Manasvi", 85)
s1.display()
print("---------------------------------------------------") 

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}")

e1 = Employee(101, "Rahul", 50000)
e1.display()

print("---------------------------------------------------")

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Price: {self.price}")

c1 = Car("BMW", 5000000)
c1.display()

print("---------------------------------------------------")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area: {self.length * self.width}")

r1 = Rectangle(10, 5)
r1.area()

print("---------------------------------------------------")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area: {3.14 * self.radius * self.radius}")

c1 = Circle(7)
c1.area()

print("---------------------------------------------------")

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")


b1 = BankAccount(12345, 10000)
b1.deposit(5000)
b1.display()

print("---------------------------------------------------")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Harry Potter", "J.K. Rowling")
book1.display()

print("---------------------------------------------------")

class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}, Price: {self.price}")

l1 = Laptop("HP", "8GB", 55000)
l1.display()

print("---------------------------------------------------")

class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

m1 = Mobile("Samsung", "Galaxy S25")
m1.display()

print("---------------------------------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("Manasvi", 22)
p1.display()
