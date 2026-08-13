#constructor chaining

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class citizen(person):
    def __init__(self,name,age,country,cid):
        super().__init__(name,age)
        self.country=country
        self.cid=cid

class refugee(person):                         #hierarchial
    def __init__(self,name,age,countryy,rid):
        super().__init__(name,age)
        self.countryy=countryy
        self.rid=rid

c=citizen("madhu",22,"coorg",111)       
print(c.__dict__) 

r=refugee("k",21,"maharashtra",25)
print(r.__dict__) 