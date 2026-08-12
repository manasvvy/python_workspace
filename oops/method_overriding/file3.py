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

c=citizen("madhu",22,"coorg",111)       
print(c.__dict__) 