#encapsulation using property decorator

class stu:
    def __init__(self):
        self.__marks=0 #priv iv

    @property               #getter should be 1st
    def marks(self):
        return self.__marks    

    def marks(self,newmarks):
        if newmarks>=0 and newmarks<=100:
            self.__marks=newmarks

        else:
            print("invalid")    

s1=stu()
print(s1.marks)            
s1.marks=444
print(s1.marks)            
