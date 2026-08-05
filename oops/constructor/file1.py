class pen:
    def __init__(self):
        self.name="natraj" #iv1
        self.cost=10       #iv2

p1=pen() #instance1 pen()=constructor call  p1=reference


p2=pen() #instance2

print(p1.__dict__)
print(p2.__dict__)