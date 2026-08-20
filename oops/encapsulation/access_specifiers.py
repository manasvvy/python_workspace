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

#PRIVATE

class emp:
    def __init__(self,name,sal):
        self.name=name           #public iv
        self.__sal=sal           #private iv

    def display_emp_deets(self): #public im
        print(self.name)
        print(self.__sal)        #accessing pvt iv inside the public im within the class

e1=emp("elon",66000)
print(e1.name)
#print(e1.__sal)                 #attr error bc we accessed pvt member outside the class
e1.display_emp_deets()

print("_________________________________________________________________________")

class student:
    def __init__(self,name,roll,marks):
        self.name=name           #public iv
        self._roll=roll          #protected iv
        self.__marks=marks       #priv iv

    def student_deets(self):     #public im
        print(self.name)          
        print(self._roll)
        print(self.__marks)      #accessing pvt iv inside the public im within the class

s1=student("idk",22,89)       
s1.student_deets()               #method call

print("_________________________________________________________________________")

#private method

class patient:
    def __init__(self,name,bp,sugar):
        self.name=name      #public iv
        self.__bp=bp        #priv iv
        self.__sugar=sugar 

    def __checkup(self):    #private instance method
        print(self.name, self.__bp, self.__sugar)    #accessing pvt instance var inside private instance method in class

    def show_report(self):    #public instance method
        self.__checkup()      #accessing priv im inside public im within the ssame class

p1=patient("b",120,140)
p1.show_report()        
