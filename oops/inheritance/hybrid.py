class employee:
    def work(self):
        print("employee works")

class fedev(employee):
    def design(self):
        print("front end developer develops designs ui")   

class bedev(employee):
    def identify_endpts(self):
        print("api endpoints")   

class fsdev(fedev,bedev):
    def set_principles(self):
        print("makes all the decisions")                  


dd=fsdev()
dd.set_principles()
dd.design()
dd.identify_endpts()
dd.work() 
print(employee.__dict__)
print(bedev.__dict__)
print(fedev.__dict__)
print(fsdev.__dict__)
print(fsdev.__mro__)
