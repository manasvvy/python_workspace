#create employee class and create 3 emp object/instances and in each empinstance declare or define 3 instance variable
 
class Employee:
    pass

e1 = Employee()
e2 = Employee()
e3 = Employee()

e1.eid=23 #iv1
e1.ename="john"
e1.salary=50000

e2.eid=45 #iv2
e2.ename="brock"
e2.salary=890000

e3.eid=22 #iv3
e3.ename="roman"
e3.salary=34000

print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)

print(e2.salary)
e3.eid=89
print(e3.eid)

