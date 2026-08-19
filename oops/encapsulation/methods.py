#setter and getter methods
class student:
    def __init__(self):
        self.__marks = 0
        self.__fees = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:   # validation logic
            self.__marks = marks          # initializing logic
        else:
            print("invalid")

    def get_fees(self):
        return self.__fees

    def set_fees(self, fees):
        if fees >= 0 and fees <= 5000000:
            self.__fees = fees
        else:
            print("go to other school")


s1 = student()
s1.set_marks(88)
print(s1.get_marks())
s1.set_fees(200000)
print(s1.get_fees())

print("__________________________________________________________________")

class BankAccount:
    def __init__(self):
        self.__balance = 30000       #private iv

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount  #private iv
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Cannot withdraw")

    def get_balance(self):
        return self.__balance


b1 = BankAccount()
print(b1.get_balance())
b1.deposit(20000)
print(b1.get_balance())
b1.withdraw(50000)
print(b1.get_balance())
b1.withdraw(5000)
print(b1.get_balance())
