class pen: #everyclass inherits from object class
    def __init__(self,name,cost,typee):
        self.name=name 
        self.cost=cost 
        self.typee=typee

    def __str__(self):   #methodname and parameters are same
        return f"{self.name} {self.cost} {self.typee}" #always return a str while overriding the __str__
    
p1=pen("natraj",10,"gel")
print(p1)    #calls #print(p1.__str__())  

p2=pen("cello",20,"ballpen")
print(p2)

p2=pen("cello",20,"ballpen")
print(p2)
