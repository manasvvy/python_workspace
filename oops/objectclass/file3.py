class employee: #everyclass inherits from object class
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age 
        self.dept=dept

    def __str__(self):   #methodname and parameters are same
        return f"{self.name} {self.age} {self.dept}" #always return a str while overriding the __str__
    
e1=employee("raj",30,"ai")
print(e1)    

e2=employee("rashmi",23,"analytics")
print(e2)

e3=employee("kavya",22,"research")
print(e3)
