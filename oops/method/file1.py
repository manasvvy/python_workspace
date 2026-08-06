#class method

class Teacher:
    school="agps" #cv
    principal="idkbro" #cv

    @classmethod
    def display_deets(cls):
        print(cls.school) #printing is basically accessing the class variable
        print(cls.principal) 

    @classmethod
    def change_principal(cls,newp):
        cls.principal=newp

print(Teacher.__dict__)
Teacher.change_principal("sybau")
Teacher.display_deets()
Teacher.change_principal("yo")
Teacher.display_deets()
