#instance variable = define a class called chocolate n this class define a constructor or initilizer and have 3 instance variable , define an instance method called display chocolate
#which when called should show val of the particular chocolate


class Chocolate:
    def __init__(self,name,price,flavour):
        self.name=name
        self.price=price
        self.flavour=flavour

    def display_details(self):
        print(self.name,self.price,self.flavour)    
         
c1=Chocolate("darkchocolate",120,"chocolate")
c2=Chocolate("kitkat",20,"milkchocolate") 

c1.display_details()
c2.display_details()

#cricket

class Cricket:
    def __init__(self,name,team,jerseyno):
        self.name=name
        self.team=team
        self.jerseyno=jerseyno

    def display_details(self):
        print(self.name,self.team,self.jerseyno)  

    def change_team(self,newteam):
        self.team=newteam

         
c1=Cricket("vk","rcb",12)
c2=Cricket("kl","srh",7) 
c2.change_team("kkr")
c1.display_details()
c2.display_details()
