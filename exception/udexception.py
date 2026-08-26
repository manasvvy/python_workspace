class InSufficientBalanceException(Exception):
    pass
class InvalidAmountException(Exception):
    pass

class atm:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,ammount):
        if ammount>self.balance:
            raise InSufficientBalanceException("AMT EXCEEDS")            
        else:
            self.balance=ammount
            print("successful")

    def deposit(self,ammount):
        if ammount<=0:
            raise InvalidAmountException("get a job")        
        else:
            self.balance+=ammount
            print("ammount deposited")

a=atm(5000)
a.deposit(2000)
a.deposit(-50)

try:
    a.deposit(-50)
except InvalidAmountException as e:
    print(e)