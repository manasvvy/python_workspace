class student:
    def __init__(self,roll,name):
        self.roll=roll 
        self.name=name

    def __eq__(self, other):
        if isinstance(other,student):  #ensures only student type instance are compared
            return self.roll==other.roll
        return False

s1=student(14,"m")        
s2=student(14,"m")      
print(s1==s2) #s1__eq__(s2)
