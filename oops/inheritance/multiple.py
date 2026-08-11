class teacher:
    def teaches(self):
        print("teacher teaches")

class student:
    def studies(self):
        print("student learns")   

class TeacherAssistant(teacher,student):
    def conduct_mock(self):
        print("conducts mock and and also is a student")   
                 

t=TeacherAssistant()
t.conduct_mock()
print(TeacherAssistant.__dict__)
print(TeacherAssistant.__mro__)
t.teaches()
print(teacher.__dict__)
t.studies()
print(student.__dict__)


