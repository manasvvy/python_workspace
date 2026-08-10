'''METHOD OVERLODING EX- ONLY LAST METHOD EXECUTES'''

class calculator:
    def add(self,n1):
        print(n1+n1)
    def add(self,n1,n2):
        print(n1+n)
    def add(self,n1,n2,n3):
        print(n1+n2+n3)   
    def add(self,n1,n2,n3,n4):
            print(n1+n2+n3,n4)       
c = calculator()
#c.add(10)
#c.add(10,20)        
c.add(10,20,30,40)
