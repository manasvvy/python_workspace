#static method

class Student:
    school="nps"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    @staticmethod
    def calculate_percentage(marks,tm):
        print((marks/tm)*100)
Student.calculate_percentage(70,25)        


#cgpa converter

#static method

class Student:
    school="nps"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    @staticmethod
    def calculate_percentage(marks,tm):
        print((marks/tm)*100)

    def cgpa_converter(cgpa):
        print((cgpa-0.75)*10)    

Student.calculate_percentage(7,25)    