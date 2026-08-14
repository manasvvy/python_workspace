class person:
    def __init__(self,mail,name,age):
        self.mail=mail
        self.name=name 
        self.age=age

    def __hash__(self):
        return hash(self.mail)


p1=person("c@gmail.com","chandana",22)        
print(hash(p1))

print("---------------------------")

p2=person("m@gmail.com","madhu",22)        
print(hash(p2))
