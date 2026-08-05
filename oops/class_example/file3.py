#create student class, have 3cv create 3 student instance in each student instance have 3 instance variable print any 1 cv and iv modify any 1 cv and iv
 
class student:
    school="AGPS"
    principal="idk"
    classroom=12

s1= student()
s2= student()
s3 = student()

s1.name= "m"
s1.age= 22 
s1.loc= "blr"

s2.name= "c"
s2.age= 28 
s2.loc= "mumbai"

s3.name= "m"
s3.age= 19
s3.loc= "pune"

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print(s2.loc) #access
s3.name= "k"  #modify
print(s1.age) #access
