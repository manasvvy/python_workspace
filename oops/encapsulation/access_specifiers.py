#PUBLIC
 
class actor:
    country="india" #public cv
    def __init__(self,name,sal,language):
        self.name=name #public iv
        self.sal=sal
        self.language=language

    def display_poster(self): #public im
        print(f"idk {self.name} boss") #accessing public iv in class

    @classmethod
    def change_city(cls): #public cm
        cls.country="nepal" #accessing public iv in class

a1=actor("rm","jk","v")
print(a1.name) #iv outside the class
print(actor.country)
a1.display_poster                
actor.change_city()
print("_________________________________________________________________________")

#PROTECTED

class bankacc:
    bank_name="union" #public cv
    _intrest_rate=5   #protected cv

    def __init__(self,acc_no):
        self._acc_no=acc_no #protected iv

    def _calc_intrest(self,ammount): #protected im
        return (self._intrest_rate*ammount)/100 #acc protected cv in the

class savingacc(bankacc):
    def show_intrest(self,ammount):
        print("the intrest amt is", self._calc_intrest(ammount)) #accessing protected im in child class

a1=savingacc(5415321654120)
a1.show_intrest(1000000000)        #access public im

print("_________________________________________________________________________")
