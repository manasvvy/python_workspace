class Student:
    '''ts student class level docstring example'''
    course_name="pythonfs"     #cv1
    classroom=201              #cv2



'''print(Student)
s1=Student()         #instantiation
s2=Student()
s3=Student()

print(s1)
print(s2)
print(s3)'''
print(Student.__dict__)

#print(s1.__dict__)

Student.institute="dcl"
print(Student.institute) #access the class variablename